# 🛡️ Crypto Scam Tracker

Un système de surveillance et de détection des fraudes crypto-monnaies qui combine données on-chain et off-chain.

## 📋 Fonctionnalités

- **Surveillance d'adresses** : Détection d'adresses crypto frauduleuses
- **Vérification de tokens** : Contrôle de sécurité des nouveaux tokens
- **Base de données collaborative** : Collecte communautaire de données de fraude
- **API publique** : Accès programmatique aux données
- **Mises à jour automatiques** : Scraping régulier des sources fiables

## 🚀 Installation

```bash
git clone https://github.com/votre-username/crypto-scam-tracker.git
cd crypto-scam-tracker
pip install -r requirements.txt
```

## 💻 Utilisation

### Vérifier une adresse crypto
```python
from scripts.verify_address import verify_address

result = verify_address("1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa")
print(f"Adresse suspecte: {result['is_scam']}")
```

### Signaler une fraude
```python
from scripts.report_scams import report_scam

report_scam({
    "address": "suspicious_address",
    "type": "ponzi",
    "description": "Schéma de Ponzi identifié"
})
```

## 📊 Structure des données

- `data/scam_addresses.json` : Adresses crypto frauduleuses
- `data/scam_phones.json` : Numéros de téléphone suspects
- `data/scam_urls.json` : URLs malveillantes
- `data/scam_platforms.csv` : Plateformes frauduleuses
- `data/sources.json` : Sources de données
- `data/stats.json` : Statistiques générales
- `data/hashes.json` : Hashes de transactions suspectes

## 🔧 Scripts disponibles

| Script | Description |
|--------|-------------|
| `scrape_bitcoinabuse.py` | Scraping de BitcoinAbuse.com |
| `check_token_safety.py` | Vérification sécurité tokens |
| `verify_address.py` | Vérification d'adresses |
| `report_scams.py` | Signalement de fraudes |
| `generate_stats.py` | Génération de statistiques |
| `update_repo.py` | Mise à jour automatique |
| `export_api.py` | Export pour API |

## 🌐 API

L'API est disponible à l'adresse : `https://api.crypto-scam-tracker.com`

Endpoints principaux :
- `GET /addresses/{address}` - Vérifier une adresse
- `GET /stats` - Statistiques générales
- `POST /report` - Signaler une fraude

Documentation complète : [docs/api_format.md](docs/api_format.md)

## 🤝 Contribution

Consultez [CONTRIBUTING.md](CONTRIBUTING.md) pour les guidelines de contribution.

## 🔒 Sécurité

Pour signaler une vulnérabilité, consultez [SECURITY.md](SECURITY.md).

## 📄 Licence

Ce projet est sous licence MIT. Voir [LICENSE](LICENSE) pour plus de détails.

## ⚠️ Avertissement

Ce projet est fourni à des fins éducatives et de recherche. Toujours vérifier les informations via plusieurs sources avant de prendre des décisions financières.

## 📞 Contact

- 📧 Email : security@crypto-scam-tracker.com
- 🐦 Twitter : @CryptoScamTracker
- 💬 Telegram : t.me/cryptoscamtracker

---

⭐ Si ce projet vous aide, n'hésitez pas à lui donner une étoile !