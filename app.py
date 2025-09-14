import streamlit as st
import pickle
import gdown
import os
import numpy as np
import math
from sklearn.exceptions import NotFittedError

# 🔹 Google Drive file ID (replace with your own)
file_id = "1cKLDI_j4P8N6T9eWZHLq1iWbaf8VW_Ha"
url = f"https://drive.google.com/uc?id={file_id}"
model_path = "pipe_fitted.pkl"


# 🔹 Download model if not present
if not os.path.exists(model_path):
    st.write("📥 Downloading model from Google Drive...")
    gdown.download(url, model_path, quiet=False)

# 🔹 Load model
try:
    with open(model_path, "rb") as f:
        pipe = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model: {e}")
    st.stop()

# 🔹 Streamlit App
st.title("💻 Laptop Price Predictor")

# Example inputs (modify based on your training features)
ram = st.number_input("Enter RAM (in GB):", min_value=2, max_value=128, step=2)
weight = st.number_input("Enter Weight (in Kg):", min_value=0.5, max_value=5.0, step=0.1)

if st.button("Predict"):
    try:
        query = np.array([[ram, weight]])  # adapt to your model features
        pred_log = pipe.predict(query)[0]  # model predicts log(price)
        pred_price = math.exp(pred_log)

        # Clip predictions to realistic range
        pred_price = max(min(pred_price, 250000), 20000)

        st.success(f"💰 Estimated Laptop Price: ₹{pred_price:,.0f}")
    except NotFittedError:
        st.error("Model is not fitted yet!")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
