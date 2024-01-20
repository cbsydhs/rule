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

def convert_list_to_yaml(list_filename, yaml_filename):
    with open(list_filename, 'r') as f:
        original_content = f.readlines()
    cleaned_content = [line.strip() for line in original_content if not line.startswith('#') and line.strip()]
    cleaned_content.insert(0, 'payload:')
    formatted_content = [cleaned_content[0]] + ['  - ' + line for line in cleaned_content[1:]]
    
    with open(yaml_filename, 'w') as f:
        f.write('\n'.join(formatted_content))

def save_to_file(texts, filename, merge_rlue=False):
    if merge_rlue:
        if filename == "rule.yaml":
            convert_list_to_yaml("ex.list", "ex.yaml")
        with open(f"ex.{os.path.splitext(filename)[1][1:]}", "r", encoding="utf-8") as local_file:
            local_text = local_file.read()
            texts.append(local_text)
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write("\n".join(texts))
    
def reformat_yaml(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    lines = [line.strip() for line in lines if not line.startswith("#") and line.strip() != "" and line.strip() != "payload:"]

    lines = ["  " + line for line in lines]

    lines.insert(0, "payload:")

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line + "\n")

def process_urls_to_list(url_list, output_list_filename):
    texts = fetch_from_urls(url_list)

    merge_rlue = url_list == surge_rule
    save_to_file(texts, output_list_filename, merge_rlue)

    print(f"\n>>> √    {output_list_filename}")

def process_urls_to_yaml(url_list, output_yaml_filename):
    texts = fetch_from_urls(url_list)

    merge_rlue = url_list == clash_rule
    save_to_file(texts, output_yaml_filename, merge_rlue)

    reformat_yaml(output_yaml_filename)

    print(f"\n>>> √    {output_yaml_filename}")


if __name__ == "__main__":

    surge_rule = [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Telegram/Telegram.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Google/Google.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/YouTube/YouTube.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitter/Twitter.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Microsoft/Microsoft.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/GitHub/GitHub.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Python/Python.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Wikipedia/Wikipedia.list",
        # "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Wikimedia/Wikimedia.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Facebook/Facebook.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Whatsapp/Whatsapp.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Instagram/Instagram.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Pixiv/Pixiv.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Discord/Discord.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Reddit/Reddit.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Twitch/Twitch.list",
        # "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Cloudflare/Cloudflare.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/PikPak/PikPak.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Steam/Steam.list"
        # "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Vercel/Vercel.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/TikTok/TikTok.list"
    ]

    surge_ai_rlue = [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/OpenAI/OpenAI.list",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Surge/Claude/Claude.list"
    ]

    clash_rule = [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitter/Twitter.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Microsoft/Microsoft.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GitHub/GitHub.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Python/Python.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Wikipedia/Wikipedia.yaml",
        # "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Wikimedia/Wikimedia.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Facebook/Facebook.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Whatsapp/Whatsapp.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Instagram/Instagram.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Pixiv/Pixiv.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Discord/Discord.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Reddit/Reddit.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Twitch/Twitch.yaml",
        # "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Cloudflare/Cloudflare.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/PikPak/PikPak.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Steam/Steam.yaml",
        # "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Vercel/Vercel.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/TikTok/TikTok.yaml"
    ]

    clash_ai_rlue = [
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/OpenAI/OpenAI.yaml",
        "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Claude/Claude.yaml"
    ]

    print("\nCheck for Updates...")

    process_urls_to_list(surge_rule, "rule.list")
    process_urls_to_list(surge_ai_rlue, "rule-ai.list")
    process_urls_to_yaml(clash_rule, "rule.yaml")
    process_urls_to_yaml(clash_ai_rlue, "rule-ai.yaml")

    input("\nPress Enter to exit...")