#!/usr/bin/env python3
"""Validate the public Fellows site and its current funding manifest.

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

    support_section = html.split('id="support"', 1)[-1].split("</section>", 1)[0]
    for obsolete in ("Technical support — in kind, not cash", "Compute &amp; infrastructure",
                     "Developer tools", "Research guidance", "not asking for money"):
        if obsolete.lower() in support_section.lower():
            fail(f"An obsolete support request remains on the site: {obsolete}")

    try:
        manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        fail(f"docs/funding.json is invalid JSON: {exc}")

    projects = manifest.get("projects", [])
    if not projects or projects[0].get("licenses") != ["spdx:MIT"]:
        fail("The funding manifest does not identify the project as MIT licensed")

    requests = manifest.get("additionalSupportRequests", {})
    if "nonFinancialSupport" in manifest:
        fail("The obsolete nonFinancialSupport policy is still present")
    if requests.get("scope") != "Fellows is seeking only AI model/API credits and financial funding.":
        fail("The manifest does not state the current API-credit and financial-funding scope")
    if requests.get("aiApiCredits", {}).get("status") != "actively-seeking":
        fail("The manifest does not actively request AI API credits")
    if requests.get("financialFunding", {}).get("status") != "actively-seeking":
        fail("The manifest does not actively request financial funding")
    if requests.get("contact", {}).get("website") != SITE_URL:
        fail("The manifest contact website does not match the Netlify site")

    funding = manifest.get("funding", {})
    channels = funding.get("channels", [])
    plans = funding.get("plans", [])
    if not channels or not plans:
        fail("The funding manifest must contain at least one channel and one plan")
    channel_ids = {channel.get("guid") for channel in channels}
    if "bank-transfer" not in channel_ids:
        fail("The funding manifest must include the stated bank-transfer contact route")
    for plan in plans:
        if plan.get("status") != "active":
            fail(f"Funding plan is not active: {plan.get('guid', 'unknown')}")
        if not plan.get("channels") or any(channel_id not in channel_ids for channel_id in plan["channels"]):
            fail(f"Funding plan references a missing channel: {plan.get('guid', 'unknown')}")

    print("PASS: Fellows public-site validation")
    print("- MIT licence and root Code of Conduct exist")
    print("- Netlify attribution, canonical URL, and social URL are correct")
    print("- Funding manifest requests AI API credits and active financial support plans")


if __name__ == "__main__":
    main()
