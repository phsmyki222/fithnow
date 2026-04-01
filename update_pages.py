import json as py
from datetime import datetime
import xml.etree.ElementTree as ET
import os
import requests
from bs4 import BeautifulSoup

# --------------------------
# File Paths
# --------------------------
updates_file = "phrinusomyis_update.py"
intelligence_file = "phrinusomyis_intelligence.py"
rss_file = "rss.xml"
keywords_file = "phrinusomyis_keywords.json"

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
# Load Data Safely
# --------------------------
if not os.path.exists(updates_file):
    print(f"{updates_file} not found, exiting.")
    exit()

if not os.path.exists(intelligence_file):
    print(f"{intelligence_file} not found, exiting.")
    exit()

if not os.path.exists(keywords_file):
    print(f"{keywords_file} not found, exiting.")
    exit()

with open(updates_file, "r", encoding="utf-8") as f:
    updates = py.load(f).get("updates", [])

with open(intelligence_file, "r", encoding="utf-8") as f:
    intelligence_data = py.load(f)

with open(keywords_file, "r", encoding="utf-8") as f:
    seo_keywords = py.load(f).get("keywords", [])

# --------------------------
# Generate RSS Feed
# --------------------------
rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")

ET.SubElement(channel, "title").text = "PHRINUSOMYIS News Feed"
ET.SubElement(channel, "link").text = "https://www.phrinusomyis.com"
ET.SubElement(channel, "description").text = "Latest updates from PHRINUSOMYIS Intelligence and Events"
ET.SubElement(channel, "language").text = "en-us"
ET.SubElement(channel, "lastBuildDate").text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

for update in updates:
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
# Update HTML Pages with SEO
# --------------------------
chunk_size = 10000  # Safe chunking for 20M+ keywords

for page in html_pages:
    if not os.path.exists(page):
        print(f"Warning: {page} not found, skipping.")
        continue

    with open(page, "r", encoding="utf-8") as f:
        content = f.read()

    # Inject updates
    updates_html = ""
    for update in updates:
        updates_html += f"<div class='update-item'><h3>{update.get('title')}</h3>"
        updates_html += f"<p>{update.get('description')}</p>"
        updates_html += f"<span>{update.get('pubDate', '')}</span></div>\n"
    content = content.replace("<!--UPDATES-HERE-->", updates_html)

    # Inject SEO keywords using BeautifulSoup safely
    soup = BeautifulSoup(content, "html.parser")
    if not soup.head:
        head_tag = soup.new_tag("head")
        if soup.html:
            soup.html.insert(0, head_tag)
        else:
            soup.insert(0, head_tag)
    else:
        head_tag = soup.head

    # Remove existing meta keywords
    for tag in head_tag.find_all("meta", attrs={"name": True}):
        if tag["name"].startswith("keywords"):
            tag.decompose()

    # Add SEO keywords in chunks to avoid browser/memory crash
    for i in range(0, len(seo_keywords), chunk_size):
        chunk = ", ".join(seo_keywords[i:i+chunk_size])
        meta_tag = soup.new_tag("meta", name=f"keywords-{i//chunk_size+1}", content=chunk)
        head_tag.append(meta_tag)

    with open(page, "w", encoding="utf-8") as f:
        f.write(str(soup))

    print(f"{page} updated with latest news and SEO keywords.")

# --------------------------
# Ping Search Engines
# --------------------------
sitemap_url = "https://www.phrinusomyis.com/rss.xml"
search_engines = {
    "Google": f"https://www.google.com/ping?sitemap={sitemap_url}",
    "Bing": f"https://www.bing.com/ping?sitemap={sitemap_url}",
    "Yandex": f"https://webmaster.yandex.com/ping?sitemap={sitemap_url}"
}

for name, url in search_engines.items():
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            print(f"{name} pinged successfully!")
        else:
            print(f"{name} ping failed, status code: {response.status_code}")
    except Exception as e:
        print(f"Error pinging {name}: {e}")

print("All updates complete!")
