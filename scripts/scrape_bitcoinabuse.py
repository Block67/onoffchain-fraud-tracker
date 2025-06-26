import requests
import json

# Scraper les adresses frauduleuses depuis BitcoinAbuse
def scrape_bitcoinabuse():
    url = "https://www.bitcoinabuse.com/api/reports"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        with open("data/scam_addresses.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print("Données BitcoinAbuse récupérées avec succès.")
    except Exception as e:
        print(f"Erreur lors du scraping : {e}")

if __name__ == "__main__":
    scrape_bitcoinabuse()