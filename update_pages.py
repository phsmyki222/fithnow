import json
import random
import os
from bs4 import BeautifulSoup, Comment
from datetime import datetime

# -----------------------------
# File Names
# -----------------------------
HTML_PAGES = [
    'index.html',
    'article.html', 'articlefull.html',
    'event.html', 'eventfull.html',
    'news.html', 'newsfull.html',
    'intelligence.html',
    'press.html'
]

SEO_FILE = 'phrinusomyis_seo.json'
UPDATE_FILE = 'phrinusomyis_update.json'
INTELLIGENCE_FILE = 'phrinusomyis_intelligence.json'
RSS_FILE = 'rss.xml'

BATCH_SIZE = 50000  # Number of keywords to inject per run

# -----------------------------
# Load JSON Files
# -----------------------------
with open(SEO_FILE, 'r', encoding='utf-8') as f:
    seo_data = json.load(f)['keywords']

with open(UPDATE_FILE, 'r', encoding='utf-8') as f:
    updates_data = json.load(f)

with open(INTELLIGENCE_FILE, 'r', encoding='utf-8') as f:
    intelligence_data = json.load(f)

# -----------------------------
# Function: Inject SEO into HTML
# -----------------------------
def inject_seo(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Clear previous SEO meta
    for meta in soup.find_all('meta', {'name': 'keywords'}):
        meta.decompose()

    # Inject a batch of SEO keywords
    seo_batch = random.sample(seo_data, min(BATCH_SIZE, len(seo_data)))

    seo_comment_start = soup.new_string("<!-- SEO KEYWORDS START -->", Comment=True)
    soup.head.append(seo_comment_start)

    for entry in seo_batch:
        meta_tag = soup.new_tag("meta")
        meta_tag.attrs['name'] = 'keywords'
        meta_tag.attrs['content'] = f"{entry['keyword']}, {entry['backlink']}"
        soup.head.append(meta_tag)

    seo_comment_end = soup.new_string("<!-- SEO KEYWORDS END -->", Comment=True)
    soup.head.append(seo_comment_end)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"[SEO] {len(seo_batch)} keywords injected into {html_file}")

# -----------------------------
# Function: Inject Updates into HTML
# -----------------------------
def inject_updates(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Create an updates section
    updates_section = soup.find(id='updates')
    if not updates_section:
        updates_section = soup.new_tag('div', id='updates')
        soup.body.append(updates_section)
    else:
        updates_section.clear()

    for update in updates_data.get('updates', []):
        update_tag = soup.new_tag('p')
        update_tag.string = f"{update['date']} - {update['title']}"
        updates_section.append(update_tag)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))
    print(f"[Updates] Updates added to {html_file}")

# -----------------------------
# Function: Generate RSS
# -----------------------------
def generate_rss():
    rss_items = ""
    for update in updates_data.get('updates', []):
        rss_items += f"""
        <item>
            <title>{update['title']}</title>
            <link>{update['link']}</link>
            <description>{update['description']}</description>
            <pubDate>{update['date']}</pubDate>
        </item>
        """

    rss_content = f"""<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0">
<channel>
    <title>PHRINUSOMYIS Updates</title>
    <link>https://phrinusomyis.com</link>
    <description>Latest news and updates from PHRINUSOMYIS</description>
    {rss_items}
</channel>
</rss>
"""
    with open(RSS_FILE, 'w', encoding='utf-8') as f:
        f.write(rss_content)
    print(f"[RSS] Generated {RSS_FILE}")

# -----------------------------
# Main Update Loop
# -----------------------------
def main():
    for html_file in HTML_PAGES:
        if os.path.exists(html_file):
            inject_seo(html_file)
            inject_updates(html_file)
        else:
            print(f"[Warning] {html_file} does not exist.")

    generate_rss()
    print(f"[{datetime.now()}] Update complete.")

# -----------------------------
# Run
# -----------------------------
if __name__ == "__main__":
    main()
