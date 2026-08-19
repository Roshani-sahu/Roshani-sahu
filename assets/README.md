# Roshani Sahu — Visual Asset Architecture

This repository uses a custom, responsive, and animated SVG asset pipeline engineered specifically for **Roshani Sahu** (Frontend Engineer & MERN Developer).

## Directory Structure

- `assets/hero/` — Animated HUD hero banner featuring glassmorphic frames, live status indicators, tech pillars, and ambient cyber-glows.
- `assets/stack/` — 4-tier interactive component and data flow architecture with traveling photon energy pulses across interface, motion, API, and cloud layers.
- `assets/projects/` — Flagship project showcase cards featuring Magdha Studios, Get2Vacation CMS, Get2Vacations Portal, and Royal IT Corporate Portal.
- `assets/focus/` — Engineering domain distribution, competency matrix, and strategic problem-solving principles.
- `assets/activity/` — Live developer activity and telemetry pulse synced with GitHub.
- `assets/footer/` — High-fidelity interactive button nodes linking to GitHub, LinkedIn, and direct Email.

## Design & Color System

| Token | Dark Mode | Light Mode | Semantic Role |
|---|---|---|---|
| Background | `#0B0F19` | `#F8FAFC` | Deep Obsidian / Crisp Paper |
| Surface Card | `#111827` | `#FFFFFF` | Elevated Glass Surface |
| Accent Primary | `#00E5FF` | `#0284C7` | Electric Cyan / Technical Focus |
| Accent Secondary | `#8B5CF6` | `#7C3AED` | Neon Violet / Interaction & Motion |
| Accent Success | `#10B981` | `#059669` | Emerald / Live Indicators & Status |
| Text Primary | `#F8FAFC` | `#0F172A` | High-contrast Typography |
| Text Secondary | `#94A3B8` | `#475569` | Labels & Descriptions |

## Regenerating Assets

To recompile all SVG assets or fetch updated telemetry:

```bash
# Generate all visual SVG assets
python tools/build_roshani_assets.py

# Fetch live telemetry from GitHub API
python tools/update_roshani_telemetry.py
```
