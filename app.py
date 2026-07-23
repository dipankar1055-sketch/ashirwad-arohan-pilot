import streamlit as st
import config

st.set_page_config(
    page_title="🌺 Ashirwad — Arohan Durga Puja 2026",
    page_icon="🌺",
    layout="wide"
)

def main():
    # Sidebar Navigation with error handling
    st.sidebar.markdown("## 🌺 Ashirwad")
    st.sidebar.caption("Organizer's Assistant")
    st.sidebar.divider()
    
    # Try to show logo, fallback to text
    try:
        st.sidebar.image("assets/aroihan logo.jpg", width=150)
    except:
        st.sidebar.markdown("🌺 **AROHAN**")
    
    # Navigation
    page = st.sidebar.radio(
        "Navigate",
        ["🏠 Home", "🌺 Register", "🤝 Donate", "📊 Dashboard"]
    )
    
    # Custom CSS
    st.markdown("""
    <style>
        .stApp { background: linear-gradient(135deg, #8B0000 0%, #A52A2A 50%, #D2691E 100%); }
        h1, h2, h3, h4 { color: #FFD700 !important; }
        .stMarkdown, .stText, .stCaption { color: #FFD700 !important; }
        .stButton > button {
            background: #FFD700 !important;
            color: #8B0000 !important;
            font-weight: bold !important;
            border-radius: 30px !important;
            padding: 10px 30px !important;
        }
        .stButton > button:hover {
            background: #FFC000 !important;
            transform: scale(1.05);
        }
        hr { border: 2px solid #FFD700 !important; opacity: 0.6 !important; }
    </style>
    """, unsafe_allow_html=True)
    
    if page == "🏠 Home":
        from pages import landing
        landing.show()
    elif page == "🌺 Register":
        from pages import register
        register.show()
    elif page == "🤝 Donate":
        from pages import donate
        donate.show()
    elif page == "📊 Dashboard":
        from pages import dashboard
        dashboard.show()
    
    st.sidebar.divider()
    st.sidebar.caption("© Arohan Durga Puja 2026")
    st.sidebar.caption("Powered by Neelkanth Governance Initiative")

if __name__ == "__main__":
    main()
