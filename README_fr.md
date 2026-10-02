*🌍 [Read this in English](README.md)*

# ⚽ FC24 Futbin Scraper

Un script de web scraping robuste développé en Python utilisant la librairie **Scrapling** (`DynamicFetcher`) pour extraire les données détaillées des joueurs de FUTBIN (EA FC 24) et générer une base de données JSON propre, consolidée et sans doublons.

## 🚀 Fonctionnalités
- **Interface en ligne de commande (CLI)** : Options personnalisables pour gérer le nombre de pages, définir un seuil d'arrêt par note, ou désactiver les délais.
- **Extraction complète** : Nom, version de carte, note, position principale et alternatives, pied fort, gestes techniques, mauvais pied, taille et type de corps (avec repli sur "Unique").
- **Gestion fine des PlayStyles** : Séparation stricte et propre entre les PlayStyles standards et les PlayStyles+, en ignorant les anciennes cartes alternatives cachées.
- **Statistiques détaillées** : Récupération précise des notes globales (Vitesse, Tir, Passe, Dribble, Défense, Physique).
- **Anti-bannissement** : Intégration de délais aléatoires pour simuler un comportement humain et contourner les protections anti-bot.

## 🛠️ Technologies utilisées
- **Python 3.10+**
- **Scrapling**

## 📦 Installation

1. Clonez le dépôt :
```bash
   git clone [https://github.com/SiguWay/Scraper-FutBin-FC24.git](https://github.com/SiguWay/Scraper-FutBin-FC24.git)
   cd Scraper-FutBin-FC24
```

2. Installez les dépendances Python requises :
```bash
  python -m pip install -r requirements.txt
```

3. Téléchargez les binaires de navigateur nécessaires pour Playwright :
```bash
  python -m playwright install
```

## ⚙️ Utilisation

Le script intègre une interface en ligne de commande (CLI) simple et puissante.

Commandes de base :
```bash
  # Voir le menu d'aide avec toutes les options disponibles
  python futbin_scraper.py --help

    # Lancer le scraper avec les options par défaut (2 pages)
    python futbin_scraper.py
```

Exemples avancés :
```bash
  # Scraper exactement 5 pages
  python futbin_scraper.py -p 5
  
  # Scraper jusqu'à 100 pages, mais s'arrêter automatiquement si un joueur a une note inférieure à 88
  python futbin_scraper.py -p 100 -r 88
  
  # Scraper sans délai de sécurité (⚠️ Attention au risque élevé de bannissement IP)
  python futbin_scraper.py -p 3 --no-delay
```
  Les données extraites seront exportées dans un fichier database_complete.json.
