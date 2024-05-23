import os
from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
import streamlit as st


st.title("Chicken Disease Classification")
st.text("Upload a chicken fecal image")


def teachable_machine_classification(img):
    model = load_model(os.path.join("artifacts", "training", "model.h5"))
    image = img
    image = np.asarray(image)
    image = np.expand_dims(image, axis=0)
    result = np.argmax(model.predict(image), axis=1)
    return result


uploaded_file = st.file_uploader("Choose a chicken fecal image ...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded fecal image.", use_column_width=True)
    print(image)
    st.write("")
    st.write("Classifying...")
    label = teachable_machine_classification(image)
    if label[0] == 1:
        st.write("Healthy")
    else:
        st.write("Coccidiosis")
