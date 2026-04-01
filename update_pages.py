import json
from datetime import datetime
import xml.etree.ElementTree as ET
import os

# File paths
updates_file = "phrinusomyis_update.json"
intelligence_json_file = "phrinusomyis_intelligence.json"
intelligence_py_file = "phrinusomyis_intelligence.py"  # optional import if needed
rss_file = "rss.xml"

# List of HTML pages to update
html_pages = [
    "index.html",
    "article.html",
    "articlefull.html",
    "event.html",
    "eventfull.html",
    "news.html",
    "newsfull.html",
    "intelligence.html",
    "press.html"
]

# Load updates
with open(updates_file, "r", encoding="utf-8") as f:
    updates = json.load(f)

# Load intelligence data
with open(intelligence_json_file, "r", encoding="utf-8") as f:
    intelligence_data = json.load(f)

# --- RSS Generation ---
rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")
ET.SubElement(channel, "title").text = "PHRINUSOMYIS News Feed"
ET.SubElement(channel, "link").text = "https://www.phrinusomyis.com"
ET.SubElement(channel, "description").text = "Latest updates from PHRINUSOMYIS Intelligence and Events"
ET.SubElement(channel, "language").text = "en-us"
ET.SubElement(channel, "lastBuildDate").text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

for update in updates.get("updates", []):
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = update.get("title", "No Title")
    ET.SubElement(item, "link").text = update.get("link", "https://www.phrinusomyis.com")
    description = update.get("description", "")
    # Ensure International Debut is correctly mentioned
    if "International Debut" not in description and "event" in update.get("title", "").lower():
        description += " International Debut: June 26, 2026 (West Africa)"
    ET.SubElement(item, "description").text = description
    pub_date = update.get("pubDate") or datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
    ET.SubElement(item, "pubDate").text = pub_date
    ET.SubElement(item, "guid").text = update.get("guid", update.get("link", ""))

ET.ElementTree(rss).write(rss_file, encoding="utf-8", xml_declaration=True)
print(f"RSS feed updated: {rss_file}")

# --- Update HTML Pages ---
for page in html_pages:
    if not os.path.exists(page):
        print(f"Warning: {page} not found, skipping.")
        continue
    
    with open(page, "r", encoding="utf-8") as f:
        content = f.read()

    # Inject latest updates into a designated div placeholder
    # Assumes each HTML has <!--UPDATES-HERE--> marker
    updates_html = ""
    for update in updates.get("updates", []):
        updates_html += f"<div class='update-item'><h3>{update.get('title')}</h3>"
        updates_html += f"<p>{update.get('description')}</p>"
        updates_html += f"<span>{update.get('pubDate', '')}</span></div>\n"

    content = content.replace("<!--UPDATES-HERE-->", updates_html)

    # Inject SEO keywords
    seo_keywords = intelligence_data.get("seo_keywords", [])
    # Combine into a single string for meta tag
    seo_content = ", ".join(seo_keywords[:20000000])  # supports huge list
    meta_tag = f'<meta name="keywords" content="{seo_content}">'
    if "<head>" in content:
        content = content.replace("<head>", f"<head>\n    {meta_tag}")
    else:
        content = meta_tag + "\n" + content

    with open(page, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{page} updated with latest news and SEO keywords.")

print("All pages updated successfully.")
