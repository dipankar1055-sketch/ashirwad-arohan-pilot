import streamlit as st
import config
from database import get_all_members, get_dashboard_stats

def show():
    st.markdown("# 📊 Admin Dashboard")
    st.caption(config.DEPLOYMENT_FULL)
    
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    
    if not st.session_state.logged_in:
        with st.form("login"):
            username = st.text_input("Username")
            password = st.text_input("Password", type="password")
            
            if st.form_submit_button("Login"):
                if username == config.DEFAULT_ADMIN_USERNAME and password == config.DEFAULT_ADMIN_PASSWORD:
                    st.session_state.logged_in = True
                    st.success("✅ Login Successful!")
                    st.rerun()
                else:
                    st.error("❌ Invalid Credentials")
        return
    
    stats = get_dashboard_stats()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("👥 Total Members", stats['total_members'])
        st.metric("📅 Today's Registrations", stats['today_registrations'])
    with col2:
        st.metric("💰 Total Membership Fees", f"₹{stats['total_membership_fees']:,}")
        st.metric("🤝 Total Donations", f"₹{stats['total_donations']:,}")
    with col3:
        st.metric("⏳ Pending Payments", stats['pending_payments'])
        st.metric("🔄 Renewals Due", stats['renewals_due'])
    
    st.divider()
    
    st.markdown("## 📋 Member List")
    
    try:
        df = get_all_members()
        search = st.text_input("🔍 Search Member")
        
        if search:
            df = df[df['name'].str.contains(search, case=False) |
                    df['phone'].str.contains(search, case=False)]
        
        st.dataframe(df[['membership_id', 'name', 'phone', 'email', 'membership_type', 'amount', 'payment_status']])
        
        if st.button("📥 Export CSV"):
            csv = df.to_csv(index=False)
            st.download_button("Download", csv, "members.csv", "text/csv")
    except Exception as e:
        st.warning("Database not yet initialized. Please complete registration first.")
    
    st.divider()
    st.caption("© Arohan Durga Puja 2026 | Powered by Neelkanth")
