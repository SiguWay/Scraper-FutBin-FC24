import json
import random
import time
from scrapling.fetchers import DynamicFetcher

# Initialisation
BASE_URL = "https://www.futbin.com"

def get_player_details(url, fetcher):
    """Extrait les détails d'un joueur."""
    page = fetcher.fetch(url)
    
    # Isolation de la carte principale
    main_card = page.css('.player-card-wrapper:not(.alternative-player-card)')
    card = main_card[0] if main_card else page
    
    # 1. Nom, Version, Note
    name = card.css('div.playercard-24-name::text').get()
    version = page.xpath("//div[normalize-space(text())='Squad']/following-sibling::a[1]/text()").get()
    rating = card.css('.playercard-24-rating::text').get()
    
    # 2. Position principale et Alternatives
    main_pos = card.css('.playercard-24-position::text').get()
    alt_pos = list(dict.fromkeys([p.strip() for p in card.css('.playercard-24-alt-pos-sub::text').getall()]))
    
    # 3. Pied, Skills, Weak Foot
    foot = card.css('.playercard-24-right-foot::text').get()
    skills_wf = card.css('.playercard-24-right-skills::text').get()
    
    skills = skills_wf.split('★')[0] if skills_wf and '★' in skills_wf else "N/A"
    weak_foot = skills_wf.split('★')[1] if skills_wf and '★' in skills_wf else "N/A"
    
    # 4. Taille et Body Type
    height = card.xpath("//div[normalize-space(text())='Height']/following-sibling::div[1]/text()").get()
    body_type = card.xpath("//div[normalize-space(text())='B.Type']/following-sibling::div[1]/text()").get()
    
    # 5. PlayStyles
    ps_container = page.css('.player-info-box-playerstyles .player-abilities-wrapper:not(.hidden)')
    ps_plus_els = ps_container.css('a.psplus .text-ellipsis::text').getall()
    ps_norm_els = ps_container.css('a.playStyle-table-icon.active:not(.psplus) .text-ellipsis::text').getall()
    
    plus_list = list(dict.fromkeys([p.strip() for p in ps_plus_els]))
    norm_list = list(dict.fromkeys([p.strip() for p in ps_norm_els if p.strip() not in plus_list]))
    
    # 6. Stats
    stats = {
        stat: card.xpath(f'.//span[contains(text(), "{stat}")]/preceding-sibling::div[contains(@class, "playercard-stat-number")]/text()').get()
        for stat in ["Pac", "Sho", "Pas", "Dri", "Def", "Phy"]
    }
             
    return {
        "Nom": name.strip() if name else "N/A",
        "Version": version.strip() if version else "N/A",
        "Note": rating.strip() if rating else "N/A",
        "Position": main_pos.strip() if main_pos else "N/A",
        "Position_Alt": alt_pos,
        "Pied": foot.strip().upper() if foot else "N/A",
        "Skills": skills.strip() if skills else "N/A",
        "WeakFoot": weak_foot.strip() if weak_foot else "N/A",
        "Taille": height.strip() if height else "N/A",
        "BodyType": body_type.strip() if body_type else "Unique",
        "Stats": stats,
        "PlayStyles+": plus_list,
        "PlayStyles": norm_list
    }

def main():
    fetcher = DynamicFetcher(headless=True)
    full_database = []
    pages_to_scrape = 18 

    for i in range(1, pages_to_scrape + 1):
        print(f"\n--- Analyse page {i} ---")
        list_page = fetcher.fetch(f"{BASE_URL}/24/players?page={i}")
        time.sleep(3)
        
        player_links = list(set(list_page.css("a.player-row-playercard::attr(href)").getall()))
        
        for link in player_links:
            player_url = BASE_URL + link
            print(f"Scraping : {player_url}")
            try:
                player_data = get_player_details(player_url, fetcher)
                full_database.append(player_data)
            except Exception as e:
                print(f"Erreur sur {player_url}: {e}")
            
            time.sleep(random.uniform(1.5, 3.0))

    with open("database_complete.json", "w", encoding="utf-8") as f:
        json.dump(full_database, f, ensure_ascii=False, indent=4)

    print("\n✅ Scraping terminé avec succès !")

if __name__ == "__main__":
    main()
