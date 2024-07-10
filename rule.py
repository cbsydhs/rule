import requests

def fetch_from_urls(url_list):
    texts = []
    for url in url_list:
        response = requests.get(url)
        if response.status_code == 200:
            texts.append(response.text)
        else:
            print(f"Unable to retrieve data from URL {url}")
    return '\n'.join(texts)

def generate_rule_file(rule, format_type):
    for rule_name, info in rule.items():
        if format_type == "yaml":
            rules = fetch_from_urls(info["urls_yaml"]) + "\n" + '\n'.join(f"  - {item}" for item in info["ex"])
            lines = [line.strip() for line in rules.split('\n') if line.strip() and not line.startswith("#") and line.strip() != "payload:"]
            rules = "payload:\n  " + "\n  ".join(lines)
            filename = f"{rule_name}.yaml"
        else:
            rules = fetch_from_urls(info["urls_list"]) + "\n" + '\n'.join(info["ex"])
            filename = f"{rule_name}.list"
    
        with open(filename, "w") as f:
            f.write(rules)

        print(f"\n>>> √    {filename}")

if __name__ == "__main__":

    rule = {
        "rule" : {
            "urls_list" : [
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Telegram/Telegram.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Google/Google.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/YouTube/YouTube.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitter/Twitter.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Microsoft/Microsoft.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/GitHub/GitHub.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Python/Python.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Wikipedia/Wikipedia.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Wikimedia/Wikimedia.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Facebook/Facebook.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Whatsapp/Whatsapp.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Instagram/Instagram.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Pixiv/Pixiv.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Discord/Discord.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Reddit/Reddit.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitch/Twitch.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PikPak/PikPak.list"
            ],
            "urls_yaml" : [
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitter/Twitter.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Microsoft/Microsoft.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GitHub/GitHub.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Python/Python.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Wikipedia/Wikipedia.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Facebook/Facebook.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Whatsapp/Whatsapp.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Instagram/Instagram.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pixiv/Pixiv.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Discord/Discord.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Reddit/Reddit.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitch/Twitch.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PikPak/PikPak.yaml"
            ],

            "ex" : [
                "DOMAIN-SUFFIX,tradingview.com",
                "DOMAIN-SUFFIX,metamask.io",
                "DOMAIN-SUFFIX,coingecko.com",
                "DOMAIN-SUFFIX,linkedin.com",
                "DOMAIN-SUFFIX,unsplash.com",
                "DOMAIN-SUFFIX,archive.org",
                "DOMAIN-SUFFIX,ycombinator.com",
                "DOMAIN-SUFFIX,ipfs.io",
                "DOMAIN-SUFFIX,binance.org",
                "DOMAIN-SUFFIX,uniswap.org",
                "DOMAIN-SUFFIX,opensea.io",
                "DOMAIN-SUFFIX,elliottwave.com",
                "DOMAIN-SUFFIX,xn--6nq44rc0n82k.com",
                "DOMAIN-SUFFIX,xn--mes358aby2apfg.com",
                "DOMAIN-SUFFIX,xn--4gq62f52gdss.com",
                "DOMAIN-SUFFIX,nanoport.xyz",
                "DOMAIN-SUFFIX,pqjc.sit",
            ]
        },

        "x" : {
            "urls_list" : [
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/OpenAI/OpenAI.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Claude/Claude.list"
            ],
            "urls_yaml" : [
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.yaml",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Claude/Claude.yaml"
            ],

            "ex" : [
                "DOMAIN-SUFFIX,gemini.google.com",
                "DOMAIN-SUFFIX,notebooklm.google",
                "DOMAIN-SUFFIX,apis.google.com",
                "DOMAIN-SUFFIX,ai.google.dev",
                "DOMAIN-SUFFIX,aistudio.google.com",
                "DOMAIN-SUFFIX,generativelanguage.googleapis.com",
                "DOMAIN-SUFFIX,huggingface.co",
                "DOMAIN-SUFFIX,perplexity.ai"
            ]
        }
    }


    print("\nCheck for Updates...")
    
    generate_rule_file(rule, format_type="list")
    generate_rule_file(rule, format_type="yaml")
    
    input("\nPress Enter to exit...")