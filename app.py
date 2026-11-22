
import streamlit as st
import pandas as pd
import joblib

model_path = "/content/drive/MyDrive/Machine_Learning_Assignment/02_Water_Potability_Classification/models/final_water_potability_model.pkl"

model = joblib.load(model_path)

st.title("Water Potability Prediction")
st.write("Enter water-quality measurements to obtain a machine learning prediction.")

st.warning(
    "This application is for educational purposes only. "
    "Its prediction is not a substitute for laboratory water-quality testing."
)

ph = st.number_input("pH", value=7.0)
hardness = st.number_input("Hardness", value=196.0)
solids = st.number_input("Solids", value=20000.0)
chloramines = st.number_input("Chloramines", value=7.0)
sulfate = st.number_input("Sulfate", value=333.0)
conductivity = st.number_input("Conductivity", value=426.0)
organic_carbon = st.number_input("Organic Carbon", value=14.0)
trihalomethanes = st.number_input("Trihalomethanes", value=66.0)
turbidity = st.number_input("Turbidity", value=4.0)

if st.button("Predict Water Potability"):

    input_data = pd.DataFrame([{
        "ph": ph,
        "Hardness": hardness,
        "Solids": solids,
        "Chloramines": chloramines,
        "Sulfate": sulfate,
        "Conductivity": conductivity,
        "Organic_carbon": organic_carbon,
        "Trihalomethanes": trihalomethanes,
        "Turbidity": turbidity
    }])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("Model prediction: Potable")
    else:
        st.error("Model prediction: Not Potable")
