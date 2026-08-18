"""Verifiziert die SEO-Ausgabe nach dem Build. Nur Leseoperationen."""

import json
import re
from collections import Counter
from pathlib import Path

SITE = Path("site")

pages = sorted(SITE.rglob("*.html"))
print(f"HTML-Seiten: {len(pages)}")

# 1. Keine rohen .md-Links
md_links = [
    (p.relative_to(SITE).as_posix(), m)
    for p in pages
    for m in re.findall(r'href="[^"]*\.md"', p.read_text(encoding="utf-8"))
]
print(f"Rohe .md-Links: {len(md_links)}")
for name, link in md_links[:5]:
    print(f"   {name}: {link}")

# 2. JSON-LD
types: Counter[str] = Counter()
invalid = 0
for p in pages:
    for block in re.findall(
        r'<script type="application/ld\+json">(.*?)</script>',
        p.read_text(encoding="utf-8"),
        re.S,
    ):
        try:
            types[json.loads(block).get("@type", "?")] += 1
        except json.JSONDecodeError:
            invalid += 1
            print(f"   ungueltiges JSON-LD in {p.relative_to(SITE)}")
print(f"JSON-LD: {sum(types.values())} gueltig, {invalid} ungueltig -> {dict(types)}")

# 3. Startseite und 404
home = (SITE / "index.html").read_text(encoding="utf-8")
og_website = 'og:type" content="website' in home
print(f"Startseite og:type=website: {og_website}")
print(f"Google-Fonts-Request: {'fonts.googleapis.com' in home}")
print(f"unpkg-Shim: {'unpkg.com' in home}")

nf = (SITE / "404.html").read_text(encoding="utf-8")
print(f"404 noindex: {'noindex, follow' in nf}")

# 4. Sitemap
sm = (SITE / "sitemap.xml").read_text(encoding="utf-8")
locs = re.findall(r"<loc>(.*?)</loc>", sm)
print(f"Sitemap: {len(locs)} URLs, {sm.count('<lastmod>')} lastmod")
bad = [u for u in locs if u.endswith(".md") or "%20" in u or ".html" in u]
print(f"Sitemap-URLs auffaellig: {bad if bad else 'keine'}")

# 5. Interne Links, die auf keine gebaute Seite zeigen
print(f"robots.txt vorhanden: {(SITE / 'robots.txt').exists()}")
