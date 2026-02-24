# SamaBoutik Pro - MVP Flask

Application web de gestion pour commerce d'alimentation générale (version MVP), inspirée de votre maquette.

## Fonctionnalités implémentées
- Tableau de bord (KPIs, graphiques, dernières factures)
- Gestion des produits & stocks
- Vue ventes / clients & commandes (résumé)
- Page de rapport de projet intégrée

## Lancer en local
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Ensuite ouvrir http://127.0.0.1:5000.

## Prochaines étapes
- Intégration MySQL
- Authentification et rôles (admin/employé)
- Facturation PDF
- APIs et déploiement
