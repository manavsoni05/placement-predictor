import streamlit as st
import pickle
import numpy as np

# Load the model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# App layout
st.set_page_config(page_title="Placement Predictor", layout="centered", )
st.markdown("<h2 style='font-size: 30px;'>🎓 Placement Predictor App - By Manav Soni</h2>", unsafe_allow_html=True)
st.markdown("Enter your CGPA and IQ to predict if placement will happen.")

# Input form
with st.form("placement_form"):
    cgpa = st.number_input("Enter your CGPA (0.0 - 10.0)", min_value=0.0, max_value=10.0, step=0.01)
    iq = st.number_input("Enter your IQ Score", min_value=0, max_value=200, step=1)
    submit = st.form_submit_button("Predict")

if submit:
    input_data = np.array([[cgpa, iq]])
    prediction = model.predict(input_data)[0]
    result = "✅ Placement will happen!" if prediction == 1 else "❌ Placement will not happen."
    st.markdown(f"### {result}")
