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

def generate_rule_file(rule):
    for rule_name, info in rule.items():
        rules = fetch_from_urls(info["urls"]) + "\n" + '\n'.join(info["ex"])
        filename = f"{rule_name}.list"
    
        with open(filename, "w") as f:
            f.write(rules)

        print(f"\n>>> √    {filename}")

if __name__ == "__main__":

    rule = {
        "rule" : {
            "urls" : [
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

            "ex" : [
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
                "DOMAIN-SUFFIX,tradingview.com",
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
                "DOMAIN-SUFFIX,pqjc.sit"
            ]
        },

        "x" : {
            "urls" : [
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/OpenAI/OpenAI.list",
                "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Claude/Claude.list"
            ],

            "ex" : [
                "DOMAIN-SUFFIX,gemini.google.com"
            ]
        }
    }


    print("\nCheck for Updates...")
 
    generate_rule_file(rule)
    
    input("\nPress Enter to exit...")