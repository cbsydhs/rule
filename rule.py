import sys
import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

SURGE_BASE = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/{name}/{name}.list"
CLASH_BASE = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/{name}/{name}.yaml"

RULES_CONFIG = {
    "rule": {
        "names": [
            "Google", "YouTube", "Twitter", "Microsoft", "GitHub", "Python",
            "Telegram", "Wikipedia", "Facebook", "Whatsapp", "Instagram",
            "Pixiv", "Discord", "Reddit"
        ],
        "suffix": [
            "tradingview.com", "linkedin.com", "elliottwave.com", "figma.com",
            "twinfoo.com", "z-library.sk", "v2ex.com", "pqjc.site",
            "xn--mes358aby2apfg.com", "xn--9kqz23b19z.com", "xmac.app",
            "vk.com", "userapi.com"
        ],
        "keyword": ["yourware", "macked"]
    },
    "x": {
        "names": ["OpenAI", "Claude", "Copilot", "Gemini"],
        "suffix": ["huggingface.co", "perplexity.ai", "pplx.ai", "x.ai", "coze.com"],
        "keyword": []
    }
}


def build_urls():
    urls = set()
    for info in RULES_CONFIG.values():
        for n in info["names"]:
            urls.add(SURGE_BASE.format(name=n))
            urls.add(CLASH_BASE.format(name=n))
    return urls


def fetch_all(urls):
    url_to_content = {}
    session = requests.Session()
    total = len(urls)
    done = 0

    print()  # 前空行

    with ThreadPoolExecutor(max_workers=10) as executor:
        future_to_url = {executor.submit(session.get, url, timeout=5): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            done += 1
            try:
                resp = future.result()
                resp.raise_for_status()
                url_to_content[url] = resp.text
            except Exception:
                pass  # 静默失败

            # 百分比进度显示
            percent = (done / total) * 100
            sys.stdout.write(f"\rChecking for updates... {percent:.0f}% ({done}/{total})")
            sys.stdout.flush()

    print("\n")  # 后空行
    return url_to_content


def generate_output(url_to_content):
    for fmt, base in (("list", SURGE_BASE), ("yaml", CLASH_BASE)):
        for name, info in RULES_CONFIG.items():
            urls = [base.format(name=n) for n in info["names"]]
            content = '\n'.join(url_to_content.get(url, '').strip() for url in urls if url_to_content.get(url, '').strip())

            # 额外规则
            extra = [f"DOMAIN-SUFFIX,{d}" for d in info["suffix"]] + [f"DOMAIN-KEYWORD,{k}" for k in info["keyword"]]

            if fmt == "yaml":
                lines = [
                    line.strip()
                    for line in content.splitlines()
                    if line.strip() and not line.lstrip().startswith(("#", "payload:", "- IP-ASN"))
                ]
                lines += [f"- {rule}" for rule in extra]
                text = "payload:\n  " + "\n  ".join(lines)
            else:
                text = (content + '\n' if content else '') + '\n'.join(extra)

            Path(f"{name}.{fmt}").write_text(text, encoding="utf-8")
            print(f"✓ {name}.{fmt}")


if __name__ == "__main__":
    urls = build_urls()
    content_map = fetch_all(urls)
    if content_map:
        generate_output(content_map)
    else:
        print("✗ Update failed. No files were generated.")