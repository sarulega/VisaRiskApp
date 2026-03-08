import streamlit as st

st.set_page_config(page_title="Visa Risk Form", page_icon="🌍", layout="centered")

st.title("🌍 Visa Application Risk Form")
st.write("Fill the details below to see a simple estimated risk (demo, not real).")

# --- FORM ---
with st.form("visa_form"):
    col1, col2 = st.columns(2)

    with col1:
        country = st.selectbox(
            "Country",
            ["India", "USA", "UK", "Canada", "Australia", "Germany", "Singapore", "Other"],
        )
        visa_type = st.selectbox(
            "Visa Type",
            ["Student", "Work", "Tourist", "H1B", "L1", "Other"],
        )

    with col2:
        age = st.slider("Age", 18, 70, 28)
        income = st.number_input("Annual Income (USD)", min_value=0, max_value=300000, value=30000, step=1000)

    submitted = st.form_submit_button("Check Risk")

# --- LOGIC + OUTPUT ---
if submitted:
    # Simple demo logic – you can change later
    risk_score = 30  # base

    # Age effect
    if age < 25:
        risk_score += 15
    elif age > 50:
        risk_score += 10

    # Income effect
    if income < 20000:
        risk_score += 25
    elif income < 50000:
        risk_score += 10
    else:
        risk_score -= 5

    # Country effect (example)
    if country == "India":
        risk_score += 10
    elif country in ["USA", "UK", "Canada", "Australia", "Germany", "Singapore"]:
        risk_score += 0
    else:
        risk_score += 5

    # Visa type effect
    if visa_type in ["Tourist", "Student"]:
        risk_score += 5
    elif visa_type in ["H1B", "L1", "Work"]:
        risk_score -= 5

    # Clamp between 0–100
    risk_score = max(0, min(100, risk_score))

    st.subheader("Result")
    st.metric("Estimated Rejection Risk", f"{risk_score:.0f}%")

    if risk_score >= 60:
        st.error("High risk. Consider improving income, documents, or choosing a different visa type.")
    elif risk_score >= 30:
        st.warning("Medium risk. Some factors may still be weak.")
    else:
        st.success("Low risk. Profile looks relatively strong.")
else:
    st.info("Submit the form to see your risk estimate.")
