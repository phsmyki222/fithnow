import datetime
import os
import re

def update_intelligence():
    # 1. Setup Parameters
    html_file = "intelligence.html"
    target_date = "June 27, 2026"
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    
    # The Elite Status Message
    new_status_text = f"System Sync Active: {now} | Finalizing Infrastructure for the {target_date} Showcase."
    
    # 2. Path Security Check
    if not os.path.exists(html_file):
        print(f"CRITICAL ERROR: {html_file} not found in the root directory.")
        return

    # 3. Read the Current Architecture
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()

    print(f"Synchronizing Intelligence for {target_date}...")

    # 4. Update the Global Status Section
    global_pattern = r'(<section id="global-status">)(.*?)(</section>)'
    global_replacement = r'\1\n            <p>' + new_status_text + r'</p>\n        \3'
    
    if 'id="global-status"' in content:
        content = re.sub(global_pattern, global_replacement, content, flags=re.DOTALL)
        print("Updated: Global Status Hook.")

    # 5. Update the Regional Auth Section
    regional_pattern = r'(<p id="regional-auth">)(.*?)(</p>)'
    regional_replacement = r'\1Aligning with Regional Sports Ministries and International Partners for the ' + target_date + r' Debut.\3'
    
    if 'id="regional-auth"' in content:
        content = re.sub(regional_pattern, regional_replacement, content, flags=re.DOTALL)
        print("Updated: Regional Authority Hook.")

    # 6. Save the Synchronized File
    with open(html_file, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"Sync Complete. PHRINUSOMYIS Engine is now locked on {target_date}.")

if __name__ == "__main__":
    update_intelligence()

