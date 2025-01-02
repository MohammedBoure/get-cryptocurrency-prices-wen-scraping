import requests

#To avoid ban
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


def GetHTMLGage(name):
    response = requests.get("https://coinmarketcap.com/currencies/bitanium/", headers=headers)
    if response.status_code == 200:  
        with open(f"{name}.html", "w", encoding="utf-8") as file:
            file.write(response.text)
    else:
        print(f"Failed to fetch the page. Status code: {response.status_code}")
