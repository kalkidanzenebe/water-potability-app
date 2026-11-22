
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# -------------------------------
# PAGE CONFIGURATION
# -------------------------------
st.set_page_config(
    page_title="Water Quality Analyzer",
    page_icon="💧",
    layout="wide"
)

# -------------------------------
# CUSTOM DESIGN
# -------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #F4F8FC;
    }

    .main-title {
        background: linear-gradient(110deg, #102B46, #176B87);
        padding: 30px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }

    .main-title h1 {
        color: white;
        font-size: 36px;
        margin-bottom: 8px;
    }

    .main-title p {
        color: #E1F1F8;
        font-size: 16px;
    }

    .section-title {
        color: #102B46;
        font-size: 22px;
        font-weight: 700;
        margin-top: 15px;
        margin-bottom: 10px;
    }

    div.stButton > button {
        background-color: #176B87;
        color: white;
        border-radius: 10px;
        border: none;
        padding: 12px 25px;
        font-size: 17px;
        font-weight: bold;
        width: 100%;
    }

    div.stButton > button:hover {
        background-color: #102B46;
        color: white;
    }

    .result-card {
        background-color: white;
        border-left: 7px solid #176B87;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0 3px 12px rgba(0,0,0,0.07);
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)

# -------------------------------
# LOAD TRAINED MODEL
# -------------------------------
current_folder = Path(__file__).resolve().parent

possible_model_paths = [
    current_folder / "final_water_potability_model.pkl",
    current_folder / "../models/final_water_potability_model.pkl",
    Path.cwd() / "final_water_potability_model.pkl"
]

model_path = next(
    (path for path in possible_model_paths if path.exists()),
    None
)

if model_path is None:
    st.error(
        "Model file not found. Please check that "
        "final_water_potability_model.pkl is included in your app repository."
    )
    st.stop()

try:
    model = joblib.load(model_path)
except Exception as error:
    st.error(f"Could not load the model: {error}")
    st.stop()

# -------------------------------
# HEADER
# -------------------------------
st.markdown("""
<div class="main-title">
    <h1>💧 Water Quality Analyzer</h1>
    <p>Predict water potability using machine learning</p>
</div>
""", unsafe_allow_html=True)

# -------------------------------
# INTRODUCTION
# -------------------------------
st.markdown(
    "<div class='section-title'>Enter Water Quality Measurements</div>",
    unsafe_allow_html=True
)

st.write(
    "Provide the nine measurements below, then select "
    "**Analyze Water Sample** to generate a prediction."
)

# -------------------------------
# INPUT FORM
# -------------------------------
with st.form("water_prediction_form"):

    col1, col2, col3 = st.columns(3)

    with col1:
        ph = st.number_input(
            "pH",
            value=7.0,
            format="%.2f"
        )

        hardness = st.number_input(
            "Hardness",
            value=200.0,
            format="%.2f"
        )

        solids = st.number_input(
            "Solids",
            value=20000.0,
            format="%.2f"
        )

    with col2:
        chloramines = st.number_input(
            "Chloramines",
            value=7.0,
            format="%.2f"
        )

        sulfate = st.number_input(
            "Sulfate",
            value=300.0,
            format="%.2f"
        )

        conductivity = st.number_input(
            "Conductivity",
            value=400.0,
            format="%.2f"
        )

    with col3:
        organic_carbon = st.number_input(
            "Organic Carbon",
            value=10.0,
            format="%.2f"
        )

        trihalomethanes = st.number_input(
            "Trihalomethanes",
            value=60.0,
            format="%.2f"
        )

        turbidity = st.number_input(
            "Turbidity",
            value=4.0,
            format="%.2f"
        )

    submitted = st.form_submit_button("💧 Analyze Water Sample")

# -------------------------------
# PREDICTION
# -------------------------------
if submitted:

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

    try:
        prediction = model.predict(input_data)[0]

        st.markdown("---")
        st.markdown(
            "<div class='section-title'>Analysis Result</div>",
            unsafe_allow_html=True
        )

        if int(prediction) == 1:
            st.success("💧 Prediction: POTABLE")
            st.markdown("""
            <div class="result-card">
                <h2 style="color:#16845B;">POTABLE</h2>
                <p style="color:#526477;">
                    The model classified this water sample as potable.
                </p>
            </div>
            """, unsafe_allow_html=True)

        else:
            st.error("Prediction: NOT POTABLE")
            st.markdown("""
            <div class="result-card">
                <h2 style="color:#C04444;">NOT POTABLE</h2>
                <p style="color:#526477;">
                    The model classified this water sample as not potable.
                </p>
            </div>
            """, unsafe_allow_html=True)

    except Exception as error:
        st.error(f"Prediction failed: {error}")

# -------------------------------
# FOOTER
# -------------------------------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#718096;'>"
    "Water Quality Analyzer | Machine Learning Project"
    "</p>",
    unsafe_allow_html=True
)
