import streamlit as st
import cv2
import numpy as np
import pytesseract
from PIL import Image

st.title("Reconocimiento óptico de Caracteres")

img_file_buffer = st.camera_input("Toma una Foto")

if img_file_buffer is not None:
    # To read image file buffer with OpenCV:
    bytes_data = img_file_buffer.getvalue()
    cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

    img_rgb = cv2.cvtColor(cv2_img, cv2.COLOR_BGR2RGB)
    st.write(pytesseract.image_to_string(img_rgb))

    


