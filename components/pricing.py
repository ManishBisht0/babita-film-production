import streamlit as st

def show_pricing():

    st.title("💰 Wedding Packages")
    st.markdown("### Choose the package that best suits your special day.")

    # CSS
    st.markdown("""
    <style>

    .card{
        background:rgba(255,255,255,0.08);
        padding:20px;
        border-radius:15px;
        margin-bottom:25px;
        border-left:8px solid #D4AF37;
        box-shadow:0 4px 12px rgba(0,0,0,.15);
    }

    .card h2{
        color:#D4AF37;
    }

    .traditional{
        border-left-color:#8E8E8E;
    }

    .delight{
        border-left-color:#ff8c42;
    }

    .gold{
        border-left-color:#D4AF37;
    }

    .silver{
        border-left-color:#C0C0C0;
    }

    .diamond{
        border-left-color:#00BFFF;
    }

    </style>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
        <div class="card traditional">
        <h3>📸 Traditional – 2 Days</h3>
        <h2>₹40,000</h2>

        ✅ Professional Photography & Videography<br>
        ✅ 30-Sheet Premium Gloss Album<br>
        ✅ HD Wedding Film (Pen Drive)<br>
        ✅ Designer Photo Frame (12×18)<br><br>

        <b>🎬 Cinematic Upgrade : ₹60,000</b>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card delight">
        <h3>🌸 Delight Package</h3>
        <h2>₹55,000</h2>

        ✅ Photography & Videography<br>
        ✅ 40-Sheet Luxury Gloss Album<br>
        ✅ HD Wedding Film (Pen Drive)<br>
        ✅ Photo Frame (16×34)<br><br>

        <b>🎬 Cinematic Upgrade : ₹70,000</b>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card gold">
        <h3>🥇 Gold Package</h3>
        <h2>₹70,000</h2>

        ✅ Photography + Videography + Drone<br>
        ✅ 50-Sheet NTR Matt Album<br>
        ✅ HD Wedding Film (Pen Drive)<br>
        ✅ Premium Photo Frame (20×30)<br><br>

        <b>🎬 Cinematic Upgrade : ₹75,000</b>
        </div>
        """, unsafe_allow_html=True)

    with col2:

        st.markdown("""
        <div class="card traditional">
        <h3>📸 Traditional – 3 Days</h3>
        <h2>₹50,000</h2>

        ✅ Photography & Videography<br>
        ✅ 35-Sheet Hi-Gloss Album<br>
        ✅ HD Wedding Film (Pen Drive)<br>
        ✅ Designer Photo Frame (12×18)<br><br>

        <b>🎬 Cinematic Upgrade : ₹65,000</b>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card silver">
        <h3>🥈 Silver Package</h3>
        <h2>₹65,000</h2>

        ✅ Photography + Videography + Drone<br>
        ✅ 50-Sheet NTR Matt Album<br>
        ✅ HD Wedding Film (Pen Drive)<br>
        ✅ Premium Photo Frame (20×30)<br><br>

        <b>🎬 Cinematic Upgrade : ₹85,000</b>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="card diamond">
        <h3>💎 Diamond Package</h3>
        <h2>₹1,30,000</h2>

        ✅ Photography + Videography + Drone<br>
        ✅ Cinematic Wedding Film<br>
        ✅ Pre Wedding / Post Wedding Shoot<br>
        ✅ 60-Sheet NTR Matt Album<br>
        ✅ HD Video (Pen Drive)<br><br>

        <b>🎬 Cinematic Upgrade : ₹85,000</b>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.header("🎬 Pre / Post Wedding Shoots")

    st.info("""
**📍 Local Shoot (Photo + Video)** : ₹35,000 + T&C

**📍 Outstation Shoot (Photo + Video)** : ₹50,000 + T&C
""")
    st.markdown("---")

    st.markdown("""
    <div style="
    background: rgba(0,0,0,0.05);
    padding: 20px;
    border-radius: 12px;
    ">

    <h3>💰 Booking Information</h3>

    <b>Pay 25% Advance to confirm your booking</b>

    <hr>

    <h4>⚠️ Important Note</h4>
    <ul>
    <li>Extra day events (Haldi, Sangeet, Ganesh Pooja etc.) - ₹20,000 per day + T&C</li>
    <li>Drone Charge: ₹6,000 per day</li>
    </ul>

    <hr>

    <h4>📞 Contact</h4>
    <b>7534060708 | 9557324310</b><br>
    📷 Instagram: @babitafilmproduction4413

    </div>
    """, unsafe_allow_html=True)