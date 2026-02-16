import json
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

SURGE_BASE = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/{name}/{name}.list"
CLASH_BASE = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/{name}/{name}.yaml"
MAX_WORKERS = 10
TIMEOUT = 8
MIN_SUCCESS_RATE = 0.8
CONFIG_FILE = Path("sources.yaml")


def load_rules_config():
    if not CONFIG_FILE.exists():
        raise FileNotFoundError(f"Config file not found: {CONFIG_FILE}")

    try:
        data = json.loads(CONFIG_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(
            f"{CONFIG_FILE} parse failed. Use YAML-compatible JSON format or install YAML parser support. "
            f"Details: {exc}"
        ) from exc

    if not isinstance(data, dict) or not data:
        raise ValueError(f"{CONFIG_FILE} must be a non-empty mapping.")

    for group, info in data.items():
        if not isinstance(info, dict):
            raise ValueError(f"{group}: value must be a mapping.")
        for key in ("names", "suffix", "keyword"):
            value = info.get(key)
            if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
                raise ValueError(f"{group}.{key} must be a list of strings.")
    return data


def build_urls(rules_config):
    urls = set()
    for info in rules_config.values():
        for n in info["names"]:
            urls.add(SURGE_BASE.format(name=n))
            urls.add(CLASH_BASE.format(name=n))
    return urls


def new_session():
    retry = Retry(
        total=3,
        backoff_factor=0.3,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET"}),
    )
    adapter = HTTPAdapter(max_retries=retry)
    session = requests.Session()
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session


def fetch_one(url):
    started = time.time()
    try:
        with new_session() as session:
            resp = session.get(url, timeout=TIMEOUT)
            resp.raise_for_status()
            return {
                "url": url,
                "ok": True,
                "status_code": resp.status_code,
                "bytes": len(resp.content),
                "duration_ms": int((time.time() - started) * 1000),
                "error": "",
                "content": resp.text,
            }
    except Exception as exc:
        return {
            "url": url,
            "ok": False,
            "status_code": None,
            "bytes": 0,
            "duration_ms": int((time.time() - started) * 1000),
            "error": str(exc),
            "content": "",
        }


def fetch_all(urls):
    url_to_content = {}
    fetch_report = {}
    total = len(urls)
    done = 0

    print()
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        futures = {executor.submit(fetch_one, url): url for url in urls}
        for future in as_completed(futures):
            result = future.result()
            done += 1
            fetch_report[result["url"]] = {
                "ok": result["ok"],
                "status_code": result["status_code"],
                "bytes": result["bytes"],
                "duration_ms": result["duration_ms"],
                "error": result["error"],
            }
            if result["ok"]:
                url_to_content[result["url"]] = result["content"]

            percent = (done / total) * 100
            sys.stdout.write(f"\rChecking for updates... {percent:.0f}% ({done}/{total})")
            sys.stdout.flush()

    print("\n")
    return url_to_content, fetch_report


def parse_rules(content, fmt):
    rules = []
    for raw in content.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue

        if fmt == "yaml":
            if line == "payload:":
                continue
            if line.startswith("- "):
                line = line[2:].strip()
            if line.startswith("IP-ASN,"):
                continue

        rules.append(line)
    return rules


def unique_rules(rules):
    seen = set()
    out = []
    for rule in rules:
        key = rule.strip()
        if key and key not in seen:
            seen.add(key)
            out.append(key)
    return out


def generate_output(url_to_content, rules_config):
    output_stats = {}
    for fmt, base in (("list", SURGE_BASE), ("yaml", CLASH_BASE)):
        for name, info in rules_config.items():
            urls = [base.format(name=n) for n in info["names"]]
            extra = [f"DOMAIN-SUFFIX,{d}" for d in info["suffix"]] + [f"DOMAIN-KEYWORD,{k}" for k in info["keyword"]]
            rules = []
            for url in urls:
                content = url_to_content.get(url, "").strip()
                if content:
                    rules.extend(parse_rules(content, fmt))
            rules.extend(extra)
            unique = unique_rules(rules)

            if fmt == "yaml":
                body = "\n  ".join(f"- {rule}" for rule in unique)
                text = f"payload:\n  {body}" if body else "payload:"
            else:
                text = "\n".join(unique)

            output_file = Path(f"{name}.{fmt}")
            output_file.write_text(text + ("\n" if text else ""), encoding="utf-8")
            output_stats[str(output_file)] = {
                "rules": len(unique),
                "source_count": len(info["names"]),
                "extra_count": len(extra),
            }
            print(f"\033[92m✔\033[0m  \033[1m{name}.{fmt}\033[0m ({len(unique)} rules)")
    return output_stats


if __name__ == "__main__":
    rules_config = load_rules_config()
    urls = build_urls(rules_config)
    content_map, fetch_report = fetch_all(urls)
    total = len(fetch_report)
    ok = sum(1 for item in fetch_report.values() if item["ok"])
    failed = total - ok
    success_rate = ok / total if total else 0

    if not total:
        print("✗ Update failed. No files were generated.")
        sys.exit(1)

    if failed:
        print("Failed URLs:")
        for url, item in fetch_report.items():
            if not item["ok"]:
                print(f"- {url} | {item['error']}")
        print()

    if success_rate < MIN_SUCCESS_RATE:
        print(f"✗ Update failed. Success rate {success_rate:.0%} is below threshold {MIN_SUCCESS_RATE:.0%}.")
        sys.exit(1)

    output_stats = generate_output(content_map, rules_config)
    manifest = {
        "generated_at_unix": int(time.time()),
        "success_rate": round(success_rate, 4),
        "total_urls": total,
        "ok_urls": ok,
        "failed_urls": failed,
        "fetch": fetch_report,
        "outputs": output_stats,
    }
    Path("manifest.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print("\033[92m✔\033[0m  \033[1mmanifest.json\033[0m")
