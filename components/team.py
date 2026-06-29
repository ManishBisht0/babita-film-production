import streamlit as st


def member_card(image, name, role, experience, description, instagram_url):

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(image, width=200)

    with col2:
        st.markdown(f"### {name}")
        st.markdown(f"**🎖️ Role:** {role}")
        st.markdown(f"**📅 Experience:** {experience}")

        st.markdown(
            f"**📷 Instagram:** "
            f'<a href="{instagram_url}" target="_blank">View Profile</a>',
            unsafe_allow_html=True,
        )

        st.write(description)

    st.divider()


def show_team():

    st.title("❤️ Meet Our Team")
    st.write("A passionate team dedicated to capturing cinematic wedding memories.")

    # ================= Row 1 =================
    col1, col2 = st.columns(2)

    with col1:
        member_card(
            "images/mannu.jpeg",
            "🎬 Mannu Airy",
            "Owner • Main & Lead Videographer",
            "2012 – Present",
            """
• Founder of Babita Film Production  
• Lead Videographer  
• Drone Specialist  
• Cinematic wedding film expert  
            """,
            "https://www.instagram.com/babita_films?igsh=MTVxbnBnYXY5ZmR6aA=="
        )

    with col2:
        member_card(
            "images/sonu.jpeg",
            "📸 Sonu Walida",
            "Main Cameraman",
            "2013 – Present",
            """
• Wedding Photographer  
• Cinematic storytelling expert  
• Candid photography specialist  
            """,
            "https://www.instagram.com/waldiasonu?igsh=MWh0MGo2bXEzdDg5cg=="
        )

    # ================= Row 2 =================
    col3, col4 = st.columns(2)

    with col3:
        member_card(
            "images/sunil.jpeg",
            "📸 Sunil Singh Soun",
            "Photo • Video • Drone",
            "2007 – Present (Babita Film Production: 2013 – Present)",
            """
• Experienced photographer  
• Videography specialist  
• Drone operator  
• 15+ years experience  
            """,
            "https://www.instagram.com/sunilsingh1529?igsh=cjR2aGs2Z3NwcGR2"
        )

    with col4:
        member_card(
            "images/vinod.jpeg",
            "📸 Vinod Singh Jyala",
            "Photographer & Videographer",
            "2022 – Present",
            """
• Creative photographer  
• Wedding videographer  
• Modern cinematic style  
            """,
            "https://www.instagram.com/vinodjyala?igsh=MW0weGs0YXRiZ3V6Mw=="
        )

    # ================= Row 3 (Centered) =================
    left, center, right = st.columns([1, 2, 1])

    with center:
        member_card(
            "images/manoj.jpeg",
            "📸 Manoj Singh Dhami",
            "Photography & Videography",
            "2021 – Present",
            """
• Wedding photographer  
• Videography specialist  
• Detail-focused storytelling  
            """,
            "https://www.instagram.com/manoj.dhami.716533?igsh=MXJraGcyaHl3b2YzeA=="
        )