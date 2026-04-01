import py
from datetime import datetime
import xml.etree.ElementTree as ET

# File paths
updates_file = "phrinusomyis_update.py"
rss_file = "rss.xml"

# Load updates
with open(updates_file, "r", encoding="utf-8") as f:
    updates = py.load(f)

# Create root RSS element
rss = ET.Element("rss", version="2.0")
channel = ET.SubElement(rss, "channel")

# Channel metadata
ET.SubElement(channel, "title").text = "PHRINUSOMYIS News Feed"
ET.SubElement(channel, "link").text = "https://www.phrinusomyis.com"
ET.SubElement(channel, "description").text = "Latest updates from PHRINUSOMYIS Intelligence and Events"
ET.SubElement(channel, "language").text = "en-us"
ET.SubElement(channel, "lastBuildDate").text = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")

# Add each update
for update in updates.get("updates", []):
    item = ET.SubElement(channel, "item")
    ET.SubElement(item, "title").text = update.get("title", "No Title")
    ET.SubElement(item, "link").text = update.get("link", "https://www.phrinusomyis.com")
    
    description = update.get("description", "")
    # Ensure International Debut is included if related
    if "International Debut" in description or "event" in update.get("title", "").lower():
        description += " International Debut: June 26, 2026 (West Africa)"
    
    ET.SubElement(item, "description").text = description
    
    # Use the date provided in PY, otherwise default to now
    pub_date = update.get("pubDate")
    if not pub_date:
        pub_date = datetime.utcnow().strftime("%a, %d %b %Y %H:%M:%S +0000")
    ET.SubElement(item, "pubDate").text = pub_date
    
    # GUID
    ET.SubElement(item, "guid").text = update.get("guid", update.get("link", ""))

# Save RSS feed
tree = ET.ElementTree(rss)
tree.write(rss_file, encoding="utf-8", xml_declaration=True)

print(f"RSS feed generated: {rss_file}")
