# -*- coding: utf-8 -*-
"""
Builder script to generate complete, production-grade index.html
with all master requirements implemented.
"""

import os, sys

def get_head_html():
    return '''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>AICTE Integrated Institution Complaint Monitoring & Tracking Dashboard | SIH 2026</title>
  <meta name="description" content="Centralized platform for AICTE officials, institutions, universities, faculty, and students to monitor, track, manage, and analyze complaints across Regulation Bureau (RB), PGRC, and other Bureaus with AI overlap detection and Hive AI evidence screening.">
  
  <!-- Google Fonts: Plus Jakarta Sans, Inter, JetBrains Mono -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700;800&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  
  <!-- Tailwind CSS CDN -->
  <script src="https://cdn.tailwindcss.com"></script>
  <script>
    tailwind.config = {
      darkMode: 'class',
      theme: {
        extend: {
          colors: {
            gov: {
              navy: '#003366',       /* AICTE Institutional Blue */
              darkNavy: '#002244',   /* Deep Government Navy */
              blue: '#004085',       /* Secondary Institutional Blue */
              lightBlue: '#0077B6',  /* Primary Accent Blue */
              teal: '#008080',       /* Restrained Government Teal */
              darkTeal: '#006666',   /* Deep Teal */
              cyan: '#00B4D8',       /* Accent Highlight */
              surface: '#F8FAFC',    /* Light Slate Background */
              card: '#FFFFFF',       /* Clean White Card */
              border: '#E2E8F0',     /* Border Gray */
              gold: '#D97706',       /* Warm Gold */
              amber: '#F59E0B',      /* Warning Amber */
              green: '#15803D',      /* Gov Forest Green */
              crimson: '#DC2626'     /* Alert Red */
            }
          },
          fontFamily: {
            sans: ['"Plus Jakarta Sans"', 'Inter', 'sans-serif'],
            mono: ['"JetBrains Mono"', 'monospace']
          },
          boxShadow: {
            'card': '0 4px 20px -2px rgba(0, 34, 68, 0.06), 0 2px 6px -1px rgba(0, 34, 68, 0.04)',
            'card-hover': '0 12px 30px -4px rgba(0, 34, 68, 0.12), 0 4px 10px -2px rgba(0, 34, 68, 0.06)',
            'modal': '0 25px 50px -12px rgba(0, 34, 68, 0.25)',
            'glow-teal': '0 0 15px rgba(0, 128, 128, 0.35)',
            'glow-amber': '0 0 15px rgba(245, 158, 11, 0.35)'
          }
        }
      }
    }
  </script>

  <!-- Chart.js for data visualization -->
  <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>

  <!-- Lucide Icons CDN -->
  <script src="https://unpkg.com/lucide@latest/dist/umd/lucide.js"></script>

  <style>
    /* Custom Scrollbar */
    ::-webkit-scrollbar {
      width: 6px;
      height: 6px;
    }
    ::-webkit-scrollbar-track {
      background: #F1F5F9;
    }
    ::-webkit-scrollbar-thumb {
      background: #CBD5E1;
      border-radius: 4px;
    }
    ::-webkit-scrollbar-thumb:hover {
      background: #94A3B8;
    }

    /* Pulse animation for overlap alert */
    @keyframes subtlePulse {
      0%, 100% { opacity: 1; transform: scale(1); }
      50% { opacity: 0.95; transform: scale(1.008); }
    }
    .pulse-urgent {
      animation: subtlePulse 2.5s infinite ease-in-out;
    }

    /* Custom badges & transitions */
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 0.375rem;
      padding: 0.25rem 0.65rem;
      border-radius: 9999px;
      font-size: 0.725rem;
      font-weight: 600;
      letter-spacing: 0.025em;
    }

    .tab-active {
      border-bottom: 2px solid #008080;
      color: #003366;
      font-weight: 700;
    }

    /* Glassmorphism subtle overlay */
    .glass-nav {
      background: rgba(0, 34, 68, 0.96);
      backdrop-filter: blur(12px);
    }

    /* Slide-Down Animation */
    @keyframes slideDownDropdown {
      0% {
        opacity: 0;
        transform: translateY(-8px) scale(0.97);
      }
      100% {
        opacity: 1;
        transform: translateY(0) scale(1);
      }
    }
    .animate-slide-down {
      animation: slideDownDropdown 0.22s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    }
  </style>
</head>
<body class="bg-gov-surface font-sans text-slate-800 antialiased min-h-screen flex flex-col">
'''

def build():
    import build_modules.landing as l
    import build_modules.wizard_modals as wm
    import build_modules.portal_views as pv
    import build_modules.scripts_logic as sl

    print("[Build] Assembling index.html from verified modular components...")
    head_html = get_head_html()
    landing_html = l.get_landing_html()
    wizard_modals_html = wm.get_wizard_and_modals_html()
    portal_html = pv.get_portal_html()
    scripts_js = sl.get_scripts_js()

    full_html = (
        head_html + "\n" +
        landing_html + "\n" +
        wizard_modals_html + "\n" +
        portal_html + "\n" +
        "  <!-- Core Logic, Data State, Router, Overlap Engine, Chart.js -->\n" +
        "  <script>\n" +
        scripts_js + "\n" +
        "  </script>\n" +
        "</body>\n" +
        "</html>\n"
    )

    out_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(full_html)

    print(f"[Build] Successfully written {len(full_html)} bytes to {out_file}.")
    return full_html

if __name__ == '__main__':
    build()
