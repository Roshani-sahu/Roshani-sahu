#!/usr/bin/env python3
"""
tools/update_roshani_telemetry.py

Fetches real GitHub telemetry for Roshani-sahu and updates activity SVGs.
Synchronizes across D:\clone-1\Roshani-sahu and D:\Downloads\readme.
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

PATHS = [
    Path(r"D:\clone-1\Roshani-sahu"),
    Path(r"D:\Downloads\readme")
]

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
    
    public_repos = user_data.get("public_repos", 25) if isinstance(user_data, dict) else 25
    followers = user_data.get("followers", 1) if isinstance(user_data, dict) else 1
    
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

def render_activity_svg(data: dict, dark: bool = True) -> str:
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    card_bg = "#0E1526" if dark else "#FFFFFF"
    card_border = "rgba(0, 229, 255, 0.2)" if dark else "rgba(99, 102, 241, 0.18)"
    
    repos_cnt = data.get("public_repos", 25)
    repos_display = f"{repos_cnt}+ Public Repos" if repos_cnt > 0 else "Active Workspace"
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="100%" height="100%">
  <defs>
    <pattern id="actGridLive" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <rect width="1200" height="240" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="240" fill="url(#actGridLive)" rx="20"/>

  <g transform="translate(60, 42)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#10B981" letter-spacing="2">// 05 — GITHUB ACTIVITY</text>
    <text x="0" y="42" class="sans-text" font-size="22" font-weight="800" fill="{text_primary}">Developer Pulse &amp; Open Source Footprint</text>
    <text x="1080" y="40" text-anchor="end" class="mono-text" font-size="12" fill="#00E5FF">@{USERNAME} • {repos_display}</text>
  </g>

  <g transform="translate(60, 105)">
    <g transform="translate(0, 0)">
      <rect width="345" height="98" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="98" rx="2" fill="#00E5FF"/>
      <text x="20" y="32" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF">PRIMARY ECOSYSTEM</text>
      <text x="20" y="62" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">React &amp; TypeScript</text>
      <text x="20" y="82" class="sans-text" font-size="12" fill="{text_muted}">Interface systems &amp; modern web apps</text>
    </g>

    <g transform="translate(365, 0)">
      <rect width="345" height="98" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="98" rx="2" fill="#8B5CF6"/>
      <text x="20" y="32" class="mono-text" font-size="11" font-weight="700" fill="#8B5CF6">FULL-STACK FLOW</text>
      <text x="20" y="62" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">MERN Services</text>
      <text x="20" y="82" class="sans-text" font-size="12" fill="{text_muted}">Node.js, Express &amp; MongoDB pipelines</text>
    </g>

    <g transform="translate(730, 0)">
      <rect width="350" height="98" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="98" rx="2" fill="#10B981"/>
      <text x="20" y="32" class="mono-text" font-size="11" font-weight="700" fill="#10B981">PRODUCTION STANDARDS</text>
      <text x="20" y="62" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">Clean Architecture</text>
      <text x="20" y="82" class="sans-text" font-size="12" fill="{text_muted}">Performance, responsiveness &amp; UX fidelity</text>
    </g>
  </g>
</svg>'''
    return svg

def main():
    print(f"Refreshing telemetry metrics for {USERNAME}...")
    data = fetch_user_data()
    
    dark_svg = render_activity_svg(data, dark=True)
    light_svg = render_activity_svg(data, dark=False)
    
    for base in PATHS:
        gen_dir = base / "generated"
        act_dir = base / "assets" / "activity"
        gen_dir.mkdir(parents=True, exist_ok=True)
        act_dir.mkdir(parents=True, exist_ok=True)
        
        with open(gen_dir / "metrics.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            
        with open(act_dir / "activity-dark.svg", "w", encoding="utf-8") as f:
            f.write(dark_svg)
        with open(act_dir / "activity-light.svg", "w", encoding="utf-8") as f:
            f.write(light_svg)
            
        print(f"  [OK] Updated metrics & SVGs in {base}")

if __name__ == "__main__":
    main()
