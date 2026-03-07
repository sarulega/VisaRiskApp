import streamlit as st

st.title("🌍 Visa Risk Calculator")
st.write("**Working!** 🎉")

name = st.text_input("Your name")
age = st.slider("Age", 18, 65, 30)

if st.button("Calculate Risk"):
    risk = 50 + (age - 40) * 2
    st.success(f"Risk: {risk}%")
    st.balloons()
