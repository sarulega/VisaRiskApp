import streamlit as st

# Page config + Custom styling
st.set_page_config(page_title="Visa Application Portal", page_icon="🛂", layout="wide")

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

# Session state for multi-page
if 'page' not in st.session_state:
    st.session_state.page = 0
if 'form_data' not in st.session_state:
    st.session_state.form_data = {}

# HEADER
st.markdown("""
<div class="main-header">
    <h1>🛂 Complete Visa Application Portal</h1>
    <p>Professional 8-Step Process | Document Checklist | Success Prediction</p>
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
    "Medical & PCC", "Results & Suggestions"
]

st.subheader(f"📋 Step {st.session_state.page + 1}/8: {pages[st.session_state.page]}")

# === PAGE 1: PERSONAL DETAILS ===
if st.session_state.page == 0:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.info("**You must provide basic personal information exactly as in passport.**")
    
    with st.form("personal"):
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.form_data['full_name'] = st.text_input("👤 Full Name (as in passport)*")
            st.session_state.form_data['dob'] = st.date_input("📅 Date of Birth*")
            st.session_state.form_data['gender'] = st.selectbox("Gender*", ["Male", "Female", "Other"])
        with col2:
            st.session_state.form_data['nationality'] = st.selectbox("🏳️ Nationality*", 
                ["India", "USA", "UK", "Canada", "Australia", "Germany", "Singapore"])
            st.session_state.form_data['marital_status'] = st.selectbox("💍 Marital Status*", 
                ["Single", "Married", "Divorced", "Widowed"])
            st.session_state.form_data['phone'] = st.text_input("📞 Phone Number*")
        
        st.session_state.form_data['email'] = st.text_input("📧 Email ID*")
        st.session_state.form_data['address'] = st.text_area("🏠 Current Address*")
        
        if st.form_submit_button("✅ Next - Passport Details", use_container_width=True):
            if all([st.session_state.form_data.get(k) for k in ['full_name', 'dob', 'nationality', 'phone', 'email']]):
                st.session_state.page = 1
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 2: PASSPORT ===
elif st.session_state.page == 1:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.warning("**Passport must have 6+ months validity from travel date**")
    
    with st.form("passport"):
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.form_data['passport_num'] = st.text_input("🛂 Passport Number*")
            st.session_state.form_data['passport_issue'] = st.date_input("📅 Issue Date*")
            st.session_state.form_data['passport_expiry'] = st.date_input("📅 Expiry Date*")
        with col2:
            st.session_state.form_data['photo_ready'] = st.checkbox("✅ Passport photos ready (2x2 inch, white bg)")
        
        if st.form_submit_button("✅ Next - Education", use_container_width=True):
            st.session_state.page = 2
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 3: EDUCATION ===
elif st.session_state.page == 2:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.info("**Required for student visas**")
    
    with st.form("education"):
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.form_data['tenth_percent'] = st.slider("10th %", 0, 100, 85)
            st.session_state.form_data['twelfth_percent'] = st.slider("12th %", 0, 100, 88)
        with col2:
            st.session_state.form_data['ug_degree'] = st.selectbox("UG Degree*", 
                ["B.Tech", "B.Sc", "B.Com", "BA", "Other"])
            st.session_state.form_data['ug_percent'] = st.slider("UG %", 0, 100, 78)
        
        st.session_state.form_data['english_test'] = st.selectbox("English Test*", 
            ["IELTS (6.5+)", "TOEFL (80+)", "PTE (58+)", "None"])
        
        if st.form_submit_button("✅ Next - University", use_container_width=True):
            st.session_state.page = 3
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 4: UNIVERSITY ===
elif st.session_state.page == 3:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.warning("**Must have OFFICIAL offer letter**")
    
    with st.form("university"):
        st.session_state.form_data['university'] = st.selectbox("🎓 University Country*", 
            ["Canada", "UK", "USA", "Australia", "Germany", "Ireland"])
        st.session_state.form_data['course'] = st.text_input("Course Name*")
        st.session_state.form_data['duration'] = st.slider("Course Duration (years)", 1, 5, 2)
        st.session_state.form_data['offer_letter'] = st.checkbox("✅ Official offer letter received*")
        
        if st.form_submit_button("✅ Next - Finances", use_container_width=True):
            st.session_state.page = 4
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 5: FINANCE ===
elif st.session_state.page == 4:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.info("**Show 6 months bank statements**")
    
    with st.form("finance"):
        col1, col2 = st.columns(2)
        with col1:
            st.session_state.form_data['annual_income'] = st.number_input("Sponsor Annual Income (₹Lakhs)*", 
                min_value=0.0, max_value=100.0, value=10.0, step=1.0)
            st.session_state.form_data['bank_balance'] = st.number_input("Bank Balance (₹Lakhs)*", 
                min_value=0.0, max_value=50.0, value=15.0, step=1.0)
        with col2:
            st.session_state.form_data['sponsor_relation'] = st.selectbox("Sponsor Relation*", 
                ["Self", "Father", "Mother", "Brother", "Other"])
            st.session_state.form_data['loan_approved'] = st.checkbox("✅ Education loan approved")
        
        if st.form_submit_button("✅ Next - Application", use_container_width=True):
            st.session_state.page = 5
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 6: APPLICATION FORM ===
elif st.session_state.page == 5:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    
    with st.form("app_form"):
        st.session_state.form_data['travel_purpose'] = st.selectbox("Travel Purpose*", 
            ["Study", "Work", "Tourism", "Conference"])
        st.session_state.form_data['return_intent'] = st.selectbox("Post-study plan*", 
            ["Return home", "Work abroad", "Further studies"])
        
        if st.form_submit_button("✅ Next - Medical", use_container_width=True):
            st.session_state.page = 6
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 7: MEDICAL & PCC ===
elif st.session_state.page == 6:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.warning("**Medical from approved panel**")
    
    with st.form("medical"):
        st.session_state.form_data['medical_done'] = st.checkbox("✅ Medical test scheduled")
        st.session_state.form_data['pcc_ready'] = st.checkbox("✅ Police Clearance Certificate ready")
        st.session_state.form_data['fees_paid'] = st.checkbox("✅ Visa fees paid")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("← Previous", use_container_width=True):
                st.session_state.page = 5
                st.rerun()
        with col2:
            if st.button("🎯 Get Results", use_container_width=True):
                st.session_state.page = 7
                st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# === PAGE 8: RESULTS ===
elif st.session_state.page == 7:
    st.markdown('<div class="page-card">', unsafe_allow_html=True)
    st.header("🎯 Visa Success Prediction")
    
    # COMPLEX RISK CALCULATION
    risk_score = 20
    
    # Academic strength
    academic_score = (st.session_state.form_data.get('tenth_percent', 0) + 
                     st.session_state.form_data.get('twelfth_percent', 0) + 
                     st.session_state.form_data.get('ug_percent', 0)) / 3
    if academic_score > 85: risk_score -= 15
    elif academic_score > 70: risk_score -= 5
    
    # Financial strength  
    finance_score = st.session_state.form_data.get('bank_balance', 0) + st.session_state.form_data.get('annual_income', 0)
    if finance_score > 25: risk_score -= 20
    elif finance_score > 15: risk_score -= 10
    
    # Other factors
    if st.session_state.form_data.get('passport_expiry'):
        months_left = (st.session_state.form_data['passport_expiry'] - st.session_state.form_data['passport_issue']).days / 30
        if months_left < 6: risk_score += 25
    
    risk_score = max(0, min(100, risk_score))
    
    # DISPLAY RESULTS
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        st.metric("📊 Rejection Risk", f"{risk_score:.0f}%", delta=None)
    
    with col2:
        if risk_score < 30:
            st.success("✅ **HIGH SUCCESS** - Excellent profile!")
        elif risk_score < 60:
            st.warning("⚠️ **MODERATE** - Some improvements needed")
        else:
            st.error("🚨 **HIGH RISK** - Urgent improvements required")
    
    with col3:
        st.metric("🎯 Success Chance", f"{100-risk_score:.0f}%")
    
    # DETAILED CHECKLIST
    st.subheader("✅ Document Readiness")
    
    checklist = {
        "Passport (6+ months valid)": st.session_state.form_data.get('passport_expiry'),
        "10th/12th/UG marksheets": academic_score > 0,
        "University offer letter": st.session_state.form_data.get('university'),
        "6 months bank statements": st.session_state.form_data.get('bank_balance'),
        "Sponsor documents": st.session_state.form_data.get('sponsor_relation'),
        "English test score": st.session_state.form_data.get('english_test'),
        "Medical test booked": st.session_state.form_data.get('medical_done'),
        "PCC ready": st.session_state.form_data.get('pcc_ready')
    }
    
    st.dataframe(pd.DataFrame(list(checklist.items()), columns=['Document', 'Status']), use_container_width=True)
    
    # PERSONALIZED RECOMMENDATIONS
    st.subheader("🎯 Action Plan")
    
    if risk_score > 60:
        st.error("**IMMEDIATE ACTIONS:**")
        st.write("• 💰 Show ₹25+ lakhs bank balance")
        st.write("• 📜 Get loan approval letter") 
        st.write("• 🩺 Complete medical test")
    else:
        st.success("**FINAL PREP:**")
        st.write("• 📋 Double-check all documents")
        st.write("• 💳 Pay visa fees online")
        st.write("• 🛫 Book appointment slot")
    
    # NAVIGATION
    col1, col2 = st.columns(2)
    col1.button("← Edit Details", on_click=lambda: setattr(st.session_state, 'page', 0))
    if st.button("🔄 New Application", type="secondary"):
        for key in list(st.session_state.form_data.keys()):
            del st.session_state.form_data[key]
        st.session_state.page = 0
        st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# NAVIGATION (Bottom)
if st.session_state.page > 0:
    if st.button("← Previous Step", key="prev"):
        st.session_state.page -= 1
        st.rerun()

st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 1rem; font-size: 0.9rem;'>
    Visa Application Portal | Demo Version | For Educational Purpose
</div>
""", unsafe_allow_html=True)
