import streamlit as st
import numpy as np

st.set_page_config(layout="wide", page_icon="🌍")
st.title("🌍 Visa Rejection Risk Calculator")
st.markdown("---")

# Sidebar inputs
st.sidebar.header("📝 Enter Details")
country = st.sidebar.selectbox("🇮🇳 Country", ['India', 'USA', 'UK', 'Canada'])
visa = st.sidebar.selectbox("📋 Visa Type", ['H1B', 'L1', 'Student', 'Tourist'])
age = st.sidebar.slider("👤 Age", 18, 65, 32)
income_k = st.sidebar.slider("💰 Income ($K)", 0, 200, 85)

if st.sidebar.button("🔮 Calculate Risk", type="primary"):
    
    # SIMULATED ML MODEL (always works!)
    risk_score = np.clip(
        0.3 + (age/1000) - (income_k/500) + 
        (1 if visa in ['Student', 'Tourist'] else 0) +
        (1 if country == 'India' else 0), 
        0, 1
    )
    
    # Results
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Rejection Risk", f"{risk_score:.1%}")
        status = "🔴 HIGH RISK" if risk_score > 0.5 else "🟢 LOW RISK"
        st.metric("Status", status)
    
    with col2:
        st.metric("Recommendation", "Improve Income" if risk_score > 0.5 else "Strong Application")
    
    # Chart
    st.subheader("📊 Risk Factors")
    factors = {
        "Age": age/5,
        "Income": 100-income_k/2,
        "Visa Type": 50 if visa in ['H1B', 'L1'] else 80,
        "Country": 60 if country == 'India' else 30
    }
    st.bar_chart(factors)

st.info("👈 Enter details → Click **Calculate Risk**")
st.markdown("**No ML model needed - Pure math simulation!** ✅")
