import json
import datetime
import requests

def update_global_seo():
    print("--- Starting Global SEO Engine ---")
    
    # 1. Load your Intelligence Brain
    try:
        with open('intelligence.json', 'r') as f:
            intel = json.load(f)
    except Exception as e:
        print(f"Error loading intelligence: {e}")
        return

    # 2. Update Sitemap.xml with the latest date
    today = datetime.datetime.now().strftime("%Y-%m-%d")
    
    # This logic automatically refreshes the lastmod tag for SEO ranking
    try:
        with open('sitemap.xml', 'r') as f:
            lines = f.readlines()
        
        with open('sitemap.xml', 'w') as f:
            for line in lines:
                if "<lastmod>" in line:
                    f.write(f"    <lastmod>{today}</lastmod>\n")
                else:
                    f.write(line)
        print(f"Sitemap.xml updated for global engines: {today}")
    except Exception as e:
        print(f"Sitemap update failed: {e}")

    # 3. Ping Search Engines (The "Boost")
    # This tells Google and Bing to come crawl your site NOW
    engines = [
        f"https://www.google.com/ping?sitemap=https://phrinusomyis.com/sitemap.xml",
        f"https://www.bing.com/ping?sitemap=https://phrinusomyis.com/sitemap.xml"
    ]
    
    for url in engines:
        try:
            requests.get(url, timeout=10)
            print(f"Pinged: {url.split('=')[0]}")
        except:
            print(f"Ping failed for {url}")

if __name__ == "__main__":
    update_global_seo()

