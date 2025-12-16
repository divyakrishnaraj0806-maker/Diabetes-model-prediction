import streamlit as st
import pickle
import numpy as np

# Load the trained model
loades_model = pickle.load(open("trained_model.sav", "rb"))

st.title("Diabetes Prediction App")

st.write("Enter the following health details:")

# 8 inputs
pregnancies = st.number_input("Pregnancies", min_value=0)
glucose = st.number_input("Glucose Level")
bp = st.number_input("Blood Pressure")
skin = st.number_input("Skin Thickness")
insulin = st.number_input("Insulin Level")
bmi = st.number_input("BMI")
dpf = st.number_input("Diabetes Pedigree Function")
age = st.number_input("Age")

if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, bp, skin, insulin, bmi, dpf, age]])
    
    prediction = loades_model.predict(input_data)

    if prediction[0] == 0:
        st.success("🟢 The person is NOT diabetic")
    else:
        st.error("🔴 The person IS diabetic")