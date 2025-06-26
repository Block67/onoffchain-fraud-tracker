import json

# Vérifier si une adresse est frauduleuse
def verify_address(address):
    with open("data/scam_addresses.json", "r", encoding="utf-8") as f:
        data = json.load(f)
    if address in [a["adresse"] for a in data["adresses_frauduleuses"]]:
        print("Attention : Cette adresse est signalée comme frauduleuse.")
    else:
        print("Cette adresse semble sûre.")

if __name__ == "__main__":
    verify_address("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")