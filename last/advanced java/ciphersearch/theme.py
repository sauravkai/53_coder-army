"""
CipherSearch UI Theme — Premium Cybersecurity SaaS
==================================================
Enhanced theme with dark mode, improved accessibility, and modern design elements.
Applies to ALL pages: Login, Dashboard, Upload, Search, Security Proof, Benchmark.
"""

CIPHERSEARCH_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500;600&display=swap');

/* ──────────────────────────────────────────────────────────────────
   COLOR PALETTE — Enhanced with dark mode support
   Light base + vibrant accents + comprehensive semantic colors
   ────────────────────────────────────────────────────────────────── */
:root {
  /* Light theme colors */
  --bg-primary:     #f8fafc;
  --bg-secondary:   #ffffff;
  --bg-tertiary:    #f1f5f9;
  --bg-warm:        #fefefe;
  --surface:        #ffffff;
  --surface-hover:  #f8fafc;
  --sidebar-bg:     #f1f5f9;
  --overlay:        rgba(15, 23, 42, 0.04);

  /* Borders */
  --border-light:   rgba(15, 23, 42, 0.08);
  --border-medium:  rgba(15, 23, 42, 0.12);
  --border-strong:  rgba(15, 23, 42, 0.16);

  /* Primary accent — vibrant teal */
  --accent-primary:     #0d9488;
  --accent-primary-dim: rgba(13, 148, 136, 0.08);
  --accent-primary-glow: rgba(13, 148, 136, 0.15);
  --accent-primary-hover: #0f766e;

  /* Secondary accent — ocean blue */
  --accent-secondary:   #0891b2;
  --accent-secondary-dim: rgba(8, 145, 178, 0.08);

  /* Tertiary accent — soft violet */
  --accent-tertiary:    #7c3aed;
  --accent-tertiary-dim: rgba(124, 58, 237, 0.08);

  /* Gradients */
  --gradient-primary: linear-gradient(135deg, #0d9488 0%, #0891b2 50%, #06b6d4 100%);
  --gradient-secondary: linear-gradient(135deg, #7c3aed 0%, #a855f7 100%);
  --gradient-surface: linear-gradient(135deg, rgba(255, 255, 255, 0.1) 0%, rgba(255, 255, 255, 0.05) 100%);

  /* Semantic colors */
  --success:        #059669;
  --success-dim:    rgba(5, 150, 105, 0.08);
  --success-light:  rgba(5, 150, 105, 0.15);
  --error:          #dc2626;
  --error-dim:      rgba(220, 38, 38, 0.08);
  --error-light:    rgba(220, 38, 38, 0.15);
  --warning:        #d97706;
  --warning-dim:    rgba(217, 119, 6, 0.08);
  --warning-light:  rgba(217, 119, 6, 0.15);
  --info:           #0891b2;
  --info-dim:       rgba(8, 145, 178, 0.08);
  --info-light:     rgba(8, 145, 178, 0.15);

  /* Text hierarchy */
  --text-primary:   #0f172a;
  --text-secondary: #334155;
  --text-tertiary:  #64748b;
  --text-muted:     #94a3b8;
  --text-inverse:   #ffffff;

  /* Shadows */
  --shadow-sm:      0 1px 2px 0 rgba(0, 0, 0, 0.05);
  --shadow-md:      0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
  --shadow-lg:      0 10px 15px -3px rgba(0, 0, 0, 0.1), 0 4px 6px -2px rgba(0, 0, 0, 0.05);
  --shadow-xl:      0 20px 25px -5px rgba(0, 0, 0, 0.1), 0 10px 10px -5px rgba(0, 0, 0, 0.04);
  --shadow-glow:    0 0 20px rgba(13, 148, 136, 0.3);

  /* Typography */
  --font-sans:      'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --font-mono:      'JetBrains Mono', 'SF Mono', 'Monaco', 'Inconsolata', monospace;

  /* Spacing */
  --radius-sm:      6px;
  --radius-md:      8px;
  --radius-lg:      12px;
  --radius-xl:      16px;
  --radius-2xl:     24px;

  /* Transitions */
  --transition-fast: all 0.15s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-normal: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
  --transition-slow: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Dark theme override */
[data-theme="dark"] {
  --bg-primary:     #0f172a;
  --bg-secondary:   #1e293b;
  --bg-tertiary:    #334155;
  --bg-warm:        #1e293b;
  --surface:        #1e293b;
  --surface-hover:  #334155;
  --sidebar-bg:     #0f172a;
  --overlay:        rgba(255, 255, 255, 0.04);

  --border-light:   rgba(255, 255, 255, 0.08);
  --border-medium:  rgba(255, 255, 255, 0.12);
  --border-strong:  rgba(255, 255, 255, 0.16);

  --accent-primary-dim: rgba(13, 148, 136, 0.12);
  --accent-primary-glow: rgba(13, 148, 136, 0.25);
  --accent-secondary-dim: rgba(8, 145, 178, 0.12);
  --accent-tertiary-dim: rgba(124, 58, 237, 0.12);

  --success-dim:    rgba(5, 150, 105, 0.12);
  --success-light:  rgba(5, 150, 105, 0.25);
  --error-dim:      rgba(220, 38, 38, 0.12);
  --error-light:    rgba(220, 38, 38, 0.25);
  --warning-dim:    rgba(217, 119, 6, 0.12);
  --warning-light:  rgba(217, 119, 6, 0.25);
  --info-dim:       rgba(8, 145, 178, 0.12);
  --info-light:     rgba(8, 145, 178, 0.25);

  --text-primary:   #f8fafc;
  --text-secondary: #cbd5e1;
  --text-tertiary:  #94a3b8;
  --text-muted:     #64748b;

  --shadow-sm:      0 1px 2px 0 rgba(0, 0, 0, 0.3);
  --shadow-md:      0 4px 6px -1px rgba(0, 0, 0, 0.4), 0 2px 4px -1px rgba(0, 0, 0, 0.3);
  --shadow-lg:      0 10px 15px -3px rgba(0, 0, 0, 0.5), 0 4px 6px -2px rgba(0, 0, 0, 0.4);
  --shadow-xl:      0 20px 25px -5px rgba(0, 0, 0, 0.6), 0 10px 10px -5px rgba(0, 0, 0, 0.5);
  --shadow-glow:    0 0 20px rgba(13, 148, 136, 0.4);

  --gradient-surface: linear-gradient(135deg, rgba(255, 255, 255, 0.05) 0%, rgba(255, 255, 255, 0.02) 100%);
}

/* ──────────────────────────────────────────────────────────────────
   BASE & LAYOUT — Enhanced with better responsive design
   ────────────────────────────────────────────────────────────────── */
.stApp {
  background: var(--bg-primary) !important;
  background-image:
    radial-gradient(ellipse 100% 60% at 50% -10%, var(--accent-primary-glow), transparent 50%),
    radial-gradient(ellipse 80% 50% at 100% 50%, rgba(124, 58, 237, 0.06), transparent 50%) !important;
  color: var(--text-primary) !important;
  font-family: var(--font-sans) !important;
  transition: var(--transition-normal) !important;
}

[data-testid="stAppViewContainer"] {
  background: transparent !important;
}

[data-testid="stHeader"] {
  background: transparent !important;
}

.main .block-container {
  padding: clamp(1rem, 4vw, 3rem) clamp(1rem, 5vw, 4rem) clamp(2rem, 6vw, 4rem) !important;
  max-width: 1400px !important;
  margin: 0 auto !important;
  position: relative !important;
  z-index: 2 !important;
}

/* ──────────────────────────────────────────────────────────────────
   SIDEBAR — Enhanced with better navigation
   ────────────────────────────────────────────────────────────────── */
[data-testid="stSidebar"] {
  background: var(--sidebar-bg) !important;
  border-right: 1px solid var(--border-light) !important;
  padding-top: 1.5rem !important;
  backdrop-filter: blur(12px) !important;
  transition: var(--transition-normal) !important;
}

[data-testid="stSidebar"] > div:first-child {
  padding-top: 0.5rem !important;
}

[data-testid="stSidebar"] [data-testid="stMarkdown"]:first-of-type {
  font-family: var(--font-sans) !important;
  font-weight: 700 !important;
  font-size: 18px !important;
  color: var(--text-primary) !important;
  letter-spacing: -0.02em !important;
  margin-bottom: 1rem !important;
  padding: 0 1rem !important;
}

[data-testid="stSidebar"] .stRadio > div {
  background: transparent !important;
  padding: 0.5rem 0.75rem !important;
  gap: 4px !important;
}

[data-testid="stSidebar"] .stRadio > div > label {
  background: transparent !important;
  border-radius: var(--radius-lg) !important;
  padding: 12px 16px !important;
  margin: 2px 0 !important;
  border: 1px solid transparent !important;
  transition: var(--transition-fast) !important;
  position: relative !important;
  overflow: hidden !important;
}

[data-testid="stSidebar"] .stRadio > div > label::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: -100% !important;
  width: 100% !important;
  height: 100% !important;
  background: linear-gradient(90deg, transparent, var(--accent-primary-glow), transparent) !important;
  transition: left 0.5s !important;
}

[data-testid="stSidebar"] .stRadio > div > label:hover::before {
  left: 100% !important;
}

[data-testid="stSidebar"] .stRadio > div > label:hover {
  background: var(--accent-primary-dim) !important;
  border-color: rgba(13, 148, 136, 0.25) !important;
  transform: translateX(4px) !important;
}

[data-testid="stSidebar"] .stRadio > div > label:has(input:checked) {
  background: var(--accent-primary-dim) !important;
  border-color: rgba(13, 148, 136, 0.35) !important;
  box-shadow: 0 0 0 2px var(--accent-primary-glow), var(--shadow-sm) !important;
  transform: translateX(4px) !important;
}

[data-testid="stSidebar"] .stRadio label span {
  font-family: var(--font-sans) !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  color: var(--text-secondary) !important;
  position: relative !important;
  z-index: 1 !important;
}

[data-testid="stSidebar"] .stRadio label:has(input:checked) span {
  color: var(--accent-primary) !important;
  font-weight: 600 !important;
}

[data-testid="stSidebar"] [data-testid="stSuccess"],
[data-testid="stSidebar"] [data-testid="stError"] {
  padding: 8px 12px !important;
  border-radius: var(--radius-lg) !important;
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  margin: 8px 0 !important;
}
[data-testid="stSidebar"] [data-testid="stSuccess"] {
  background: var(--success-dim) !important;
  color: var(--success) !important;
  border: 1px solid var(--success-light) !important;
}
[data-testid="stSidebar"] [data-testid="stError"] {
  background: var(--error-dim) !important;
  color: var(--error) !important;
  border: 1px solid var(--error-light) !important;
}

/* ──────────────────────────────────────────────────────────────────
   TYPOGRAPHY — Enhanced hierarchy and readability
   ────────────────────────────────────────────────────────────────── */
.main h1 {
  font-family: var(--font-sans) !important;
  font-size: clamp(24px, 5vw, 32px) !important;
  font-weight: 700 !important;
  color: var(--text-primary) !important;
  letter-spacing: -0.03em !important;
  line-height: 1.25 !important;
  margin-bottom: 1rem !important;
}

.main h2 {
  font-family: var(--font-sans) !important;
  font-size: clamp(20px, 4vw, 24px) !important;
  font-weight: 600 !important;
  color: var(--text-primary) !important;
  letter-spacing: -0.02em !important;
  margin-bottom: 0.75rem !important;
}

.main h3 {
  font-family: var(--font-sans) !important;
  font-size: clamp(16px, 3vw, 18px) !important;
  font-weight: 600 !important;
  color: var(--text-secondary) !important;
  margin-bottom: 0.5rem !important;
}

.main p, .main span, .main label {
  font-family: var(--font-sans) !important;
  color: var(--text-secondary) !important;
  font-size: 14px !important;
  line-height: 1.6 !important;
}

.main [data-testid="stCaptionContainer"] {
  color: var(--text-tertiary) !important;
  font-family: var(--font-sans) !important;
}

/* ──────────────────────────────────────────────────────────────────
   METRIC CARDS — Enhanced with glassmorphism effect
   ────────────────────────────────────────────────────────────────── */
div[data-testid="stMetric"] {
  background: var(--surface) !important;
  border: 1px solid var(--border-light) !important;
  border-radius: var(--radius-xl) !important;
  padding: 24px !important;
  text-align: center !important;
  transition: var(--transition-slow) !important;
  box-shadow: var(--shadow-sm) !important;
  backdrop-filter: blur(12px) !important;
  position: relative !important;
  overflow: hidden !important;
}

div[data-testid="stMetric"]::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  height: 3px !important;
  background: var(--gradient-primary) !important;
  opacity: 0 !important;
  transition: var(--transition-normal) !important;
}

div[data-testid="stMetric"]:hover {
  transform: translateY(-4px) scale(1.02) !important;
  border-color: var(--border-medium) !important;
  box-shadow: var(--shadow-lg), 0 0 0 1px var(--accent-primary-glow) !important;
}

div[data-testid="stMetric"]:hover::before {
  opacity: 1 !important;
}

div[data-testid="stMetric"] label {
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 500 !important;
  color: var(--text-muted) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
  margin-bottom: 8px !important;
}

div[data-testid="stMetric"] [data-testid="stMetricValue"] {
  font-family: var(--font-sans) !important;
  font-size: clamp(28px, 6vw, 36px) !important;
  font-weight: 700 !important;
  color: var(--accent-primary) !important;
  letter-spacing: -0.02em !important;
  background: linear-gradient(135deg, var(--accent-primary), var(--accent-secondary)) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
}

/* ──────────────────────────────────────────────────────────────────
   BUTTONS — Enhanced with better states and accessibility
   ────────────────────────────────────────────────────────────────── */
.stButton > button {
  font-family: var(--font-sans) !important;
  font-size: 14px !important;
  font-weight: 600 !important;
  border-radius: var(--radius-lg) !important;
  padding: 12px 24px !important;
  transition: var(--transition-fast) !important;
  border: none !important;
  position: relative !important;
  overflow: hidden !important;
  cursor: pointer !important;
  outline: none !important;
}

.stButton > button:focus-visible {
  box-shadow: 0 0 0 3px var(--accent-primary-glow) !important;
}

.stButton > button[kind="primary"] {
  background: var(--gradient-primary) !important;
  color: var(--text-inverse) !important;
  box-shadow: var(--shadow-md) !important;
  position: relative !important;
}

.stButton > button[kind="primary"]::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: -100% !important;
  width: 100% !important;
  height: 100% !important;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.2), transparent) !important;
  transition: left 0.5s !important;
}

.stButton > button[kind="primary"]:hover::before {
  left: 100% !important;
}

.stButton > button[kind="primary"]:hover {
  transform: translateY(-2px) !important;
  box-shadow: var(--shadow-lg), 0 0 20px var(--accent-primary-glow) !important;
  filter: brightness(1.05) !important;
}

.stButton > button[kind="primary"]:active {
  transform: translateY(0) !important;
  box-shadow: var(--shadow-md) !important;
}

.stButton > button[kind="secondary"] {
  background: var(--surface) !important;
  border: 1px solid var(--border-medium) !important;
  color: var(--text-secondary) !important;
  box-shadow: var(--shadow-sm) !important;
}

.stButton > button[kind="secondary"]:hover {
  background: var(--surface-hover) !important;
  border-color: var(--accent-primary) !important;
  color: var(--accent-primary) !important;
  transform: translateY(-1px) !important;
  box-shadow: var(--shadow-md) !important;
}

/* ──────────────────────────────────────────────────────────────────
   INPUTS — Enhanced with better focus states
   ────────────────────────────────────────────────────────────────── */
.stTextInput input, .stTextArea textarea {
  background: var(--surface) !important;
  border: 1px solid var(--border-medium) !important;
  border-radius: var(--radius-lg) !important;
  font-family: var(--font-sans) !important;
  font-size: 14px !important;
  color: var(--text-primary) !important;
  padding: 14px 16px !important;
  transition: var(--transition-fast) !important;
  box-shadow: var(--shadow-sm) !important;
}

.stTextInput input:focus, .stTextArea textarea:focus {
  border-color: var(--accent-primary) !important;
  box-shadow: 0 0 0 3px var(--accent-primary-glow), var(--shadow-md) !important;
  outline: none !important;
  transform: translateY(-1px) !important;
}

.stTextInput input::placeholder, .stTextArea textarea::placeholder {
  color: var(--text-muted) !important;
  font-style: italic !important;
}

/* ──────────────────────────────────────────────────────────────────
   RADIO / TABS — Enhanced with better visual feedback
   ────────────────────────────────────────────────────────────────── */
.stRadio > div {
  background: var(--surface) !important;
  border: 1px solid var(--border-light) !important;
  border-radius: var(--radius-xl) !important;
  padding: 8px !important;
  box-shadow: var(--shadow-sm) !important;
  backdrop-filter: blur(8px) !important;
}

.stRadio label {
  font-family: var(--font-sans) !important;
  font-size: 14px !important;
  font-weight: 500 !important;
  color: var(--text-secondary) !important;
  border-radius: var(--radius-md) !important;
  padding: 10px 18px !important;
  transition: var(--transition-fast) !important;
  cursor: pointer !important;
  position: relative !important;
}

.stRadio label:hover {
  color: var(--text-primary) !important;
  background: var(--accent-primary-dim) !important;
  transform: translateY(-1px) !important;
}

.stRadio label:has(input:checked) {
  background: var(--gradient-primary) !important;
  color: var(--text-inverse) !important;
  box-shadow: var(--shadow-sm) !important;
  font-weight: 600 !important;
}

/* ──────────────────────────────────────────────────────────────────
   ALERTS — Enhanced with better visual hierarchy
   ────────────────────────────────────────────────────────────────── */
.stAlert {
  border-radius: var(--radius-lg) !important;
  font-family: var(--font-sans) !important;
  font-size: 14px !important;
  border: 1px solid !important;
  padding: 16px 20px !important;
  margin: 12px 0 !important;
  box-shadow: var(--shadow-sm) !important;
  backdrop-filter: blur(8px) !important;
  position: relative !important;
  overflow: hidden !important;
}

.stAlert::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  width: 4px !important;
  height: 100% !important;
  background: var(--gradient-primary) !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="info"] {
  background: var(--info-dim) !important;
  border-color: var(--info-light) !important;
  color: var(--info) !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="success"] {
  background: var(--success-dim) !important;
  border-color: var(--success-light) !important;
  color: var(--success) !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="error"] {
  background: var(--error-dim) !important;
  border-color: var(--error-light) !important;
  color: var(--error) !important;
}

[data-testid="stAlert"][data-baseweb="notification"][kind="warning"] {
  background: var(--warning-dim) !important;
  border-color: var(--warning-light) !important;
  color: var(--warning) !important;
}

/* ──────────────────────────────────────────────────────────────────
   CODE BLOCKS & EXPANDERS — Enhanced styling
   ────────────────────────────────────────────────────────────────── */
.stCodeBlock, code {
  background: var(--bg-tertiary) !important;
  border: 1px solid var(--border-light) !important;
  border-radius: var(--radius-lg) !important;
  font-family: var(--font-mono) !important;
  font-size: 13px !important;
  color: var(--text-secondary) !important;
  padding: 16px !important;
  box-shadow: var(--shadow-sm) !important;
  position: relative !important;
}

.stCodeBlock::before {
  content: 'Code' !important;
  position: absolute !important;
  top: 8px !important;
  right: 12px !important;
  font-size: 10px !important;
  font-weight: 600 !important;
  color: var(--text-muted) !important;
  text-transform: uppercase !important;
  letter-spacing: 0.08em !important;
}

.streamlit-expanderHeader {
  background: var(--surface) !important;
  border: 1px solid var(--border-light) !important;
  border-radius: var(--radius-lg) !important;
  color: var(--text-primary) !important;
  font-family: var(--font-sans) !important;
  font-weight: 500 !important;
  transition: var(--transition-fast) !important;
  box-shadow: var(--shadow-sm) !important;
  backdrop-filter: blur(8px) !important;
  padding: 16px 20px !important;
}

.streamlit-expanderHeader:hover {
  background: var(--surface-hover) !important;
  border-color: var(--border-medium) !important;
  transform: translateY(-1px) !important;
  box-shadow: var(--shadow-md) !important;
}

.streamlit-expanderContent {
  background: var(--bg-secondary) !important;
  border: 1px solid var(--border-light) !important;
  border-top: none !important;
  border-radius: 0 0 var(--radius-lg) var(--radius-lg) !important;
  padding: 20px !important;
}

/* ──────────────────────────────────────────────────────────────────
   PROGRESS BARS — Enhanced visual feedback
   ────────────────────────────────────────────────────────────────── */
.stProgress > div > div {
  background: var(--gradient-primary) !important;
  border-radius: var(--radius-sm) !important;
  transition: width 0.3s ease !important;
  box-shadow: 0 0 10px var(--accent-primary-glow) !important;
}

.stProgress > div {
  background: var(--bg-tertiary) !important;
  border-radius: var(--radius-sm) !important;
  height: 8px !important;
}

/* ──────────────────────────────────────────────────────────────────
   LOGIN PAGE — Enhanced with modern design
   ────────────────────────────────────────────────────────────────── */
.login-container {
  min-height: calc(100vh - 120px);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.login-box {
  background: var(--surface) !important;
  border: 1px solid var(--border-light) !important;
  border-radius: var(--radius-2xl) !important;
  padding: clamp(32px, 8vw, 48px) !important;
  position: relative !important;
  overflow: hidden !important;
  max-width: 480px !important;
  margin: 0 auto !important;
  box-shadow: var(--shadow-xl) !important;
  backdrop-filter: blur(20px) !important;
}

.login-box::before {
  content: '' !important;
  position: absolute !important;
  top: 0 !important;
  left: 0 !important;
  right: 0 !important;
  height: 4px !important;
  background: var(--gradient-primary) !important;
}

.login-box::after {
  content: '' !important;
  position: absolute !important;
  top: -50% !important;
  left: -50% !important;
  width: 200% !important;
  height: 200% !important;
  background: var(--gradient-surface) !important;
  opacity: 0.5 !important;
  z-index: -1 !important;
}

.login-title {
  font-family: var(--font-sans) !important;
  font-size: clamp(24px, 6vw, 28px) !important;
  font-weight: 700 !important;
  color: var(--text-primary) !important;
  text-align: center !important;
  margin-bottom: 8px !important;
  letter-spacing: -0.03em !important;
}

.login-sub {
  font-family: var(--font-mono) !important;
  font-size: 12px !important;
  color: var(--text-muted) !important;
  text-align: center !important;
  letter-spacing: 0.08em !important;
  text-transform: uppercase !important;
}

.security-note {
  margin-top: 24px !important;
  padding: 20px !important;
  background: var(--bg-tertiary) !important;
  border: 1px solid var(--border-light) !important;
  border-radius: var(--radius-lg) !important;
  font-family: var(--font-mono) !important;
  font-size: 11px !important;
  font-weight: 600 !important;
  color: var(--text-muted) !important;
  letter-spacing: 0.08em !important;
  box-shadow: var(--shadow-sm) !important;
}

.security-note-desc {
  font-size: 14px !important;
  font-weight: 400 !important;
  color: var(--text-secondary) !important;
  line-height: 1.6 !important;
  margin-top: 8px !important;
}

/* ──────────────────────────────────────────────────────────────────
   ANIMATIONS & MICRO-INTERACTIONS
   ────────────────────────────────────────────────────────────────── */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(16px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes slideInRight {
  from {
    opacity: 0;
    transform: translateX(24px);
  }
  to {
    opacity: 1;
    transform: translateX(0);
  }
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.7;
  }
}

@keyframes shimmer {
  0% {
    background-position: -200px 0;
  }
  100% {
    background-position: calc(200px + 100%) 0;
  }
}

.fade-in {
  animation: fadeInUp 0.6s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.slide-in {
  animation: slideInRight 0.5s cubic-bezier(0.4, 0, 0.2, 1) forwards;
}

.pulse {
  animation: pulse 2s infinite;
}

.loading-shimmer {
  background: linear-gradient(90deg, var(--bg-tertiary) 25%, var(--surface-hover) 50%, var(--bg-tertiary) 75%);
  background-size: 200px 100%;
  animation: shimmer 1.5s infinite;
}

/* ──────────────────────────────────────────────────────────────────
   RESPONSIVE DESIGN
   ────────────────────────────────────────────────────────────────── */
@media (max-width: 768px) {
  .main .block-container {
    padding: 1rem !important;
  }

  .login-box {
    margin: 1rem !important;
    padding: 24px !important;
  }

  div[data-testid="stMetric"] {
    padding: 16px !important;
  }

  [data-testid="stSidebar"] {
    width: 280px !important;
  }
}

@media (max-width: 480px) {
  .main h1 {
    font-size: 24px !important;
  }

  .login-box {
    padding: 20px !important;
  }

  .stButton > button {
    padding: 10px 20px !important;
    font-size: 13px !important;
  }
}

/* ──────────────────────────────────────────────────────────────────
   ACCESSIBILITY IMPROVEMENTS
   ────────────────────────────────────────────────────────────────── */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}

*:focus-visible {
  outline: 2px solid var(--accent-primary) !important;
  outline-offset: 2px !important;
}

/* High contrast mode support */
@media (prefers-contrast: high) {
  :root {
    --border-light: rgba(255, 255, 255, 0.2);
    --border-medium: rgba(255, 255, 255, 0.4);
    --border-strong: rgba(255, 255, 255, 0.6);
  }

  [data-theme="dark"] {
    --border-light: rgba(0, 0, 0, 0.3);
    --border-medium: rgba(0, 0, 0, 0.5);
    --border-strong: rgba(0, 0, 0, 0.7);
  }
}

/* ──────────────────────────────────────────────────────────────────
   SCROLLBAR & UTILITIES
   ────────────────────────────────────────────────────────────────── */
::-webkit-scrollbar {
  width: 8px;
  height: 8px;
}

::-webkit-scrollbar-track {
  background: var(--bg-tertiary);
  border-radius: var(--radius-sm);
}

::-webkit-scrollbar-thumb {
  background: var(--text-muted);
  border-radius: var(--radius-sm);
  transition: var(--transition-fast);
}

::-webkit-scrollbar-thumb:hover {
  background: var(--text-tertiary);
}

hr {
  border: none !important;
  height: 1px !important;
  background: var(--border-light) !important;
  margin: 2rem 0 !important;
}

/* Utility classes */
.glass-effect {
  backdrop-filter: blur(12px) !important;
  background: var(--gradient-surface) !important;
}

.shadow-glow {
  box-shadow: var(--shadow-glow) !important;
}

.text-gradient {
  background: var(--gradient-primary) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
}
"""
