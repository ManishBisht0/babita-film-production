import streamlit as st


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


st.set_page_config(
    page_title="Babita Film Production",
    page_icon="📸",
    layout="wide"
)

# ======================
# CUSTOM CSS
# ======================

st.markdown("""
<style>

.stApp{
    background-color:#f8f4ef;
}

.hero{
    background:linear-gradient(135deg,#fff8f0,#f4ebe2);
    padding:40px;
    border-radius:20px;
    text-align:center;
    margin-bottom:30px;
    border:1px solid #e5d5c7;
}

.hero h1{
    color:#8B0000;
    font-size:50px;
}

.hero h3{
    color:#555;
}

.card{
    padding:25px;
    border-radius:20px;
    margin-bottom:20px;
    box-shadow:0px 5px 15px rgba(0,0,0,0.08);
}

.traditional{
    background:#FFF4E6;
}

.delight{
    background:#FFEFF4;
}

.silver{
    background:#F2F2F2;
}

.gold{
    background:#FFF8D6;
}

.diamond{
    background:#EAF5FF;
}

.service-box{
    background:white;
    padding:20px;
    border-radius:15px;
    text-align:center;
    box-shadow:0px 3px 10px rgba(0,0,0,0.08);
}

.footer{
    text-align:center;
    padding:20px;
    color:#555;
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

<h1>📸 Babita Film Production</h1>

<h3>
Capturing Love • Emotions • Timeless Stories
</h3>

<p>
📍 Near Airport Road, Khankhar Piranju
</p>

<p>
☎️ <a href="tel:+917534060708">7534060708</a>
&nbsp;&nbsp;|&nbsp;&nbsp;
☎️ <a href="tel:+919557324310">9557324310</a>
</p>

<p>
📷
<a href="https://www.instagram.com/babitafilmproduction413/" target="_blank">
Instagram : @babitafilmproduction413
</a>
</p>

<p>
💬
<a href="https://wa.me/917534060708" target="_blank">
Chat on WhatsApp
</a>
</p>

</div>
""", unsafe_allow_html=True)


# Hero Section
st.markdown("""
<div class="hero">
...
</div>
""", unsafe_allow_html=True)

# ======================
# OWNER SECTION (INSERT HERE)
# ======================

st.header("📸 Meet the Founder")

col1, col2 = st.columns([1, 2])

with col1:
    st.image("owner.jpeg", width=300)

with col2:
    st.markdown("""
    ## Mr. Mannu Airy
    Owner & Lead Photographer

    With years of experience in wedding and event photography,
    Mr. Mannu has dedicated his life to capturing emotions,
    love, and unforgettable moments.

    His passion for photography goes beyond taking pictures—
    he believes every photograph tells a story and preserves
    memories that last forever.

    **Turning precious moments into timeless memories.**
    """)

# ======================
# ABOUT US
# ======================

st.header("✨ About Us")

# ======================
# ABOUT
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

# ======================
# SERVICES
# ======================

st.header("📷 Our Services")

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="service-box">
    <h3>💍 Wedding Photography</h3>
    <p>Traditional and cinematic wedding coverage.</p>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class="service-box">
    <h3>👶 Naming Ceremony</h3>
    <p>Capture your baby's special moments beautifully.</p>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class="service-box">
    <h3>🎂 Birthday Photography</h3>
    <p>Professional birthday event photography.</p>
    </div>
    """, unsafe_allow_html=True)

# ======================
# PACKAGES
# ======================

st.header("💍 Our Wedding Collections")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    <div class="card traditional">
    <h3>📸 Traditional – 2 Days</h3>
    <h2>₹35,000</h2>

    ✅ Professional Photography & Videography<br>
    ✅ 30-Sheet Premium Gloss Album<br>
    ✅ HD Wedding Film (Pen Drive)<br>
    ✅ Designer Photo Frame (12×18)<br><br>

    🎬 Cinematic Upgrade : ₹60,000
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card delight">
    <h3>🌸 Delight Package</h3>
    <h2>₹45,000</h2>

    ✅ Photography & Videography<br>
    ✅ 40-Sheet Luxury Gloss Album<br>
    ✅ HD Wedding Film (Pen Drive)<br>
    ✅ Photo Frame (16×34)<br><br>

    🎬 Cinematic Upgrade : ₹70,000
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card gold">
    <h3>🥇 Gold Package</h3>
    <h2>₹60,000</h2>

    ✅ Photography + Videography + Drone<br>
    ✅ 50-Sheet NTR Matt Album<br>
    ✅ HD Wedding Film (Pen Drive)<br>
    ✅ Premium Photo Frame (20×30)<br><br>

    🎬 Cinematic Upgrade : ₹75,000
    </div>
    """, unsafe_allow_html=True)

with col2:

    st.markdown("""
    <div class="card traditional">
    <h3>📸 Traditional – 3 Days</h3>
    <h2>₹40,000</h2>

    ✅ Photography & Videography<br>
    ✅ 35-Sheet Hi-Gloss Album<br>
    ✅ HD Wedding Film (Pen Drive)<br>
    ✅ Designer Photo Frame (12×18)<br><br>

    🎬 Cinematic Upgrade : ₹65,000
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card silver">
    <h3>🥈 Silver Package</h3>
    <h2>₹50,000</h2>

    ✅ Photography + Videography + Drone<br>
    ✅ 50-Sheet NTR Matt Album<br>
    ✅ HD Wedding Film (Pen Drive)<br>
    ✅ Premium Photo Frame (20×30)<br><br>

    🎬 Cinematic Upgrade : ₹85,000
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card diamond">
    <h3>💎 Diamond Package</h3>
    <h2>₹1,20,000</h2>

    ✅ Photography + Videography + Drone<br>
    ✅ Cinematic Wedding Film<br>
    ✅ Pre Wedding / Post Wedding Shoot<br>
    ✅ 60-Sheet NTR Matt Album<br>
    ✅ HD Video (Pen Drive)<br><br>

    🎬 Cinematic Upgrade : ₹85,000
    </div>
    """, unsafe_allow_html=True)

# ======================
# PRE WEDDING
# ======================

st.header("🎬 Pre / Post Wedding Shoots")

st.info("""
📍 Local Shoot (Photo + Video): ₹30,000 + T&C

📍 Outstation Shoot (Photo + Video): ₹45,000 + T&C
""")

# ======================
# CONTACT
# ======================

st.header("📞 Contact Us")

st.markdown("""
☎️ [7534060708](tel:+917534060708)

☎️ [9557324310](tel:+919557324310)

📷 [Instagram - @babitafilmproduction413](https://www.instagram.com/babitafilmproduction413/)

💬 [WhatsApp Chat](https://wa.me/917534060708)
""")

st.markdown("""
<div class="footer">
<h3>❤️ Thank You For Choosing Babita Film Production ❤️</h3>
</div>
""", unsafe_allow_html=True)
