import json
from datetime import datetime
import xml.etree.ElementTree as ET
import os
from bs4 import BeautifulSoup

# File paths
updates_file = "phrinusomyis_update.json"
intelligence_file = "phrinusomyis_intelligence.json"
keywords_file = "phrinusomyis_keywords.json"
rss_file = "rss.xml"

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

# --------------------------
# Load data
# --------------------------
with open(updates_file, "r", encoding="utf-8") as f:
    updates_data = json.load(f)

with open(intelligence_file, "r", encoding="utf-8") as f:
    intelligence_data = json.load(f)

with open(keywords_file, "r", encoding="utf-8") as f:
    seo_keywords = json.load(f).get("seo_keywords", [])

# --------------------------
# Generate RSS feed
# --------------------------
rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")

ET.SubElement(channel, "title").text = "PHRINUSOMYIS News Feed"
ET.SubElement(channel, "link").text = "https://www.phrinusomyis.com"
ET.SubElement(channel, "description").text = "Latest updates from PHRINUSOMYIS Intelligence and Events"
ET.SubElement(channel, "language").text = "en-us"
ET.SubElement(channel, "lastBuildDate").text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

for update in updates_data.get("updates", []):
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = update.get("title", "No Title")
    ET.SubElement(item, "link").text = update.get("link", "https://www.phrinusomyis.com")
    
    description = update.get("description", "")
    if "International Debut" not in description and "event" in update.get("title", "").lower():
        description += " International Debut: June 26, 2026 (West Africa)"
    ET.SubElement(item, "description").text = description
    
    pub_date = update.get("pubDate") or datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
    ET.SubElement(item, "pubDate").text = pub_date
    ET.SubElement(item, "guid").text = update.get("guid", update.get("link", ""))

ET.ElementTree(rss).write(rss_file, encoding="utf-8", xml_declaration=True)
print(f"RSS feed generated: {rss_file}")

# --------------------------
# Update HTML pages
# --------------------------
seo_content = ", ".join(seo_keywords)

for page in html_pages:
    if not os.path.exists(page):
        print(f"Warning: {page} not found, skipping.")
        continue

    with open(page, "r", encoding="utf-8") as f:
        content = f.read()

    # Inject updates into <!--UPDATES-HERE-->
    updates_html = ""
    for update in updates_data.get("updates", []):
        updates_html += f"<div class='update-item'><h3>{update.get('title')}</h3>"
        updates_html += f"<p>{update.get('description')}</p>"
        updates_html += f"<span>{update.get('pubDate', '')}</span></div>\n"
    content = content.replace("<!--UPDATES-HERE-->", updates_html)

    # Inject SEO keywords
    soup = BeautifulSoup(content, "html.parser")
    if soup.head:
        for tag in soup.head.find_all("meta", attrs={"name": "keywords"}):
            tag.decompose()
        meta_tag = soup.new_tag("meta", name="keywords", content=seo_content)
        soup.head.append(meta_tag)
    content = str(soup)

    with open(page, "w", encoding="utf-8") as f:
        f.write(content)

    print(f"{page} updated with news and SEO keywords.")

print("All updates complete!")
