import requests
import re
from datetime import datetime

# ✅ Webhook Discord già inserito
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1389652708620898416/vtrph05DPhCru7NIetNx556YPBT92kntl0dpQL0EZEtwENZSkNNRgViGQffETFG651f_"

# ✅ Keyword monitorate
KEYWORDS = [
    "napoli incidente",
    "napoli rapina",
    "napoli violenza",
    "napoli botte",
    "napoli omicidio",
    "napoli furto",
    "napoli aggressione",
    "napoli attualità"
]

# 🔍 Cerca su Google Video (TikTok) filtrando ultimi 24h
def cerca_video(keyword):
    print(f"[{datetime.now().strftime('%H:%M')}] Cerco: {keyword}")
    headers = {
        "User-Agent": "Mozilla/5.0"
    }
    params = {
        "q": f"{keyword} site:tiktok.com",
        "tbm": "vid",
        "tbs": "qdr:d",  # ultimi 24h
        "hl": "it"
    }
    url = "https://www.google.com/search"
    response = requests.get(url, headers=headers, params=params)

    links = re.findall(r"https:\/\/www\.tiktok\.com\/@[^\s\"']+", response.text)
    links = list(set(links))  # rimuove duplicati
    return links

# 🚀 Invia i risultati al canale Discord
def invia_a_discord(link, keyword):
    data = {
        "content": f"📹 Nuovo video TikTok per **{keyword}**:\n{link}"
    }
    try:
        requests.post(DISCORD_WEBHOOK_URL, json=data)
    except Exception as e:
        print("Errore nell'invio a Discord:", e)

# ▶️ Esecuzione principale
def main():
    for keyword in KEYWORDS:
        results = cerca_video(keyword)
        for link in results:
            invia_a_discord(link, keyword)

if __name__ == "__main__":
    main()
