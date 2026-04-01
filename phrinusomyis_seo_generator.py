# phrinusomyis_seo_generator.py

import itertools
import json

# -----------------------------
# Define keyword categories
# -----------------------------
sports = ["football", "basketball", "tennis", "wrestling", "UFC", "WWE"]
clubs = ["Chelsea", "Manchester City", "Barcelona", "Lakers", "Yankees"]
stadiums = ["Wembley", "Camp Nou", "Madison Square Garden"]
events = ["World Cup", "Olympics", "Super Bowl", "Global Concert"]
brands = ["PHRINUSOMYIS", "Luxury Entertainment", "Legacy Moments"]

# Optional: regional keywords
regions = ["Global", "West Africa", "China", "Russia"]

# -----------------------------
# Generate dynamic keyword combinations
# -----------------------------
def generate_keywords():
    for sport, club, stadium, event, brand, region in itertools.product(
        sports, clubs, stadiums, events, brands, regions
    ):
        yield f"{sport} {club} {stadium} {event} {brand} {region}"

# -----------------------------
# Export to JSON for SEO use
# -----------------------------
def save_keywords(filename="phrinusomyis_keywords.json", max_keywords=None):
    keywords_list = []
    for i, keyword in enumerate(generate_keywords(), start=1):
        keywords_list.append(keyword)
        if max_keywords and i >= max_keywords:
            break

    seo_data = {
        "meta_title": "PHRINUSOMYIS - Engineering Legacy Moments Worldwide",
        "meta_description": "Experience luxury stadium-scale events with PHRINUSOMYIS.",
        "keywords": keywords_list,
        "sitemap_priority": 1.0,
        "sitemap_changefreq": "weekly"
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(seo_data, f, ensure_ascii=False, indent=2)

    print(f"Saved {len(keywords_list)} SEO keywords to {filename}")

# -----------------------------
# Main Execution
# -----------------------------
if __name__ == "__main__":
    # Example: generate first 100 keywords for testing
    save_keywords(max_keywords=100)
