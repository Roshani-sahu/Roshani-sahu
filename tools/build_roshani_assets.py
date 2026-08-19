#!/usr/bin/env python3
"""
tools/build_roshani_assets.py

Generates the redesigned, cinematic, editorial SVG visual asset suite for Roshani Sahu:
- assets/hero/hero-dark.svg & hero-light.svg (Expansive 1200x580 animated centerpiece)
- assets/flow/flow-dark.svg & flow-light.svg (Continuous flowing pipeline 1200x360)
- assets/projects/builds-dark.svg & builds-light.svg (Editorial Featured Build + Sub-builds 1200x520)
- assets/capabilities/capabilities-dark.svg & capabilities-light.svg (Interconnected Domain Map 1200x420)
- assets/activity/activity-dark.svg & activity-light.svg (Compact GitHub Pulse 1200x240)
- assets/footer/signature-dark.svg & signature-light.svg (Portfolio signature 1200x220)
- assets/footer/btn-github-dark.svg, btn-linkedin-dark.svg, btn-email-dark.svg (& light variants)

Synchronizes across D:\clone-1\Roshani-sahu and D:\Downloads\readme.
"""

import os
import re
import shutil
import xml.etree.ElementTree as ET

PATHS = [
    r"D:\clone-1\Roshani-sahu",
    r"D:\Downloads\readme"
]

CACHE_DIR = os.path.join(PATHS[0], "tools", "skillicons_cache")
if not os.path.exists(CACHE_DIR):
    CACHE_DIR = os.path.join(PATHS[1], "tools", "skillicons_cache")

def get_icon_inner(icon_filename):
    """Read SVG file from skillicons_cache and return clean inner SVG markup."""
    path = os.path.join(CACHE_DIR, icon_filename)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        content = re.sub(r'<\?xml.*?\?>', '', content)
        m = re.search(r'<svg[^>]*>(.*)</svg>', content, re.DOTALL)
        if m:
            return m.group(1).strip()
    except Exception as e:
        print(f"Error reading {icon_filename}: {e}")
    return None

def xml_escape(text):
    if not isinstance(text, str):
        return text
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))

CUSTOM_ICONS = {
    "FramerMotion": '<path d="M4 4h16v8h-8zM4 12h8l8 8H4zM4 20l8-8v8z" fill="#00E5FF"/>',
    "GSAP": '<path d="M12 2L2 7v10l10 5 10-5V7L12 2zm0 2.8l7 3.5v7.4l-7 3.5-7-3.5V8.3l7-3.5z" fill="#88CE02"/><path d="M12 7l4 2.5v5L12 17l-4-2.5v-5L12 7z" fill="#88CE02" opacity="0.8"/>',
    "ChartJS": '<path d="M4 20h16M7 16v-4M12 16V8M17 16v-9" stroke="#FF6384" stroke-width="2.5" stroke-linecap="round"/>',
    "JWT": '<path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z" fill="#D63AFF" opacity="0.2"/><circle cx="12" cy="12" r="4" fill="#D63AFF"/>',
    "Sequelize": '<path d="M12 3L2 8.5v7L12 21l10-5.5v-7L12 3zm0 2.3l7.5 4.1-3.2 1.8-7.5-4.1 3.2-1.8z" fill="#52B0E7"/>',
    "Axios": '<path d="M12 3L3 18h4.5l4.5-8 4.5 8H21L12 3z" fill="#5A29E4"/>',
    "VSCode": '<path d="M17.5 2.5L7.2 10.5 3.5 7.5 1.5 8.5v7l2 1 3.7-3 10.3 8 4.5-2V4.5l-4.5-2zm0 4.2v10.6l-6.8-5.3 6.8-5.3z" fill="#007ACC"/>',
    "ReactRouter": '<path d="M4 6h16v3H4zm0 5h16v3H4zm0 5h10v3H4z" fill="#CA4245"/>',
}

# ==============================================================================
# 01. CINEMATIC HERO SECTION (1200 x 580)
# ==============================================================================
def build_hero_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    win_bg = "rgba(15, 23, 42, 0.75)" if dark else "rgba(255, 255, 255, 0.9)"
    win_border = "rgba(0, 229, 255, 0.25)" if dark else "rgba(99, 102, 241, 0.2)"
    card_shadow = "drop-shadow(0 20px 30px rgba(0, 0, 0, 0.5))" if dark else "drop-shadow(0 15px 25px rgba(0, 0, 0, 0.08))"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 580" width="100%" height="100%">
  <defs>
    <!-- Background Grid -->
    <pattern id="cinematicGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
      <circle cx="48" cy="48" r="0.75" fill="{grid_stroke}"/>
    </pattern>

    <!-- Shimmer Gradients -->
    <linearGradient id="heroTitleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="45%" stop-color="#8B5CF6"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>

    <linearGradient id="beamGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00F2FE" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </linearGradient>

    <radialGradient id="ambientCyanGlow" cx="15%" cy="30%" r="60%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="{ '0.12' if dark else '0.06' }"/>
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="ambientVioletGlow" cx="85%" cy="70%" r="65%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="{ '0.14' if dark else '0.06' }"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>

    <style>
      @keyframes floatSlow {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-10px) rotate(0.5deg); }}
      }}
      @keyframes scanline {{
        0% {{ transform: translateY(0px); opacity: 0; }}
        20% {{ opacity: 0.8; }}
        80% {{ opacity: 0.8; }}
        100% {{ transform: translateY(320px); opacity: 0; }}
      }}
      @keyframes pulseBeacon {{
        0%, 100% {{ transform: scale(1); opacity: 1; }}
        50% {{ transform: scale(1.3); opacity: 0.4; }}
      }}
      @keyframes codeGlow {{
        0%, 100% {{ filter: drop-shadow(0 0 6px rgba(0, 242, 254, 0.4)); }}
        50% {{ filter: drop-shadow(0 0 14px rgba(139, 92, 246, 0.8)); }}
      }}
      .floating-window {{ animation: floatSlow 7s ease-in-out infinite; transform-origin: center; }}
      .scanner {{ animation: scanline 5s ease-in-out infinite; }}
      .beacon {{ animation: pulseBeacon 2s ease-in-out infinite; transform-origin: center; }}
      .title-glow {{ animation: codeGlow 6s ease-in-out infinite; }}
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="580" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="580" fill="url(#cinematicGrid)" rx="20"/>
  <rect width="1200" height="580" fill="url(#ambientCyanGlow)" rx="20"/>
  <rect width="1200" height="580" fill="url(#ambientVioletGlow)" rx="20"/>

  <!-- Top Status / Navigation Header -->
  <g transform="translate(60, 48)">
    <circle cx="8" cy="8" r="4" fill="#10B981" class="beacon"/>
    <text x="24" y="12" class="mono-text" font-size="12" font-weight="700" fill="#10B981" letter-spacing="1.5">ROSHANI.ENGINEERING // ONLINE</text>
    
    <text x="1080" y="12" text-anchor="end" class="mono-text" font-size="12" fill="{text_muted}" letter-spacing="1">REACT SPECIALIST • MERN DEVELOPER</text>
    <line x1="0" y1="28" x2="1080" y2="28" stroke="{win_border}" stroke-width="1" stroke-dasharray="4,4"/>
  </g>

  <!-- Left Main Content Column -->
  <g transform="translate(60, 115)">
    <!-- Overline Badge -->
    <g transform="translate(0, 15)">
      <rect x="0" y="-14" width="235" height="26" rx="13" fill="rgba(0, 242, 254, 0.1)" stroke="rgba(0, 242, 254, 0.3)" stroke-width="1"/>
      <text x="16" y="3" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">FRONTEND ENGINEER</text>
    </g>

    <!-- Bold Striking Name -->
    <text x="0" y="105" class="sans-text title-glow" font-size="76" font-weight="900" letter-spacing="-2px" fill="url(#heroTitleGrad)">ROSHANI SAHU</text>

    <!-- Subtitle Role -->
    <text x="2" y="152" class="sans-text" font-size="24" font-weight="700" fill="{text_primary}" letter-spacing="0.2">
      Crafting High-Performance User Interfaces
    </text>

    <!-- Positioning Statement (Readable & Spacious) -->
    <text x="2" y="192" class="sans-text" font-size="16" fill="{text_secondary}" font-weight="400">
      Building thoughtful interfaces and turning ideas into production-ready web experiences.
    </text>
    <text x="2" y="218" class="sans-text" font-size="16" fill="{text_secondary}" font-weight="400">
      Specialized in scalable React component systems, fluid motion, and end-to-end MERN architecture.
    </text>

    <!-- Core Technology Pills -->
    <g transform="translate(0, 260)">
      <!-- Pill 1 -->
      <rect x="0" y="0" width="130" height="38" rx="8" fill="rgba(0, 229, 255, 0.08)" stroke="rgba(0, 229, 255, 0.25)" stroke-width="1"/>
      <text x="65" y="24" text-anchor="middle" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">⚛️ React.js</text>

      <!-- Pill 2 -->
      <rect x="142" y="0" width="135" height="38" rx="8" fill="rgba(139, 92, 246, 0.08)" stroke="rgba(139, 92, 246, 0.25)" stroke-width="1"/>
      <text x="209" y="24" text-anchor="middle" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">📘 TypeScript</text>

      <!-- Pill 3 -->
      <rect x="289" y="0" width="145" height="38" rx="8" fill="rgba(16, 185, 129, 0.08)" stroke="rgba(16, 185, 129, 0.25)" stroke-width="1"/>
      <text x="361" y="24" text-anchor="middle" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">🎨 Tailwind CSS</text>

      <!-- Pill 4 -->
      <rect x="446" y="0" width="145" height="38" rx="8" fill="rgba(236, 72, 153, 0.08)" stroke="rgba(236, 72, 153, 0.25)" stroke-width="1"/>
      <text x="518" y="24" text-anchor="middle" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">🚀 MERN Stack</text>
    </g>

    <!-- Professional Experience Indicator -->
    <g transform="translate(2, 330)">
      <circle cx="6" cy="6" r="4" fill="#00E5FF"/>
      <text x="20" y="10" class="mono-text" font-size="12.5" font-weight="600" fill="{text_muted}">
        ROYAL IT SERVICES <tspan fill="{text_primary}">• Frontend Developer</tspan> <tspan fill="#8B5CF6">•</tspan> 1.5+ Yrs Industry Experience
      </text>
    </g>
  </g>

  <!-- Right Centerpiece: Floating Futuristic Interface Viewport -->
  <g transform="translate(680, 110)" class="floating-window" style="filter: {card_shadow};">
    <!-- Browser/IDE Frame -->
    <rect width="460" height="360" rx="14" fill="{win_bg}" stroke="{win_border}" stroke-width="1.5"/>
    
    <!-- Window Header -->
    <path d="M 0 14 Q 0 0 14 0 L 446 0 Q 460 0 460 14 L 460 36 L 0 36 Z" fill="rgba(0, 229, 255, 0.06)"/>
    <circle cx="20" cy="18" r="4" fill="#EF4444"/>
    <circle cx="34" cy="18" r="4" fill="#F59E0B"/>
    <circle cx="48" cy="18" r="4" fill="#10B981"/>
    <text x="230" y="22" text-anchor="middle" class="mono-text" font-size="11" font-weight="600" fill="{text_muted}">App.tsx — Dynamic Interface Canvas</text>

    <!-- Code & Visual Conduits Inside Window -->
    <g transform="translate(24, 56)">
      <!-- Code block -->
      <text x="0" y="16" class="mono-text" font-size="12.5" fill="#8B5CF6">const <tspan fill="#00E5FF">RoshaniApp</tspan>: React.FC = () =&gt; {{</text>
      <text x="18" y="40" class="mono-text" font-size="12" fill="{text_secondary}">const [state, setState] = useMotionState();</text>
      
      <!-- Visual UI Layer Card (Dynamic Interface Preview) -->
      <g transform="translate(18, 58)">
        <rect width="375" height="150" rx="8" fill="rgba(0, 229, 255, 0.04)" stroke="rgba(0, 229, 255, 0.2)" stroke-width="1"/>
        
        <!-- Live Interface Elements -->
        <rect x="16" y="16" width="120" height="24" rx="4" fill="rgba(139, 92, 246, 0.15)"/>
        <text x="24" y="32" class="mono-text" font-size="10.5" font-weight="700" fill="#8B5CF6">&lt;UI.Navbar /&gt;</text>

        <rect x="150" y="16" width="205" height="24" rx="4" fill="rgba(0, 229, 255, 0.1)"/>
        <text x="160" y="32" class="mono-text" font-size="10.5" font-weight="700" fill="#00E5FF">&lt;InteractiveHero /&gt;</text>

        <!-- Simulated Grid -->
        <rect x="16" y="52" width="165" height="78" rx="6" fill="rgba(255, 255, 255, 0.03)" stroke="{win_border}" stroke-width="1"/>
        <text x="28" y="74" class="sans-text" font-size="11" font-weight="700" fill="{text_primary}">Performance &amp; UX</text>
        <text x="28" y="92" class="mono-text" font-size="10" fill="#10B981">● 60 FPS MOTION</text>
        <text x="28" y="112" class="mono-text" font-size="10" fill="{text_muted}">Tailwind + GSAP</text>

        <rect x="192" y="52" width="165" height="78" rx="6" fill="rgba(255, 255, 255, 0.03)" stroke="{win_border}" stroke-width="1"/>
        <text x="204" y="74" class="sans-text" font-size="11" font-weight="700" fill="{text_primary}">API Architecture</text>
        <text x="204" y="92" class="mono-text" font-size="10" fill="#00E5FF">● REST &amp; AXIOS</text>
        <text x="204" y="112" class="mono-text" font-size="10" fill="{text_muted}">Node • Express • Mongo</text>

        <!-- Scanning Beam -->
        <rect x="0" y="0" width="375" height="2" fill="url(#beamGrad)" class="scanner"/>
      </g>

      <text x="18" y="235" class="mono-text" font-size="12" fill="{text_secondary}">return &lt;DesignSystem theme="future" /&gt;;</text>
      <text x="0" y="260" class="mono-text" font-size="12.5" fill="#8B5CF6">}};</text>
    </g>
  </g>

  <!-- Bottom Ambient Beam Line -->
  <g transform="translate(60, 545)">
    <line x1="0" y1="0" x2="1080" y2="0" stroke="url(#heroTitleGrad)" stroke-width="2" stroke-linecap="round"/>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 02. CONTINUOUS ENGINEERING FLOW (1200 x 360)
# ==============================================================================
def build_flow_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    node_bg = "#0E1526" if dark else "#FFFFFF"
    node_border = "rgba(0, 229, 255, 0.25)" if dark else "rgba(99, 102, 241, 0.2)"

    PIPELINE_NODES = [
        {
            "step": "01",
            "title": "IDE &amp; WORKSPACE",
            "tech": "VS Code • Git • Vite",
            "icon": "CUSTOM_VSCode",
            "accent": "#00E5FF",
            "x": 120,
            "y": 190
        },
        {
            "step": "02",
            "title": "REACT &amp; TYPESCRIPT",
            "tech": "Components • State",
            "icon": "React-Dark.svg" if dark else "React-Light.svg",
            "accent": "#00F2FE",
            "x": 360,
            "y": 190
        },
        {
            "step": "03",
            "title": "UI MOTION &amp; STYLING",
            "tech": "Tailwind • GSAP • Framer",
            "icon": "TailwindCSS-Dark.svg" if dark else "TailwindCSS-Light.svg",
            "accent": "#8B5CF6",
            "x": 600,
            "y": 190
        },
        {
            "step": "04",
            "title": "API &amp; AUTH LAYER",
            "tech": "REST APIs • Axios • JWT",
            "icon": "CUSTOM_JWT",
            "accent": "#EC4899",
            "x": 840,
            "y": 190
        },
        {
            "step": "05",
            "title": "DATA &amp; CLOUD",
            "tech": "Node • Express • MongoDB",
            "icon": "NodeJS-Dark.svg" if dark else "NodeJS-Light.svg",
            "accent": "#10B981",
            "x": 1080,
            "y": 190
        }
    ]

    nodes_svg = ""
    for n in PIPELINE_NODES:
        accent = n["accent"]
        icon_key = n["icon"]
        if icon_key.startswith("CUSTOM_"):
            cname = icon_key.replace("CUSTOM_", "")
            inner_icon = CUSTOM_ICONS.get(cname, '<circle cx="12" cy="12" r="8" fill="#00E5FF"/>')
        else:
            inner_icon = get_icon_inner(icon_key) or '<circle cx="12" cy="12" r="8" fill="#00E5FF"/>'

        nodes_svg += f'''
        <!-- Node {n["step"]}: {n["title"]} -->
        <g transform="translate({n["x"]}, {n["y"]})">
          <!-- Outer Pulsing Halo -->
          <circle cx="0" cy="0" r="38" fill="{node_bg}" stroke="{accent}" stroke-width="2"/>
          <circle cx="0" cy="0" r="46" fill="none" stroke="{accent}" stroke-width="1" stroke-dasharray="3,3" opacity="0.4"/>
          
          <!-- Icon -->
          <g transform="translate(-14, -14) scale(1.15)">
            <svg width="24" height="24" viewBox="0 0 24 24">{inner_icon}</svg>
          </g>

          <!-- Step Label -->
          <text x="0" y="62" text-anchor="middle" class="mono-text" font-size="11" font-weight="700" fill="{accent}" letter-spacing="1">[{n["step"]}] {n["title"]}</text>
          <text x="0" y="80" text-anchor="middle" class="sans-text" font-size="12" fill="{text_secondary}">{n["tech"]}</text>
        </g>
        '''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 360" width="100%" height="100%">
  <defs>
    <pattern id="flowGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>

    <linearGradient id="pipeGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="25%" stop-color="#00F2FE"/>
      <stop offset="50%" stop-color="#8B5CF6"/>
      <stop offset="75%" stop-color="#EC4899"/>
      <stop offset="100%" stop-color="#10B981"/>
    </linearGradient>

    <style>
      @keyframes cruisePhoton {{
        0% {{ stroke-dashoffset: 960; }}
        100% {{ stroke-dashoffset: 0; }}
      }}
      .pipe-active {{
        stroke-dasharray: 20, 20;
        animation: cruisePhoton 8s linear infinite;
      }}
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="360" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="360" fill="url(#flowGrid)" rx="20"/>

  <!-- Section Title & Narrative -->
  <g transform="translate(60, 48)">
    <text x="0" y="16" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">// 02 — ARCHITECTURE PIPELINE</text>
    <text x="0" y="46" class="sans-text" font-size="24" font-weight="800" fill="{text_primary}">Engineering Flow: Ideation to Production</text>
    <text x="0" y="70" class="sans-text" font-size="14" fill="{text_secondary}">
      Continuous data flow from modular React components down through REST API services into scalable persistence.
    </text>
  </g>

  <!-- Connecting Backbone Conduit Line -->
  <g>
    <!-- Background Pipeline -->
    <path d="M 120 190 L 1080 190" fill="none" stroke="rgba(148, 163, 184, 0.15)" stroke-width="4"/>
    <!-- Animated Glowing Energy Line -->
    <path d="M 120 190 L 1080 190" fill="none" stroke="url(#pipeGrad)" stroke-width="4" class="pipe-active"/>
  </g>

  <!-- Pipeline Nodes -->
  {nodes_svg}
</svg>'''
    return svg


# ==============================================================================
# 03. EDITORIAL SELECTED BUILDS (1200 x 520)
# ==============================================================================
def build_projects_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    card_bg = "#0E1526" if dark else "#FFFFFF"
    card_border = "rgba(0, 229, 255, 0.2)" if dark else "rgba(99, 102, 241, 0.18)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 520" width="100%" height="100%">
  <defs>
    <pattern id="projGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>

    <linearGradient id="heroCardGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.15"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.05"/>
    </linearGradient>

    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="520" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="520" fill="url(#projGrid)" rx="20"/>

  <!-- Section Header -->
  <g transform="translate(60, 45)">
    <text x="0" y="16" class="mono-text" font-size="11" font-weight="700" fill="#8B5CF6" letter-spacing="2">// 03 — SELECTED BUILDS</text>
    <text x="0" y="46" class="sans-text" font-size="24" font-weight="800" fill="{text_primary}">Featured Engineering Implementations</text>
  </g>

  <!-- Left: PREMIER FEATURED BUILD (Dominant Presence) -->
  <g transform="translate(60, 105)">
    <!-- Container Card -->
    <rect width="560" height="375" rx="14" fill="{card_bg}" stroke="#00E5FF" stroke-width="1.5"/>
    <rect width="560" height="375" rx="14" fill="url(#heroCardGlow)"/>
    
    <!-- Top Badge -->
    <g transform="translate(28, 28)">
      <rect width="180" height="24" rx="12" fill="rgba(0, 229, 255, 0.15)" stroke="rgba(0, 229, 255, 0.4)" stroke-width="1"/>
      <text x="90" y="16" text-anchor="middle" class="mono-text" font-size="10.5" font-weight="700" fill="#00E5FF">★ FEATURED PRODUCTION</text>
    </g>

    <!-- Project Title -->
    <text x="28" y="92" class="sans-text" font-size="28" font-weight="900" fill="{text_primary}">Magdha Studios</text>
    <text x="28" y="116" class="sans-text" font-size="14" font-weight="600" fill="#8B5CF6">Interactive Game Promotion Platform</text>

    <!-- Description -->
    <text x="28" y="152" class="sans-text" font-size="14" fill="{text_secondary}">
      Engineered an interactive gaming showcase portal featuring modular
    </text>
    <text x="28" y="174" class="sans-text" font-size="14" fill="{text_secondary}">
      React components, fluid motion choreography, dynamic media sections,
    </text>
    <text x="28" y="196" class="sans-text" font-size="14" fill="{text_secondary}">
      and responsive layouts optimized for cross-device fidelity.
    </text>

    <!-- Engineering Highlight Box -->
    <g transform="translate(28, 225)">
      <rect width="504" height="65" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="{card_border}" stroke-width="1"/>
      <text x="16" y="24" class="mono-text" font-size="11" font-weight="700" fill="#10B981">ARCHITECTURAL HIGHLIGHT</text>
      <text x="16" y="46" class="sans-text" font-size="12.5" fill="{text_primary}">Reusable Component Library &amp; Smooth Animation Choreography</text>
    </g>

    <!-- Tech Badges -->
    <g transform="translate(28, 318)">
      <rect x="0" y="0" width="84" height="26" rx="5" fill="rgba(0, 229, 255, 0.1)"/>
      <text x="42" y="17" text-anchor="middle" class="mono-text" font-size="11" font-weight="600" fill="#00E5FF">React.js</text>

      <rect x="94" y="0" width="105" height="26" rx="5" fill="rgba(139, 92, 246, 0.1)"/>
      <text x="146" y="17" text-anchor="middle" class="mono-text" font-size="11" font-weight="600" fill="#8B5CF6">Tailwind CSS</text>

      <rect x="209" y="0" width="95" height="26" rx="5" fill="rgba(236, 72, 153, 0.1)"/>
      <text x="256" y="17" text-anchor="middle" class="mono-text" font-size="11" font-weight="600" fill="#EC4899">JavaScript</text>

      <rect x="314" y="0" width="85" height="26" rx="5" fill="rgba(16, 185, 129, 0.1)"/>
      <text x="356" y="17" text-anchor="middle" class="mono-text" font-size="11" font-weight="600" fill="#10B981">Motion FX</text>
    </g>
  </g>

  <!-- Right: SECONDARY BUILDS COLUMN (2 Sleek Cards) -->
  <g transform="translate(645, 105)">
    <!-- Build 02: Get2Vacation CMS -->
    <g transform="translate(0, 0)">
      <rect width="495" height="178" rx="12" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="178" rx="2" fill="#8B5CF6"/>
      
      <text x="24" y="32" class="mono-text" font-size="10.5" font-weight="700" fill="#8B5CF6" letter-spacing="1">PROJECT // 02</text>
      <text x="24" y="60" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">Get2Vacation CMS &amp; Admin Suite</text>
      <text x="24" y="85" class="sans-text" font-size="13" fill="{text_secondary}">
        Full CRUD dashboard for managing destination catalogs, tour packages,
      </text>
      <text x="24" y="105" class="sans-text" font-size="13" fill="{text_secondary}">
        and marketing campaigns with dynamic REST API integration via Axios.
      </text>
      
      <g transform="translate(24, 130)">
        <text x="0" y="16" class="mono-text" font-size="11" fill="{text_muted}">React • Node.js • Express • REST APIs • Axios</text>
      </g>
    </g>

    <!-- Build 03: Get2Vacations Portal & Royal IT -->
    <g transform="translate(0, 197)">
      <rect width="495" height="178" rx="12" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="178" rx="2" fill="#10B981"/>
      
      <text x="24" y="32" class="mono-text" font-size="10.5" font-weight="700" fill="#10B981" letter-spacing="1">PROJECT // 03</text>
      <text x="24" y="60" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">Get2Vacations Travel Experience</text>
      <text x="24" y="85" class="sans-text" font-size="13" fill="{text_secondary}">
        Modern travel portal with seamless client-side routing, query filters,
      </text>
      <text x="24" y="105" class="sans-text" font-size="13" fill="{text_secondary}">
        and scalable component architecture for rich travel itineraries.
      </text>
      
      <g transform="translate(24, 130)">
        <text x="0" y="16" class="mono-text" font-size="11" fill="{text_muted}">React • Tailwind CSS • React Router • REST Integration</text>
      </g>
    </g>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 04. INTERCONNECTED CAPABILITIES MAP (1200 x 420)
# ==============================================================================
def build_capabilities_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    hub_bg = "#0E1526" if dark else "#FFFFFF"
    hub_border = "rgba(0, 229, 255, 0.25)" if dark else "rgba(99, 102, 241, 0.2)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 420" width="100%" height="100%">
  <defs>
    <pattern id="capGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>

    <radialGradient id="centerGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.2"/>
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0"/>
    </radialGradient>

    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="420" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="420" fill="url(#capGrid)" rx="20"/>

  <!-- Section Header -->
  <g transform="translate(60, 45)">
    <text x="0" y="16" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">// 04 — CAPABILITIES &amp; DOMAINS</text>
    <text x="0" y="46" class="sans-text" font-size="24" font-weight="800" fill="{text_primary}">Technology Spectrum &amp; Core Competencies</text>
  </g>

  <!-- 4 Major Domain Columns (Spacious, Open & Clear) -->
  <g transform="translate(60, 110)">
    <!-- Domain 1: FRONTEND -->
    <g transform="translate(0, 0)">
      <rect width="255" height="260" rx="12" fill="{hub_bg}" stroke="{hub_border}" stroke-width="1.2"/>
      <rect width="255" height="4" rx="2" fill="#00E5FF"/>
      <text x="24" y="36" class="mono-text" font-size="12" font-weight="700" fill="#00E5FF" letter-spacing="1">01 // FRONTEND</text>
      <text x="24" y="65" class="sans-text" font-size="18" font-weight="800" fill="{text_primary}">Interface Architecture</text>
      
      <g transform="translate(24, 90)">
        <text x="0" y="16" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• React.js &amp; Vite</text>
        <text x="0" y="42" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• TypeScript &amp; ES6+</text>
        <text x="0" y="68" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Tailwind CSS</text>
        <text x="0" y="94" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• HTML5 &amp; CSS3</text>
        <text x="0" y="120" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• React Router</text>
      </g>
    </g>

    <!-- Domain 2: MOTION & UI -->
    <g transform="translate(275, 0)">
      <rect width="255" height="260" rx="12" fill="{hub_bg}" stroke="{hub_border}" stroke-width="1.2"/>
      <rect width="255" height="4" rx="2" fill="#8B5CF6"/>
      <text x="24" y="36" class="mono-text" font-size="12" font-weight="700" fill="#8B5CF6" letter-spacing="1">02 // MOTION &amp; UX</text>
      <text x="24" y="65" class="sans-text" font-size="18" font-weight="800" fill="{text_primary}">Interaction &amp; Visuals</text>
      
      <g transform="translate(24, 90)">
        <text x="0" y="16" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Framer Motion</text>
        <text x="0" y="42" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• GSAP &amp; ScrollTrigger</text>
        <text x="0" y="68" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Chart.js &amp; ApexCharts</text>
        <text x="0" y="94" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Micro-Interactions</text>
        <text x="0" y="120" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Responsive Fidelity</text>
      </g>
    </g>

    <!-- Domain 3: BACKEND & APIS -->
    <g transform="translate(550, 0)">
      <rect width="255" height="260" rx="12" fill="{hub_bg}" stroke="{hub_border}" stroke-width="1.2"/>
      <rect width="255" height="4" rx="2" fill="#EC4899"/>
      <text x="24" y="36" class="mono-text" font-size="12" font-weight="700" fill="#EC4899" letter-spacing="1">03 // SERVICES</text>
      <text x="24" y="65" class="sans-text" font-size="18" font-weight="800" fill="{text_primary}">Backend &amp; APIs</text>
      
      <g transform="translate(24, 90)">
        <text x="0" y="16" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Node.js &amp; Express</text>
        <text x="0" y="42" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• RESTful API Design</text>
        <text x="0" y="68" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• JWT &amp; Auth Flows</text>
        <text x="0" y="94" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Axios Integration</text>
        <text x="0" y="120" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• bcrypt Security</text>
      </g>
    </g>

    <!-- Domain 4: DATA & CLOUD -->
    <g transform="translate(825, 0)">
      <rect width="255" height="260" rx="12" fill="{hub_bg}" stroke="{hub_border}" stroke-width="1.2"/>
      <rect width="255" height="4" rx="2" fill="#10B981"/>
      <text x="24" y="36" class="mono-text" font-size="12" font-weight="700" fill="#10B981" letter-spacing="1">04 // PERSISTENCE</text>
      <text x="24" y="65" class="sans-text" font-size="18" font-weight="800" fill="{text_primary}">Data &amp; Tooling</text>
      
      <g transform="translate(24, 90)">
        <text x="0" y="16" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• MongoDB &amp; MySQL</text>
        <text x="0" y="42" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Sequelize ORM</text>
        <text x="0" y="68" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Git &amp; GitHub</text>
        <text x="0" y="94" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Postman &amp; npm</text>
        <text x="0" y="120" class="sans-text" font-size="13.5" font-weight="600" fill="{text_primary}">• Vercel &amp; Netlify</text>
      </g>
    </g>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 05. REFINED GITHUB ACTIVITY PULSE (1200 x 240)
# ==============================================================================
def build_activity_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    card_bg = "#0E1526" if dark else "#FFFFFF"
    card_border = "rgba(0, 229, 255, 0.2)" if dark else "rgba(99, 102, 241, 0.18)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="100%" height="100%">
  <defs>
    <pattern id="actGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="240" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="240" fill="url(#actGrid)" rx="20"/>

  <!-- Section Header -->
  <g transform="translate(60, 42)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#10B981" letter-spacing="2">// 05 — GITHUB ACTIVITY</text>
    <text x="0" y="42" class="sans-text" font-size="22" font-weight="800" fill="{text_primary}">Developer Pulse &amp; Open Source Footprint</text>
    <text x="1080" y="40" text-anchor="end" class="mono-text" font-size="12" fill="#00E5FF">@Roshani-sahu</text>
  </g>

  <!-- 3 Sleek Metric Chips -->
  <g transform="translate(60, 105)">
    <!-- Metric 1 -->
    <g transform="translate(0, 0)">
      <rect width="345" height="98" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="98" rx="2" fill="#00E5FF"/>
      <text x="20" y="32" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF">PRIMARY ECOSYSTEM</text>
      <text x="20" y="62" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">React &amp; TypeScript</text>
      <text x="20" y="82" class="sans-text" font-size="12" fill="{text_muted}">Interface systems &amp; modern web apps</text>
    </g>

    <!-- Metric 2 -->
    <g transform="translate(365, 0)">
      <rect width="345" height="98" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="98" rx="2" fill="#8B5CF6"/>
      <text x="20" y="32" class="mono-text" font-size="11" font-weight="700" fill="#8B5CF6">FULL-STACK FLOW</text>
      <text x="20" y="62" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">MERN Services</text>
      <text x="20" y="82" class="sans-text" font-size="12" fill="{text_muted}">Node.js, Express &amp; MongoDB pipelines</text>
    </g>

    <!-- Metric 3 -->
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


# ==============================================================================
# 06. PORTFOLIO SIGNATURE & CONNECT (1200 x 220)
# ==============================================================================
def build_signature_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 220" width="100%" height="100%">
  <defs>
    <linearGradient id="sigGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="50%" stop-color="#8B5CF6"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <rect width="1200" height="220" fill="{bg_color}" rx="20"/>

  <g transform="translate(60, 50)">
    <text x="0" y="20" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">// 06 — CONNECT</text>
    <text x="0" y="64" class="sans-text" font-size="32" font-weight="900" fill="{text_primary}">Let's build something meaningful.</text>
    <text x="0" y="98" class="sans-text" font-size="15" fill="{text_secondary}">
      Always open to discussing frontend architecture, React development, and engineering opportunities.
    </text>
  </g>

  <line x1="60" y1="185" x2="1140" y2="185" stroke="url(#sigGrad)" stroke-width="2" stroke-linecap="round"/>
</svg>'''
    return svg


def build_button_svg(channel="github", dark=True):
    bg_color = "#0E1526" if dark else "#FFFFFF"
    border_color = "rgba(0, 229, 255, 0.3)" if dark else "rgba(99, 102, 241, 0.25)"
    text_primary = "#F8FAFC" if dark else "#0F172A"

    if channel == "github":
        accent = "#00E5FF"
        label = "GitHub"
        handle = "@Roshani-sahu"
        icon = get_icon_inner("Github-Dark.svg" if dark else "Github-Light.svg") or '<circle cx="12" cy="12" r="8" fill="#00E5FF"/>'
    elif channel == "linkedin":
        accent = "#8B5CF6"
        label = "LinkedIn"
        handle = "in/roshani-sahu"
        icon = '<path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z" fill="#8B5CF6"/>'
    else:
        accent = "#10B981"
        label = "Email Direct"
        handle = "roshani032003@gmail.com"
        icon = '<path d="M20 4H4c-1.1 0-1.99.9-1.99 2L2 18c0 1.1.9 2 2 2h16c1.1 0 2-.9 2-2V6c0-1.1-.9-2-2-2zm0 4l-8 5-8-5V6l8 5 8-5v2z" fill="#10B981"/>'

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 360 84" width="100%" height="100%">
  <defs>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>
  <rect width="360" height="84" rx="10" fill="{bg_color}" stroke="{border_color}" stroke-width="1.5"/>
  <rect width="4" height="84" rx="2" fill="{accent}"/>
  
  <g transform="translate(20, 20) scale(1.8)">
    <svg width="24" height="24" viewBox="0 0 24 24">{icon}</svg>
  </g>

  <g transform="translate(80, 22)">
    <text x="0" y="16" class="sans-text" font-size="14" font-weight="700" fill="{text_primary}">{label}</text>
    <text x="0" y="36" class="mono-text" font-size="12" fill="{accent}">{handle}</text>
  </g>
</svg>'''
    return svg


def main():
    print("Building redesigned cinematic portfolio assets for Roshani Sahu...")

    targets = [
        ("hero", "hero-dark.svg", build_hero_svg(dark=True)),
        ("hero", "hero-light.svg", build_hero_svg(dark=False)),
        ("flow", "flow-dark.svg", build_flow_svg(dark=True)),
        ("flow", "flow-light.svg", build_flow_svg(dark=False)),
        ("projects", "builds-dark.svg", build_projects_svg(dark=True)),
        ("projects", "builds-light.svg", build_projects_svg(dark=False)),
        ("capabilities", "capabilities-dark.svg", build_capabilities_svg(dark=True)),
        ("capabilities", "capabilities-light.svg", build_capabilities_svg(dark=False)),
        ("activity", "activity-dark.svg", build_activity_svg(dark=True)),
        ("activity", "activity-light.svg", build_activity_svg(dark=False)),
        ("footer", "signature-dark.svg", build_signature_svg(dark=True)),
        ("footer", "signature-light.svg", build_signature_svg(dark=False)),
        ("footer", "btn-github-dark.svg", build_button_svg("github", dark=True)),
        ("footer", "btn-github-light.svg", build_button_svg("github", dark=False)),
        ("footer", "btn-linkedin-dark.svg", build_button_svg("linkedin", dark=True)),
        ("footer", "btn-linkedin-light.svg", build_button_svg("linkedin", dark=False)),
        ("footer", "btn-email-dark.svg", build_button_svg("email", dark=True)),
        ("footer", "btn-email-light.svg", build_button_svg("email", dark=False)),
    ]

    for base_path in PATHS:
        print(f"\nWriting to: {base_path}")
        assets_base = os.path.join(base_path, "assets")
        for subdir, filename, content in targets:
            dirpath = os.path.join(assets_base, subdir)
            os.makedirs(dirpath, exist_ok=True)
            filepath = os.path.join(dirpath, filename)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            
            # XML Validation
            try:
                ET.fromstring(content)
                print(f"  [OK] Validated XML: assets/{subdir}/{filename}")
            except ET.ParseError as err:
                print(f"  [ERROR] XML syntax error in assets/{subdir}/{filename}: {err}")

    print("\nAll assets successfully generated and synced across all paths!")

if __name__ == "__main__":
    main()
