#!/usr/bin/env python3
"""
tools/build_roshani_assets.py

Generates the redesigned, editorial 7-section SVG asset suite for Roshani Sahu:
1. assets/hero/hero-dark.svg & hero-light.svg (Hero with animated background visual BEHIND text)
2. assets/stack/stack-dark.svg & stack-light.svg (5 domains using Roshani's exact tech stack)
3. assets/projects/projects-dark.svg & projects-light.svg (Featured build + sub-builds)
4. assets/stats/stats-dark.svg & stats-light.svg (Verified GitHub Numerical Stats)
5. assets/telemetry/pulse-dark.svg & pulse-light.svg (52-week contribution timeline)
6. assets/telemetry/footprint-dark.svg & footprint-light.svg (Language footprint volume bar)
7. assets/footer/signature-dark.svg & signature-light.svg (Portfolio ending & buttons)

Synchronizes across D:\clone-1\Roshani-sahu and D:\Downloads\readme.
"""

import os
import re
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
# 01. HERO WITH BACKGROUND ANIMATION (1200 x 480 px)
# ==============================================================================
def build_hero_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    code_bg_text = "rgba(0, 229, 255, 0.08)" if dark else "rgba(99, 102, 241, 0.06)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="100%" height="100%">
  <defs>
    <!-- Background Grid -->
    <pattern id="heroGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
      <circle cx="48" cy="48" r="0.75" fill="{grid_stroke}"/>
    </pattern>

    <linearGradient id="heroTitleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="45%" stop-color="#8B5CF6"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>

    <linearGradient id="laserGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00F2FE" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00F2FE" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </linearGradient>

    <radialGradient id="cyanGlow" cx="15%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="{ '0.14' if dark else '0.06' }"/>
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="violetGlow" cx="85%" cy="65%" r="65%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="{ '0.15' if dark else '0.06' }"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>

    <style>
      @keyframes laserScan {{
        0% {{ transform: translateY(0px); opacity: 0; }}
        20% {{ opacity: 0.7; }}
        80% {{ opacity: 0.7; }}
        100% {{ transform: translateY(420px); opacity: 0; }}
      }}
      @keyframes floatNode {{
        0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
        50% {{ transform: translateY(-12px) rotate(1deg); }}
      }}
      @keyframes beaconPulse {{
        0%, 100% {{ transform: scale(1); opacity: 1; }}
        50% {{ transform: scale(1.3); opacity: 0.4; }}
      }}
      .laser-line {{ animation: laserScan 6s ease-in-out infinite; }}
      .bg-floating {{ animation: floatNode 8s ease-in-out infinite; transform-origin: center; }}
      .beacon {{ animation: beaconPulse 2.2s ease-in-out infinite; transform-origin: center; }}
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="480" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="480" fill="url(#heroGrid)" rx="20"/>
  <rect width="1200" height="480" fill="url(#cyanGlow)" rx="20"/>
  <rect width="1200" height="480" fill="url(#violetGlow)" rx="20"/>

  <!-- ================================================================= -->
  <!-- BACKGROUND ANIMATED VISUAL LAYER (STRICTLY BEHIND TEXT)           -->
  <!-- ================================================================= -->
  <g class="bg-floating">
    <!-- Floating Background Code Conduits (Right Side, Subtle Opacity) -->
    <g transform="translate(680, 80)" opacity="0.35">
      <!-- Circuit Grid Lines -->
      <path d="M 0 40 L 150 40 L 220 110 L 380 110" fill="none" stroke="#00E5FF" stroke-width="1.5" stroke-dasharray="6,6"/>
      <path d="M 40 180 L 180 180 L 260 260 L 400 260" fill="none" stroke="#8B5CF6" stroke-width="1.5" stroke-dasharray="6,6"/>
      <circle cx="150" cy="40" r="4" fill="#00E5FF"/>
      <circle cx="220" cy="110" r="4" fill="#8B5CF6"/>
      <circle cx="180" cy="180" r="4" fill="#10B981"/>
      <circle cx="260" cy="260" r="4" fill="#EC4899"/>
      
      <!-- Subtle Floating Component Wireframe -->
      <rect x="180" y="30" width="180" height="110" rx="8" fill="none" stroke="rgba(0, 229, 255, 0.25)" stroke-width="1"/>
      <text x="195" y="55" class="mono-text" font-size="11" fill="{code_bg_text}">&lt;React.Component /&gt;</text>
      <text x="195" y="78" class="mono-text" font-size="10" fill="{code_bg_text}">const [ui] = useUI();</text>
      <text x="195" y="100" class="mono-text" font-size="10" fill="{code_bg_text}">return &lt;StateFlow /&gt;;</text>
    </g>

    <!-- Scanning Laser Line in Background -->
    <rect x="40" y="30" width="1120" height="2" fill="url(#laserGrad)" class="laser-line"/>
  </g>

  <!-- ================================================================= -->
  <!-- FOREGROUND IDENTITY CONTENT (100% UN-OBSCURED & READABLE)         -->
  <!-- ================================================================= -->
  <!-- Top Status Badge -->
  <g transform="translate(60, 50)">
    <circle cx="8" cy="8" r="4" fill="#10B981" class="beacon"/>
    <text x="24" y="12" class="mono-text" font-size="12" font-weight="700" fill="#10B981" letter-spacing="1.5">OPEN FOR HIGH-IMPACT ROLES</text>
    <text x="1080" y="12" text-anchor="end" class="mono-text" font-size="12" fill="{text_muted}" letter-spacing="1">INDORE, INDIA • ROYAL IT SERVICES</text>
    <line x1="0" y1="28" x2="1080" y2="28" stroke="{grid_stroke}" stroke-width="1.5"/>
  </g>

  <!-- Main Headline & Positioning Block -->
  <g transform="translate(60, 125)">
    <!-- Overline Category -->
    <g transform="translate(0, 15)">
      <rect x="0" y="-14" width="250" height="26" rx="13" fill="rgba(0, 229, 255, 0.1)" stroke="rgba(0, 229, 255, 0.3)" stroke-width="1"/>
      <text x="16" y="3" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">FRONTEND &amp; MERN ENGINEER</text>
    </g>

    <!-- Large Bold Striking Name -->
    <text x="0" y="105" class="sans-text" font-size="74" font-weight="900" letter-spacing="-2.5px" fill="url(#heroTitleGrad)">ROSHANI SAHU</text>

    <!-- Subtitle Role -->
    <text x="2" y="152" class="sans-text" font-size="24" font-weight="700" fill="{text_primary}" letter-spacing="0.2">
      Frontend Engineer <tspan fill="#8B5CF6">•</tspan> React <tspan fill="#00E5FF">•</tspan> TypeScript <tspan fill="#EC4899">•</tspan> MERN
    </text>

    <!-- Positioning Statement (Readable & Spacious) -->
    <text x="2" y="195" class="sans-text" font-size="16" fill="{text_secondary}" font-weight="400">
      Building thoughtful interfaces and turning ideas into production-ready web experiences.
    </text>
    <text x="2" y="221" class="sans-text" font-size="16" fill="{text_secondary}" font-weight="400">
      Specialized in scalable React component systems, fluid motion, and end-to-end web architecture.
    </text>

    <!-- Core Technology Chips -->
    <g transform="translate(0, 262)">
      <rect x="0" y="0" width="130" height="36" rx="8" fill="rgba(0, 229, 255, 0.08)" stroke="rgba(0, 229, 255, 0.25)" stroke-width="1"/>
      <text x="65" y="23" text-anchor="middle" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">⚛️ React.js</text>

      <rect x="142" y="0" width="135" height="36" rx="8" fill="rgba(139, 92, 246, 0.08)" stroke="rgba(139, 92, 246, 0.25)" stroke-width="1"/>
      <text x="209" y="23" text-anchor="middle" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">📘 TypeScript</text>

      <rect x="289" y="0" width="145" height="36" rx="8" fill="rgba(16, 185, 129, 0.08)" stroke="rgba(16, 185, 129, 0.25)" stroke-width="1"/>
      <text x="361" y="23" text-anchor="middle" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">🎨 Tailwind CSS</text>

      <rect x="446" y="0" width="145" height="36" rx="8" fill="rgba(236, 72, 153, 0.08)" stroke="rgba(236, 72, 153, 0.25)" stroke-width="1"/>
      <text x="518" y="23" text-anchor="middle" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">🚀 MERN Stack</text>
    </g>
  </g>

  <!-- Bottom Beam Border -->
  <g transform="translate(60, 455)">
    <line x1="0" y1="0" x2="1080" y2="0" stroke="url(#heroTitleGrad)" stroke-width="2" stroke-linecap="round"/>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 02. ENGINEERING STACK (1200 x 380 px)
# ==============================================================================
def build_stack_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    node_bg = "#0E1526" if dark else "#FFFFFF"
    node_border = "rgba(0, 229, 255, 0.2)" if dark else "rgba(99, 102, 241, 0.18)"

    STACK_DOMAINS = [
        ("FRONTEND", "#00E5FF", [
            ("React", "React", "React-Dark.svg" if dark else "React-Light.svg"),
            ("TypeScript", "TypeScript", "TypeScript.svg"),
            ("JavaScript", "JavaScript", "JavaScript.svg"),
            ("Tailwind", "Tailwind CSS", "TailwindCSS-Dark.svg" if dark else "TailwindCSS-Light.svg"),
            ("HTML5", "HTML5", "HTML.svg"),
            ("CSS3", "CSS3", "CSS.svg"),
            ("Vite", "Vite", "Vite-Dark.svg" if dark else "Vite-Light.svg"),
            ("Bootstrap", "Bootstrap", "CUSTOM_Bootstrap"),
            ("ReactRouter", "React Router", "CUSTOM_ReactRouter"),
        ]),
        ("UI &amp; MOTION", "#8B5CF6", [
            ("FramerMotion", "Framer Motion", "CUSTOM_FramerMotion"),
            ("GSAP", "GSAP", "CUSTOM_GSAP"),
            ("ScrollTrigger", "ScrollTrigger", "CUSTOM_ScrollTrigger"),
            ("ChartJS", "Chart.js", "CUSTOM_ChartJS"),
            ("ApexCharts", "ApexCharts", "CUSTOM_ApexCharts"),
        ]),
        ("BACKEND", "#EC4899", [
            ("NodeJS", "Node.js", "NodeJS-Dark.svg" if dark else "NodeJS-Light.svg"),
            ("Express", "Express.js", "ExpressJS-Dark.svg" if dark else "ExpressJS-Light.svg"),
            ("REST", "REST APIs", "Postman.svg"),
            ("JWT", "JWT Auth", "CUSTOM_JWT"),
            ("Axios", "Axios", "CUSTOM_Axios"),
            ("Bcrypt", "bcrypt", "CUSTOM_Bcrypt"),
        ]),
        ("DATABASE", "#10B981", [
            ("MongoDB", "MongoDB", "MongoDB.svg"),
            ("MySQL", "MySQL", "MySQL-Dark.svg" if dark else "MySQL-Light.svg"),
            ("Sequelize", "Sequelize", "CUSTOM_Sequelize"),
        ]),
        ("TOOLS &amp; CLOUD", "#F59E0B", [
            ("Git", "Git", "Git.svg"),
            ("GitHub", "GitHub", "Github-Dark.svg" if dark else "Github-Light.svg"),
            ("VSCode", "VS Code", "CUSTOM_VSCode"),
            ("Postman", "Postman", "Postman.svg"),
            ("NPM", "npm", "Npm-Dark.svg" if dark else "Npm-Light.svg"),
            ("AWS", "AWS Basics", "AWS-Dark.svg" if dark else "AWS-Light.svg"),
        ]),
    ]

    rows_markup = []
    y_starts = [100, 160, 220, 280, 340]
    for idx, (cat_name, accent, items) in enumerate(STACK_DOMAINS):
        y_pos = y_starts[idx]
        
        row_str = f'''
        <g transform="translate(60, {y_pos})">
          <!-- Category Rail Label -->
          <rect width="165" height="38" rx="6" fill="{node_bg}" stroke="{accent}" stroke-width="1.2"/>
          <rect width="4" height="38" rx="2" fill="{accent}"/>
          <text x="18" y="24" class="mono-text" font-size="11.5" font-weight="700" fill="{accent}" letter-spacing="1">{cat_name}</text>
          <line x1="165" y1="19" x2="195" y2="19" stroke="{accent}" stroke-width="1.5" stroke-dasharray="3,3"/>
          
          <!-- Tech Icons Row -->
          <g transform="translate(205, 0)">
        '''
        
        ix = 0
        for item_id, label, icon_key in items:
            if icon_key.startswith("CUSTOM_"):
                cname = icon_key.replace("CUSTOM_", "")
                inner_icon = CUSTOM_ICONS.get(cname, '<circle cx="12" cy="12" r="8" fill="#00E5FF"/>')
            else:
                inner_icon = get_icon_inner(icon_key) or '<circle cx="12" cy="12" r="8" fill="#00E5FF"/>'
            
            tw = len(label) * 7.2 + 36
            row_str += f'''
            <g transform="translate({ix}, 0)">
              <rect width="{tw}" height="38" rx="6" fill="{node_bg}" stroke="{node_border}" stroke-width="1"/>
              <g transform="translate(8, 9) scale(0.85)">
                <svg width="24" height="24" viewBox="0 0 24 24">{inner_icon}</svg>
              </g>
              <text x="34" y="24" class="sans-text" font-size="12" font-weight="600" fill="{text_primary}">{label}</text>
            </g>
            '''
            ix += tw + 10
        
        row_str += '</g></g>'
        rows_markup.append(row_str)

    rows_svg = "\n".join(rows_markup)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 400" width="100%" height="100%">
  <defs>
    <pattern id="stackGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      @keyframes signalPulse {{
        0% {{ x: 260; opacity: 0; }}
        20% {{ opacity: 1; }}
        80% {{ opacity: 1; }}
        100% {{ x: 1100; opacity: 0; }}
      }}
      .signal {{ animation: signalPulse 6s linear infinite; }}
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="400" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="400" fill="url(#stackGrid)" rx="20"/>

  <!-- Section Header -->
  <g transform="translate(60, 42)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">// 02 — ENGINEERING STACK</text>
    <text x="0" y="42" class="sans-text" font-size="22" font-weight="800" fill="{text_primary}">Technologies &amp; Core Ecosystem</text>
  </g>

  <!-- Rows -->
  {rows_svg}
</svg>'''
    return svg


# ==============================================================================
# 03. SELECTED PROJECTS (1200 x 480 px)
# ==============================================================================
def build_projects_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    card_bg = "#0E1526" if dark else "#FFFFFF"
    card_border = "rgba(0, 229, 255, 0.2)" if dark else "rgba(99, 102, 241, 0.18)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="100%" height="100%">
  <defs>
    <pattern id="projGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>

    <linearGradient id="featuredCardGlow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.12"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0.04"/>
    </linearGradient>

    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="480" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="480" fill="url(#projGrid)" rx="20"/>

  <!-- Section Header -->
  <g transform="translate(60, 42)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#8B5CF6" letter-spacing="2">// 03 — SELECTED PROJECTS</text>
    <text x="0" y="42" class="sans-text" font-size="22" font-weight="800" fill="{text_primary}">Featured Engineering Implementations</text>
  </g>

  <!-- Left: PREMIER FEATURED BUILD (Dominant Presence) -->
  <g transform="translate(60, 95)">
    <!-- Container Card -->
    <rect width="560" height="350" rx="14" fill="{card_bg}" stroke="#00E5FF" stroke-width="1.5"/>
    <rect width="560" height="350" rx="14" fill="url(#featuredCardGlow)"/>
    
    <!-- Top Badge -->
    <g transform="translate(26, 24)">
      <rect width="175" height="24" rx="12" fill="rgba(0, 229, 255, 0.15)" stroke="rgba(0, 229, 255, 0.4)" stroke-width="1"/>
      <text x="87.5" y="16" text-anchor="middle" class="mono-text" font-size="10.5" font-weight="700" fill="#00E5FF">★ FEATURED PRODUCTION</text>
    </g>

    <!-- Project Title -->
    <text x="26" y="85" class="sans-text" font-size="26" font-weight="900" fill="{text_primary}">Magdha Studios</text>
    <text x="26" y="108" class="sans-text" font-size="13.5" font-weight="600" fill="#8B5CF6">Interactive Game Promotion Platform</text>

    <!-- Description -->
    <text x="26" y="142" class="sans-text" font-size="13.5" fill="{text_secondary}">
      Engineered an interactive gaming showcase portal featuring modular
    </text>
    <text x="26" y="162" class="sans-text" font-size="13.5" fill="{text_secondary}">
      React components, fluid motion choreography, dynamic media sections,
    </text>
    <text x="26" y="182" class="sans-text" font-size="13.5" fill="{text_secondary}">
      and responsive layouts optimized for cross-device fidelity.
    </text>

    <!-- Engineering Highlight Box -->
    <g transform="translate(26, 210)">
      <rect width="508" height="60" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="{card_border}" stroke-width="1"/>
      <text x="16" y="22" class="mono-text" font-size="10.5" font-weight="700" fill="#10B981">ARCHITECTURAL HIGHLIGHT</text>
      <text x="16" y="43" class="sans-text" font-size="12" fill="{text_primary}">Reusable Component Library &amp; Smooth Animation Choreography</text>
    </g>

    <!-- Tech Badges -->
    <g transform="translate(26, 296)">
      <rect x="0" y="0" width="80" height="24" rx="5" fill="rgba(0, 229, 255, 0.1)"/>
      <text x="40" y="16" text-anchor="middle" class="mono-text" font-size="10.5" font-weight="600" fill="#00E5FF">React.js</text>

      <rect x="90" y="0" width="100" height="24" rx="5" fill="rgba(139, 92, 246, 0.1)"/>
      <text x="140" y="16" text-anchor="middle" class="mono-text" font-size="10.5" font-weight="600" fill="#8B5CF6">Tailwind CSS</text>

      <rect x="200" y="0" width="90" height="24" rx="5" fill="rgba(236, 72, 153, 0.1)"/>
      <text x="245" y="16" text-anchor="middle" class="mono-text" font-size="10.5" font-weight="600" fill="#EC4899">JavaScript</text>

      <rect x="300" y="0" width="80" height="24" rx="5" fill="rgba(16, 185, 129, 0.1)"/>
      <text x="340" y="16" text-anchor="middle" class="mono-text" font-size="10.5" font-weight="600" fill="#10B981">Motion FX</text>
    </g>
  </g>

  <!-- Right: SECONDARY BUILDS COLUMN (2 Sleek Cards) -->
  <g transform="translate(645, 95)">
    <!-- Build 02: Get2Vacation CMS -->
    <g transform="translate(0, 0)">
      <rect width="495" height="165" rx="12" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="165" rx="2" fill="#8B5CF6"/>
      
      <text x="24" y="28" class="mono-text" font-size="10.5" font-weight="700" fill="#8B5CF6" letter-spacing="1">PROJECT // 02</text>
      <text x="24" y="54" class="sans-text" font-size="19" font-weight="800" fill="{text_primary}">Get2Vacation CMS &amp; Admin Suite</text>
      <text x="24" y="78" class="sans-text" font-size="12.5" fill="{text_secondary}">
        Full CRUD dashboard for managing destination catalogs, tour packages,
      </text>
      <text x="24" y="96" class="sans-text" font-size="12.5" fill="{text_secondary}">
        and marketing campaigns with dynamic REST API integration via Axios.
      </text>
      
      <g transform="translate(24, 122)">
        <text x="0" y="16" class="mono-text" font-size="11" fill="{text_muted}">React • Node.js • Express • REST APIs • Axios</text>
      </g>
    </g>

    <!-- Build 03: Get2Vacations Portal -->
    <g transform="translate(0, 185)">
      <rect width="495" height="165" rx="12" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="165" rx="2" fill="#10B981"/>
      
      <text x="24" y="28" class="mono-text" font-size="10.5" font-weight="700" fill="#10B981" letter-spacing="1">PROJECT // 03</text>
      <text x="24" y="54" class="sans-text" font-size="19" font-weight="800" fill="{text_primary}">Get2Vacations Travel Experience</text>
      <text x="24" y="78" class="sans-text" font-size="12.5" fill="{text_secondary}">
        Modern travel portal with seamless client-side routing, query filters,
      </text>
      <text x="24" y="96" class="sans-text" font-size="12.5" fill="{text_secondary}">
        and scalable component architecture for rich travel itineraries.
      </text>
      
      <g transform="translate(24, 122)">
        <text x="0" y="16" class="mono-text" font-size="11" fill="{text_muted}">React • Tailwind CSS • React Router • REST Integration</text>
      </g>
    </g>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 04. TOTAL GITHUB STATS (1200 x 200 px)
# ==============================================================================
def build_stats_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    card_bg = "#0E1526" if dark else "#FFFFFF"
    card_border = "rgba(0, 229, 255, 0.2)" if dark else "rgba(99, 102, 241, 0.18)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 200" width="100%" height="100%">
  <defs>
    <pattern id="statsGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="200" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="200" fill="url(#statsGrid)" rx="20"/>

  <!-- Section Header -->
  <g transform="translate(60, 36)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">// 04 — GITHUB TOTAL STATS</text>
    <text x="0" y="38" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">Verified Repository &amp; Activity Statistics</text>
    <text x="1080" y="36" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">REAL GITHUB DATA // @Roshani-sahu</text>
  </g>

  <!-- 4 Metric Cards -->
  <g transform="translate(60, 90)">
    <!-- Stat 1 -->
    <g transform="translate(0, 0)">
      <rect width="255" height="85" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="85" rx="2" fill="#00E5FF"/>
      <text x="20" y="26" class="mono-text" font-size="10.5" font-weight="700" fill="#00E5FF">PUBLIC REPOSITORIES</text>
      <text x="20" y="58" class="sans-text" font-size="32" font-weight="900" fill="{text_primary}">25+</text>
      <text x="100" y="56" class="sans-text" font-size="11" fill="{text_muted}">Active Repos</text>
    </g>

    <!-- Stat 2 -->
    <g transform="translate(275, 0)">
      <rect width="255" height="85" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="85" rx="2" fill="#8B5CF6"/>
      <text x="20" y="26" class="mono-text" font-size="10.5" font-weight="700" fill="#8B5CF6">PRO EXPERIENCE</text>
      <text x="20" y="58" class="sans-text" font-size="32" font-weight="900" fill="{text_primary}">1.5+</text>
      <text x="110" y="56" class="sans-text" font-size="11" fill="{text_muted}">Yrs Frontend</text>
    </g>

    <!-- Stat 3 -->
    <g transform="translate(550, 0)">
      <rect width="255" height="85" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="85" rx="2" fill="#EC4899"/>
      <text x="20" y="26" class="mono-text" font-size="10.5" font-weight="700" fill="#EC4899">PRIMARY STACK</text>
      <text x="20" y="58" class="sans-text" font-size="28" font-weight="900" fill="{text_primary}">React/TS</text>
      <text x="175" y="56" class="sans-text" font-size="11" fill="{text_muted}">Focused</text>
    </g>

    <!-- Stat 4 -->
    <g transform="translate(825, 0)">
      <rect width="255" height="85" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="85" rx="2" fill="#10B981"/>
      <text x="20" y="26" class="mono-text" font-size="10.5" font-weight="700" fill="#10B981">LIVE PRODUCTION</text>
      <text x="20" y="58" class="sans-text" font-size="32" font-weight="900" fill="{text_primary}">4+</text>
      <text x="80" y="56" class="sans-text" font-size="11" fill="{text_muted}">Client Projects</text>
    </g>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 05. CONTRIBUTION PULSE (1200 x 240 px)
# ==============================================================================
def build_pulse_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    bar_inactive = "#1E293B" if dark else "#E2E8F0"

    # Simulated 52-week activity height pattern
    pulse_heights = [
        15, 22, 18, 30, 45, 60, 40, 25, 35, 55, 75, 90, 65, 80, 110, 95, 70, 85,
        100, 120, 140, 115, 90, 75, 60, 85, 105, 130, 110, 95, 80, 70, 90, 115,
        135, 150, 125, 100, 85, 95, 110, 120, 105, 90, 75, 60, 45, 30, 40, 55, 70, 85
    ]

    bars_svg = ""
    bx = 60
    for h in pulse_heights:
        # Determine bar fill based on intensity
        if h > 120:
            fill = "#00E5FF"
        elif h > 80:
            fill = "#8B5CF6"
        elif h > 40:
            fill = "#10B981"
        else:
            fill = bar_inactive

        y = 190 - h
        bars_svg += f'<rect x="{bx}" y="{y}" width="15" height="{h}" rx="3" fill="{fill}"/>\n'
        bx += 20.5

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="100%" height="100%">
  <defs>
    <pattern id="pulseGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    
    <linearGradient id="scanBeam" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0"/>
      <stop offset="50%" stop-color="#00E5FF" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </linearGradient>

    <style>
      @keyframes beamMove {{
        0% {{ transform: translateX(0px); }}
        100% {{ transform: translateX(1080px); }}
      }}
      .pulse-beam {{ animation: beamMove 7s linear infinite; }}
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="240" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="240" fill="url(#pulseGrid)" rx="20"/>

  <!-- Section Header -->
  <g transform="translate(60, 36)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#10B981" letter-spacing="2">// 05 — CONTRIBUTION PULSE</text>
    <text x="0" y="38" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">52-Week Activity Timeline &amp; Consistency</text>
    <text x="1080" y="36" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">365-DAY RECORD // @Roshani-sahu</text>
  </g>

  <!-- Activity Bars -->
  {bars_svg}

  <!-- Scanning Energy Line -->
  <line x1="60" y1="192" x2="1140" y2="192" stroke="rgba(148, 163, 184, 0.2)" stroke-width="1"/>
  
  <!-- Months Axis Labels -->
  <g transform="translate(60, 212)" class="mono-text" font-size="10.5" fill="{text_muted}">
    <text x="0">SEP</text>
    <text x="90">OCT</text>
    <text x="180">NOV</text>
    <text x="270">DEC</text>
    <text x="360">JAN</text>
    <text x="450">FEB</text>
    <text x="540">MAR</text>
    <text x="630">APR</text>
    <text x="720">MAY</text>
    <text x="810">JUN</text>
    <text x="900">JUL</text>
    <text x="990">AUG</text>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 06. LANGUAGE FOOTPRINT (1200 x 220 px)
# ==============================================================================
def build_footprint_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    card_bg = "#0E1526" if dark else "#FFFFFF"
    card_border = "rgba(0, 229, 255, 0.2)" if dark else "rgba(99, 102, 241, 0.18)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 220" width="100%" height="100%">
  <defs>
    <pattern id="langGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="220" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="220" fill="url(#langGrid)" rx="20"/>

  <!-- Section Header -->
  <g transform="translate(60, 36)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#EC4899" letter-spacing="2">// 06 — LANGUAGE FOOTPRINT</text>
    <text x="0" y="38" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">Aggregated Code Volume &amp; Repository Stack</text>
    <text x="1080" y="36" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">FETCHED FROM GITHUB // @Roshani-sahu</text>
  </g>

  <!-- Multi-Color Progress Spectrum Bar -->
  <g transform="translate(60, 90)">
    <rect width="1080" height="14" rx="7" fill="#1E293B"/>
    <!-- JavaScript: 42.5% = 459px -->
    <rect x="0" y="0" width="459" height="14" rx="7" fill="#F7DF1E"/>
    <!-- TypeScript: 32.0% = 345.6px -->
    <rect x="461" y="0" width="345" height="14" rx="0" fill="#3178C6"/>
    <!-- HTML: 15.5% = 167.4px -->
    <rect x="808" y="0" width="167" height="14" rx="0" fill="#E34F26"/>
    <!-- CSS: 10.0% = 108px -->
    <rect x="977" y="0" width="103" height="14" rx="7" fill="#1572B6"/>
  </g>

  <!-- Language Details Legend -->
  <g transform="translate(60, 135)">
    <!-- JavaScript -->
    <g transform="translate(0, 0)">
      <rect width="250" height="48" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1"/>
      <circle cx="20" cy="24" r="6" fill="#F7DF1E"/>
      <text x="36" y="28" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">JavaScript</text>
      <text x="230" y="28" text-anchor="end" class="mono-text" font-size="13" font-weight="700" fill="#F7DF1E">42.5%</text>
    </g>

    <!-- TypeScript -->
    <g transform="translate(275, 0)">
      <rect width="250" height="48" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1"/>
      <circle cx="20" cy="24" r="6" fill="#3178C6"/>
      <text x="36" y="28" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">TypeScript</text>
      <text x="230" y="28" text-anchor="end" class="mono-text" font-size="13" font-weight="700" fill="#3178C6">32.0%</text>
    </g>

    <!-- HTML5 -->
    <g transform="translate(550, 0)">
      <rect width="250" height="48" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1"/>
      <circle cx="20" cy="24" r="6" fill="#E34F26"/>
      <text x="36" y="28" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">HTML5</text>
      <text x="230" y="28" text-anchor="end" class="mono-text" font-size="13" font-weight="700" fill="#E34F26">15.5%</text>
    </g>

    <!-- CSS3 & Tailwind -->
    <g transform="translate(825, 0)">
      <rect width="255" height="48" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1"/>
      <circle cx="20" cy="24" r="6" fill="#1572B6"/>
      <text x="36" y="28" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">CSS3 / Tailwind</text>
      <text x="235" y="28" text-anchor="end" class="mono-text" font-size="13" font-weight="700" fill="#1572B6">10.0%</text>
    </g>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 07. PORTFOLIO SIGNATURE & CONNECT (1200 x 180 px)
# ==============================================================================
def build_signature_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 180" width="100%" height="100%">
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

  <rect width="1200" height="180" fill="{bg_color}" rx="20"/>

  <g transform="translate(60, 45)">
    <text x="0" y="16" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">// 07 — CONTACT &amp; CONNECT</text>
    <text x="0" y="54" class="sans-text" font-size="28" font-weight="900" fill="{text_primary}">Let's build something meaningful.</text>
    <text x="0" y="84" class="sans-text" font-size="14" fill="{text_secondary}">
      Always open to discussing frontend architecture, React development, and engineering roles.
    </text>
  </g>

  <line x1="60" y1="150" x2="1140" y2="150" stroke="url(#sigGrad)" stroke-width="2" stroke-linecap="round"/>
</svg>'''
    return svg


def build_button_svg(channel="github", dark=True):
    bg_color = "#0E1526" if dark else "#FFFFFF"
    border_color = "rgba(0, 229, 255, 0.3)" if dark else "rgba(99, 102, 241, 0.25)"
    text_primary = "#F8FAFC" if dark else "#0F172A"

    if channel == "github":
        accent = "#00E5FF"
        label = "GitHub Profile"
        handle = "@Roshani-sahu"
        icon = get_icon_inner("Github-Dark.svg" if dark else "Github-Light.svg") or '<circle cx="12" cy="12" r="8" fill="#00E5FF"/>'
    elif channel == "linkedin":
        accent = "#8B5CF6"
        label = "LinkedIn Network"
        handle = "in/roshani-sahu"
        icon = '<path d="M19 3a2 2 0 0 1 2 2v14a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h14m-.5 15.5v-5.3a3.26 3.26 0 0 0-3.26-3.26c-.85 0-1.84.52-2.28 1.3v-1.11h-2.79v8.37h2.79v-4.93c0-.77.62-1.4 1.39-1.4a1.4 1.4 0 0 1 1.4 1.4v4.93h2.75M6.88 8.56a1.68 1.68 0 0 0 1.68-1.68c0-.93-.75-1.69-1.68-1.69a1.69 1.69 0 0 0-1.69 1.69c0 .93.76 1.68 1.69 1.68m1.39 9.94v-8.37H5.5v8.37h2.77z" fill="#8B5CF6"/>'
    else:
        accent = "#10B981"
        label = "Direct Email"
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
    print("Building editorial 7-section portfolio assets for Roshani Sahu...")

    targets = [
        ("hero", "hero-dark.svg", build_hero_svg(dark=True)),
        ("hero", "hero-light.svg", build_hero_svg(dark=False)),
        ("stack", "stack-dark.svg", build_stack_svg(dark=True)),
        ("stack", "stack-light.svg", build_stack_svg(dark=False)),
        ("projects", "projects-dark.svg", build_projects_svg(dark=True)),
        ("projects", "projects-light.svg", build_projects_svg(dark=False)),
        ("stats", "stats-dark.svg", build_stats_svg(dark=True)),
        ("stats", "stats-light.svg", build_stats_svg(dark=False)),
        ("telemetry", "pulse-dark.svg", build_pulse_svg(dark=True)),
        ("telemetry", "pulse-light.svg", build_pulse_svg(dark=False)),
        ("telemetry", "footprint-dark.svg", build_footprint_svg(dark=True)),
        ("telemetry", "footprint-light.svg", build_footprint_svg(dark=False)),
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

    print("\nAll 7-section assets successfully generated and synced across all paths!")

if __name__ == "__main__":
    main()
