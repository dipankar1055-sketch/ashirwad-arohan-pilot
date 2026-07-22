import streamlit as st
import config
from pages import landing, register, donate, payment, dashboard

st.set_page_config(
    page_title="🌺 Ashirwad — Arohan Durga Puja 2026",
    page_icon="🌺",
    layout="wide"
)

def main():
    # Sidebar Navigation
try:
    st.sidebar.image("assets/aroihan logo.jpg", width=150)
except:
    st.sidebar.markdown("🌺 **AROHAN**")
    st.sidebar.markdown("## 🌺 Ashirwad")
    st.sidebar.caption("Organizer's Assistant")
    st.sidebar.divider()
    
    # Navigation
    page = st.sidebar.radio(
        "Navigate",
        ["🏠 Home", "🌺 Register", "🤝 Donate", "📊 Dashboard"]
    )
    
    if page == "🏠 Home":
        landing.show()
    elif page == "🌺 Register":
        register.show()
    elif page == "🤝 Donate":
        donate.show()
    elif page == "📊 Dashboard":
        dashboard.show()
    
    # Footer
    st.sidebar.divider()
    st.sidebar.caption("© Arohan Durga Puja 2026")
    st.sidebar.caption("Powered by Neelkanth Governance Initiative")

if __name__ == "__main__":
    main()
