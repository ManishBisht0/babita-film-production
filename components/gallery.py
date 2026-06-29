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
    st.write("A glimpse into our cinematic storytelling and unforgettable wedding moments.")

    folders = {
        "💛 Haldi Ceremony": {
            "path": "gallery/haldi",
            "desc": "Bright colors, joyful rituals, and pure emotions captured in golden haldi moments."
        },

        "🎬 Cinematic Weddings": {
            "path": "gallery/cinematic",
            "desc": "A film-like storytelling experience where every frame feels like a movie scene."
        },

        "💍 Wedding Photography": {
            "path": "gallery/wedding",
            "desc": "Timeless wedding memories captured with elegance, emotion, and perfection."
        },

        "🎉 Party Celebrations": {
            "path": "gallery/party",
            "desc": "Energetic, fun-filled moments of celebration, laughter, and unforgettable memories."
        },

        "🌸 Mehandi Moments": {
            "path": "gallery/mehandi",
            "desc": "Beautiful henna rituals filled with tradition, love, and emotional family bonding."
        },
    }

    for title, data in folders.items():

        st.header(title)
        st.write(data["desc"])

        folder = data["path"]

        if os.path.exists(folder):

            files = os.listdir(folder)

            cols = st.columns(3)

            for i, file in enumerate(files):

                path = os.path.join(folder, file)

                with cols[i % 3]:
                    st.image(path, use_container_width=True)