import streamlit as st
import pickle
import numpy as np
import math

# Load the fitted pipeline
with open('pipe_fitted.pkl', 'rb') as f:
    pipe = pickle.load(f)

# Load the DataFrame (for dropdowns/options)
with open('df.pkl', 'rb') as f:
    df = pickle.load(f)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4B8BBE;
        color: white;
        height: 3em;
        width: 100%;
        font-size: 18px;
        border-radius: 10px;
    }
    .stSlider>div>div>div>div>input {
        color: #4B8BBE;
    }
    </style>
""", unsafe_allow_html=True)

# App Title
st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>💻 Laptop Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Predict the price of a laptop based on its specifications.</p>", unsafe_allow_html=True)
st.write("---")

# Layout with two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("🖥 Laptop Specifications")
    company = st.selectbox("Brand", df['Company'].unique())
    laptop_type = st.selectbox("Type", df['TypeName'].unique())
    ram = st.selectbox("RAM (GB)", [2, 4, 6, 8, 12, 16, 24, 32, 64])
    weight = st.number_input("Weight (Kg)", min_value=0.5, max_value=5.0, value=1.5, step=0.1)
    touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])
    ips = st.selectbox("IPS", ["No", "Yes"])

with col2:
    st.subheader("📺 Display & Hardware")
    screen_size = st.slider("Screen Size (inches)", 10.0, 18.0, 13.0, 0.1)
    resolution = st.selectbox(
        "Screen Resolution",
        ["1920x1080", "1366x768", "1600x900", "3840x2160", "3200x1800",
         "2880x1800", "2560x1600", "2560x1440", "2304x1440"]
    )
    cpu = st.selectbox("CPU", df['Cpu brand'].unique())
    hdd = st.selectbox("HDD (GB)", [0, 128, 256, 512, 1024, 2048])
    ssd = st.selectbox("SSD (GB)", [0, 8, 128, 256, 512, 1024])
    gpu = st.selectbox("GPU", df['Gpu brand'].unique())
    os = st.selectbox("OS", df['os'].unique())

st.write("---")

# Predict Button
if st.button("Predict Price 💰"):
    touchscreen_val = 1 if touchscreen == "Yes" else 0
    ips_val = 1 if ips == "Yes" else 0

    # Calculate PPI
    X_res, Y_res = map(int, resolution.split("x"))
    ppi = ((X_res ** 2 + Y_res ** 2) ** 0.5) / screen_size

    # Prepare query
    query = np.array([company, laptop_type, ram, weight,
                      touchscreen_val, ips_val, ppi,
                      cpu, hdd, ssd, gpu, os]).reshape(1, 12)

    try:
        pred_log = pipe.predict(query)[0]  # model predicts log(price)
        pred_price = math.exp(pred_log)

        # Clip predictions to realistic range
        pred_price = max(min(pred_price, 250000), 20000)

        st.markdown(f"<h2 style='text-align: center; color: green;'>💰 Estimated Price: ₹ {pred_price:,.0f}</h2>", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error: {e}")
