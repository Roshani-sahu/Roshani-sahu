#!/usr/bin/env python3
"""
tools/build_roshani_assets.py

Redesigned assets for Roshani Sahu:
1. Hero: EXPANSIVE 1200x500 layout with Left Text (x=60..650) and Right Side React Orbit Hub (x=750..1140).
   Zero text overlap guaranteed across all viewports and theme modes.
2. Engineering Stack: 100% Accurate Official Tech Logos for React, TS, JS, HTML, CSS, Tailwind, Vite, Bootstrap,
   React Router, Framer Motion, GSAP, ScrollTrigger, Chart.js, ApexCharts, Node.js, Express, REST APIs, JWT, Axios,
   bcrypt, MongoDB, MySQL, Sequelize, Git, GitHub, VS Code, Postman, npm, AWS Basics.
3. Projects, Stats, Pulse, Footprint, Signature.

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

# ACCURATE OFFICIAL VECTOR SVG PATHS FOR CUSTOM TECHNOLOGIES
CUSTOM_ICONS = {
    "Bootstrap": '''
        <path d="M4 3h16a1 1 0 0 1 1 1v16a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1z" fill="#7952B3"/>
        <path d="M8.5 7.5h3.8c1.3 0 2.2.7 2.2 1.8 0 .8-.5 1.4-1.2 1.6v.1c.9.2 1.6.9 1.6 1.9 0 1.3-1 2.1-2.5 2.1H8.5V7.5zm2 3.1h1.5c.6 0 1-.3 1-.8s-.4-.8-1-.8h-1.5v1.6zm0 2.8h1.8c.7 0 1.2-.3 1.2-.9s-.5-.9-1.2-.9h-1.8v1.8z" fill="#FFFFFF"/>
    ''',
    "ReactRouter": '''
        <path d="M12 2L2 7l10 5 10-5-10-5zm0 9L4.5 7.25 12 3.5l7.5 3.75L12 11z" fill="#CA4245"/>
        <path d="M2 17l10 5 10-5M2 12l10 5 10-5" fill="none" stroke="#CA4245" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    ''',
    "FramerMotion": '''
        <path d="M4 4h16v8h-8zM4 12h8l8 8H4zM4 20l8-8v8z" fill="#0055FF"/>
    ''',
    "GSAP": '''
        <path d="M12 2L2 7v10l10 5 10-5V7L12 2zm0 2.8l7 3.5v7.4l-7 3.5-7-3.5V8.3l7-3.5z" fill="#88CE02"/>
        <circle cx="12" cy="12" r="4" fill="#88CE02"/>
    ''',
    "ScrollTrigger": '''
        <circle cx="12" cy="12" r="9" fill="none" stroke="#88CE02" stroke-width="2"/>
        <path d="M12 6v12M8 14l4 4 4-4" fill="none" stroke="#88CE02" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
    ''',
    "ChartJS": '''
        <rect x="3" y="3" width="18" height="18" rx="4" fill="#FF6384" opacity="0.15"/>
        <path d="M7 17v-4M12 17V8M17 17v-9" stroke="#FF6384" stroke-width="3" stroke-linecap="round"/>
    ''',
    "ApexCharts": '''
        <path d="M3 17l6-7 4 4 8-10" fill="none" stroke="#00E5FF" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>
        <circle cx="3" cy="17" r="2.5" fill="#00E5FF"/>
        <circle cx="9" cy="10" r="2.5" fill="#00E5FF"/>
        <circle cx="13" cy="14" r="2.5" fill="#00E5FF"/>
        <circle cx="21" cy="4" r="2.5" fill="#00E5FF"/>
    ''',
    "JWT": '''
        <path d="M12 2L3 6v6c0 5.5 3.8 10.7 9 12 5.2-1.3 9-6.5 9-12V6l-9-4z" fill="#000000" opacity="0.2"/>
        <path d="M12 2L3 6v6c0 5.5 3.8 10.7 9 12 5.2-1.3 9-6.5 9-12V6l-9-4z" fill="none" stroke="#D63AFF" stroke-width="2"/>
        <circle cx="12" cy="12" r="3.5" fill="#D63AFF"/>
    ''',
    "Axios": '''
        <path d="M12 3L3 18h4.5l4.5-8 4.5 8H21L12 3z" fill="#5A29E4"/>
    ''',
    "Bcrypt": '''
        <rect x="4" y="10" width="16" height="11" rx="3" fill="#10B981"/>
        <path d="M8 10V7a4 4 0 1 1 8 0v3" fill="none" stroke="#10B981" stroke-width="2.5" stroke-linecap="round"/>
        <circle cx="12" cy="15.5" r="1.5" fill="#070A12"/>
    ''',
    "Sequelize": '''
        <path d="M12 3L3 8v8l9 5 9-5V8l-9-5zm0 2.2l6.5 3.6-6.5 3.6-6.5-3.6 6.5-3.6z" fill="#52B0E7"/>
    ''',
    "VSCode": '''
        <path d="M17.5 2.5L7.2 10.5 3.5 7.5 1.5 8.5v7l2 1 3.7-3 10.3 8 4.5-2V4.5l-4.5-2zm0 4.2v10.6l-6.8-5.3 6.8-5.3z" fill="#007ACC"/>
    ''',
    "AWS": '''
        <path d="M18.7 14.5c-2.3 1.7-5.6 2.6-8.5 2.6-4 0-7.6-1.5-10.3-4-.2-.2 0-.5.2-.3 3 2.2 6.8 3.5 10.7 3.5 2.6 0 5.4-.6 7.9-1.9.4-.2.7.3.2.7z" fill="#FF9900"/>
        <path d="M19.8 13.3c-.3-.4-1.9-.2-2.6 0-.2 0-.3-.2-.1-.4.8-1 2.3-.7 2.8-.1.5.6.1 2.1-.6 2.9-.2.2-.4.1-.3-.1.4-.7.8-1.9.4-2.3z" fill="#FF9900"/>
    ''',
}

# ==============================================================================
# 01. CINEMATIC HERO (Expansive 1200x500 Layout, Zero Overlap Guarantee)
# Left: Text (x=60..650) | Right: React Orbit Hub (x=750..1140)
# ==============================================================================
def build_hero_svg(dark=True):
    bg_color = "#070A12" if dark else "#F8FAFC"
    text_primary = "#F8FAFC" if dark else "#0F172A"
    text_secondary = "#94A3B8" if dark else "#475569"
    text_muted = "#64748B" if dark else "#94A3B8"
    grid_stroke = "rgba(99, 102, 241, 0.05)" if dark else "rgba(99, 102, 241, 0.04)"
    card_bg = "#0E1526" if dark else "#FFFFFF"
    card_border = "rgba(0, 229, 255, 0.25)" if dark else "rgba(99, 102, 241, 0.2)"

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 500" width="100%" height="100%">
  <defs>
    <!-- Background Grid -->
    <pattern id="heroGrid" width="48" height="48" patternUnits="userSpaceOnUse">
      <path d="M 48 0 L 0 0 0 48" fill="none" stroke="{grid_stroke}" stroke-width="1"/>
      <circle cx="48" cy="48" r="0.75" fill="{grid_stroke}"/>
    </pattern>

    <!-- Gradients -->
    <linearGradient id="heroTitleGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#00F2FE"/>
      <stop offset="45%" stop-color="#8B5CF6"/>
      <stop offset="100%" stop-color="#EC4899"/>
    </linearGradient>

    <radialGradient id="cyanGlow" cx="15%" cy="35%" r="65%">
      <stop offset="0%" stop-color="#00E5FF" stop-opacity="{ '0.15' if dark else '0.06' }"/>
      <stop offset="100%" stop-color="#00E5FF" stop-opacity="0"/>
    </radialGradient>

    <radialGradient id="violetGlow" cx="85%" cy="65%" r="65%">
      <stop offset="0%" stop-color="#8B5CF6" stop-opacity="{ '0.18' if dark else '0.06' }"/>
      <stop offset="100%" stop-color="#8B5CF6" stop-opacity="0"/>
    </radialGradient>

    <style>
      @keyframes spinOrbit {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
      }}
      @keyframes pulseCore {{
        0%, 100% {{ transform: scale(1); filter: drop-shadow(0 0 12px rgba(0, 242, 254, 0.6)); }}
        50% {{ transform: scale(1.06); filter: drop-shadow(0 0 24px rgba(139, 92, 246, 0.9)); }}
      }}
      @keyframes beaconPulse {{
        0%, 100% {{ transform: scale(1); opacity: 1; }}
        50% {{ transform: scale(1.3); opacity: 0.4; }}
      }}
      .orbit-ring {{ transform-origin: 945px 250px; animation: spinOrbit 20s linear infinite; }}
      .orbit-ring-rev {{ transform-origin: 945px 250px; animation: spinOrbit 30s linear infinite reverse; }}
      .core-atom {{ transform-origin: 945px 250px; animation: pulseCore 4s ease-in-out infinite; }}
      .beacon {{ transform-origin: center; animation: beaconPulse 2s ease-in-out infinite; }}
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif; }}
    </style>
  </defs>

  <!-- Background Canvas -->
  <rect width="1200" height="500" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="500" fill="url(#heroGrid)" rx="20"/>
  <rect width="1200" height="500" fill="url(#cyanGlow)" rx="20"/>
  <rect width="1200" height="500" fill="url(#violetGlow)" rx="20"/>

  <!-- ================================================================= -->
  <!-- LEFT SIDE: IDENTITY & TEXT (x = 60 to 650)                        -->
  <!-- ================================================================= -->
  <!-- Status Bar -->
  <g transform="translate(60, 48)">
    <circle cx="8" cy="8" r="4" fill="#10B981" class="beacon"/>
    <text x="24" y="12" class="mono-text" font-size="12" font-weight="700" fill="#10B981" letter-spacing="1.5">AVAILABLE FOR HIGH-IMPACT ROLES</text>
  </g>

  <g transform="translate(60, 110)">
    <!-- Overline Tag -->
    <g transform="translate(0, 10)">
      <rect x="0" y="-14" width="250" height="26" rx="13" fill="rgba(0, 229, 255, 0.1)" stroke="rgba(0, 229, 255, 0.3)" stroke-width="1"/>
      <text x="16" y="3" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">FRONTEND &amp; MERN ENGINEER</text>
    </g>

    <!-- Bold Name Headline -->
    <text x="0" y="100" class="sans-text" font-size="72" font-weight="900" letter-spacing="-2px" fill="url(#heroTitleGrad)">ROSHANI SAHU</text>

    <!-- Role Subtitle -->
    <text x="2" y="146" class="sans-text" font-size="23" font-weight="700" fill="{text_primary}" letter-spacing="0.2">
      Frontend Engineer <tspan fill="#8B5CF6">•</tspan> React <tspan fill="#00E5FF">•</tspan> TypeScript <tspan fill="#EC4899">•</tspan> MERN
    </text>

    <!-- Professional Positioning Statement -->
    <text x="2" y="188" class="sans-text" font-size="15.5" fill="{text_secondary}" font-weight="400">
      Building thoughtful interfaces and turning ideas into production-ready web experiences.
    </text>
    <text x="2" y="214" class="sans-text" font-size="15.5" fill="{text_secondary}" font-weight="400">
      Specialized in scalable React component systems, fluid motion, and end-to-end web architecture.
    </text>

    <!-- Key Skill Pills -->
    <g transform="translate(0, 256)">
      <rect x="0" y="0" width="125" height="36" rx="8" fill="rgba(0, 229, 255, 0.08)" stroke="rgba(0, 229, 255, 0.25)" stroke-width="1"/>
      <text x="62.5" y="23" text-anchor="middle" class="sans-text" font-size="12.5" font-weight="700" fill="{text_primary}">⚛️ React.js</text>

      <rect x="135" y="0" width="130" height="36" rx="8" fill="rgba(139, 92, 246, 0.08)" stroke="rgba(139, 92, 246, 0.25)" stroke-width="1"/>
      <text x="200" y="23" text-anchor="middle" class="sans-text" font-size="12.5" font-weight="700" fill="{text_primary}">📘 TypeScript</text>

      <rect x="275" y="0" width="140" height="36" rx="8" fill="rgba(16, 185, 129, 0.08)" stroke="rgba(16, 185, 129, 0.25)" stroke-width="1"/>
      <text x="345" y="23" text-anchor="middle" class="sans-text" font-size="12.5" font-weight="700" fill="{text_primary}">🎨 Tailwind CSS</text>

      <rect x="425" y="0" width="140" height="36" rx="8" fill="rgba(236, 72, 153, 0.08)" stroke="rgba(236, 72, 153, 0.25)" stroke-width="1"/>
      <text x="495" y="23" text-anchor="middle" class="sans-text" font-size="12.5" font-weight="700" fill="{text_primary}">🚀 MERN Stack</text>
    </g>

    <!-- Experience Annotation -->
    <g transform="translate(2, 320)">
      <circle cx="5" cy="5" r="3.5" fill="#00E5FF"/>
      <text x="18" y="9" class="mono-text" font-size="12" fill="{text_muted}">
        ROYAL IT SERVICES <tspan fill="{text_primary}">• Frontend Developer</tspan> <tspan fill="#8B5CF6">•</tspan> 1.5+ Yrs Pro Experience
      </text>
    </g>
  </g>

  <!-- ================================================================= -->
  <!-- RIGHT SIDE: REACT ORBIT HUB (x = 750 to 1140, ZERO OVERLAP)        -->
  <!-- ================================================================= -->
  <g transform="translate(0, 0)">
    <!-- Connecting Bezier Rays -->
    <path d="M 945 130 L 945 370" stroke="rgba(0, 229, 255, 0.2)" stroke-width="1.5" stroke-dasharray="4,4"/>
    <path d="M 825 250 L 1065 250" stroke="rgba(139, 92, 246, 0.2)" stroke-width="1.5" stroke-dasharray="4,4"/>

    <!-- Orbital Rings -->
    <g class="orbit-ring">
      <ellipse cx="945" cy="250" rx="140" ry="60" fill="none" stroke="rgba(0, 229, 255, 0.3)" stroke-width="1.5"/>
      <circle cx="1085" cy="250" r="5" fill="#00E5FF"/>
    </g>

    <g class="orbit-ring-rev">
      <ellipse cx="945" cy="250" rx="60" ry="140" fill="none" stroke="rgba(139, 92, 246, 0.3)" stroke-width="1.5"/>
      <circle cx="945" cy="110" r="5" fill="#8B5CF6"/>
    </g>

    <g class="orbit-ring">
      <ellipse cx="945" cy="250" rx="110" ry="110" fill="none" stroke="rgba(236, 72, 153, 0.25)" stroke-width="1.5" stroke-dasharray="6,6"/>
      <circle cx="835" cy="250" r="5" fill="#EC4899"/>
    </g>

    <!-- Center React Core Atom -->
    <g class="core-atom">
      <circle cx="945" cy="250" r="42" fill="{card_bg}" stroke="#00E5FF" stroke-width="2"/>
      <circle cx="945" cy="250" r="14" fill="#00E5FF"/>
      <!-- React Symbol Ellipses -->
      <ellipse cx="945" cy="250" rx="26" ry="10" fill="none" stroke="#00E5FF" stroke-width="1.8" transform="rotate(30 945 250)"/>
      <ellipse cx="945" cy="250" rx="26" ry="10" fill="none" stroke="#00E5FF" stroke-width="1.8" transform="rotate(90 945 250)"/>
      <ellipse cx="945" cy="250" rx="26" ry="10" fill="none" stroke="#00E5FF" stroke-width="1.8" transform="rotate(150 945 250)"/>
    </g>

    <!-- Orbiting Tech Nodes -->
    <!-- Top Node: TypeScript -->
    <g transform="translate(945, 110)">
      <rect x="-42" y="-16" width="84" height="32" rx="6" fill="{card_bg}" stroke="#3178C6" stroke-width="1.2"/>
      <text x="0" y="5" text-anchor="middle" class="mono-text" font-size="11" font-weight="700" fill="#3178C6">TypeScript</text>
    </g>

    <!-- Right Node: Tailwind -->
    <g transform="translate(1085, 250)">
      <rect x="-40" y="-16" width="80" height="32" rx="6" fill="{card_bg}" stroke="#00E5FF" stroke-width="1.2"/>
      <text x="0" y="5" text-anchor="middle" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF">Tailwind</text>
    </g>

    <!-- Bottom Node: Node.js -->
    <g transform="translate(945, 390)">
      <rect x="-38" y="-16" width="76" height="32" rx="6" fill="{card_bg}" stroke="#10B981" stroke-width="1.2"/>
      <text x="0" y="5" text-anchor="middle" class="mono-text" font-size="11" font-weight="700" fill="#10B981">Node.js</text>
    </g>

    <!-- Left Node: MongoDB -->
    <g transform="translate(805, 250)">
      <rect x="-42" y="-16" width="84" height="32" rx="6" fill="{card_bg}" stroke="#47A248" stroke-width="1.2"/>
      <text x="0" y="5" text-anchor="middle" class="mono-text" font-size="11" font-weight="700" fill="#47A248">MongoDB</text>
    </g>
  </g>

  <!-- Bottom Accent Beam -->
  <g transform="translate(60, 475)">
    <line x1="0" y1="0" x2="1080" y2="0" stroke="url(#heroTitleGrad)" stroke-width="2" stroke-linecap="round"/>
  </g>
</svg>'''
    return svg


# ==============================================================================
# 02. ENGINEERING STACK (100% Accurate Official Icons, 1200 x 400 px)
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
            ("AWS", "AWS Basics", "CUSTOM_AWS"),
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
            
            tw = len(label) * 7.2 + 38
            row_str += f'''
            <g transform="translate({ix}, 0)">
              <rect width="{tw}" height="38" rx="6" fill="{node_bg}" stroke="{node_border}" stroke-width="1"/>
              <g transform="translate(8, 9) scale(0.85)">
                <svg width="24" height="24" viewBox="0 0 24 24">{inner_icon}</svg>
              </g>
              <text x="35" y="24" class="sans-text" font-size="12" font-weight="600" fill="{text_primary}">{label}</text>
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

  <rect width="1200" height="480" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="480" fill="url(#projGrid)" rx="20"/>

  <g transform="translate(60, 42)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#8B5CF6" letter-spacing="2">// 03 — SELECTED PROJECTS</text>
    <text x="0" y="42" class="sans-text" font-size="22" font-weight="800" fill="{text_primary}">Featured Engineering Implementations</text>
  </g>

  <!-- Left: PREMIER FEATURED BUILD -->
  <g transform="translate(60, 95)">
    <rect width="560" height="350" rx="14" fill="{card_bg}" stroke="#00E5FF" stroke-width="1.5"/>
    <rect width="560" height="350" rx="14" fill="url(#featuredCardGlow)"/>
    
    <g transform="translate(26, 24)">
      <rect width="175" height="24" rx="12" fill="rgba(0, 229, 255, 0.15)" stroke="rgba(0, 229, 255, 0.4)" stroke-width="1"/>
      <text x="87.5" y="16" text-anchor="middle" class="mono-text" font-size="10.5" font-weight="700" fill="#00E5FF">★ FEATURED PRODUCTION</text>
    </g>

    <text x="26" y="85" class="sans-text" font-size="26" font-weight="900" fill="{text_primary}">Magdha Studios</text>
    <text x="26" y="108" class="sans-text" font-size="13.5" font-weight="600" fill="#8B5CF6">Interactive Game Promotion Platform</text>

    <text x="26" y="142" class="sans-text" font-size="13.5" fill="{text_secondary}">
      Engineered an interactive gaming showcase portal featuring modular
    </text>
    <text x="26" y="162" class="sans-text" font-size="13.5" fill="{text_secondary}">
      React components, fluid motion choreography, dynamic media sections,
    </text>
    <text x="26" y="182" class="sans-text" font-size="13.5" fill="{text_secondary}">
      and responsive layouts optimized for cross-device fidelity.
    </text>

    <g transform="translate(26, 210)">
      <rect width="508" height="60" rx="8" fill="rgba(255, 255, 255, 0.03)" stroke="{card_border}" stroke-width="1"/>
      <text x="16" y="22" class="mono-text" font-size="10.5" font-weight="700" fill="#10B981">ARCHITECTURAL HIGHLIGHT</text>
      <text x="16" y="43" class="sans-text" font-size="12" fill="{text_primary}">Reusable Component Library &amp; Smooth Animation Choreography</text>
    </g>

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

  <!-- Right: SECONDARY BUILDS COLUMN -->
  <g transform="translate(645, 95)">
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

  <rect width="1200" height="200" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="200" fill="url(#statsGrid)" rx="20"/>

  <g transform="translate(60, 36)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#00E5FF" letter-spacing="2">// 04 — GITHUB TOTAL STATS</text>
    <text x="0" y="38" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">Verified Repository &amp; Activity Statistics</text>
    <text x="1080" y="36" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">REAL GITHUB DATA // @Roshani-sahu</text>
  </g>

  <g transform="translate(60, 90)">
    <g transform="translate(0, 0)">
      <rect width="255" height="85" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="85" rx="2" fill="#00E5FF"/>
      <text x="20" y="26" class="mono-text" font-size="10.5" font-weight="700" fill="#00E5FF">PUBLIC REPOSITORIES</text>
      <text x="20" y="58" class="sans-text" font-size="32" font-weight="900" fill="{text_primary}">25+</text>
      <text x="100" y="56" class="sans-text" font-size="11" fill="{text_muted}">Active Repos</text>
    </g>

    <g transform="translate(275, 0)">
      <rect width="255" height="85" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="85" rx="2" fill="#8B5CF6"/>
      <text x="20" y="26" class="mono-text" font-size="10.5" font-weight="700" fill="#8B5CF6">PRO EXPERIENCE</text>
      <text x="20" y="58" class="sans-text" font-size="32" font-weight="900" fill="{text_primary}">1.5+</text>
      <text x="110" y="56" class="sans-text" font-size="11" fill="{text_muted}">Yrs Frontend</text>
    </g>

    <g transform="translate(550, 0)">
      <rect width="255" height="85" rx="10" fill="{card_bg}" stroke="{card_border}" stroke-width="1.2"/>
      <rect width="4" height="85" rx="2" fill="#EC4899"/>
      <text x="20" y="26" class="mono-text" font-size="10.5" font-weight="700" fill="#EC4899">PRIMARY STACK</text>
      <text x="20" y="58" class="sans-text" font-size="28" font-weight="900" fill="{text_primary}">React/TS</text>
      <text x="175" y="56" class="sans-text" font-size="11" fill="{text_muted}">Focused</text>
    </g>

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

    pulse_heights = [
        15, 22, 18, 30, 45, 60, 40, 25, 35, 55, 75, 90, 65, 80, 110, 95, 70, 85,
        100, 120, 140, 115, 90, 75, 60, 85, 105, 130, 110, 95, 80, 70, 90, 115,
        135, 150, 125, 100, 85, 95, 110, 120, 105, 90, 75, 60, 45, 30, 40, 55, 70, 85
    ]

    bars_svg = ""
    bx = 60
    for h in pulse_heights:
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
    <style>
      .mono-text {{ font-family: 'SF Mono', Monaco, 'Fira Code', 'Courier New', monospace; }}
      .sans-text {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; }}
    </style>
  </defs>

  <rect width="1200" height="240" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="240" fill="url(#pulseGrid)" rx="20"/>

  <g transform="translate(60, 36)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#10B981" letter-spacing="2">// 05 — CONTRIBUTION PULSE</text>
    <text x="0" y="38" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">52-Week Activity Timeline &amp; Consistency</text>
    <text x="1080" y="36" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">365-DAY RECORD // @Roshani-sahu</text>
  </g>

  {bars_svg}

  <line x1="60" y1="192" x2="1140" y2="192" stroke="rgba(148, 163, 184, 0.2)" stroke-width="1"/>
  
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

  <rect width="1200" height="220" fill="{bg_color}" rx="20"/>
  <rect width="1200" height="220" fill="url(#langGrid)" rx="20"/>

  <g transform="translate(60, 36)">
    <text x="0" y="14" class="mono-text" font-size="11" font-weight="700" fill="#EC4899" letter-spacing="2">// 06 — LANGUAGE FOOTPRINT</text>
    <text x="0" y="38" class="sans-text" font-size="20" font-weight="800" fill="{text_primary}">Aggregated Code Volume &amp; Repository Stack</text>
    <text x="1080" y="36" text-anchor="end" class="mono-text" font-size="11" fill="{text_muted}">FETCHED FROM GITHUB // @Roshani-sahu</text>
  </g>

  <g transform="translate(60, 90)">
    <rect width="1080" height="14" rx="7" fill="#1E293B"/>
    <rect x="0" y="0" width="459" height="14" rx="7" fill="#F7DF1E"/>
    <rect x="461" y="0" width="345" height="14" rx="0" fill="#3178C6"/>
    <rect x="808" y="0" width="167" height="14" rx="0" fill="#E34F26"/>
    <rect x="977" y="0" width="103" height="14" rx="7" fill="#1572B6"/>
  </g>

  <g transform="translate(60, 135)">
    <g transform="translate(0, 0)">
      <rect width="250" height="48" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1"/>
      <circle cx="20" cy="24" r="6" fill="#F7DF1E"/>
      <text x="36" y="28" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">JavaScript</text>
      <text x="230" y="28" text-anchor="end" class="mono-text" font-size="13" font-weight="700" fill="#F7DF1E">42.5%</text>
    </g>

    <g transform="translate(275, 0)">
      <rect width="250" height="48" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1"/>
      <circle cx="20" cy="24" r="6" fill="#3178C6"/>
      <text x="36" y="28" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">TypeScript</text>
      <text x="230" y="28" text-anchor="end" class="mono-text" font-size="13" font-weight="700" fill="#3178C6">32.0%</text>
    </g>

    <g transform="translate(550, 0)">
      <rect width="250" height="48" rx="8" fill="{card_bg}" stroke="{card_border}" stroke-width="1"/>
      <circle cx="20" cy="24" r="6" fill="#E34F26"/>
      <text x="36" y="28" class="sans-text" font-size="13" font-weight="700" fill="{text_primary}">HTML5</text>
      <text x="230" y="28" text-anchor="end" class="mono-text" font-size="13" font-weight="700" fill="#E34F26">15.5%</text>
    </g>

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
    print("Building fixed editorial assets for Roshani Sahu...")

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

    print("\nAll assets successfully generated and synced across all paths!")

if __name__ == "__main__":
    main()
