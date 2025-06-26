from web3 import Web3

# Vérifier la sécurité d'un token
def check_token_safety(contract_address):
    w3 = Web3(Web3.HTTPProvider("https://mainnet.infura.io/v3/YOUR_INFURA_KEY"))
    # Exemple : Vérifier si l'adresse du contrat est signalée
    with open("data/hashes.json", "r", encoding="utf-8") as f:
        scams = json.load(f)
    if contract_address in [h["hash"] for h in scams["hachages_frauduleux"]]:
        print("Attention : Ce contrat est signalé comme frauduleux.")
    else:
        print("Ce contrat semble sûr.")

if __name__ == "__main__":
    check_token_safety("0x1234567890abcdef")