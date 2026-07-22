import streamlit as st
import random
import time
from datetime import datetime
import config
from database import get_connection

def show():
    st.markdown("# 💳 Payment")
    
    if 'membership_id' in st.session_state:
        st.caption(f"Membership ID: {st.session_state.membership_id}")
        amount = st.session_state.amount
        payment_type = "membership"
    elif 'donation_amount' in st.session_state:
        st.caption("Donation")
        amount = st.session_state.donation_amount
        payment_type = "donation"
    else:
        st.warning("No payment pending")
        return
    
    st.divider()
    
    st.markdown("### Payment Details")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Amount", f"₹{amount}")
    with col2:
        st.metric("Status", "⏳ Pending")
    
    st.info("🔴 **DEMO MODE** — No real money will be deducted")
    
    if st.button("💳 Pay Now", use_container_width=True):
        with st.spinner("Processing Payment..."):
            time.sleep(2)
            success = random.random() < 0.9
            
            trace_id = config.TRACE_ID_FORMAT.format(
                date=datetime.now().strftime("%Y%m%d"),
                id=random.randint(1, 999)
            )
            
            try:
                conn = get_connection()
                cursor = conn.cursor()
                
                if success:
                    status = "Success"
                    st.balloons()
                    st.success("✅ Payment Successful!")
                else:
                    status = "Failed"
                    st.error("❌ Payment Failed. Please try again.")
                
                cursor.execute('''
                    INSERT INTO transactions (user_id, type, amount, status, trace_id)
                    VALUES (?, ?, ?, ?, ?)
                ''', (0, payment_type, amount, status, trace_id))
                
                if payment_type == "membership":
                    cursor.execute('''
                        UPDATE members SET payment_status = ?
                        WHERE membership_id = ?
                    ''', ("Payment Made" if success else "Pending", st.session_state.membership_id))
                
                conn.commit()
                conn.close()
                
                st.info(f"Trace ID: {trace_id}")
            except Exception as e:
                st.error(f"Error: {e}")
