import streamlit as st
import os


def show_home():

    # ======================
    # CSS
    # ======================

    st.markdown("""
    <style>
    html, body, [class*="css"] {
        color: #222222;
    }

    h1 {
        color: #8B0000 !important;
    }

    h2, h3, h4, h5, h6 {
        color: #333333 !important;
    }

    p, li, span, div {
        color: #333333 !important;
    }

    .stMarkdown {
        color: #333333 !important;
    }

    .stApp {
        background-color: #f8f4ef;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>

    .stApp{
        background-color:#f8f4ef;
    }

    .hero{
        background:linear-gradient(135deg,#fff8f0,#f4ebe2);
        padding:45px;
        border-radius:25px;
        text-align:center;
        margin-bottom:35px;
        border:1px solid #e5d5c7;
    }

    .hero-title{
        color:#8B0000;
        font-size:50px;
        font-weight:bold;
    }

    .hero-subtitle{
        color:#555;
        font-size:28px;
    }

    .card{
        background:white;
        padding:30px;
        border-radius:20px;
        box-shadow:0px 5px 15px rgba(0,0,0,0.08);
    }

    .service-box{
        background:white;
        padding:20px;
        border-radius:20px;
        text-align:center;
        box-shadow:0px 5px 15px rgba(0,0,0,0.08);
        height:180px;
    }

    .footer{
        text-align:center;
        color:#555;
        margin-top:40px;
    }

    a{
        text-decoration:none;
    }

    </style>
    """, unsafe_allow_html=True)

    # ======================
    # HERO SECTION
    # ======================

    st.markdown("""
    <div class="hero">

    <div class="hero-title">
    📸 Babita Film Production
    </div>

    <br>

    <div class="hero-subtitle">
    Capturing Love • Emotions • Timeless Stories
    </div>


    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### 🎬 About Babita Film Production

    Babita Film Production is a passionate wedding photography and cinematography team dedicated to capturing timeless memories with creativity and emotion. Every frame we create is focused on storytelling, authenticity, and cinematic excellence.

    The journey began with **Mannu Airy**, who stepped into the world of photography and videography in **2010** as a camera operator. With strong dedication, consistency, and a deep love for visual storytelling, he worked tirelessly for nearly **two years gaining hands-on experience in the field**.

    Through hard work, learning, and commitment to perfection, he turned his passion into a professional vision and established **Babita Film Production**, a brand that now represents trust, quality, and cinematic wedding filmmaking.

    Today, Babita Film Production is known for its professional team, modern cinematic style, drone coverage, and attention to every detail — making every wedding story truly unforgettable.
    """)

    # ======================
    # OWNER SECTION
    # ======================

    st.header("📸 Meet The Founder")

    col1, col2 = st.columns([1, 2])

    with col1:
        if os.path.exists("images/owner.jpeg"):
            st.image("images/owner.jpeg", width=350)

    with col2:
        st.markdown("""
        ## Mr. Mannu Airy

        **Founder & Lead Photographer**

        With years of experience in wedding and event photography,
        Mr. Mannu Airy has dedicated his life to capturing emotions,
        love and unforgettable moments.

        His passion for photography goes beyond taking pictures.
        He believes every photograph tells a story and preserves
        memories that last forever.

        We use:

        ✅ Professional Cinematic Cameras

        ✅ Drone Photography & Videography

        ✅ Professional Editing Team

        ✅ Creative Storytelling

        ✅ Experienced Wedding Specialists

        **Turning precious moments into unforgettable memories.**
        """)

    st.divider()

    # ======================
    # ABOUT US
    # ======================

    st.header("✨ About Us")

    st.write("""
    Babita Film Production specializes in:

    📸 Wedding Photography

    🎥 Wedding Cinematography

    💍 Pre Wedding Shoots

    👶 Naming Ceremony Photography

    🎂 Birthday Photography

    🎉 Event Photography

    We capture your precious moments and turn them into timeless memories.
    """)

    st.divider()

    # ======================
    # SERVICES
    # ======================

    st.header("📷 Our Services")

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown("""
        <div class="service-box">
        <h3>💍 Wedding Photography</h3>
        <br>
        Traditional and cinematic wedding coverage.
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class="service-box">
        <h3>👶 Naming Ceremony</h3>
        <br>
        Capture your baby's special moments beautifully.
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class="service-box">
        <h3>🎂 Birthday Photography</h3>
        <br>
        Professional birthday event photography.
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    # ======================
    # GALLERY
    # ======================

    st.header("✨ Some Beautiful Memories")

    folder = "home_page"

    if os.path.exists(folder):

        files = os.listdir(folder)

        if files:

            cols = st.columns(3)

            for i, file in enumerate(files):

                path = os.path.join(folder, file)

                with cols[i % 3]:
                    st.image(path, use_container_width=True)

        else:
            st.info("No images found in home_page folder.")

    else:
        st.info("Create a folder named home_page and add photos.")

    st.divider()

    # ======================
    # CONTACT
    # ======================

    st.header("📞 Contact Us")

    st.markdown("""
    ☎️ [7534060708](tel:+917534060708)
    ☎️ [9557324310](tel:+919557324310)
    📷 [Instagram - @babitafilmproduction413](https://www.instagram.com/babitafilmproduction4413/)
    💬 [WhatsApp Chat](https://wa.me/917534060708)
    """)

    st.markdown("""
    <div class="footer">
    <h3>❤️ Thank You For Choosing Babita Film Production ❤️</h3>
    </div>
    """, unsafe_allow_html=True)