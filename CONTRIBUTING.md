# Guide de contribution

Merci de contribuer à Crypto Scam Tracker !

## Ajout d’une entrée

- Pour les adresses et numéros, ajoute une entrée JSON valide dans `data/`
- Pour les plateformes, ajoute une ligne CSV dans `data/scam_platforms.csv`
- Assure-toi que toutes les données ont une source fiable et datée

## Validation

Avant de faire une PR, lance :

```bash
python scripts/validate_json.py
