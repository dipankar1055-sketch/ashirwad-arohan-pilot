import streamlit as st
import config
from datetime import datetime

def show():
    # ──────────────────────────────────────────────────────────────
    # CUSTOM CSS — Cultural Theme
    # ──────────────────────────────────────────────────────────────
    
    st.markdown("""
    <style>
        .main { background: linear-gradient(135deg, #8B0000 0%, #A52A2A 50%, #D2691E 100%); }
        .stApp { background: linear-gradient(135deg, #8B0000 0%, #A52A2A 50%, #D2691E 100%); }
        .stMarkdown, .stText, .stCaption { color: #FFD700 !important; }
        h1, h2, h3, h4, h5, h6 { color: #FFD700 !important; }
        .stButton > button {
            background: #FFD700 !important;
            color: #8B0000 !important;
            font-weight: bold !important;
            border-radius: 30px !important;
            border: 2px solid #FFD700 !important;
            padding: 10px 30px !important;
        }
        .stButton > button:hover {
            background: #FFC000 !important;
            color: #6B0000 !important;
            transform: scale(1.05);
        }
        .stMetric {
            background: rgba(139, 0, 0, 0.8) !important;
            border-radius: 15px !important;
            padding: 15px !important;
            border: 2px solid #FFD700 !important;
        }
        .stMetric label, .stMetric div { color: #FFD700 !important; }
        .stAlert { background: rgba(139, 0, 0, 0.9) !important; border-color: #FFD700 !important; color: #FFD700 !important; }
        hr { border: 2px solid #FFD700 !important; opacity: 0.6 !important; }
        .subho { font-size: 28px; font-weight: bold; color: #FFD700; text-align: center; font-family: 'Georgia', serif; }
        .feature-card {
            background: rgba(139, 0, 0, 0.7);
            padding: 20px;
            border-radius: 15px;
            border: 2px solid #FFD700;
            text-align: center;
            margin: 5px;
        }
        .feature-card h3 { color: #FFD700; }
        .feature-card p { color: #FFD700; }
        .footer {
            text-align: center;
            color: #FFD700 !important;
            font-size: 14px;
            border-top: 2px solid #FFD700;
            padding-top: 20px;
            margin-top: 30px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # ──────────────────────────────────────────────────────────────
    # HERO SECTION
    # ──────────────────────────────────────────────────────────────
    
    st.markdown("""
    <div style="text-align: center; padding: 20px 0;">
        <h1 style="color: #FFD700; font-size: 36px;">🌺 ASHIRWAD</h1>
        <p style="color: #FFD700; font-size: 18px; margin-top: -10px;"><strong>ORGANIZER'S ASSISTANT</strong></p>
        <p style="color: #FFD700; font-size: 14px; opacity: 0.8;">Your Trusted Assistant for Seamless Event & Community Management</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    # ──────────────────────────────────────────────────────────────
    # DURGA PUJA HERO
    # ──────────────────────────────────────────────────────────────
    
    col1, col2 = st.columns([1, 3])
    
    with col1:
        st.image(config.AROHAN_LOGO, width=120)
    
    with col2:
        st.markdown("""
        <div class="subho">🌺 Subho Sharodiya! 🌺</div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        # AROHAN DURGA PUJA 2026
        ## Welcome the Goddess of Strength
        ### Digital Governance Platform
        """)
        
        st.caption("📍 Krishnarajapuram · Bengaluru")
        st.caption("🌺 Powered by **Neelkanth Governance Initiative**")
    
    st.divider()
    
    # ──────────────────────────────────────────────────────────────
    # MAHALAYA COUNTDOWN
    # ──────────────────────────────────────────────────────────────
    
    mahalaya_date = datetime(2026, 10, 8, 0, 0, 0)
    now = datetime.now()
    delta = mahalaya_date - now
    
    if delta.total_seconds() > 0:
        days = delta.days
        hours = delta.seconds // 3600
        minutes = (delta.seconds % 3600) // 60
        
        st.markdown("""
        <div style="text-align: center; background: rgba(139,0,0,0.8); padding: 20px; border-radius: 15px; border: 2px solid #FFD700;">
            <h2 style="color: #FFD700;">🕯️ Mahalaya Awakening</h2>
            <p style="color: #FFD700; font-size: 24px;">
                <strong>{} Days · {} Hours · {} Minutes</strong>
            </p>
            <p style="color: #FFD700; font-size: 16px;">"The countdown to Sharodotsav begins"</p>
        </div>
        """.format(days, hours, minutes), unsafe_allow_html=True)
    
    st.divider()
    
    # ──────────────────────────────────────────────────────────────
    # CTA BUTTONS
    # ──────────────────────────────────────────────────────────────
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("🌺 Become a Member", use_container_width=True):
                st.session_state.page = "Register"
                st.rerun()
        with col_btn2:
            if st.button("🤝 Donate Now", use_container_width=True):
                st.session_state.page = "Donate"
                st.rerun()
    
    st.divider()
    
    # ──────────────────────────────────────────────────────────────
    # FEATURES
    # ──────────────────────────────────────────────────────────────
    
    st.markdown("## 🌺 Ashirwad Features")
    st.caption("Empowering Organizers. Strengthening Communities.")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h3>📋 Plan</h3>
            <p>Organize<br>Manage<br>Collaborate</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h3>🤝 Volunteer</h3>
            <p>Coordination<br>Donations<br>Sponsors</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h3>💰 Finance</h3>
            <p>Tracking<br>Reports<br>Insights</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        st.markdown("""
        <div class="feature-card">
            <h3>📱 Mobile</h3>
            <p>First Experience<br>Announcements<br>Updates</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.divider()
    
    # ──────────────────────────────────────────────────────────────
    # ABOUT AROHAN
    # ──────────────────────────────────────────────────────────────
    
    st.markdown("## 🌺 About Arohan")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        ### Mission
        To preserve and celebrate Bengali culture and traditions through 
        Durga Puja, fostering community spirit and cultural heritage.
        """)
    
    with col2:
        st.markdown("""
        ### Community Impact
        - 🏛️ 172+ Active Members
        - 🌺 Annual Durga Puja Celebration
        - 🎭 Cultural Programs & Events
        - 🤝 Community Bonding & Support
        """)
    
    st.divider()
    
    # ──────────────────────────────────────────────────────────────
    # MEMBERSHIP TIERS
    # ──────────────────────────────────────────────────────────────
    
    st.markdown("## 🌺 Membership Tiers")
    st.caption("Join the Arohan community for Durga Puja 2026")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div style="background: rgba(139,0,0,0.7); padding: 20px; border-radius: 15px; border: 2px solid #FFD700; text-align: center;">
            <h3 style="color: #FFD700;">🌺 New</h3>
            <p style="color: #FFD700; font-size: 28px;"><strong>₹6,000</strong></p>
            <p style="color: #FFD700;">Full membership<br>Voting rights<br>Event access</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Register →", key="new_member"):
            st.session_state.membership_type = "New Member"
            st.session_state.amount = 6000
            st.session_state.page = "Register"
            st.rerun()
    
    with col2:
        st.markdown("""
        <div style="background: rgba(139,0,0,0.7); padding: 20px; border-radius: 15px; border: 2px solid #FFD700; text-align: center;">
            <h3 style="color: #FFD700;">🔄 Existing</h3>
            <p style="color: #FFD700; font-size: 28px;"><strong>₹5,500</strong></p>
            <p style="color: #FFD700;">Renewal benefits<br>Voting rights<br>Event access</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Register →", key="existing_member"):
            st.session_state.membership_type = "Existing Member"
            st.session_state.amount = 5500
            st.session_state.page = "Register"
            st.rerun()
    
    with col3:
        st.markdown("""
        <div style="background: rgba(139,0,0,0.7); padding: 20px; border-radius: 15px; border: 2px solid #FFD700; text-align: center;">
            <h3 style="color: #FFD700;">🪶 Solo New</h3>
            <p style="color: #FFD700; font-size: 28px;"><strong>₹2,500</strong></p>
            <p style="color: #FFD700;">Single member<br>Voting rights<br>Event access</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Register →", key="solo_new"):
            st.session_state.membership_type = "Solo (New Member)"
            st.session_state.amount = 2500
            st.session_state.page = "Register"
            st.rerun()
    
    with col4:
        st.markdown("""
        <div style="background: rgba(139,0,0,0.7); padding: 20px; border-radius: 15px; border: 2px solid #FFD700; text-align: center;">
            <h3 style="color: #FFD700;">🪶 Solo Exist</h3>
            <p style="color: #FFD700; font-size: 28px;"><strong>₹2,200</strong></p>
            <p style="color: #FFD700;">Single renewal<br>Voting rights<br>Event access</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("Register →", key="solo_existing"):
            st.session_state.membership_type = "Solo (Existing Member)"
            st.session_state.amount = 2200
            st.session_state.page = "Register"
            st.rerun()
    
    st.divider()
    
    # ──────────────────────────────────────────────────────────────
    # DONATION SECTION
    # ──────────────────────────────────────────────────────────────
    
    st.markdown("## 🤝 Digital Pushpanjali")
    st.caption("Offer your devotion from home — Up to ₹1,00,000")
    
    col1, col2, col3, col4, col5, col6, col7, col8 = st.columns(8)
    
    suggested = [500, 1000, 5000, 10000, 25000, 50000, 75000, 100000]
    labels = ["₹500", "₹1K", "₹5K", "₹10K", "₹25K", "₹50K", "₹75K", "₹1L"]
    
    for i, (amount, label) in enumerate(zip(suggested, labels)):
        with eval(f"col{i+1}"):
            if st.button(label, key=f"donate_{amount}"):
                st.session_state.donation_amount = amount
                st.session_state.page = "Donate"
                st.rerun()
    
    st.markdown("### Custom Offering")
    custom_amount = st.number_input(
        "Enter your donation amount (₹1 — ₹1,00,000)",
        min_value=1,
        max_value=100000,
        value=1000,
        step=100
    )
    
    if st.button("🤝 Offer Pushpanjali", key="donate_custom"):
        st.session_state.donation_amount = custom_amount
        st.session_state.page = "Donate"
        st.rerun()
    
    st.info("🔴 **DEMO MODE** — No real payment will be processed")
    
    st.divider()
    
    # ──────────────────────────────────────────────────────────────
    # COMMITTEE CONTACTS
    # ──────────────────────────────────────────────────────────────
    
    st.markdown("## 📞 Committee Contacts")
    
    col1, col2, col3, col4, col5 = st.columns(5)
    
    admins = ["Souvick Sengupta", "Rishi", "Kaushik Acharya", "Soumitra", "Anirban"]
    for i, name in enumerate(admins):
        with eval(f"col{i+1}"):
            st.markdown(f"""
            <div style="text-align: center; background: rgba(139,0,0,0.7); padding: 15px; border-radius: 10px; border: 1px solid #FFD700;">
                <p style="color: #FFD700;"><strong>{name}</strong><br>Admin</p>
            </div>
            """, unsafe_allow_html=True)
    
    st.info("📱 Join our WhatsApp group for updates and announcements")
    
    st.divider()
    
    # ──────────────────────────────────────────────────────────────
    # FOOTER
    # ──────────────────────────────────────────────────────────────
    
    st.markdown("""
    <div class="footer">
        <p style="color: #FFD700; font-size: 20px;">🌺 ASHIRWAD — ORGANIZER'S ASSISTANT</p>
        <p style="color: #FFD700; font-size: 16px;"><strong>Empowering Organizers. Strengthening Communities.</strong></p>
        <p style="color: #FFD700;">NEW NAME. SAME VISION.</p>
        <hr style="border: 1px solid #FFD700; opacity: 0.3; width: 50%;">
        <p style="color: #FFD700;">🌺 AROHAN — Durga Puja 2026</p>
        <p style="color: #FFD700;">© Arohan Durga Puja Committee — Krishnarajapuram · Bengaluru</p>
        <p style="color: #FFD700;">Powered by <strong>Neelkanth Governance Initiative</strong></p>
        <p style="color: #FFD700; font-size: 18px; margin-top: 10px;">"Subho Sharodiya!"</p>
    </div>
    """, unsafe_allow_html=True)
