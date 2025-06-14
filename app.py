import streamlit as st
import joblib
import numpy as np

model = joblib.load('KNNclassifier.pkl')
scaler = joblib.load('scaler.pkl')

st.title("💓 Heart Failure Prediction")

time = st.number_input("⏱️ Time (days)", min_value=0)
serum_creatinine = st.number_input("🩸 Serum Creatinine", min_value=0.0, step=0.1)
ejection_fraction = st.number_input("💓 Ejection Fraction (%)", min_value=0, max_value=100)

if st.button("🔍 Predict"):
    input_data = np.array([[time, serum_creatinine, ejection_fraction]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)

    if prediction[0] == 1:
        st.markdown(
            "<h3 style='color: red;'>❌ Prediction: The patient is likely to DIE.</h3>",
            unsafe_allow_html=True
        )
    else:
        st.success("✅ Prediction: The patient is likely to SURVIVE.")
