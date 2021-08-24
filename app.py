import streamlit as st
import requests
import streamlit as st
from PIL import Image, ImageOps

st.title("Upload + Classification Example")

uploaded_file = st.file_uploader("Choose an image...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("")
    image_gray = ImageOps.grayscale(image)
    st.image(image_gray, caption='grayscaled Image.', use_column_width=True)
