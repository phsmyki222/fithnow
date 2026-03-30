import json
import os
from datetime import datetime
import seo_engine

# 1. Load the Intelligence Database
def load_intelligence():
    try:
        with open('intelligence.json', 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading intelligence.json: {e}")
        return {}

# 2. Save the Intelligence Database
def save_intelligence(data):
    with open('intelligence.json', 'w') as f:
        json.dump(data, f, indent=4)

# 3. THE SMART PARSER: Reads updates.txt
def parse_updates():
    if not os.path.exists('updates.txt'):
        return None
    
    with open('updates.txt', 'r') as f:
        new_content = f.read().strip()
    
    if not new_content:
        return None
        
    return new_content

# 4. Main Automation Loop
def run_automation():
    print(f"--- PHRINUSOMYIS Engine Start: {datetime.now()} ---")
    
    # Check for new updates
    raw_update = parse_updates()
    data = load_intelligence()
    
    if raw_update:
        print(f"New Update Found: {raw_update}")
        
        # Add update to the 'news' or 'events' section of your JSON
        if "news" not in data:
            data["news"] = []
            
        new_entry = {
            "date": datetime.now().strftime("%Y-%m-%d"),
            "content": raw_update
        }
        data["news"].insert(0, new_entry) # Put newest at the top
        
        save_intelligence(data)
        
        # CLEAR the updates.txt so it doesn't repeat next time
        with open('updates.txt', 'w') as f:
            f.write("")
        print("Intelligence.json updated and updates.txt cleared.")
    else:
        print("No new updates in updates.txt. Skipping data sync.")

    # Run the SEO Specialist
    seo_engine.update_global_seo()
    
    print("--- Engine Task Complete ---")

if __name__ == "__main__":
    run_automation()
