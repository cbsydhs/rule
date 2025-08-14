import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

SURGE_BASE = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/{name}/{name}.list"
CLASH_BASE = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/{name}/{name}.yaml"

RULES_CONFIG = {
    "rule": {
        "names": [
            "Google", "YouTube", "Twitter", "Microsoft", "GitHub", "Python", "Telegram",
            "Wikipedia", "Facebook", "Whatsapp", "Instagram", "Pixiv", "Discord", "Reddit"
        ],
        "suffix": [
            "tradingview.com", "linkedin.com", "elliottwave.com", "figma.com", "twinfoo.com",
            "z-library.sk", "v2ex.com", "pqjc.site", "xn--mes358aby2apfg.com",
            "xn--9kqz23b19z.com", "xmac.app", "vk.com", "userapi.com"
        ],
        "keyword": ["yourware", "macked"]
    },
    "x": {
        "names": ["OpenAI", "Claude", "Copilot", "Gemini"],
        "suffix": ["huggingface.co", "perplexity.ai", "pplx.ai", "x.ai", "coze.com"],
        "keyword": []
    }
}

def build_urls(info):
    return [
        SURGE_BASE.format(name=n) for n in info["names"]
    ] + [
        CLASH_BASE.format(name=n) for n in info["names"]
    ]

def fetch_all_urls_concurrently(urls):
    url_to_content = {}
    with ThreadPoolExecutor() as executor:
        future_to_url = {executor.submit(requests.get, url, timeout=10): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                resp = future.result()
                resp.raise_for_status()
                url_to_content[url] = resp.text
            except requests.exceptions.RequestException as e:
                print(f"Failed to fetch {url}: {e}")
    return url_to_content

def format_rules(info, fmt, fetched_content_map):
    base = CLASH_BASE if fmt == "yaml" else SURGE_BASE
    urls = [base.format(name=n) for n in info["names"]]
    content_parts = [fetched_content_map.get(url, '') for url in urls]
    content = '\n'.join(part for part in content_parts if part.strip())
    extra_rules = ([f"DOMAIN-SUFFIX,{d}" for d in info.get("suffix", [])] +
                   [f"DOMAIN-KEYWORD,{k}" for k in info.get("keyword", [])])
    if fmt == "yaml":
        lines = [
            line.strip() for line in content.split('\n')
            if line.strip() and not line.lstrip().startswith(("#", "payload:", "- IP-ASN"))
        ]
        lines += [f"- {rule}" for rule in extra_rules]
        return "payload:\n  " + "\n  ".join(lines)
    return (content + '\n' if content else '') + '\n'.join(extra_rules)

def main():
    print("\nChecking for updates...\n")
    all_urls = set()
    for info in RULES_CONFIG.values():
        all_urls.update(build_urls(info))
    fetched_content_map = fetch_all_urls_concurrently(list(all_urls))
    if fetched_content_map:
        for fmt in ("list", "yaml"):
            ext = "yaml" if fmt == "yaml" else "list"
            for name, info in sorted(RULES_CONFIG.items()):
                text = format_rules(info, fmt, fetched_content_map)
                with open(f"{name}.{ext}", "w", encoding="utf-8") as f:
                    f.write(text)
                print(f"✔ {name}.{ext}")
    else:
        print("✖ Upgrade failed. No files were generated.")
    input("\nPress Enter to exit...")

if __name__ == "__main__":
    main()
