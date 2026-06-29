import streamlit as st
from components.home import show_home
from components.gallery import show_gallery
from components.team import show_team
from components.pricing import show_pricing

# Must be the first Streamlit command
st.set_page_config(
    page_title="Babita Film Production",
    page_icon="📸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Global CSS (works in both light and dark themes)
st.markdown("""
<style>

/* Center the logo */
.logo {
    display: flex;
    justify-content: center;
    margin-bottom: 20px;
}

/* Sidebar title */
section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] label {
    font-weight: 600;
}

/* ========================= */
/* GLOBAL IMAGE STYLE FIX    */
/* ========================= */

/* Only apply to main content images (not sidebar/logo) */
.main img {
    width: 100% !important;
    height: 320px !important;      /* uniform portrait size */
    object-fit: cover !important;  /* crop landscape properly */
    border-radius: 12px !important;
}

/* Optional spacing improvement */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

</style>
""", unsafe_allow_html=True)

# Logo
st.markdown('<div class="logo">', unsafe_allow_html=True)
st.image("images/logo.png", width=220)
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📸 Babita Film Production")

page = st.sidebar.radio(
    "Navigation",
    ["Home", "Our Work", "Pricing", "Our Team"]
)

# Page Routing
if page == "Home":
    show_home()

elif page == "Our Work":
    show_gallery()

elif page == "Pricing":
    show_pricing()

elif page == "Our Team":
    show_team()