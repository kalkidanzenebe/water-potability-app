
import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

# =====================================
# PAGE CONFIGURATION
# =====================================
st.set_page_config(
    page_title="Water Quality Analyzer",
    page_icon="💧",
    layout="wide"
)

# =====================================
# BLACK AND GOLD DESIGN
# =====================================
st.markdown("""
<style>
    .stApp {
        background-color: #111111;
        color: #F5F5F5;
    }

    [data-testid="stHeader"] {
        background-color: #111111;
    }

    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
    }

    .main-title {
        background: linear-gradient(120deg, #171717, #353020);
        border: 1px solid #D4AF37;
        padding: 35px 20px;
        border-radius: 18px;
        text-align: center;
        margin-bottom: 30px;
    }

    .main-title h1 {
        color: #D4AF37;
        font-size: 38px;
        font-weight: 800;
    }

    .main-title p {
        color: #F5F5F5;
        font-size: 16px;
    }

    h2, h3 {
        color: #D4AF37 !important;
    }

    label, p, span {
        color: #F5F5F5;
    }

    [data-testid="stNumberInput"] input {
        background-color: #252525;
        color: #F5F5F5;
        border: 1px solid #D4AF37;
        border-radius: 8px;
    }

    [data-testid="stNumberInput"] button {
        background-color: #252525;
        color: #D4AF37;
        border: 1px solid #D4AF37;
    }

    div.stButton > button,
    div[data-testid="stFormSubmitButton"] > button {
        background-color: #D4AF37;
        color: #111111;
        border: none;
        border-radius: 10px;
        padding: 13px 20px;
        font-size: 17px;
        font-weight: 800;
        width: 100%;
        transition: 0.3s;
    }

    div.stButton > button:hover,
    div[data-testid="stFormSubmitButton"] > button:hover {
        background-color: #F0D36B;
        color: #111111;
        border: none;
    }

    .result-card {
        background-color: #252525;
        border: 1px solid #D4AF37;
        border-radius: 15px;
        padding: 30px;
        text-align: center;
        margin-top: 20px;
    }

    .result-card h2 {
        font-size: 30px;
        margin-bottom: 10px;
    }

    .result-card p {
        color: #F5F5F5;
        font-size: 16px;
    }

    hr {
        border-color: #D4AF37;
    }

    [data-testid="stForm"] {
        background-color: #191919;
        padding: 20px;
        border: 1px solid #444444;
        border-radius: 15px;
    }

    .footer {
        text-align: center;
        color: #D4AF37;
        padding: 20px;
        font-size: 13px;
    }
</style>
""", unsafe_allow_html=True)

# =====================================
# LOAD TRAINED MODEL
# =====================================
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
        "final_water_potability_model.pkl is included in your repository."
    )
    st.stop()

try:
    model = joblib.load(model_path)
except Exception as error:
    st.error(f"Could not load model: {error}")
    st.stop()

# =====================================
# HEADER
# =====================================
st.markdown("""
<div class="main-title">
    <h1>💧 WATER QUALITY ANALYZER</h1>
    <p>Intelligent Water Potability Prediction System</p>
</div>
""", unsafe_allow_html=True)

# =====================================
# INTRODUCTION
# =====================================
st.markdown("## Enter Water Measurements")

st.write(
    "Enter the nine water-quality measurements below "
    "to generate a machine learning prediction."
)

# =====================================
# INPUT FORM
# =====================================
with st.form("water_prediction_form"):

    st.markdown("### Water Quality Parameters")

    col1, col2, col3 = st.columns(3)

    with col1:
        ph = st.number_input(
            "pH",
            min_value=0.0,
            value=7.0,
            format="%.2f"
        )

        hardness = st.number_input(
            "Hardness",
            min_value=0.0,
            value=200.0,
            format="%.2f"
        )

        solids = st.number_input(
            "Solids",
            min_value=0.0,
            value=20000.0,
            format="%.2f"
        )

    with col2:
        chloramines = st.number_input(
            "Chloramines",
            min_value=0.0,
            value=7.0,
            format="%.2f"
        )

        sulfate = st.number_input(
            "Sulfate",
            min_value=0.0,
            value=300.0,
            format="%.2f"
        )

        conductivity = st.number_input(
            "Conductivity",
            min_value=0.0,
            value=400.0,
            format="%.2f"
        )

    with col3:
        organic_carbon = st.number_input(
            "Organic Carbon",
            min_value=0.0,
            value=10.0,
            format="%.2f"
        )

        trihalomethanes = st.number_input(
            "Trihalomethanes",
            min_value=0.0,
            value=60.0,
            format="%.2f"
        )

        turbidity = st.number_input(
            "Turbidity",
            min_value=0.0,
            value=4.0,
            format="%.2f"
        )

    submitted = st.form_submit_button(
        "💧 ANALYZE WATER SAMPLE"
    )

# =====================================
# PREDICTION
# =====================================
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
        st.markdown("## Prediction Result")

        if int(prediction) == 1:

            st.markdown("""
            <div class="result-card">
                <h2 style="color:#D4AF37;">
                    💧 POTABLE
                </h2>
                <p>
                    The model classified this water sample as potable.
                </p>
            </div>
            """, unsafe_allow_html=True)

        else:

            st.markdown("""
            <div class="result-card">
                <h2 style="color:#E6A0A0;">
                    NOT POTABLE
                </h2>
                <p>
                    The model classified this water sample as not potable.
                </p>
            </div>
            """, unsafe_allow_html=True)

    except Exception as error:
        st.error(f"Prediction failed: {error}")

# =====================================
# FOOTER
# =====================================
st.markdown("""
<hr>
<div class="footer">
    WATER QUALITY ANALYZER | MACHINE LEARNING PROJECT
</div>
""", unsafe_allow_html=True)
