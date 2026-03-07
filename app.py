import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Load model
model = joblib.load('visa_risk_model.pkl')
encoder = joblib.load('visa_type_encoder.pkl')

st.title("🌍 Visa Rejection Risk Analysis System")
st.markdown("---")

# Form
col1, col2 = st.columns(2)
with col1:
    visa_type = st.selectbox("Visa Type", ['Student', 'Work', 'Tourist'])
    age = st.slider("Age", 18, 65, 25)
    countries = ['India', 'USA', 'UK', 'Canada', 'Australia', 'Germany', 'China', 'Singapore']
    country = st.selectbox('🇮🇳 Country:', countries)

with col2:
    income = st.slider("Income (USD)", 10000, 100000, 30000)
    language = st.slider("IELTS Score", 4.0, 9.0, 6.5)
    prior_reject = st.checkbox("Previous Rejection")

if st.button("🚀 PREDICT RISK", type="primary"):
    visa_code = encoder.transform([visa_type])[0]
    data = np.array([[age, income, visa_code, language, 0, country_risk, 
                     int(prior_reject), 15000, 0.7]])
    
    risk = model.predict_proba(data)[0][1]
    approve = 1 - risk * 100
    
    st.success(f"✅ Approval Chance: **{approve:.0f}%**")
    
    if approve > 75:
        st.success("🎉 LOW RISK - Apply immediately!")
    elif approve > 50:
        st.warning("⚠️ MEDIUM RISK - Improve 1-2 factors")
    else:
        st.error("❌ HIGH RISK - Major changes needed")

st.markdown("---")
st.caption("Model Accuracy: 91% | March 2026")
