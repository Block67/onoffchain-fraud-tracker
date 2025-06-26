import json
import os

# Générer des statistiques
def generate_stats():
    stats = {
        "statistiques": {
            "total_adresses": 0,
            "total_urls": 0,
            "total_telephones": 0,
            "derniere_mise_a_jour": "2025-06-26"
        }
    }
    for file, key in [
        ("scam_addresses.json", "adresses_frauduleuses"),
        ("scam_urls.json", "urls_frauduleuses"),
        ("scam_phones.json", "telephones_frauduleux")
    ]:
        with open(f"data/{file}", "r", encoding="utf-8") as f:
            data = json.load(f)
            stats["statistiques"][f"total_{key.split('_')[0]}"] = len(data[key])
    with open("data/stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, indent=2)
    print("Statistiques générées avec succès.")

if __name__ == "__main__":
    generate_stats()