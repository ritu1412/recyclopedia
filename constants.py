import os
import streamlit as st

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", st.secrets["GEMINI_API_KEY"])

LLM_OUTPUT_LENGTH_SIZE = 1024
LOGO_PATH = "asset/logo.png"
STREAMLIT_CLOUD_HOSTNAME = "localhost"

STREAMLIT_HOMEPAGE_CONTENT = """
<style>
.stApp {
    background-color: #81C784;
}
.reportview-container .markdown-text-container {
    color: #ffffff;
}
.reportview-container .css-1d391kg {
    color: #ffffff;
}
h1, h2, h3, h4, h5, h6 {
    color: #ffffff;
    font-weight: bold;
}
.stButton>button {
    color: #ffffff;
    background-color: #4caf50;
}
.stFileUploader .css-1m6mopr {
    color: #ffffff;
    background-color: #4caf50;
}
</style>
"""

RECYCLING_INSTRUCTIONS_PROMPT = """
Based on the image of an item provided by the user, which represents a product they wish to recycle, repurpose, or upcycle, please analyze the item and generate one innovative and practical idea for extending its lifecycle.
Your suggestions should focus on creative uses that go beyond traditional recycling methods, especially for items not typically considered recyclable.
After identifying a potential new use, provide a detailed step-by-step guide on how the user can transform the item from its current state into the new, repurposed form.
Your recommendations should be feasible for the average person to accomplish with common tools and materials.
Please draw from your extensive database of knowledge to ensure the ideas are both unique and practical, highlighting any specific techniques or materials needed for the transformation.
"""

RECYCLING_LOCATIONS_PROMPT_COORDINATES = """
Based on the image give me all the locations nearby to geo-coordinates (latitude, longitude): ({}, {}).
I can sell or recycle this item. Give top three locations based on the ratings and distance from the mentioned location's city. 
Make sure to include the address, phone number, and website for each location.
Your locations should be relevant to the item in the image and should include recycling centers, donation centers, or other places where the item can be repurposed or recycled.
Please ensure that the locations are within a reasonable distance from the user's current location.
Give the output in a tabular format in markdown.
"""

RECYCLING_LOCATIONS_PROMPT_DURHAM = """
Based on the image give me all the locations nearby to Durham, NC, USA.
I can sell or recycle this item. Give top three locations based on the ratings and distance from the mentioned location's city. 
Make sure to include the address, phone number, and website for each location.
Your locations should be relevant to the item in the image and should include recycling centers, donation centers, or other places where the item can be repurposed or recycled.
Please ensure that the locations are within a reasonable distance from the given location.
Give the output in a tabular format in markdown.
"""