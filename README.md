*🌍 [Lire en français](README_fr.md)*

# ⚽ FC24 Futbin Scraper

A robust Python web scraper built using the **Scrapling** library (`DynamicFetcher`) to extract detailed EA FC 24 player attributes, positions, stats, and PlayStyles from Futbin.com into a clean, consolidated JSON database.

## 🚀 Features
- **Command Line Interface (CLI)**: Customizable arguments for page limits, minimum rating thresholds, and delay toggles.
- **Comprehensive Data Extraction**: Name, card version, rating, main and alternative positions, preferred foot, skill moves, weak foot, height, and body type (with a fallback to "Unique").
- **Advanced PlayStyles Management**: Strict separation between standard PlayStyles and PlayStyles+, automatically filtering out hidden alternative card versions.
- **Detailed In-Game Stats**: Accurate scraping of Pace, Shooting, Passing, Dribbling, Defending, and Physicality.
- **Anti-Bot Protections**: Implements random delays to mimic human behavior and avoid automated rate-limiting.

## 🛠️ Tech Stack
- **Python 3.10+**
- **Scrapling**

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/SiguWay/Scraper-FutBin-FC24.git](https://github.com/SiguWay/Scraper-FutBin-FC24.git)
   cd Scraper-FutBin-FC24
    ```
2. Install the required Python packages:
   ```bash
   python -m pip install -r requirements.txt
    ```
3. Download the necessary browser binaries for Scrapling/Playwright:
  ```bash
   python -m playwright install
   ```
## ⚙️ Usage

The script features a built-in CLI for easy customization.

Basic Commands:
  ```bash
    # Show the help menu with all available options
    python futbin_scraper.py --help
    
    # Run the scraper with default options (2 pages)
    python futbin_scraper.py
    ```
Advanced Examples:
```bash
    # Scrape exactly 5 pages
    python futbin_scraper.py -p 5
    
    # Scrape up to 100 pages, but STOP automatically when hitting a player with a rating below 88
    python futbin_scraper.py -p 100 -r 88
    
    # Scrape without human-like delays **(⚠️ Warning: High risk of IP ban)**
    python futbin_scraper.py -p 3 --no-delay
```
The scraped data will be exported to a database_complete.json file.
