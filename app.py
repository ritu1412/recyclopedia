import streamlit as st
import google.generativeai as genai

from PIL import Image

# Local
from constants import *
from util import *


def __get_gemini_client__() -> genai.GenerativeModel:
    genai.configure(api_key=GEMINI_API_KEY)
    gemini_model = genai.GenerativeModel("gemini-pro-vision")
    return gemini_model

def main():
    gemini_model = __get_gemini_client__()

    # Streamlit app interface customization
    st.markdown(
        STREAMLIT_HOMEPAGE_CONTENT,
        unsafe_allow_html=True
    )

    st.image(LOGO_PATH, width = 100)
    st.title('Recyclopedia')
    st.header('Find out how to recycle your items and where')
    st.write('Upload an image of the item you wish to recycle, and we\'ll tell you how!')

    uploaded_image = st.file_uploader("",type=['png', 'jpg', 'jpeg'])

    if uploaded_image is not None:
        # Display a progress bar   
        image = Image.open(uploaded_image)
        st.image(image, caption='Your Uploaded Image', use_column_width=True)

        # Get recycling instructions
        instructions = get_recycling_instructions(image, gemini_model)
        if instructions:
            st.subheader("Instructions on how to recycle the item:")
            st.markdown(instructions, unsafe_allow_html=True)

            # Find nearby recycling places
            recycling_places = find_nearby_recycling_places(image, gemini_model)
            st.write("\n\n")
            st.subheader("Nearby places where you can recycle:")
            st.markdown(recycling_places, unsafe_allow_html=True)
        else:
            st.error("Could not get instructions for recycling this item.")
    

if __name__ == "__main__":
    main()