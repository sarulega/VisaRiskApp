import streamlit as st
import pandas as pd

# Page config 
st.set_page_config(
    page_title="Visa Risk Rejection Analysis", 
    page_icon="🛂", 
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    padding: 3rem;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin-bottom: 2rem;
    box-shadow: 0 15px 35px rgba(0,0,0,0.2);
}
.page-card {
    background: white;
    padding: 2.5rem;
    border-radius: 15px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.1);
    border-left: 5px solid #1e3c72;
}
.progress-bar {
    background: linear-gradient(90deg, #1e3c72 0%, #2a5298 100%);
    height: 8px;
    border-radius: 10px;
    margin: 2rem 0;
}
</style>
""", unsafe_allow_html=True)

# Session state
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# MAIN TITLE - Changed everywhere
st.markdown("""
<div class="main-header">
    <h1>🛂 Visa Risk Rejection Analysis</h1>
    <p>Complete Multi-Type Visa Rejection Predictor | All Visa Categories | Professional Analysis</p>
</div>
""", unsafe_allow_html=True)

# PROGRESS BAR
progress = st.progress(st.session_state.page / 8)
st.markdown(f"""
<div class="progress-bar" style="width: {(st.session_state.page/8)*100}%"></div>
""", unsafe_allow_html=True)

# PAGES
pages = [
    "Personal Details", "Passport Details", "Educational Details", 
    "University Details", "Financial Proof", "Application Form", 
    "Medical & PCC", "Visa Risk Rejection Analysis"
]

st.subheader(f"📋 Step {st.session_state.page + 1}/8: {pages[st.session_state.page]}")

# === PAGE 1: PERSONAL DETAILS ===
if st.session_state.page == 0:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.info("**Personal information for Visa Risk Rejection Analysis**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.form_data['full_name'] = st.text_input("👤 Full Name (as in passport)*")
        
        # FIXED DOB - Shows 2000-2026 in calendar!
        st.session_state.form_data['dob'] = st.date_input(
            "📅 Date of Birth*", 
            min_value=datetime.date(2000, 1, 1),
            max_value=datetime.date(2026, 12, 31),
            value=datetime.date(2005, 6, 15)  # Defaults to age ~21
        )
        
        st.session_state.form_data['gender'] = st.selectbox("♂️ Gender*", ["Male", "Female", "Other"])
    
    with col2:
        st.session_state.form_data['nationality'] = st.selectbox("🏳️ Nationality*", 
            ["India", "USA", "UK", "Canada", "Australia", "Germany", "Singapore"])
        st.session_state.form_data['marital_status'] = st.selectbox("💍 Marital Status*", 
            ["Single", "Married", "Divorced", "Widowed"])
        st.session_state.form_data['phone'] = st.text_input("📞 Phone*")
    
    st.session_state.form_data['email'] = st.text_input("📧 Email*")
    st.session_state.form_data['address'] = st.text_area("🏠 Address*")
    
    col1, col2 = st.columns(2)
    col1.button("➡️ Next", on_click=lambda: setattr(st.session_state, 'page', 1))
    col2.button("🔄 Reset", on_click=lambda: (setattr(st.session_state, 'page', 0), setattr(st.session_state, 'form_data', {})))
    
    st.markdown('</div>', unsafe_allow_html=True)


# === PAGE 2: PASSPORT ===
elif st.session_state.page == 1:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.warning("**Passport validity critical for rejection analysis**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.form_data['passport_num'] = st.text_input("🛂 Passport Number*")
        st.session_state.form_data['passport_issue'] = st.date_input("📅 Issue Date*")
        st.session_state.form_data['passport_expiry'] = st.date_input("📅 Expiry Date*")
    with col2:
        st.session_state.form_data['photo_ready'] = st.checkbox("✅ Photos ready (2x2 inch)")
    
    col_prev, col_next = st.columns([1,1])
    col_prev.button("⬅️ Previous", on_click=lambda: setattr(st.session_state, 'page', 0))
    col_next.button("➡️ Next", on_click=lambda: setattr(st.session_state, 'page', 2))
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 3: EDUCATION ===
elif st.session_state.page == 2:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.info("**Academic records impact rejection rates**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.form_data['tenth_percent'] = st.slider("📚 10th %", 0, 100, 85)
        st.session_state.form_data['twelfth_percent'] = st.slider("📚 12th %", 0, 100, 88)
    with col2:
        st.session_state.form_data['ug_degree'] = st.selectbox("🎓 UG Degree*", 
            ["B.Tech", "B.Sc", "B.Com", "BA", "Other"])
        st.session_state.form_data['ug_percent'] = st.slider("📚 UG %", 0, 100, 78)
    
    st.session_state.form_data['english_test'] = st.selectbox("📝 English Test*", 
        ["IELTS 6.5+", "TOEFL 80+", "PTE 58+", "None"])
    
    col_prev, col_next = st.columns([1,1])
    col_prev.button("⬅️ Previous", on_click=lambda: setattr(st.session_state, 'page', 1))
    col_next.button("➡️ Next", on_click=lambda: setattr(st.session_state, 'page', 3))
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 4: UNIVERSITY ===
elif st.session_state.page == 3:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.warning("**University reputation affects rejection**")
    
    st.session_state.form_data['university_country'] = st.selectbox("🎓 University Country*", 
        ["Canada", "UK", "USA", "Australia", "Germany", "Ireland"])
    st.session_state.form_data['course'] = st.text_input("📖 Course Name*")
    st.session_state.form_data['duration'] = st.slider("⏱️ Duration (years)", 1, 5, 2)
    st.session_state.form_data['offer_letter'] = st.checkbox("✅ Official Offer Letter*")
    
    col_prev, col_next = st.columns([1,1])
    col_prev.button("⬅️ Previous", on_click=lambda: setattr(st.session_state, 'page', 2))
    col_next.button("➡️ Next", on_click=lambda: setattr(st.session_state, 'page', 4))
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 5: FINANCE ===
elif st.session_state.page == 4:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.info("**Financial proof = #1 rejection reason**")
    
    col1, col2 = st.columns(2)
    with col1:
        st.session_state.form_data['annual_income'] = st.number_input("💰 Sponsor Income (₹Lakhs)*", 
            min_value=0.0, max_value=100.0, value=10.0, step=1.0)
        st.session_state.form_data['bank_balance'] = st.number_input("🏦 Bank Balance (₹Lakhs)*", 
            min_value=0.0, max_value=50.0, value=15.0, step=1.0)
    with col2:
        st.session_state.form_data['sponsor_relation'] = st.selectbox("👨‍👩‍👦 Sponsor*", 
            ["Self", "Father", "Mother", "Brother", "Other"])
        st.session_state.form_data['loan_approved'] = st.checkbox("✅ Loan Approved")
    
    col_prev, col_next = st.columns([1,1])
    col_prev.button("⬅️ Previous", on_click=lambda: setattr(st.session_state, 'page', 3))
    col_next.button("➡️ Next", on_click=lambda: setattr(st.session_state, 'page', 5))
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 6: APPLICATION ===
elif st.session_state.page == 5:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    
    st.session_state.form_data['visa_type'] = st.selectbox("🛂 Visa Type*", 
        ["F1 Student", "H1B Work", "B1/B2 Tourist", "L1 Transfer", "J1 Exchange"])
    st.session_state.form_data['travel_purpose'] = st.selectbox("🎯 Purpose*", 
        ["Study", "Work", "Tourism", "Business"])
    st.session_state.form_data['return_intent'] = st.selectbox("🏠 Post-Visa Plan*", 
        ["Return India", "Work Abroad", "Further Study"])
    
    col_prev, col_next = st.columns([1,1])
    col_prev.button("⬅️ Previous", on_click=lambda: setattr(st.session_state, 'page', 4))
    col_next.button("➡️ Next", on_click=lambda: setattr(st.session_state, 'page', 6))
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 7: MEDICAL & PCC ===
elif st.session_state.page == 6:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.warning("**Complete before appointment**")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("🩺 Medical", "✅" if st.session_state.form_data.get('medical_done', False) else "❌")
    col2.metric("📜 PCC", "✅" if st.session_state.form_data.get('pcc_ready', False) else "❌")
    col3.metric("💳 Fees", "✅" if st.session_state.form_data.get('fees_paid', False) else "❌")
    
    st.session_state.form_data['medical_done'] = st.checkbox("✅ Medical Test Done")
    st.session_state.form_data['pcc_ready'] = st.checkbox("✅ PCC Ready") 
    st.session_state.form_data['fees_paid'] = st.checkbox("✅ Fees Paid")
    
    col_prev, col_next = st.columns([1,1])
    col_prev.button("⬅️ Previous", on_click=lambda: setattr(st.session_state, 'page', 5))
    col_next.button("🎯 Visa Risk Analysis", on_click=lambda: setattr(st.session_state, 'page', 7))
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 8: RESULTS ===
elif st.session_state.page == 7:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.header("🚨 Visa Risk Rejection Analysis - Final Report")
    
    # ADVANCED RISK CALCULATION
    risk_score = 25
    
    # Academic (40% weight)
    academic = (st.session_state.form_data.get('tenth_percent', 0) + 
               st.session_state.form_data.get('twelfth_percent', 0) + 
               st.session_state.form_data.get('ug_percent', 0)) / 3
    if academic > 85: risk_score -= 15
    elif academic < 70: risk_score += 20
    
    # Financial (30% weight)  
    finance = st.session_state.form_data.get('bank_balance', 0) + st.session_state.form_data.get('annual_income', 0)
    if finance > 25: risk_score -= 20
    elif finance < 10: risk_score += 25
    
    # Documents (20% weight)
    docs_ready = sum([
        st.session_state.form_data.get('offer_letter', False),
        st.session_state.form_data.get('medical_done', False),
        st.session_state.form_data.get('pcc_ready', False),
        st.session_state.form_data.get('fees_paid', False)
    ])
    if docs_ready >= 3: risk_score -= 10
    else: risk_score += 15
    
    risk_score = max(0, min(100, risk_score))
    
    # RESULTS DISPLAY
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        st.metric("📊 Predicted Rejection Risk", f"{risk_score:.0f}%", delta=None)
    with col2:
        status = "🟢 LOW RISK" if risk_score < 30 else "🟡 MODERATE" if risk_score < 60 else "🔴 HIGH RISK"
        st.markdown(f"### {status}")
    with col3:
        st.metric("✅ Success Probability", f"{100-risk_score:.0f}%")
    
    # RISK BREAKDOWN CHART
    st.subheader("📈 Rejection Risk Factors")
    factors = {
        "Academics": max(0, 90-academic),
        "Finances": max(0, 30-finance),
        "Documents": max(0, 4-docs_ready),
        "Visa Type": 15 if st.session_state.form_data.get('visa_type') == "B1/B2 Tourist" else 5
    }
    st.bar_chart(factors)
    
    # DETAILED CHECKLIST
    st.subheader("📋 Document Status")
    checklist = pd.DataFrame([
        ["Passport Valid", "✅" if st.session_state.form_data.get('passport_expiry') else "❌"],
        ["Offer Letter", "✅" if st.session_state.form_data.get('offer_letter') else "❌"],
        ["Bank Statements", "✅" if st.session_state.form_data.get('bank_balance', 0) > 10 else "❌"],
        ["English Test", "✅" if st.session_state.form_data.get('english_test') != "None" else "❌"],
        ["Medical Test", "✅" if st.session_state.form_data.get('medical_done') else "❌"],
        ["PCC", "✅" if st.session_state.form_data.get('pcc_ready') else "❌"]
    ], columns=['Document', 'Status'])
    st.dataframe(checklist, use_container_width=True)
    
    # PERSONALIZED RECOMMENDATIONS
    st.subheader("🎯 Rejection Prevention Strategy")
    
    if risk_score > 60:
        st.error("🔴 **HIGH REJECTION RISK** - Urgent Actions:")
        st.write("• 💰 **Show ₹25+ Lakhs** bank balance (6 months)")
        st.write("• 📜 **Loan approval** letter from bank") 
        st.write("• 🩺 **Medical test** from approved panel")
        st.write("• 👮 **PCC** from Passport Seva")
    elif risk_score > 40:
        st.warning("🟡 **MODERATE RISK** - Improve these:")
        st.write("• 💼 **Stronger sponsor** documents")
        st.write("• 🎓 **English test score** improvement")
        st.write("• 📋 **Complete all checkboxes**")
    else:
        st.success("🟢 **LOW RISK** - Excellent Profile:")
        st.write("• ✅ **Ready for submission**")
        st.write("• 💳 **Pay visa fees** online")
        st.write("• 🛫 **Book appointment slot**")
    
    # NAVIGATION
    col1, col2 = st.columns(2)
    col1.button("⬅️ Edit Profile", on_click=lambda: setattr(st.session_state, 'page', 0))
    col2.button("🔄 New Analysis", on_click=lambda: (setattr(st.session_state, 'page', 0), setattr(st.session_state, 'form_data', {})))
    
    st.markdown('</div>', unsafe_allow_html=True)

# FOOTER
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem; font-size: 0.9rem;'>
    <strong>Visa Risk Rejection Analysis</strong> | All Visa Types | Professional Tool
</div>
""", unsafe_allow_html=True)
