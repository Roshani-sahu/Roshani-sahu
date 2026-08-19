#!/usr/bin/env python3
"""
tools/build_roshani_assets.py

Generates custom, high-fidelity animated SVG assets for Roshani Sahu's GitHub Profile:
- assets/hero/hero-dark.svg & hero-light.svg
- assets/stack/stack-flow-dark.svg & stack-flow-light.svg
- assets/projects/showcase-dark.svg & showcase-light.svg
- assets/focus/focus-matrix-dark.svg & focus-matrix-light.svg
- assets/activity/telemetry-dark.svg & telemetry-light.svg
- assets/footer/connect-dark.svg & connect-light.svg
- assets/footer/btn-github.svg, btn-linkedin.svg, btn-email.svg
"""

import os
import re
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
CACHE_DIR = os.path.join(BASE_DIR, "tools", "skillicons_cache")

def get_icon_inner(icon_filename):
    """Read SVG file from skillicons_cache and return clean inner SVG markup."""
    path = os.path.join(CACHE_DIR, icon_filename)
    if not os.path.exists(path):
        return None
    try:
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
        # Remove xml declaration and outer svg tag
        content = re.sub(r'<\?xml.*?\?>', '', content)
        m = re.search(r'<svg[^>]*>(.*)</svg>', content, re.DOTALL)
        if m:
            return m.group(1).strip()
    except Exception as e:
        print(f"Error reading {icon_filename}: {e}")
    return None

# Custom vector icons for technologies not in skillicons_cache
CUSTOM_ICONS = {
    "FramerMotion": '''
        <path d="M4 4h16v8h-8zM4 12h8l8 8H4zM4 20l8-8v8z" fill="#00E5FF"/>
    ''',
    "GSAP": '''
        <path d="M12 2L2 7v10l10 5 10-5V7L12 2zm0 2.8l7 3.5v7.4l-7 3.5-7-3.5V8.3l7-3.5z" fill="#88CE02"/>
        <path d="M12 7l4 2.5v5L12 17l-4-2.5v-5L12 7z" fill="#88CE02" opacity="0.8"/>
    ''',
    "ScrollTrigger": '''
        <circle cx="12" cy="12" r="9" fill="none" stroke="#00E5FF" stroke-width="2"/>
        <path d="M12 7v10M7 12l5 5 5-5" fill="none" stroke="#00E5FF" stroke-width="2" stroke-linecap="round"/>
    ''',
    "ChartJS": '''
        <path d="M4 20h16M7 16v-4M12 16V8M17 16v-9" stroke="#FF6384" stroke-width="2.5" stroke-linecap="round"/>
    ''',
    "ApexCharts": '''
        <path d="M3 18l6-7 4 4 8-10" fill="none" stroke="#00E5FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="3" cy="18" r="2" fill="#00E5FF"/>
        <circle cx="9" cy="11" r="2" fill="#00E5FF"/>
        <circle cx="13" cy="15" r="2" fill="#00E5FF"/>
        <circle cx="21" cy="5" r="2" fill="#00E5FF"/>
    ''',
    "JWT": '''
        <path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5z" fill="#D63AFF" opacity="0.2"/>
        <path d="M12 2L3 7v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V7l-9-5zm0 2.2l7 3.9v5c0 4.4-3 8.5-7 9.7-4-1.2-7-5.3-7-9.7V8.1l7-3.9z" fill="#D63AFF"/>
        <circle cx="12" cy="12" r="3" fill="#D63AFF"/>
    ''',
    "Sequelize": '''
        <path d="M12 3L2 8.5v7L12 21l10-5.5v-7L12 3zm0 2.3l7.5 4.1-3.2 1.8-7.5-4.1 3.2-1.8zm-8 4.6l7 3.8v7.2l-7-3.8V9.9zm9 11v-7.2l7-3.8v7.2l-7 3.8z" fill="#52B0E7"/>
    ''',
    "Axios": '''
        <path d="M12 3L3 18h4.5l4.5-8 4.5 8H21L12 3z" fill="#5A29E4"/>
    ''',
    "VSCode": '''
        <path d="M17.5 2.5L7.2 10.5 3.5 7.5 1.5 8.5v7l2 1 3.7-3 10.3 8 4.5-2V4.5l-4.5-2zm0 4.2v10.6l-6.8-5.3 6.8-5.3z" fill="#007ACC"/>
    ''',
    "Bootstrap": '''
        <rect x="3" y="3" width="18" height="18" rx="4" fill="#7952B3"/>
        <path d="M8.5 7.5h3.8c1.3 0 2.2.7 2.2 1.8 0 .8-.5 1.4-1.2 1.6v.1c.9.2 1.6.9 1.6 1.9 0 1.3-1 2.1-2.5 2.1H8.5V7.5zm2 3.1h1.5c.6 0 1-.3 1-.8s-.4-.8-1-.8h-1.5v1.6zm0 2.8h1.8c.7 0 1.2-.3 1.2-.9s-.5-.9-1.2-.9h-1.8v1.8z" fill="#FFF"/>
    ''',
    "ReactRouter": '''
        <path d="M4 6h16v3H4zm0 5h16v3H4zm0 5h10v3H4z" fill="#CA4245"/>
    ''',
    "Bcrypt": '''
        <rect x="5" y="10" width="14" height="10" rx="2" fill="#10B981"/>
        <path d="M8 10V7a4 4 0 0 1 8 0v3" fill="none" stroke="#10B981" stroke-width="2"/>
        <circle cx="12" cy="15" r="1.5" fill="#0A0E1A"/>
    ''',
    "Render": '''
        <path d="M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm0 3c3.87 0 7 3.13 7 7s-3.13 7-7 7-7-3.13-7-7 3.13-7 7-7zm-1 3v8l6-4-6-4z" fill="#46E3B7"/>
    ''',
}

# ==============================================================================
# 01. HERO BANNER
# ==============================================================================
def build_hero_svg(dark=True):
    bg_color = "#0B0F19" if dark else "#F8FAFC"
    card_bg = "#111827" if dark else "#FFFFFF"
    card_border = "rgba(99, 102, 241, 0.25)" if dark else "rgba(99, 102, 241, 0.2)"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.07)" if dark else "rgba(99, 102, 241, 0.05)"
    badge_bg = "rgba(0, 229, 255, 0.1)" if dark else "rgba(14, 165, 233, 0.1)"
    badge_border = "rgba(0, 229, 255, 0.3)" if dark else "rgba(14, 165, 233, 0.3)"
    badge_text = "#00E5FF" if dark else "#0284C7"
    glow_opacity = "0.15" if dark else "0.08"
    
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 480" width="100%" height="100%">
  <defs>
    <!-- Background Grid Pattern -->
    <pattern id="heroGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
      <circle cx="40" cy="40" r="1" fill="{grid_stroke}"/>
    </pattern>

    <!-- Linear Gradients -->
    <linearGradient id="cyanPurpleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="50%" stop-color="#8B5CF6"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>

    <linearGradient id="borderGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="0.8"/>
      <stop offset="50%" stop-color="#8B5CF6" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0.8"/>
    </linearGradient>

    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="{card_bg}" stop-opacity="0.95"/>
      <stop offset="100%" stop-color="{card_bg}" stop-opacity="0.85"/>
    </linearGradient>

    <!-- Radial Ambient Glows -->
    <radialGradient id="radialCyan" cx="20%" cy="40%" r="45%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="{glow_opacity}"/>
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="radialViolet" cx="80%" cy="60%" r="50%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="{glow_opacity}"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>

    <style>
      @keyframes floatSlow {{
        0%, 100% {{ transform: translateY(0px); }}
        50% {{ transform: translateY(-8px); }}
      }}
      @keyframes pulseGlow {{
        0%, 100% {{ opacity: 0.8; filter: drop-shadow(0 0 8px rgba(0, 229, 255, 0.4)); }}
        50% {{ opacity: 1; filter: drop-shadow(0 0 16px rgba(139, 92, 246, 0.8)); }}
      }}
      @keyframes shimmer {{
        0% {{ transform: translateX(-100%); }}
        100% {{ transform: translateX(200%); }}
      }}
      @keyframes beaconBlink {{
        0%, 100% {{ opacity: 1; transform: scale(1); }}
        50% {{ opacity: 0.3; transform: scale(0.85); }}
      }}
      @keyframes orbitSpin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}
      .floating-card {{ animation: floatSlow 6s ease-in-out infinite; }}
      .beacon {{ animation: beaconBlink 2.2s infinite ease-in-out; transform-origin: center; }}
      .shimmer-line {{ animation: shimmer 4s infinite linear; }}
      .title-text {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
        font-weight: 900;
        letter-spacing: -1.5px;
      }}
      .mono-text {{
        font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace;
      }}
      .sans-text {{
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
      }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="480" fill="{bg_color}" rx="16"/>
  <rect width="1200" height="480" fill="url(#heroGrid)" rx="16"/>
  <rect width="1200" height="480" fill="url(#radialCyan)" rx="16"/>
  <rect width="1200" height="480" fill="url(#radialViolet)" rx="16"/>

  <!-- Outer Glass Frame -->
  <rect x="20" y="20" width="1160" height="440" rx="14" fill="none" stroke="{card_border}" stroke-width="1.5"/>

  <!-- Corner Tech Accents -->
  <path d="M 20 45 L 20 20 L 45 20" fill="none" stroke="#00E5FF" stroke-width="3" stroke-linecap="round"/>
  <path d="M 1180 45 L 1180 20 L 1155 20" fill="none" stroke="#8B5CF6" stroke-width="3" stroke-linecap="round"/>
  <path d="M 20 435 L 20 460 L 45 460" fill="none" stroke="#8B5CF6" stroke-width="3" stroke-linecap="round"/>
  <path d="M 1180 435 L 1180 460 L 1155 460" fill="none" stroke="#00E5FF" stroke-width="3" stroke-linecap="round"/>

  <!-- Top Studio / HUD Status Bar -->
  <g transform="translate(45, 42)">
    <!-- Terminal Dots -->
    <circle cx="8" cy="8" r="4.5" fill="#EF4444"/>
    <circle cx="24" cy="8" r="4.5" fill="#F59E0B"/>
    <circle cx="40" cy="8" r="4.5" fill="#10B981"/>
    
    <!-- System Status Badge -->
    <rect x="68" y="-4" width="220" height="24" rx="12" fill="{badge_bg}" stroke="{badge_border}" stroke-width="1"/>
    <circle cx="82" cy="8" r="3.5" fill="#10B981" class="beacon"/>
    <text x="94" y="12" class="mono-text" font-size="11" font-weight="600" fill="{badge_text}" letter-spacing="1">SYSTEM READY // ONLINE</text>

    <!-- Location & Experience Metadata -->
    <text x="820" y="12" class="mono-text" font-size="11.5" fill="{text_muted}" letter-spacing="1.2">INDORE, INDIA • 1.5+ YRS PRO EXP</text>
    <rect x="795" y="-4" width="315" height="24" rx="6" fill="none" stroke="{card_border}" stroke-width="1"/>
  </g>

  <!-- Center Identity & Typography -->
  <g transform="translate(60, 100)">
    <!-- Supertitle Category -->
    <g transform="translate(0, 24)">
      <rect x="0" y="-14" width="265" height="22" rx="4" fill="rgba(139, 92, 246, 0.12)" stroke="rgba(139, 92, 246, 0.35)" stroke-width="1"/>
      <text x="10" y="2" class="mono-text" font-size="11" font-weight="700" fill="#8B5CF6" letter-spacing="2">FRONTEND &amp; MERN ENGINEER</text>
    </g>

    <!-- Main Name Headline -->
    <text x="0" y="105" class="title-text" font-size="64" fill="url(#cyanPurpleGrad)">ROSHANI SAHU</text>

    <!-- Subtitle Role -->
    <text x="2" y="150" class="sans-text" font-size="22" font-weight="600" fill="{text_primary}" letter-spacing="0.5">
      React Specialist <tspan fill="#8B5CF6">•</tspan> UI Architecture <tspan fill="#00E5FF">•</tspan> Full-Stack Engineering
    </text>

    <!-- Engineering Statement -->
    <text x="2" y="185" class="sans-text" font-size="15" fill="{text_secondary}" font-weight="400">
      Engineering high-performance web applications, scalable React component systems,
    </text>
    <text x="2" y="208" class="sans-text" font-size="15" fill="{text_secondary}" font-weight="400">
      and fluid motion experiences with modern state and API architecture.
    </text>

    <!-- Feature Pillars -->
    <g transform="translate(0, 240)">
      <!-- Pillar 1 -->
      <rect x="0" y="0" width="165" height="38" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <circle cx="20" cy="19" r="5" fill="#00E5FF"/>
      <text x="35" y="23" class="sans-text" font-size="13" font-weight="600" fill="{text_primary}">React &amp; TypeScript</text>

      <!-- Pillar 2 -->
      <rect x="180" y="0" width="165" height="38" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <circle cx="200" cy="19" r="5" fill="#8B5CF6"/>
      <text x="215" y="23" class="sans-text" font-size="13" font-weight="600" fill="{text_primary}">Tailwind &amp; Motion</text>

      <!-- Pillar 3 -->
      <rect x="360" y="0" width="165" height="38" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <circle cx="380" cy="19" r="5" fill="#10B981"/>
      <text x="395" y="23" class="sans-text" font-size="13" font-weight="600" fill="{text_primary}">MERN Full-Stack</text>

      <!-- Pillar 4 -->
      <rect x="540" y="0" width="180" height="38" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <circle cx="560" cy="19" r="5" fill="#EC4899"/>
      <text x="575" y="23" class="sans-text" font-size="13" font-weight="600" fill="{text_primary}">REST APIs &amp; Dashboards</text>
    </g>
  </g>

  <!-- Right Floating Architecture Visual / Interactive HUD Card -->
  <g transform="translate(820, 110)" class="floating-card">
    <!-- Card Container -->
    <rect width="320" height="295" rx="12" fill="url(#cardGrad)" stroke="{card_border}" stroke-width="1.5"/>
    <rect width="320" height="32" rx="12" fill="rgba(99, 102, 241, 0.12)"/>
    <rect y="24" width="320" height="8" fill="{card_bg}"/>
    <text x="16" y="21" class="mono-text" font-size="11" font-weight="700" fill="{text_muted}" letter-spacing="1">COMPONENT_PIPELINE.tsx</text>
    
    <!-- Code Simulation / Architecture Flow inside Card -->
    <g transform="translate(16, 48)">
      <!-- Line 1 -->
      <text x="0" y="15" class="mono-text" font-size="12" fill="#8B5CF6">interface <tspan fill="#00E5FF">FrontendEngine</tspan> {{</text>
      <text x="14" y="36" class="mono-text" font-size="11.5" fill="{text_secondary}">core: <tspan fill="#10B981">'React'</tspan> | <tspan fill="#10B981">'TypeScript'</tspan>;</text>
      <text x="14" y="55" class="mono-text" font-size="11.5" fill="{text_secondary}">styling: <tspan fill="#10B981">'TailwindCSS'</tspan>;</text>
      <text x="14" y="74" class="mono-text" font-size="11.5" fill="{text_secondary}">motion: <tspan fill="#10B981">'GSAP'</tspan> | <tspan fill="#10B981">'Framer'</tspan>;</text>
      <text x="14" y="93" class="mono-text" font-size="11.5" fill="{text_secondary}">backend: <tspan fill="#10B981">'Node'</tspan> | <tspan fill="#10B981">'Express'</tspan>;</text>
      <text x="14" y="112" class="mono-text" font-size="11.5" fill="{text_secondary}">database: <tspan fill="#10B981">'MongoDB'</tspan> | <tspan fill="#10B981">'MySQL'</tspan>;</text>
      <text x="0" y="132" class="mono-text" font-size="12" fill="#8B5CF6">}}</text>

      <!-- Divider -->
      <line x1="0" y1="145" x2="288" y2="145" stroke="{card_border}" stroke-width="1"/>

      <!-- Live Metric Pill -->
      <g transform="translate(0, 158)">
        <rect width="288" height="64" rx="8" fill="rgba(0, 229, 255, 0.05)" stroke="rgba(0, 229, 255, 0.2)" stroke-width="1"/>
        <text x="12" y="24" class="mono-text" font-size="11" fill="{text_muted}">PRODUCTION IMPACT</text>
        <text x="12" y="48" class="sans-text" font-size="17" font-weight="700" fill="{text_primary}">Royal IT Services</text>
        <text x="185" y="48" class="mono-text" font-size="12" font-weight="600" fill="#10B981">4+ APPS LIVE</text>
      </g>
    </g>
  </g>

  <!-- Bottom Animated Energy Beam -->
  <g transform="translate(20, 462)">
    <rect width="1160" height="2" fill="url(#borderGrad)"/>
    <circle cx="580" cy="1" r="3" fill="#00E5FF">
      <animate attributeName="cx" values="50;1110;50" dur="8s" repeatCount="indefinite"/>
    </circle>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 02. ENGINEERING STACK & COMPONENT FLOW
# ==============================================================================
def build_stack_svg(dark=True):
    bg_color = "#0B0F19" if dark else "#F8FAFC"
    card_bg = "#111827" if dark else "#FFFFFF"
    card_border = "rgba(99, 102, 241, 0.2)" if dark else "rgba(99, 102, 241, 0.15)"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.06)" if dark else "rgba(99, 102, 241, 0.04)"
    node_bg = "#161F30" if dark else "#F1F5F9"
    node_border = "rgba(148, 163, 184, 0.15)" if dark else "rgba(148, 163, 184, 0.3)"

    # Define the 4 Stack Tiers specifically for Roshani
    TIERS = [
        {
            "num": "01",
            "tier_name": "INTERFACE &amp; CLIENT ARCHITECTURE",
            "accent": "#00E5FF",
            "bg_accent": "rgba(0, 229, 255, 0.08)",
            "items": [
                ("React", "React", "React-Dark.svg" if dark else "React-Light.svg"),
                ("TypeScript", "TypeScript", "TypeScript.svg"),
                ("JavaScript", "JavaScript", "JavaScript.svg"),
                ("TailwindCSS", "Tailwind CSS", "TailwindCSS-Dark.svg" if dark else "TailwindCSS-Light.svg"),
                ("Vite", "Vite", "Vite-Dark.svg" if dark else "Vite-Light.svg"),
                ("HTML5", "HTML5", "HTML.svg"),
                ("CSS3", "CSS3", "CSS.svg"),
                ("Bootstrap", "Bootstrap", "CUSTOM_Bootstrap"),
                ("ReactRouter", "React Router", "CUSTOM_ReactRouter"),
            ]
        },
        {
            "num": "02",
            "tier_name": "MOTION, INTERACTION &amp; VISUAL DATA",
            "accent": "#8B5CF6",
            "bg_accent": "rgba(139, 92, 246, 0.08)",
            "items": [
                ("FramerMotion", "Framer Motion", "CUSTOM_FramerMotion"),
                ("GSAP", "GSAP", "CUSTOM_GSAP"),
                ("ScrollTrigger", "ScrollTrigger", "CUSTOM_ScrollTrigger"),
                ("ChartJS", "Chart.js", "CUSTOM_ChartJS"),
                ("ApexCharts", "ApexCharts", "CUSTOM_ApexCharts"),
            ]
        },
        {
            "num": "03",
            "tier_name": "API, BACKEND &amp; APPLICATION SERVICES",
            "accent": "#10B981",
            "bg_accent": "rgba(16, 185, 129, 0.08)",
            "items": [
                ("NodeJS", "Node.js", "NodeJS-Dark.svg" if dark else "NodeJS-Light.svg"),
                ("Express", "Express.js", "ExpressJS-Dark.svg" if dark else "ExpressJS-Light.svg"),
                ("REST", "REST APIs", "Postman.svg"),
                ("JWT", "JWT Auth", "CUSTOM_JWT"),
                ("Axios", "Axios", "CUSTOM_Axios"),
                ("Bcrypt", "bcrypt", "CUSTOM_Bcrypt"),
            ]
        },
        {
            "num": "04",
            "tier_name": "PERSISTENCE, CLOUD &amp; WORKFLOW TOOLS",
            "accent": "#F59E0B",
            "bg_accent": "rgba(245, 158, 11, 0.08)",
            "items": [
                ("MongoDB", "MongoDB", "MongoDB.svg"),
                ("MySQL", "MySQL", "MySQL-Dark.svg" if dark else "MySQL-Light.svg"),
                ("Sequelize", "Sequelize", "CUSTOM_Sequelize"),
                ("Git", "Git", "Git.svg"),
                ("GitHub", "GitHub", "Github-Dark.svg" if dark else "Github-Light.svg"),
                ("VSCode", "VS Code", "CUSTOM_VSCode"),
                ("Postman", "Postman", "Postman.svg"),
                ("NPM", "npm", "Npm-Dark.svg" if dark else "Npm-Light.svg"),
                ("Vercel", "Vercel", "Vercel-Dark.svg" if dark else "Vercel-Light.svg"),
                ("Netlify", "Netlify", "Netlify-Dark.svg" if dark else "Netlify-Light.svg"),
                ("Render", "Render", "CUSTOM_Render"),
                ("AWS", "AWS Basics", "AWS-Dark.svg" if dark else "AWS-Light.svg"),
            ]
        }
    ]

    tier_y_starts = [105, 235, 365, 495]
    total_height = 680

    svg_defs = f'''
    <pattern id="stackGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      @keyframes pulseLine {{
        0% {{ stroke-dashoffset: 200; }}
        100% {{ stroke-dashoffset: 0; }}
      }}
      @keyframes photonFlow {{
        0% {{ cx: 280; opacity: 0; }}
        20% {{ opacity: 1; }}
        80% {{ opacity: 1; }}
        100% {{ cx: 1140; opacity: 0; }}
      }}
      .photon {{ animation: photonFlow 4s infinite linear; }}
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
    '''

    rendered_tiers = []
    for idx, tier in enumerate(TIERS):
        y_pos = tier_y_starts[idx]
        accent = tier["accent"]
        bg_accent = tier["bg_accent"]
        tier_num = tier["num"]
        tier_title = tier["tier_name"]
        
        # Left badge
        tier_markup = f'''
        <!-- TIER {tier_num} -->
        <g transform="translate(40, {y_pos})">
          <!-- Tier Badge & Header -->
          <rect width="220" height="98" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
          <rect width="6" height="98" rx="3" fill="{accent}"/>
          <text x="20" y="28" class="mono-text" font-size="12" font-weight="700" fill="{accent}" letter-spacing="2">[{tier_num}] TIER</text>
          <text x="20" y="52" class="sans-text" font-size="11.5" font-weight="700" fill="{text_primary}">{tier_title}</text>
          <text x="20" y="74" class="mono-text" font-size="10.5" fill="{text_muted}">{len(tier["items"])} TECHNOLOGIES</text>

          <!-- Connecting Track Line -->
          <line x1="220" y1="49" x2="250" y2="49" stroke="{accent}" stroke-width="2" stroke-dasharray="4,4"/>
        </g>
        
        <!-- Technology Node Grid -->
        <g transform="translate(295, {y_pos})">
        '''

        # Render items horizontally
        for col_idx, (item_id, label, icon_key) in enumerate(tier["items"]):
            # Wrap to 2 rows if needed (for tier 4 which has 12 items)
            if len(tier["items"]) > 9:
                row = col_idx // 6
                col = col_idx % 6
                x = col * 142
                y = row * 48
                card_w = 134
                card_h = 42
            else:
                x = col_idx * 96
                y = 12
                card_w = 88
                card_h = 74

            # Get icon content
            if icon_key.startswith("CUSTOM_"):
                custom_name = icon_key.replace("CUSTOM_", "")
                icon_inner = CUSTOM_ICONS.get(custom_name, '<circle cx="12" cy="12" r="8" fill="#8B5CF6"/>')
            else:
                icon_inner = get_icon_inner(icon_key)
                if not icon_inner:
                    icon_inner = '<circle cx="12" cy="12" r="8" fill="#00E5FF"/>'

            if len(tier["items"]) > 9:
                # Wide mini-card format
                tier_markup += f'''
                <g transform="translate({x}, {y})">
                  <rect width="{card_w}" height="{card_h}" rx="6" fill="{node_bg}" stroke="{node_border}" stroke-width="1"/>
                  <g transform="translate(10, 9) scale(0.95)">
                    <svg width="24" height="24" viewBox="0 0 24 24">{icon_inner}</svg>
                  </g>
                  <text x="42" y="26" class="sans-text" font-size="11" font-weight="600" fill="{text_primary}">{label}</text>
                </g>
                '''
            else:
                # Vertical node card format
                tier_markup += f'''
                <g transform="translate({x}, {y})">
                  <rect width="{card_w}" height="{card_h}" rx="8" fill="{node_bg}" stroke="{node_border}" stroke-width="1"/>
                  <g transform="translate(32, 14) scale(1)">
                    <svg width="24" height="24" viewBox="0 0 24 24">{icon_inner}</svg>
                  </g>
                  <text x="{card_w/2}" y="56" text-anchor="middle" class="sans-text" font-size="11" font-weight="600" fill="{text_primary}">{label}</text>
                </g>
                '''

        tier_markup += '</g>'
        rendered_tiers.append(tier_markup)

    tiers_content = "\n".join(rendered_tiers)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {total_height}" width="100%" height="100%">
  <defs>
    {svg_defs}
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="{total_height}" fill="{bg_color}" rx="16"/>
  <rect width="1200" height="{total_height}" fill="url(#stackGrid)" rx="16"/>
  <rect x="20" y="20" width="1160" height="{total_height-40}" rx="14" fill="none" stroke="{card_border}" stroke-width="1.5"/>

  <!-- Section Header -->
  <g transform="translate(40, 45)">
    <rect x="0" y="0" width="190" height="24" rx="4" fill="rgba(0, 229, 255, 0.1)" stroke="rgba(0, 229, 255, 0.3)" stroke-width="1"/>
    <text x="10" y="16" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">02 // ARCHITECTURE</text>
    <text x="210" y="18" class="sans-text" font-size="18" font-weight="700" fill="{text_primary}">Frontend Engine &amp; Full-Stack Pipeline</text>
    <text x="1120" y="17" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">MODULAR • REACT-CENTRIC</text>
    <line x1="0" y1="36" x2="1120" y2="36" stroke="{card_border}" stroke-width="1"/>
  </g>

  <!-- Tiers Content -->
  {tiers_content}

  <!-- Data Flow Animation Indicator -->
  <g transform="translate(40, {total_height-35})">
    <rect width="1120" height="1" fill="{card_border}"/>
    <circle cx="280" cy="0" r="3.5" fill="#00E5FF" class="photon"/>
    <text x="0" y="18" class="mono-text" font-size="10.5" fill="{text_muted}">DATA FLOW: CLIENT RUNTIME ➔ MOTION LAYER ➔ REST API INTEGRATION ➔ PERSISTENCE</text>
  </g>
</svg>'''
    return svg


def xml_escape(text):
    if not isinstance(text, str):
        return text
    return (text.replace("&", "&amp;")
                .replace("<", "&lt;")
                .replace(">", "&gt;"))

# ==============================================================================
# 03. FEATURED PROJECTS SHOWCASE
# ==============================================================================
def build_projects_svg(dark=True):
    bg_color = "#0B0F19" if dark else "#F8FAFC"
    card_bg = "#111827" if dark else "#FFFFFF"
    card_border = "rgba(99, 102, 241, 0.2)" if dark else "rgba(99, 102, 241, 0.15)"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.06)" if dark else "rgba(99, 102, 241, 0.04)"
    tag_bg = "rgba(139, 92, 246, 0.12)" if dark else "rgba(139, 92, 246, 0.08)"
    tag_border = "rgba(139, 92, 246, 0.25)" if dark else "rgba(139, 92, 246, 0.2)"
    tag_text = "#8B5CF6" if dark else "#6D28D9"

    PROJECTS = [
        {
            "num": "01",
            "name": "Magdha Studios",
            "category": "Interactive Game Promotion Platform",
            "desc": "High-impact gaming showcase portal engineered with modular React componentry, fluid UI animations, dynamic interactive showcases, and low-latency asset delivery across devices.",
            "tech": ["React.js", "Tailwind CSS", "JavaScript", "Motion UI", "Vite"],
            "accent": "#00E5FF",
            "status": "Production Release"
        },
        {
            "num": "02",
            "name": "Get2Vacation CMS",
            "category": "Travel Content Management System &amp; Suite",
            "desc": "Comprehensive administrative dashboard with dynamic CRUD workflows, destination catalog managers, package builders, and integrated REST API pipelines via Axios.",
            "tech": ["React.js", "Tailwind CSS", "Node.js", "Express.js", "REST APIs", "Axios"],
            "accent": "#8B5CF6",
            "status": "Enterprise Core"
        },
        {
            "num": "03",
            "name": "Get2Vacations Portal",
            "category": "Travel Discovery &amp; Booking Experience",
            "desc": "Consumer travel portal featuring high-performance React Router client-side navigation, dynamic query filtering, and scalable component architecture for rich travel itineraries.",
            "tech": ["React.js", "Tailwind CSS", "React Router", "Axios", "REST APIs"],
            "accent": "#10B981",
            "status": "Active Deployment"
        },
        {
            "num": "04",
            "name": "Royal IT Corporate Portal",
            "category": "Enterprise Services &amp; Client Platform",
            "desc": "Engineered responsive, accessible corporate portal delivering ~50% enhanced mobile usability, cross-browser compatibility, and modular reusable design system components.",
            "tech": ["React.js", "JavaScript ES6+", "Tailwind CSS", "HTML5", "CSS3"],
            "accent": "#F59E0B",
            "status": "Client Production"
        }
    ]

    cards_markup = []
    positions = [
        (40, 95),   # Top Left
        (610, 95),  # Top Right
        (40, 320),  # Bottom Left
        (610, 320)  # Bottom Right
    ]

    for idx, p in enumerate(PROJECTS):
        px, py = positions[idx]
        accent = p["accent"]
        tags_svg = ""
        tx = 24
        for tag in p["tech"]:
            tag_escaped = xml_escape(tag)
            tw = len(tag) * 7.5 + 16
            tags_svg += f'''
            <rect x="{tx}" y="165" width="{tw}" height="24" rx="4" fill="{tag_bg}" stroke="{tag_border}" stroke-width="1"/>
            <text x="{tx + tw/2}" y="181" text-anchor="middle" class="mono-text" font-size="10.5" font-weight="600" fill="{tag_text}">{tag_escaped}</text>
            '''
            tx += tw + 8

        cards_markup.append(f'''
        <!-- Card {p["num"]}: {p["name"]} -->
        <g transform="translate({px}, {py})">
          <!-- Card Container -->
          <rect width="550" height="205" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
          <rect width="5" height="205" rx="2.5" fill="{accent}"/>

          <!-- Card Header -->
          <text x="24" y="32" class="mono-text" font-size="11" font-weight="700" fill="{accent}" letter-spacing="1.5">PROJECT // {p["num"]}</text>
          <rect x="400" y="16" width="130" height="22" rx="11" fill="rgba(16, 185, 129, 0.08)" stroke="rgba(16, 185, 129, 0.25)" stroke-width="1"/>
          <circle cx="414" cy="27" r="3" fill="#10B981"/>
          <text x="424" y="31" class="mono-text" font-size="10" font-weight="600" fill="#10B981">{p["status"]}</text>

          <!-- Project Title & Subtitle -->
          <text x="24" y="62" class="sans-text" font-size="20" font-weight="700" fill="{text_primary}">{p["name"]}</text>
          <text x="24" y="82" class="sans-text" font-size="12.5" font-weight="600" fill="{text_secondary}">{p["category"]}</text>

          <!-- Description (2 lines) -->
          <text x="24" y="112" class="sans-text" font-size="12" fill="{text_muted}">{xml_escape(p["desc"][:75])}...</text>
          <text x="24" y="130" class="sans-text" font-size="12" fill="{text_muted}">{xml_escape(p["desc"][75:150])}...</text>

          <!-- Tech Tags -->
          {tags_svg}
        </g>
        ''')

    cards_str = "\n".join(cards_markup)

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 560" width="100%" height="100%">
  <defs>
    <pattern id="projGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="560" fill="{bg_color}" rx="16"/>
  <rect width="1200" height="560" fill="url(#projGrid)" rx="16"/>
  <rect x="20" y="20" width="1160" height="520" rx="14" fill="none" stroke="{card_border}" stroke-width="1.5"/>

  <!-- Section Header -->
  <g transform="translate(40, 45)">
    <rect x="0" y="0" width="165" height="24" rx="4" fill="rgba(139, 92, 246, 0.1)" stroke="rgba(139, 92, 246, 0.3)" stroke-width="1"/>
    <text x="10" y="16" class="mono-text" font-size="11" font-weight="700" fill="#8B5CF6" letter-spacing="2">03 // PROJECTS</text>
    <text x="185" y="18" class="sans-text" font-size="18" font-weight="700" fill="{text_primary}">Featured Engineering Implementations</text>
    <text x="1120" y="17" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">PRODUCTION &amp; CLIENT SYSTEMS</text>
    <line x1="0" y1="36" x2="1120" y2="36" stroke="{card_border}" stroke-width="1"/>
  </g>

  <!-- Grid of Cards -->
  {cards_str}
</svg>'''
    return svg


# ==============================================================================
# 04. FOCUS & COMPETENCY MATRIX
# ==============================================================================
def build_focus_svg(dark=True):
    bg_color = "#0B0F19" if dark else "#F8FAFC"
    card_bg = "#111827" if dark else "#FFFFFF"
    card_border = "rgba(99, 102, 241, 0.2)" if dark else "rgba(99, 102, 241, 0.15)"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.06)" if dark else "rgba(99, 102, 241, 0.04)"
    bar_bg = "#1E293B" if dark else "#E2E8F0"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 450" width="100%" height="100%">
  <defs>
    <pattern id="focusGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="450" fill="{bg_color}" rx="16"/>
  <rect width="1200" height="450" fill="url(#focusGrid)" rx="16"/>
  <rect x="20" y="20" width="1160" height="410" rx="14" fill="none" stroke="{card_border}" stroke-width="1.5"/>

  <!-- Section Header -->
  <g transform="translate(40, 45)">
    <rect x="0" y="0" width="150" height="24" rx="4" fill="rgba(16, 185, 129, 0.1)" stroke="rgba(16, 185, 129, 0.3)" stroke-width="1"/>
    <text x="10" y="16" class="mono-text" font-size="11" font-weight="700" fill="#10B981" letter-spacing="2">04 // DOMAINS</text>
    <text x="170" y="18" class="sans-text" font-size="18" font-weight="700" fill="{text_primary}">Engineering Focus &amp; Core Competencies</text>
    <text x="1120" y="17" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">CRAFT &amp; ARCHITECTURE</text>
    <line x1="0" y1="36" x2="1120" y2="36" stroke="{card_border}" stroke-width="1"/>
  </g>

  <!-- Left Column: Engineering Allocation -->
  <g transform="translate(40, 95)">
    <rect width="540" height="250" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
    <text x="24" y="32" class="mono-text" font-size="12" font-weight="700" fill="#00E5FF" letter-spacing="1.5">ENGINEERING ALLOCATION</text>
    <text x="24" y="52" class="sans-text" font-size="12" fill="{text_muted}">Focus distribution across product delivery lifecycle</text>

    <!-- Bar 1: Frontend Architecture -->
    <g transform="translate(24, 75)">
      <text x="0" y="12" class="sans-text" font-size="12.5" font-weight="600" fill="{text_primary}">Frontend Architecture &amp; Component Systems</text>
      <text x="492" y="12" text-anchor="end" class="mono-text" font-size="12" font-weight="700" fill="#00E5FF">40%</text>
      <rect y="20" width="492" height="8" rx="4" fill="{bar_bg}"/>
      <rect y="20" width="197" height="8" rx="4" fill="#00E5FF"/>
    </g>

    <!-- Bar 2: UI Motion & Interaction -->
    <g transform="translate(24, 118)">
      <text x="0" y="12" class="sans-text" font-size="12.5" font-weight="600" fill="{text_primary}">Motion, Interaction &amp; Responsive UI</text>
      <text x="492" y="12" text-anchor="end" class="mono-text" font-size="12" font-weight="700" fill="#8B5CF6">25%</text>
      <rect y="20" width="492" height="8" rx="4" fill="{bar_bg}"/>
      <rect y="20" width="123" height="8" rx="4" fill="#8B5CF6"/>
    </g>

    <!-- Bar 3: REST APIs & Services -->
    <g transform="translate(24, 161)">
      <text x="0" y="12" class="sans-text" font-size="12.5" font-weight="600" fill="{text_primary}">REST APIs &amp; Application Services</text>
      <text x="492" y="12" text-anchor="end" class="mono-text" font-size="12" font-weight="700" fill="#10B981">20%</text>
      <rect y="20" width="492" height="8" rx="4" fill="{bar_bg}"/>
      <rect y="20" width="98" height="8" rx="4" fill="#10B981"/>
    </g>

    <!-- Bar 4: Data & Cloud Persistence -->
    <g transform="translate(24, 204)">
      <text x="0" y="12" class="sans-text" font-size="12.5" font-weight="600" fill="{text_primary}">Data Models, Databases &amp; Cloud Workflows</text>
      <text x="492" y="12" text-anchor="end" class="mono-text" font-size="12" font-weight="700" fill="#F59E0B">15%</text>
      <rect y="20" width="492" height="8" rx="4" fill="{bar_bg}"/>
      <rect y="20" width="74" height="8" rx="4" fill="#F59E0B"/>
    </g>
  </g>

  <!-- Right Column: Core Competency Matrix -->
  <g transform="translate(620, 95)">
    <rect width="540" height="250" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
    <text x="24" y="32" class="mono-text" font-size="12" font-weight="700" fill="#8B5CF6" letter-spacing="1.5">PROFESSIONAL COMPETENCIES</text>
    <text x="24" y="52" class="sans-text" font-size="12" fill="{text_muted}">Key engineering principles &amp; methodologies</text>

    <!-- Competency Badges Grid -->
    <g transform="translate(24, 75)">
      <!-- Comp 1 -->
      <rect x="0" y="0" width="235" height="38" rx="6" fill="rgba(99, 102, 241, 0.08)" stroke="{card_border}" stroke-width="1"/>
      <circle cx="16" cy="19" r="4" fill="#00E5FF"/>
      <text x="28" y="23" class="sans-text" font-size="11.5" font-weight="600" fill="{text_primary}">Component Reusability</text>

      <!-- Comp 2 -->
      <rect x="250" y="0" width="242" height="38" rx="6" fill="rgba(99, 102, 241, 0.08)" stroke="{card_border}" stroke-width="1"/>
      <circle cx="266" cy="19" r="4" fill="#8B5CF6"/>
      <text x="278" y="23" class="sans-text" font-size="11.5" font-weight="600" fill="{text_primary}">Cross-Browser Fidelity</text>

      <!-- Comp 3 -->
      <rect x="0" y="50" width="235" height="38" rx="6" fill="rgba(99, 102, 241, 0.08)" stroke="{card_border}" stroke-width="1"/>
      <circle cx="16" cy="69" r="4" fill="#10B981"/>
      <text x="28" y="73" class="sans-text" font-size="11.5" font-weight="600" fill="{text_primary}">Async API State Handling</text>

      <!-- Comp 4 -->
      <rect x="250" y="50" width="242" height="38" rx="6" fill="rgba(99, 102, 241, 0.08)" stroke="{card_border}" stroke-width="1"/>
      <circle cx="266" cy="69" r="4" fill="#F59E0B"/>
      <text x="278" y="73" class="sans-text" font-size="11.5" font-weight="600" fill="{text_primary}">Performance Optimization</text>

      <!-- Comp 5 -->
      <rect x="0" y="100" width="235" height="38" rx="6" fill="rgba(99, 102, 241, 0.08)" stroke="{card_border}" stroke-width="1"/>
      <circle cx="16" cy="119" r="4" fill="#EC4899"/>
      <text x="28" y="123" class="sans-text" font-size="11.5" font-weight="600" fill="{text_primary}">Responsive Architecture</text>

      <!-- Comp 6 -->
      <rect x="250" y="100" width="242" height="38" rx="6" fill="rgba(99, 102, 241, 0.08)" stroke="{card_border}" stroke-width="1"/>
      <circle cx="266" cy="119" r="4" fill="#00E5FF"/>
      <text x="278" y="123" class="sans-text" font-size="11.5" font-weight="600" fill="{text_primary}">Agile Team Collaboration</text>
    </g>
  </g>

  <!-- Bottom Passion & Strategy Bar -->
  <g transform="translate(40, 360)">
    <rect width="1120" height="55" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1"/>
    <text x="24" y="32" class="mono-text" font-size="11" font-weight="700" fill="{text_muted}" letter-spacing="1.5">BEYOND CODE:</text>
    
    <!-- Item 1 -->
    <text x="160" y="32" class="sans-text" font-size="12" font-weight="600" fill="{text_primary}">♟️ Chess Tactics <tspan fill="{text_muted}" font-weight="400">(Strategic problem solving)</tspan></text>
    <!-- Item 2 -->
    <text x="470" y="32" class="sans-text" font-size="12" font-weight="600" fill="{text_primary}">🎨 UI &amp; Interaction Craft <tspan fill="{text_muted}" font-weight="400">(Micro-interactions)</tspan></text>
    <!-- Item 3 -->
    <text x="790" y="32" class="sans-text" font-size="12" font-weight="600" fill="{text_primary}">✍️ Creative Writing &amp; Tech Exploration</text>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 05. GITHUB ACTIVITY & TELEMETRY
# ==============================================================================
def build_telemetry_svg(dark=True):
    bg_color = "#0B0F19" if dark else "#F8FAFC"
    card_bg = "#111827" if dark else "#FFFFFF"
    card_border = "rgba(99, 102, 241, 0.2)" if dark else "rgba(99, 102, 241, 0.15)"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.06)" if dark else "rgba(99, 102, 241, 0.04)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 320" width="100%" height="100%">
  <defs>
    <pattern id="telemGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="320" fill="{bg_color}" rx="16"/>
  <rect width="1200" height="320" fill="url(#telemGrid)" rx="16"/>
  <rect x="20" y="20" width="1160" height="280" rx="14" fill="none" stroke="{card_border}" stroke-width="1.5"/>

  <!-- Section Header -->
  <g transform="translate(40, 45)">
    <rect x="0" y="0" width="155" height="24" rx="4" fill="rgba(0, 229, 255, 0.1)" stroke="rgba(0, 229, 255, 0.3)" stroke-width="1"/>
    <text x="10" y="16" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">05 // TELEMETRY</text>
    <text x="175" y="18" class="sans-text" font-size="18" font-weight="700" fill="{text_primary}">Developer Activity &amp; Engineering Pulse</text>
    <text x="1120" y="17" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">GITHUB @Roshani-sahu</text>
    <line x1="0" y1="36" x2="1120" y2="36" stroke="{card_border}" stroke-width="1"/>
  </g>

  <!-- 3 Metric Panels -->
  <g transform="translate(40, 95)">
    <!-- Metric 1: Focus Stack -->
    <g transform="translate(0, 0)">
      <rect width="350" height="175" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="175" rx="2" fill="#00E5FF"/>
      <text x="24" y="32" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="1">PRIMARY DOMAIN</text>
      <text x="24" y="68" class="sans-text" font-size="28" font-weight="800" fill="{text_primary}">React &amp; UI</text>
      <text x="24" y="98" class="sans-text" font-size="13" fill="{text_secondary}">Frontend Application Architecture</text>
      <text x="24" y="122" class="sans-text" font-size="13" fill="{text_secondary}">Tailwind CSS • TypeScript • Vite</text>
      <text x="24" y="152" class="mono-text" font-size="11" fill="#10B981">● ACTIVE DEVELOPMENT</text>
    </g>

    <!-- Metric 2: Full-Stack Integration -->
    <g transform="translate(385, 0)">
      <rect width="350" height="175" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="175" rx="2" fill="#8B5CF6"/>
      <text x="24" y="32" class="mono-text" font-size="11" font-weight="700" fill="#8B5CF6" letter-spacing="1">SERVICES &amp; DATA</text>
      <text x="24" y="68" class="sans-text" font-size="28" font-weight="800" fill="{text_primary}">MERN Stack</text>
      <text x="24" y="98" class="sans-text" font-size="13" fill="{text_secondary}">REST APIs • Node.js • Express</text>
      <text x="24" y="122" class="sans-text" font-size="13" fill="{text_secondary}">MongoDB • MySQL • JWT Auth</text>
      <text x="24" y="152" class="mono-text" font-size="11" fill="#8B5CF6">● END-TO-END FLOW</text>
    </g>

    <!-- Metric 3: Engineering Standards -->
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


# ==============================================================================
# 06. CONNECT FOOTER & BUTTON NODES
# ==============================================================================
def build_footer_svg(dark=True):
    bg_color = "#0B0F19" if dark else "#F8FAFC"
    card_bg = "#111827" if dark else "#FFFFFF"
    card_border = "rgba(99, 102, 241, 0.25)" if dark else "rgba(99, 102, 241, 0.2)"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.06)" if dark else "rgba(99, 102, 241, 0.04)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 240" width="100%" height="100%">
  <defs>
    <pattern id="footGrid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
    </pattern>
    <linearGradient id="footAccent" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#00E5FF"/>
      <stop offset="50%" stop-color="#8B5CF6"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <!-- Background Base -->
  <rect width="1200" height="240" fill="{bg_color}" rx="16"/>
  <rect width="1200" height="240" fill="url(#footGrid)" rx="16"/>
  <rect x="20" y="20" width="1160" height="200" rx="14" fill="none" stroke="{card_border}" stroke-width="1.5"/>

  <!-- Top Accent Bar -->
  <rect x="20" y="20" width="1160" height="3" fill="url(#footAccent)"/>

  <!-- Center Content -->
  <g transform="translate(60, 55)">
    <text x="0" y="24" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">06 // GET IN TOUCH</text>
    <text x="0" y="60" class="sans-text" font-size="26" font-weight="800" fill="{text_primary}">Let's Build Something Exceptional Together</text>
    <text x="0" y="90" class="sans-text" font-size="14" fill="{text_secondary}">
      Open for frontend engineering roles, React development, full-stack opportunities, and innovative web projects.
    </text>
  </g>

  <!-- Channels Info Box -->
  <g transform="translate(760, 50)">
    <rect width="380" height="135" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
    
    <!-- GitHub -->
    <g transform="translate(20, 24)">
      <circle cx="6" cy="6" r="3.5" fill="#00E5FF"/>
      <text x="20" y="10" class="sans-text" font-size="12.5" font-weight="700" fill="{text_primary}">GitHub:</text>
      <text x="80" y="10" class="mono-text" font-size="12" fill="#00E5FF">github.com/Roshani-sahu</text>
    </g>

    <!-- LinkedIn -->
    <g transform="translate(20, 60)">
      <circle cx="6" cy="6" r="3.5" fill="#8B5CF6"/>
      <text x="20" y="10" class="sans-text" font-size="12.5" font-weight="700" fill="{text_primary}">LinkedIn:</text>
      <text x="90" y="10" class="mono-text" font-size="12" fill="#8B5CF6">roshani-sahu-1606b5228</text>
    </g>

    <!-- Email -->
    <g transform="translate(20, 96)">
      <circle cx="6" cy="6" r="3.5" fill="#10B981"/>
      <text x="20" y="10" class="sans-text" font-size="12.5" font-weight="700" fill="{text_primary}">Email:</text>
      <text x="75" y="10" class="mono-text" font-size="12" fill="#10B981">roshani032003@gmail.com</text>
    </g>
  </g>
</svg>'''
    return svg


def build_button_svg(channel="github", dark=True):
    bg_color = "#111827" if dark else "#FFFFFF"
    border_color = "rgba(99, 102, 241, 0.3)" if dark else "rgba(99, 102, 241, 0.2)"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_muted = "#94A3B8" if dark else "#64748B"

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

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 380 90" width="100%" height="100%">
  <defs>
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>
  <rect width="380" height="90" rx="10" fill="{bg_color}" stroke="{border_color}" stroke-width="1.5"/>
  <rect width="4" height="90" rx="2" fill="{accent}"/>
  
  <g transform="translate(20, 23) scale(1.8)">
    <svg width="24" height="24" viewBox="0 0 24 24">{icon}</svg>
  </g>

  <g transform="translate(80, 24)">
    <text x="0" y="16" class="sans-text" font-size="14" font-weight="700" fill="{text_primary}">{label}</text>
    <text x="0" y="38" class="mono-text" font-size="12" fill="{accent}">{handle}</text>
  </g>
</svg>'''
    return svg


def main():
    print("Building all custom SVG assets for Roshani Sahu...")

    targets = [
        ("hero", "hero-dark.svg", build_hero_svg(dark=True)),
        ("hero", "hero-light.svg", build_hero_svg(dark=False)),
        ("stack", "stack-flow-dark.svg", build_stack_svg(dark=True)),
        ("stack", "stack-flow-light.svg", build_stack_svg(dark=False)),
        ("projects", "showcase-dark.svg", build_projects_svg(dark=True)),
        ("projects", "showcase-light.svg", build_projects_svg(dark=False)),
        ("focus", "focus-matrix-dark.svg", build_focus_svg(dark=True)),
        ("focus", "focus-matrix-light.svg", build_focus_svg(dark=False)),
        ("activity", "telemetry-dark.svg", build_telemetry_svg(dark=True)),
        ("activity", "telemetry-light.svg", build_telemetry_svg(dark=False)),
        ("footer", "connect-dark.svg", build_footer_svg(dark=True)),
        ("footer", "connect-light.svg", build_footer_svg(dark=False)),
        ("footer", "btn-github-dark.svg", build_button_svg("github", dark=True)),
        ("footer", "btn-github-light.svg", build_button_svg("github", dark=False)),
        ("footer", "btn-linkedin-dark.svg", build_button_svg("linkedin", dark=True)),
        ("footer", "btn-linkedin-light.svg", build_button_svg("linkedin", dark=False)),
        ("footer", "btn-email-dark.svg", build_button_svg("email", dark=True)),
        ("footer", "btn-email-light.svg", build_button_svg("email", dark=False)),
    ]

    for subdir, filename, content in targets:
        dirpath = os.path.join(ASSETS_DIR, subdir)
        os.makedirs(dirpath, exist_ok=True)
        filepath = os.path.join(dirpath, filename)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        
        # XML Validation
        try:
            ET.fromstring(content)
            print(f"  [OK] Generated & validated XML: assets/{subdir}/{filename}")
        except ET.ParseError as err:
            print(f"  [ERROR] XML syntax error in assets/{subdir}/{filename}: {err}")

    print("All assets successfully created and validated!")

if __name__ == "__main__":
    main()
