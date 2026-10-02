import json
import random
import time
import argparse
from scrapling.fetchers import DynamicFetcher

# Initialization
BASE_URL = "https://www.futbin.com"

def get_player_details(url, fetcher):
    """Extracts player details."""
    page = fetcher.fetch(url)

    # Isolate the main card
    main_card = page.css('.player-card-wrapper:not(.alternative-player-card)')
    card = main_card[0] if main_card else page

    # 1. Name, Version, Rating
    name = card.css('div.playercard-24-name::text').get()
    version = page.xpath("//div[normalize-space(text())='Squad']/following-sibling::a[1]/text()").get()
    rating = card.css('.playercard-24-rating::text').get()

    # 2. Main position and Alternatives
    main_pos = card.css('.playercard-24-position::text').get()
    alt_pos = list(dict.fromkeys([p.strip() for p in card.css('.playercard-24-alt-pos-sub::text').getall()]))

    # 3. Foot, Skills, Weak Foot
    foot = card.css('.playercard-24-right-foot::text').get()
    skills_wf = card.css('.playercard-24-right-skills::text').get()

    skills = skills_wf.split('★')[0] if skills_wf and '★' in skills_wf else "N/A"
    weak_foot = skills_wf.split('★')[1] if skills_wf and '★' in skills_wf else "N/A"

    # 4. Height and Body Type
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
        "Name": name.strip() if name else "N/A",
        "Version": version.strip() if version else "N/A",
        "Rating": rating.strip() if rating else "N/A",
        "Position": main_pos.strip() if main_pos else "N/A",
        "Alternative_Positions": alt_pos,
        "Foot": foot.strip().upper() if foot else "N/A",
        "Skills": skills.strip() if skills else "N/A",
        "Weak_Foot": weak_foot.strip() if weak_foot else "N/A",
        "Height": height.strip() if height else "N/A",
        "Body_Type": body_type.strip() if body_type else "Unique",
        "Stats": stats,
        "PlayStyles+": plus_list,
        "PlayStyles": norm_list
    }

def main():
    # Setup CLI Arguments
    parser = argparse.ArgumentParser(description="EA FC 24 Futbin Scraper CLI")
    parser.add_argument("-p", "--pages", type=int, default=2, help="Number of pages to scrape (default: 2)")
    parser.add_argument("--no-delay", action="store_true", help="Disable human simulation delays (Warning: Risk of IP ban)")
    parser.add_argument("-r", "--min-rating", type=int, default=0, help="Stop scraping if a player rating drops below this value")
    args = parser.parse_args()

    DynamicFetcher.configure(headless=True)
    fetcher = DynamicFetcher()

    full_database = []
    stop_scraping = False

    for i in range(1, args.pages + 1):
        if stop_scraping:
            break

        print(f"\n--- Analyzing page {i} ---")
        players_list_page = fetcher.fetch(f"{BASE_URL}/24/players?page={i}")

        # Delay on list page
        if not args.no_delay:
            time.sleep(3)

        player_links = list(set(players_list_page.css("a.player-row-playercard::attr(href)").getall()))

        for link in player_links:
            player_url = BASE_URL + link
            print(f"Scraping: {player_url}")
            try:
                player_data = get_player_details(player_url, fetcher)
                full_database.append(player_data)

                # Check if we reached the minimum rating limit
                if args.min_rating > 0 and player_data["Rating"] != "N/A":
                    try:
                        current_rating = int(player_data["Rating"])
                        if current_rating < args.min_rating:
                            print(f"🛑 Reached a player with rating {current_rating} (Threshold: {args.min_rating}). Stopping scraper.")
                            stop_scraping = True
                            break
                    except ValueError:
                        pass # Ignore if rating is somehow not a number

            except Exception as e:
                print(f"Error on {player_url}: {e}")

            # Delay on player page
            if not stop_scraping and not args.no_delay:
                time.sleep(random.uniform(1.5, 3.0))

    with open("database_complete.json", "w", encoding="utf-8") as f:
        json.dump(full_database, f, ensure_ascii=False, indent=4)

    print(f"\n✅ Scraping finished successfully! {len(full_database)} players saved.")

if __name__ == "__main__":
    main()
