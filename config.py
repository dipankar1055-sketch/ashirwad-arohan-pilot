# 🌺 ASHIRWAD — ORGANIZER'S ASSISTANT
# Configuration File — Arohan Deployment

# ──────────────────────────────────────────────────────────────
# PRODUCT IDENTITY
# ──────────────────────────────────────────────────────────────

PRODUCT_NAME = "Ashirwad – Organizer's Assistant"
TAGLINE = "Helping Communities Organize Better. Govern Better. Grow Together."
PRODUCT_EMOJI = "🌺"

# ──────────────────────────────────────────────────────────────
# DEPLOYMENT
# ──────────────────────────────────────────────────────────────

DEPLOYMENT_NAME = "Arohan Pilot"
DEPLOYMENT_FULL = "Ashirwad × Arohan"
ORGANIZATION_NAME = "Arohan Durga Puja Committee"
LOCATION = "Krishnarajapuram · Bengaluru"

# ──────────────────────────────────────────────────────────────
# BRANDING
# ──────────────────────────────────────────────────────────────

AROHAN_LOGO = "assets/arohan_logo.png"
ASHIRWAD_LOGO = "assets/ashirwad_logo.png"
NEELKANTH_LOGO = "assets/neelkanth_logo.png"
FAVICON = "assets/favicon.ico"

# ──────────────────────────────────────────────────────────────
# MEMBERSHIP TYPES
# ──────────────────────────────────────────────────────────────

MEMBERSHIP_TYPES = {
    "New Member": 6000,
    "Existing Member": 5500,
    "Solo (New Member)": 2500,
    "Solo (Existing Member)": 2200
}

# ──────────────────────────────────────────────────────────────
# DEFAULT VALUES
# ──────────────────────────────────────────────────────────────

DEFAULT_MEMBERSHIP_TYPE = "New Member"
DEFAULT_AMOUNT = 6000
DEFAULT_PAYMENT_STATUS = "Pending"
DEFAULT_FOLLOWUP_STATUS = "Not Updated"

# ──────────────────────────────────────────────────────────────
# DONATION — ₹1 LAKH LIMIT
# ──────────────────────────────────────────────────────────────

MAX_DONATION_AMOUNT = 100000
MIN_DONATION_AMOUNT = 1

SUGGESTED_DONATIONS = [
    500, 1000, 5000, 10000, 25000, 50000, 75000, 100000
]

# ──────────────────────────────────────────────────────────────
# ADMIN USERS
# ──────────────────────────────────────────────────────────────

ADMIN_USERS = [
    {"name": "Souvick Sengupta", "role": "admin"},
    {"name": "Rishi", "role": "admin"},
    {"name": "Kaushik Acharya", "role": "admin"},
    {"name": "Soumitra", "role": "admin"},
    {"name": "Anirban", "role": "admin"},
    {"name": "Dipankar Kundu (TIGER)", "role": "super_admin"}
]

# ──────────────────────────────────────────────────────────────
# TEMPORARY CREDENTIALS
# ──────────────────────────────────────────────────────────────

DEFAULT_ADMIN_USERNAME = "admin"
DEFAULT_ADMIN_PASSWORD = "admin123"

# ──────────────────────────────────────────────────────────────
# ID FORMATS
# ──────────────────────────────────────────────────────────────

MEMBERSHIP_ID_FORMAT = "ARH-2026-M{id:04d}"
TRACE_ID_FORMAT = "TRC-ASH-{date}-{id:03d}"

# ──────────────────────────────────────────────────────────────
# PERFORMANCE
# ──────────────────────────────────────────────────────────────

LOAD_TIME_TARGET = "<3 seconds"
RESPONSIVE = True
SUPPORTED_BROWSERS = ["Chrome", "Edge", "Firefox"]
MOBILE_REQUIRED = True
OFFLINE_SUPPORT = False

# ──────────────────────────────────────────────────────────────
# CULTURAL THEME — Durga Puja
# ──────────────────────────────────────────────────────────────

THEME_COLORS = {
    "primary": "#8B0000",      # Crimson
    "secondary": "#A52A2A",    # Terracotta
    "accent": "#FFD700",       # Gold
    "text": "#FFD700",
    "background": "linear-gradient(135deg, #8B0000 0%, #A52A2A 50%, #D2691E 100%)"
}

FESTIVAL_TAGLINE = "🌺 Subho Sharodiya!"
FESTIVAL_EMOJI = "🌺"
