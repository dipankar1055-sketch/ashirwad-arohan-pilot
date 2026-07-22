import streamlit as st
import config
from database import get_connection

def show():
    st.markdown("# 🤝 Donate to Arohan")
    st.caption("Your contribution supports our community — Up to ₹1,00,000")
    st.divider()
    
    st.markdown("### Suggested Amounts")
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    
    suggested = [500, 1000, 5000, 10000, 25000, 50000, 75000, 100000]
    labels = ["₹500", "₹1K", "₹5K", "₹10K", "₹25K", "₹50K", "₹75K", "₹1L"]
    
    for i, (amount, label) in enumerate(zip(suggested, labels)):
        with eval(f"col{i+1}"):
            if st.button(label, key=f"donate_{amount}"):
                st.session_state.donation_amount = amount
                st.rerun()
    
    st.markdown("### Custom Amount")
    amount = st.number_input(
        "Enter donation amount (₹1 — ₹1,00,000)",
        min_value=1,
        max_value=100000,
        value=1000,
        step=100
    )
    
    with st.form("donation_form"):
        donor_name = st.text_input("Your Name *")
        email = st.text_input("Email")
        phone = st.text_input("Phone Number")
        message = st.text_area("Message (Optional)")
        
        submitted = st.form_submit_button("🤝 Donate Now")
        
        if submitted:
            if not donor_name:
                st.error("Please enter your name")
            else:
                try:
                    conn = get_connection()
                    cursor = conn.cursor()
                    cursor.execute('''
                        INSERT INTO donations (donor_name, email, phone, amount, message, status)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (donor_name, email, phone, amount, message, 'Pending'))
                    conn.commit()
                    conn.close()
                    st.success(f"✅ Donation Registered!")
                    st.info(f"Amount: ₹{amount}")
                    st.balloons()
                except Exception as e:
                    st.error(f"Error: {e}")
    
    st.info("🔴 **DEMO MODE** — No real payment will be processed")
