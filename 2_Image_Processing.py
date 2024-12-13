import streamlit as st
from PIL import Image, ImageFilter

st.title("Image Processing Application")
st.write("Upload an image to apply processing.")

uploaded_image = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    st.write("Choose an image processing operation:")
    operation = st.selectbox("Operation", ["Original", "Grayscale", "Blur"])

    if operation == "Grayscale":
        processed_image = image.convert("L")
        st.image(processed_image, caption="Grayscale Image", use_column_width=True)

    elif operation == "Blur":
        processed_image = image.filter(ImageFilter.BLUR)
        st.image(processed_image, caption="Blurred Image", use_column_width=True)

    else:
        st.write("No processing applied.")
