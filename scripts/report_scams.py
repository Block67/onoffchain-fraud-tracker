import json

# Ajouter un nouveau signalement
def report_scam(category, value, source):
    file_map = {
        "adresse": "scam_addresses.json",
        "url": "scam_urls.json",
        "telephone": "scam_phones.json"
    }
    file = file_map.get(category)
    if not file:
        print("Catégorie non valide.")
        return
    with open(f"data/{file}", "r+", encoding="utf-8") as f:
        data = json.load(f)
        key = f"{category}s_frauduleux"
        data[key].append({"value": value, "source": source, "signalé_le": "2025-06-26"})
        f.seek(0)
        json.dump(data, f, indent=2)
    print(f"Signalement ajouté à {file}.")

if __name__ == "__main__":
    report_scam("adresse", "1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa", "utilisateur")