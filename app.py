import streamlit as st
import pickle
import numpy as np

# Load trained Random Forest model
@st.cache_resource
def load_model():
    with open("rf_water_model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

# Page configuration
st.set_page_config(page_title="💧 Water Potability Predictor", layout="centered")

# CSS for background and layout
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #a8edea, #fed6e3);
        background-attachment: fixed;
    }
    .stButton>button {
        background-color: #2E86C1;
        color: white;
        border-radius: 8px;
        padding: 0.6rem 1rem;
        border: none;
    }
    .stButton>button:hover {
        background-color: #1B4F72;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.markdown("<h1 style='text-align: center; color: #2E86C1;'>💧 Water Potability Predictor</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #566573;'>Predict whether water is safe for drinking</p>", unsafe_allow_html=True)
st.markdown("---")

# Input Form
st.subheader("Enter Water Quality Parameters")

col1, col2 = st.columns(2)

with col1:
    ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
    Hardness = st.number_input("Hardness (mg/L)", value=200.0)
    Solids = st.number_input("Total Dissolved Solids (ppm)", value=500.0)
    Chloramines = st.number_input("Chloramines (ppm)", value=7.0)
    Sulfate = st.number_input("Sulfate (mg/L)", value=250.0)

with col2:
    Conductivity = st.number_input("Conductivity (μS/cm)", value=400.0)
    Organic_carbon = st.number_input("Organic Carbon (ppm)", value=10.0)
    Trihalomethanes = st.number_input("Trihalomethanes (μg/L)", value=70.0)
    Turbidity = st.number_input("Turbidity (NTU)", value=3.0)

st.markdown("---")

# Prediction Section
if st.button("Predict 💡"):
    features = np.array([
        ph, Hardness, Solids, Chloramines, Sulfate,
        Conductivity, Organic_carbon, Trihalomethanes, Turbidity
    ]).reshape(1, -1)

    prob = model.predict_proba(features)[0][1]
    threshold = 0.42  # Tuned threshold
    prediction = int(prob >= threshold)

    # Display Result
    if prediction == 1:
        st.markdown(
            f"""
            <div style='padding: 20px; border-radius: 10px;
                        background-color: #d4edda; color: #155724; text-align:center'>
            <h2>✅ Water is Potable (Safe to Drink)</h2>
            <p>Probability of Potable: {prob:.2f}</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"""
            <div style='padding: 20px; border-radius: 10px;
                        background-color: #f8d7da; color: #721c24; text-align:center'>
            <h2>❌ Water is Not Potable (Unsafe)</h2>
            <p>Probability of Potable: {prob:.2f}</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.markdown("---")
st.markdown("<p style='text-align: center; color: #7F8C8D;'>Created by <b>Sunmathi 💙</b></p>", unsafe_allow_html=True)
