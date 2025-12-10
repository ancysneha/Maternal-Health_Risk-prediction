import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🩺 Maternal Health Risk Predictor")
st.write("Enter the details to predict the maternal health risk level.")

age = st.number_input("Age", 10, 60)
systolic_bp = st.number_input("Systolic BP")
diastolic_bp = st.number_input("Diastolic BP")
bs = st.number_input("Blood Sugar")
body_temp = st.number_input("Body Temperature")
heart_rate = st.number_input("Heart Rate")

if st.button("Predict"):
    features = np.array([[age, systolic_bp, diastolic_bp, bs, body_temp, heart_rate]])
    prediction = model.predict(features)[0]

    labels = {0: "High Risk", 1: "Low Risk", 2: "Mid Risk"}
    st.success(f"Prediction: **{labels[prediction]}**")
