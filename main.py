from tensorflow import keras
import streamlit as st
import cv2
import numpy as np
from PIL import Image

model =  keras.models.load_model('model/model.h5')

def predict(image):
    st.write("#### Input Image:")
    st.image(image)
    image = np.array(image)
    image = cv2.resize(image, dsize=(32,32),interpolation=cv2.INTER_CUBIC)
    image = image/255
    classes = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]
    probs = model.predict(image.reshape(1,32,32,3))[0]
    st.write("#### Output: ")
    st.write(f'Predicted output is {classes[np.argmax(probs)]} with {np.max(probs)*100}% accuracy')

st.write("# Image Classification")
st.write("### Classes predicted by model are Airplane, Automobile, Bird, Cat, Deer, Dog, Frog, Horse, Ship, truck")
uploaded_file = st.file_uploader("Browse image", type=['jpg','png'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    predict(image)