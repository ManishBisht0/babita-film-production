import streamlit as st
from components.home import show_home
from components.gallery import show_gallery
from components.team import show_team
from components.pricing import show_pricing

# ============================
# PAGE CONFIG
# ============================
st.set_page_config(
    page_title="Babita Film Production",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================
# GLOBAL CSS
# ============================
st.markdown("""
<style>

/* Main app background */
.stApp {
    background-color: #f8f4ef;
}

/* ========================= */
/* SIDEBAR */
/* ========================= */

section[data-testid="stSidebar"] {
    background-color: #1f2230;
}

/* Sidebar text */
section[data-testid="stSidebar"] * {
    color: white !important;
}

/* Sidebar title */
section[data-testid="stSidebar"] h1 {
    color: white !important;
    font-weight: bold;
}

/* Radio labels */
div[role="radiogroup"] label {
    color: white !important;
}

/* Selected radio text */
div[role="radiogroup"] p {
    color: white !important;
}

/* ========================= */
/* LOGO */
/* ========================= */

.logo {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

/* ========================= */
/* IMAGE FIX */
/* ========================= */

/* Main content images */
.main img {
    width: 100% !important;
    height: 320px !important;
    object-fit: cover !important;
    border-radius: 15px !important;
}

/* ========================= */
/* PAGE SPACING */
/* ========================= */

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* ========================= */
/* HERO SECTION */
/* ========================= */

.hero {
    background: linear-gradient(
        135deg,
        #fff8f0,
        #f4ebe2
    );
    padding: 40px;
    border-radius: 20px;
    border: 1px solid #e5d5c7;
}

/* ========================= */
/* CARDS */
/* ========================= */

.card {
    background: white;
    padding: 20px;
    border-radius: 20px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
}

</style>
""", unsafe_allow_html=True)

# ============================
# SIDEBAR LOGO
# ============================
with st.sidebar:
    st.image("images/logo.png", width=180)

# ============================
# SIDEBAR TITLE
# ============================
st.sidebar.title("📸 Babita Film Production")

# ============================
# NAVIGATION
# ============================
page = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Our Work",
        "Pricing",
        "Our Team"
    ]
)

# ============================
# PAGE ROUTING
# ============================
if page == "Home":
    show_home()

elif page == "Our Work":
    show_gallery()

elif page == "Pricing":
    show_pricing()

elif page == "Our Team":
    show_team()