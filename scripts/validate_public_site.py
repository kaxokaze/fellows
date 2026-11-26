#!/usr/bin/env python3
"""Validate the public Fellows documentation site and support manifest.

This check uses only the Python standard library and makes no network calls.
"""

from __future__ import annotations

import json
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SITE = ROOT / "docs" / "index.html"
MANIFEST = ROOT / "docs" / "funding.json"
SITE_URL = "https://okay-fellows.netlify.app/"


class SiteInspector(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.netlify_attribution = False
        self.canonical_url = False
        self.og_url = False
        self.links: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = dict(attrs)
        if tag == "a":
            href = values.get("href")
            if href:
                self.links.append(href)
            if values.get("href") == "https://www.netlify.com/":
                self.netlify_attribution = True
        elif tag == "link" and values.get("rel") == "canonical":
            self.canonical_url = values.get("href") == SITE_URL
        elif tag == "meta" and values.get("property") == "og:url":
            self.og_url = values.get("content") == SITE_URL


def fail(message: str) -> None:
    print(f"FAIL: {message}", file=sys.stderr)
    raise SystemExit(1)


def main() -> None:
    for required in (SITE, MANIFEST, ROOT / "LICENSE", ROOT / "CODE_OF_CONDUCT.md"):
        if not required.is_file():
            fail(f"Required file is missing: {required.relative_to(ROOT)}")

    license_text = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if not license_text.startswith("MIT License"):
        fail("Root LICENSE does not identify the MIT License")

    html = SITE.read_text(encoding="utf-8")
    inspector = SiteInspector()
    inspector.feed(html)
    inspector.close()

    if not inspector.netlify_attribution or "This site is powered by Netlify" not in html:
        fail("The required Netlify attribution link is missing")
    if not inspector.canonical_url:
        fail("The canonical URL does not point to the Netlify site")
    if not inspector.og_url:
        fail("The Open Graph URL does not point to the Netlify site")
    if any("kaxokaze.github.io/fellows" in url for url in inspector.links):
        fail("A stale GitHub Pages link remains in the landing page")

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"docs/funding.json is invalid JSON: {exc}")

    if manifest.get("projects", [{}])[0].get("licenses") != ["spdx:MIT"]:
        fail("The support manifest does not identify the project as MIT licensed")
    contact = manifest.get("nonFinancialSupport", {}).get("contact", {})
    if contact.get("website") != SITE_URL:
        fail("The support manifest website does not match the Netlify site")
    support = manifest.get("nonFinancialSupport", {})
    if support.get("cashRequested") is not False:
        fail("The support manifest must explicitly say cashRequested is false")
    if support.get("financialSponsorshipRequested") is not False:
        fail("The support manifest must explicitly say financialSponsorshipRequested is false")

    print("PASS: Fellows public-site validation")
    print("- MIT licence and root Code of Conduct exist")
    print("- Netlify attribution, canonical URL, and social URL are correct")
    print("- Funding manifest is valid and consistently describes non-financial support")


if __name__ == "__main__":
    main()
