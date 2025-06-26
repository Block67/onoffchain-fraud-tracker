import json
import os

# Générer les fichiers de l'API
def export_api():
    os.makedirs("api", exist_ok=True)
    for file in os.listdir("data"):
        if file.endswith(".json"):
            with open(f"data/{file}", "r", encoding="utf-8") as f:
                data = json.load(f)
            with open(f"api/{file}", "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2)
    print("API générée avec succès.")

if __name__ == "__main__":
    export_api()