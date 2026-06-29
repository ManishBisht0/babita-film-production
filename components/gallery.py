# import streamlit as st
# import os


# def show_gallery():

#     st.title("✨ Our Work")

#     folders = {
#         "💛 Haldi Ceremony": "gallery/haldi",
#         "🎬 Cinematic Weddings": "gallery/cinematic",
#         "💍 Wedding Photography": "gallery/wedding",
#         # "🎂 Birthday Memories": "gallery/birthday",
#         "🎉 Party Celebrations": "gallery/party",
#         "🎉 Party Celebrations": "gallery/mehandi",
#     }

#     for title, folder in folders.items():

#         st.header(title)

#         if os.path.exists(folder):

#             files = os.listdir(folder)

#             cols = st.columns(3)

#             for i, file in enumerate(files):

#                 path = os.path.join(folder, file)

#                 with cols[i % 3]:
#                     st.image(path, use_container_width=True)

import streamlit as st
import os


def show_gallery():

    st.title("✨ Our Work")
    st.write("A glimpse into our cinematic storytelling and unforgettable moments.")

    folders = {
        "🎂 Birthday Celebration": {
            "path": "gallery/Birthday",
            "desc": "Cherishing every birthday with joyful moments, laughter, and unforgettable memories."
        },

        "📸 Candid Photography": {
            "path": "gallery/Candit",
            "desc": "Natural, unposed moments that beautifully capture genuine emotions and expressions."
        },

        "💛 Haldi Ceremony": {
            "path": "gallery/Haldi",
            "desc": "Bright colors, joyful rituals, and heartfelt emotions from the Haldi ceremony."
        },

        "👶 Naming Ceremony": {
            "path": "gallery/Naming Ceremony",
            "desc": "Precious moments celebrating the arrival and naming of a new family member."
        },

        "🌄 Outdoor Shoots": {
            "path": "gallery/outdoor",
            "desc": "Creative outdoor photography with stunning natural backdrops and cinematic visuals."
        },

        "💍 Ring Ceremony": {
            "path": "gallery/Ring Ceremony",
            "desc": "Capturing the love, excitement, and beautiful moments of your engagement ceremony."
        },

        "👰 Wedding Photography": {
            "path": "gallery/Wedding",
            "desc": "Timeless wedding memories captured with elegance, emotion, and perfection."
        },
    }

    for title, data in folders.items():

        st.header(title)
        st.write(data["desc"])

        folder = data["path"]

        if os.path.exists(folder):

            # Load only image files
            files = sorted([
                f for f in os.listdir(folder)
                if f.lower().endswith((".jpg", ".jpeg", ".png", ".webp"))
            ])

            if files:
                cols = st.columns(3)

                for i, file in enumerate(files):

                    path = os.path.join(folder, file)

                    with cols[i % 3]:
                        st.image(
                            path,
                            caption=os.path.splitext(file)[0],
                            use_container_width=True,
                        )
            else:
                st.info("No images found in this folder.")

        else:
            st.warning(f"Folder not found: {folder}")

        st.divider()