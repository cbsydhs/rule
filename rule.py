import os
import requests

def fetch_from_urls(url_list):
    texts = []
    for url in url_list:
        response = requests.get(url)
        if response.status_code == 200:
            texts.append(response.text)
        else:
            print(f"Unable to retrieve data from URL {url}")
    return texts

def convert_list_to_yaml(list_filename):
    yaml_filename = os.path.splitext(list_filename)[0] + '.yaml'

    with open(list_filename, 'r') as list_file, open(yaml_filename, 'w') as yaml_file:
        cleaned_content = ['  - ' + line.strip() for line in list_file if not line.startswith('#') and line.strip()]
        yaml_file.write('payload:\n' + '\n'.join(cleaned_content))

def reformat_yaml(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if not line.startswith("#") and line.strip() != "" and line.strip() != "payload:"]

    lines = ["  " + line for line in lines]

    lines.insert(0, "payload:")

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + "\n")

def process_urls_to_file(url_list):
    texts = fetch_from_urls(url_list)
    filename = url_list
    convert_list_to_yaml("ex.list")

    if filename.startswith('clash'):
        with open("ex.yaml}", "r", encoding="utf-8") as local_file:
            local_text = local_file.read()
            texts.append(local_text)
        filename += '.yaml'
        reformat_yaml(filename)
    else:
        with open("ex.list}", "r", encoding="utf-8") as local_file:
            local_text = local_file.read()
            texts.append(local_text)
        filename += '.list'

    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(texts))

    print(f"\n>>> √    {filename}")

if __name__ == "__main__":

    rule = [
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
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PikPak/PikPak.list",
    ]

    rule_x = [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/OpenAI/OpenAI.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Claude/Claude.list"
    ]

    rules = [
        "DOMAIN-KEYWORD,pornhub",
        "DOMAIN-KEYWORD,xvideos",
        "DOMAIN-SUFFIX,archive.org",
        "DOMAIN-SUFFIX,beehiiv.com",
        "DOMAIN-SUFFIX,newsminimalist.com",
        "DOMAIN-SUFFIX,theverge.com",
        "DOMAIN-SUFFIX,rsshub.app",
        "DOMAIN-SUFFIX,ycombinator.com",
        "DOMAIN-SUFFIX,bloomberg.com",
        "DOMAIN-SUFFIX,engadget.com",
        "DOMAIN-SUFFIX,ipfs.io",
        "DOMAIN-SUFFIX,binance.org",
        "DOMAIN-SUFFIX,uniswap.org",
        "DOMAIN-SUFFIX,infura.io",
        "DOMAIN-SUFFIX,opensea.io",
        "DOMAIN-SUFFIX,metamask.io",
        "DOMAIN-SUFFIX,coingecko.com",
        "DOMAIN-SUFFIX,linkedin.com",
        "DOMAIN-SUFFIX,unsplash.com",
        "DOMAIN-SUFFIX,epg.pw",
        "DOMAIN-SUFFIX,hostloc.com",
        "DOMAIN-SUFFIX,elliottwave.com",
        "DOMAIN-SUFFIX,xn--6nq44rc0n82k.com",
        "DOMAIN-SUFFIX,xn--mes358aby2apfg.com",
        "DOMAIN-SUFFIX,xn--4gq62f52gdss.com",
        "DOMAIN-SUFFIX,nanoport.xyz",
        "DOMAIN-SUFFIX,pqjc.site"
    ]

    rules_x = [
        "DOMAIN-SUFFIX,tradingview.com"
    ]

    clash = [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitter/Twitter.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Microsoft/Microsoft.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GitHub/GitHub.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Python/Python.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Wikipedia/Wikipedia.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Wikimedia/Wikimedia.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Facebook/Facebook.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Whatsapp/Whatsapp.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Instagram/Instagram.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pixiv/Pixiv.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Discord/Discord.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Reddit/Reddit.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitch/Twitch.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PikPak/PikPak.yaml",
    ]

    clash_ai = [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Claude/Claude.yaml"
    ]

    print("\nCheck for Updates...")
  
    process_urls_to_file(rule)
    process_urls_to_file(rule_x)
    process_urls_to_file(clash)
    process_urls_to_file(clash_ai)

    input("\nPress Enter to exit...")




