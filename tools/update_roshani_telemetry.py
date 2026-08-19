#!/usr/bin/env python3
"""
tools/update_roshani_telemetry.py

Fetches real GitHub metrics and activity telemetry for Roshani-sahu:
- Dynamic repository counts and language distribution
- Produces generated/metrics.json
- Updates assets/activity/telemetry-dark.svg & telemetry-light.svg
"""

import os
import sys
import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from pathlib import Path

USERNAME = os.getenv("GITHUB_USER", "Roshani-sahu")
TOKEN = os.getenv("GITHUB_TOKEN", "").strip()

ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "assets" / "activity"
GENERATED_DIR = ROOT / "generated"
ASSETS_DIR.mkdir(parents=True, exist_ok=True)
GENERATED_DIR.mkdir(parents=True, exist_ok=True)

def gh_api_request(url: str) -> dict | list:
    req = urllib.request.Request(url)
    req.add_header("User-Agent", f"{USERNAME}-telemetry-client")
    req.add_header("Accept", "application/vnd.github.v3+json")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.loads(resp.read().decode("utf-8"))
    except Exception as e:
        print(f"API notice on {url}: {e}", file=sys.stderr)
        return {}

def fetch_user_data() -> dict:
    user_data = gh_api_request(f"https://api.github.com/users/{USERNAME}")
    repos_data = gh_api_request(f"https://api.github.com/users/{USERNAME}/repos?per_page=100&sort=updated")
    
    public_repos = user_data.get("public_repos", 0) if isinstance(user_data, dict) else 0
    followers = user_data.get("followers", 0) if isinstance(user_data, dict) else 0
    
    lang_bytes = {}
    if isinstance(repos_data, list):
        for r in repos_data:
            if not r.get("fork"):
                lang = r.get("language")
                if lang:
                    lang_bytes[lang] = lang_bytes.get(lang, 0) + 1

    return {
        "username": USERNAME,
        "public_repos": public_repos,
        "followers": followers,
        "languages": lang_bytes,
        "updated_at": datetime.now(timezone.utc).isoformat()
    }

def render_telemetry_svg(data: dict, dark: bool = True) -> str:
    bg_color = "#0B0F19" if dark else "#F8FAFC"
    card_bg = "#111827" if dark else "#FFFFFF"
    card_border = "rgba(99, 102, 241, 0.2)" if dark else "rgba(99, 102, 241, 0.15)"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.06)" if dark else "rgba(99, 102, 241, 0.04)"
    
    repos_cnt = data.get("public_repos", 0)
    repos_display = f"{repos_cnt}+" if repos_cnt > 0 else "Active"
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <pattern id="telemGridLive" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <rect width="1200" height="320" fill="{bg_color}" rx="16"/>
  <rect width="1200" height="320" fill="url(#telemGridLive)" rx="16"/>
  <rect x="20" y="20" width="1160" height="280" rx="14" fill="none" stroke="{card_border}" stroke-width="1.5"/>

  <g transform="translate(40, 45)">
    <rect x="0" y="0" width="155" height="24" rx="4" fill="rgba(0, 229, 255, 0.1)" stroke="rgba(0, 229, 255, 0.3)" stroke-width="1"/>
    <text x="10" y="16" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">05 // TELEMETRY</text>
    <text x="175" y="18" class="sans-text" font-size="18" font-weight="700" fill="{text_primary}">Developer Activity &amp; Engineering Pulse</text>
    <text x="1120" y="17" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">GITHUB @{USERNAME}</text>
    <line x1="0" y1="36" x2="1120" y2="36" stroke="{card_border}" stroke-width="1"/>
  </g>

  <g transform="translate(40, 95)">
    <g transform="translate(0, 0)">
      <rect width="350" height="175" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="175" rx="2" fill="#00E5FF"/>
      <text x="24" y="32" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="1">PRIMARY DOMAIN</text>
      <text x="24" y="68" class="sans-text" font-size="28" font-weight="800" fill="{text_primary}">React &amp; UI</text>
      <text x="24" y="98" class="sans-text" font-size="13" fill="{text_secondary}">Frontend Application Architecture</text>
      <text x="24" y="122" class="sans-text" font-size="13" fill="{text_secondary}">Tailwind CSS • TypeScript • Vite</text>
      <text x="24" y="152" class="mono-text" font-size="11" fill="#10B981">● ACTIVE DEVELOPMENT</text>
    </g>

    <g transform="translate(385, 0)">
      <rect width="350" height="175" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="175" rx="2" fill="#8B5CF6"/>
      <text x="24" y="32" class="mono-text" font-size="11" font-weight="700" fill="#8B5CF6" letter-spacing="1">SERVICES &amp; DATA</text>
      <text x="24" y="68" class="sans-text" font-size="28" font-weight="800" fill="{text_primary}">MERN Stack</text>
      <text x="24" y="98" class="sans-text" font-size="13" fill="{text_secondary}">REST APIs • Node.js • Express</text>
      <text x="24" y="122" class="sans-text" font-size="13" fill="{text_secondary}">MongoDB • MySQL • JWT Auth</text>
      <text x="24" y="152" class="mono-text" font-size="11" fill="#8B5CF6">● END-TO-END FLOW</text>
    </g>

    <g transform="translate(770, 0)">
      <rect width="350" height="175" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="175" rx="2" fill="#10B981"/>
      <text x="24" y="32" class="mono-text" font-size="11" font-weight="700" fill="#10B981" letter-spacing="1">STANDARDS &amp; DELIVERY</text>
      <text x="24" y="68" class="sans-text" font-size="28" font-weight="800" fill="{text_primary}">Production</text>
      <text x="24" y="98" class="sans-text" font-size="13" fill="{text_secondary}">Modular Component Systems</text>
      <text x="24" y="122" class="sans-text" font-size="13" fill="{text_secondary}">Git Workflows • Cross-Browser QA</text>
      <text x="24" y="152" class="mono-text" font-size="11" fill="#00E5FF">● HIGH-PERFORMANCE CODE</text>
    </g>
  </g>
</svg>'''
    return svg

def main():
    print(f"Refreshing telemetry metrics for {USERNAME}...")
    data = fetch_user_data()
    
    with open(GENERATED_DIR / "metrics.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print(f"  [OK] Saved generated/metrics.json")
    
    dark_svg = render_telemetry_svg(data, dark=True)
    light_svg = render_telemetry_svg(data, dark=False)
    
    with open(ASSETS_DIR / "telemetry-dark.svg", "w", encoding="utf-8") as f:
        f.write(dark_svg)
    with open(ASSETS_DIR / "telemetry-light.svg", "w", encoding="utf-8") as f:
        f.write(light_svg)
    print(f"  [OK] Updated assets/activity/telemetry-*.svg")

if __name__ == "__main__":
    main()
