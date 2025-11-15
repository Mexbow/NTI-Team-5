import streamlit as st
import requests
from PIL import Image

st.title("📤 Upload Image to FastAPI Server")

uploaded_image = st.file_uploader("Upload an image:", type=["jpg", "jpeg", "png"])

if uploaded_image is not None:
    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

    if st.button("Send to FastAPI"):
        with st.spinner("Sending..."):
            # Send the file to FastAPI
            files = {"file": (uploaded_image.name, uploaded_image, uploaded_image.type)}

            response = requests.post("http://127.0.0.1:8000/upload-image", files=files)

            if response.status_code == 200:
                st.success("Image sent successfully!")
                st.json(response.json())
            else:
                st.error("Failed to send image!")
