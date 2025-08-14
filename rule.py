import requests

SURGE_BASE = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/{name}/{name}.list"
CLASH_BASE = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/{name}/{name}.yaml"

RULES_CONFIG = {
    "rule": {
        "names": [
            "Google", "YouTube", "Twitter", "Microsoft", "GitHub", "Python", "Telegram",
            "Wikipedia", "Facebook", "Whatsapp", "Instagram", "Pixiv", "Discord", "Reddit"
        ],
        "suffix": [
            "tradingview.com",
            "linkedin.com",
            "elliottwave.com",
            "figma.com",
            "twinfoo.com",
            "z-library.sk",
            "v2ex.com",
            "pqjc.site",
            "xn--mes358aby2apfg.com",
            "xn--9kqz23b19z.com",
            "xmac.app",
            "vk.com",
            "userapi.com"
        ],
        "keyword": [
            "yourware",
            "macked"
        ]
    },
    "x": {
        "names": [
            "OpenAI", "Claude", "Copilot", "Gemini"
        ],
        "suffix": [
            "huggingface.co",
            "perplexity.ai",
            "pplx.ai",
            "x.ai",
            "coze.com"
        ],
        "keyword": []
    }
}

def fetch_from_urls(urls):
    texts = []
    for url in urls:
        try:
            resp = requests.get(url, timeout=10)
            resp.raise_for_status()
            texts.append(resp.text)
        except Exception as e:
            print(f"Failed: {url} ({e})")
    return '\n'.join(texts)

def build_urls(names, base):
    return [base.format(name=n) for n in names]

def build_ex(suffixes, keywords):
    ex = []
    ex += [f"DOMAIN-SUFFIX,{d}" for d in suffixes]
    ex += [f"DOMAIN-KEYWORD,{k}" for k in keywords]
    return ex

def format_rules(info, fmt):
    urls = build_urls(info["names"], CLASH_BASE if fmt == "yaml" else SURGE_BASE)
    content = fetch_from_urls(urls)
    if fmt == "yaml":
        extra_rules = build_ex(info.get("suffix", []), info.get("keyword", []))
        # Combine remote content with local rules, ensuring local rules are formatted for YAML lists.
        all_rules_text = content + '\n' + '\n'.join([f"- {rule}" for rule in extra_rules])
        lines = [
            line.strip() for line in all_rules_text.split('\n')
            if line.strip() and not line.lstrip().startswith("#") and line.strip() != "payload:" and not line.strip().startswith("- IP-ASN")
        ]
        return "payload:\n  " + "\n  ".join(lines)
    else:
        extra = build_ex(info.get("suffix", []), info.get("keyword", []))
        return content + '\n' + '\n'.join(extra)

def generate_rule_files(rules_config, fmt):
    ext = "yaml" if fmt == "yaml" else "list"
    for name, info in rules_config.items():
        text = format_rules(info, fmt)
        filename = f"{name}.{ext}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(text)
        print(f"\033[92m✔\033[0m \033[1m{filename}\033[0m")

if __name__ == "__main__":
    print("Check for Updates...")
    for fmt in ("list", "yaml"):
        generate_rule_files(RULES_CONFIG, fmt)
    input("Press Enter to exit...")