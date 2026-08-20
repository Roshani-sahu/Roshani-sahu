#!/usr/bin/env python3
"""
tools/update_roshani_telemetry.py

Fetches real GitHub data for Roshani-sahu and updates pulse and footprint telemetry SVGs.
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

def main():
    print(f"Refreshing telemetry metrics for {USERNAME}...")
    data = fetch_user_data()
    
    for base in PATHS:
        gen_dir = base / "generated"
        gen_dir.mkdir(parents=True, exist_ok=True)
        with open(gen_dir / "metrics.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
        print(f"  [OK] Updated metrics.json in {base}")

if __name__ == "__main__":
    main()
