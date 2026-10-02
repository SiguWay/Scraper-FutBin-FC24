*🌍 [Lire en français](README_fr.md)*

# ⚽ FC24 Futbin Scraper

A robust Python web scraper built using the **Scrapling** library (`DynamicFetcher`) to extract detailed EA FC 24 player attributes, positions, stats, and PlayStyles from Futbin.com into a clean, consolidated JSON database.

## 🚀 Features
- **Comprehensive Data Extraction**: Name, card version, rating, main and alternative positions, preferred foot, skill moves, weak foot, height, and body type (with a fallback to "Unique").
- **Advanced PlayStyles Management**: Strict separation between standard PlayStyles and PlayStyles+, automatically filtering out hidden alternative card versions.
- **Detailed In-Game Stats**: Accurate scraping of Pace, Shooting, Passing, Dribbling, Defending, and Physicality.
- **Anti-Bot Protections**: Implements random delays to mimic human behavior and avoid automated rate-limiting.

## 🛠️ Tech Stack
- **Python 3.10+**
- **Scrapling**

## 📦 Installation

pip install -r requirements.txt
python -m playwright install

1. Clone the repository:
   ```bash
   git clone [https://github.com/SiguWay/Scraper-FutBin-FC24.git](https://github.com/SiguWay/Scraper-FutBin-FC24.git)
   python -m pip install -r requirements.txt
   python -m playwright install
   cd Scraper-FutBin-FC24
