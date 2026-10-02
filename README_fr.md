*🌍 [Read this in English](README.md)*

# ⚽ FC24 Futbin Scraper

Un script de web scraping robuste développé en Python utilisant la librairie **Scrapling** (`DynamicFetcher`) pour extraire les données détaillées des joueurs de FUTBIN (EA FC 24) et générer une base de données JSON propre, consolidée et sans doublons.

## 🚀 Fonctionnalités
- **Extraction complète** : Nom, version de carte, note, position principale et alternatives, pied fort, gestes techniques, mauvais pied, taille et type de corps (avec repli sur "Unique").
- **Gestion fine des PlayStyles** : Séparation stricte et propre entre les PlayStyles standards et les PlayStyles+ (version améliorée), en ignorant les anciennes cartes alternatives cachées.
- **Statistiques détaillées** : Récupération précise des notes globales (Vitesse, Tir, Passe, Dribble, Défense, Physique).
- **Anti-bannissement** : Intégration de délais aléatoires pour simuler un comportement humain et contourner les protections anti-bot.

## 🛠️ Technologies utilisées
- **Python 3.10+**
- **Scrapling**

## 📦 Installation

pip install -r requirements.txt
python -m playwright install

1. Clonez le dépôt :
   ```bash
   git clone [https://github.com/SiguWay/Scraper-FutBin-FC24.git](https://github.com/SiguWay/Scraper-FutBin-FC24.git)
   python -m pip install -r requirements.txt
   python -m playwright install
   cd Scraper-FutBin-FC24
