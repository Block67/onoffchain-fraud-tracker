import json
from scrape_bitcoinabuse import scrape_bitcoinabuse

# Mettre à jour le dépôt avec de nouvelles données
def update_repo():
    scrape_bitcoinabuse()
    # Ajouter ici d'autres sources de données
    with open("data/stats.json", "r+", encoding="utf-8") as f:
        stats = json.load(f)
        stats["statistiques"]["derniere_mise_a_jour"] = "2025-06-26"
        f.seek(0)
        json.dump(stats, f, indent=2)
    print("Dépôt mis à jour avec succès.")

if __name__ == "__main__":
    update_repo()