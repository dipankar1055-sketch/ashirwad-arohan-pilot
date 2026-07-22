import streamlit as st
import config
from database import add_member

def show():
    st.markdown("# 🌺 Become a Member")
    st.caption("Join the Arohan community for Durga Puja 2026")
    st.divider()
    
    membership_options = {
        "New Member": 6000,
        "Existing Member": 5500,
        "Solo (New Member)": 2500,
        "Solo (Existing Member)": 2200
    }
    
    selected_type = st.radio(
        "Choose your membership type:",
        list(membership_options.keys()),
        format_func=lambda x: f"{x} — ₹{membership_options[x]}"
    )
    
    st.divider()
    
    with st.form("registration_form"):
        name = st.text_input("Full Name *")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number *")
        address = st.text_area("Address")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            children_below_5 = st.number_input("Children Below 5", min_value=0, value=0)
        with col2:
            children_5_12 = st.number_input("Children 5-12", min_value=0, value=0)
        with col3:
            adults = st.number_input("Adults", min_value=1, value=1)
        
        submitted = st.form_submit_button("🌺 Register Now")
        
        if submitted:
            if not name or not phone:
                st.error("Please fill in all required fields (*)")
            else:
                data = {
                    'name': name,
                    'email': email,
                    'phone': phone,
                    'address': address,
                    'children_below_5': children_below_5,
                    'children_5_12': children_5_12,
                    'adults': adults,
                    'membership_type': selected_type,
                    'amount': membership_options[selected_type]
                }
                
                try:
                    membership_id = add_member(data)
                    st.success(f"✅ Registration Complete!")
                    st.info(f"Your Membership ID: **{membership_id}**")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")
