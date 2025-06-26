# Format de l'API

L'API fournit des données sur les fraudes cryptographiques. Les fichiers JSON sont disponibles dans le dossier `api/`.

## Structure des fichiers

### scam_addresses.json
- **adresses_frauduleuses**: Liste des adresses cryptographiques frauduleuses.
  - `adresse`: Adresse crypto (ex. Bitcoin, Ethereum).
  - `type`: Type de blockchain (ex. BTC, ETH).
  - `source`: Source du signalement.
  - `signalé_le`: Date du signalement.

### scam_urls.json
- **urls_frauduleuses**: Liste des URLs frauduleuses.
  - `url`: URL du site frauduleux.
  - `type`: Type de fraude (ex. phishing).
  - `source`: Source du signalement.
  - `signalé_le`: Date du signalement.

## Exemple d'utilisation
```bash
curl https://<votre-domaine>/api/scam_addresses.json