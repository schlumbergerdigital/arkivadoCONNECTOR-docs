"""Ergaenzt die von Zensical erzeugte sitemap.xml um <lastmod>-Angaben.

Das Sitemap-Template von Zensical kennt nur die kanonische URL und keine
Datumsangaben. Der Zeitpunkt der letzten inhaltlichen Aenderung wird daher aus
dem letzten Git-Commit der jeweiligen Quelldatei abgeleitet.

Aufruf nach dem Build:  python seo_postbuild.py
"""

from __future__ import annotations

import re
import subprocess
import sys
from datetime import date
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parent
DOCS_DIR = ROOT / "docs"
SITEMAP = ROOT / "site" / "sitemap.xml"

LOC_PATTERN = re.compile(r"(?P<indent>[ \t]*)<loc>(?P<url>[^<]+)</loc>")


def source_for(url: str) -> Path | None:
    """Ermittelt die Markdown-Quelldatei zu einer Sitemap-URL."""
    path = unquote(urlparse(url).path).strip("/")
    if not path:
        return DOCS_DIR / "index.md"

    for candidate in (DOCS_DIR / f"{path}.md", DOCS_DIR / path / "index.md"):
        if candidate.is_file():
            return candidate
    return None


def last_modified(path: Path) -> str | None:
    """Liefert das Datum der letzten Aenderung einer Datei als ISO-Datum.

    Bevorzugt wird der letzte Commit; fuer noch nicht committete Dateien
    dient der Zeitstempel im Dateisystem als Rueckfallebene.
    """
    try:
        result = subprocess.run(
            ["git", "log", "-1", "--format=%cs", "--", str(path)],
            cwd=ROOT,
            capture_output=True,
            text=True,
            check=True,
        )
        stamp = result.stdout.strip()
        if stamp:
            return stamp
    except (OSError, subprocess.CalledProcessError):
        pass

    try:
        return date.fromtimestamp(path.stat().st_mtime).isoformat()
    except OSError:
        return None


def main() -> int:
    if not SITEMAP.is_file():
        print(f"FEHLER: {SITEMAP} nicht gefunden - zuerst bauen.", file=sys.stderr)
        return 1

    content = SITEMAP.read_text(encoding="utf-8")
    if "<lastmod>" in content:
        print("Sitemap enthaelt bereits <lastmod> - nichts zu tun.")
        return 0

    annotated = 0
    skipped: list[str] = []

    def replace(match: re.Match[str]) -> str:
        nonlocal annotated
        url = match.group("url")
        indent = match.group("indent")
        original = match.group(0)

        source = source_for(url)
        if source is None:
            skipped.append(url)
            return original

        stamp = last_modified(source)
        if stamp is None:
            skipped.append(url)
            return original

        annotated += 1
        return f"{original}\n{indent}<lastmod>{stamp}</lastmod>"

    content = LOC_PATTERN.sub(replace, content)
    SITEMAP.write_text(content, encoding="utf-8")

    print(f"sitemap.xml: {annotated} Eintraege mit <lastmod> versehen.")
    for url in skipped:
        print(f"  ohne Datum: {url}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
