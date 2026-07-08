import streamlit as st
import hashlib
import requests
from zxcvbn import zxcvbn
import random
import string

st.set_page_config(page_title="Password Fortress", page_icon="🔐", layout="centered")

st.title("🔐 Password Fortress")
st.markdown("**Advanced Password Strength Analyzer & Secure Generator**")

tab1, tab2 = st.tabs(["🔍 Password Analyzer", "🔑 Password Generator"])

with tab1:
    st.subheader("Test Your Password")
    password = st.text_input("Enter password", type="password", key="analyzer")
    
    if password:
        result = zxcvbn(password)
        score = result["score"]
        
        labels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong"]
        colors = ["#ff4444", "#ff8800", "#ffaa00", "#00cc00", "#00cc66"]
        
        st.progress(score / 4.0)
        st.markdown(f"**Strength:** <span style='color:{colors[score]}'>{labels[score]}</span> ({score}/4)", unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Guesses Needed", f"{result['guesses']:,}")
        with col2:
            ct = result.get('crack_times_display', {})
            st.metric("Offline Crack Time", ct.get('offline_slow_hashing', 'N/A'))
        
        st.subheader("Feedback")
        feedback = result.get("feedback", {})
        if feedback.get("warning"):
            st.warning("⚠️ " + feedback["warning"])
        for suggestion in feedback.get("suggestions", []):
            st.info("💡 " + suggestion)
        
        if st.button("🔍 Check Have I Been Pwned"):
            with st.spinner("Checking..."):
                try:
                    sha1 = hashlib.sha1(password.encode()).hexdigest().upper()
                    prefix = sha1[:5]
                    suffix = sha1[5:]
                    r = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")
                    leaked = any(line.startswith(suffix) for line in r.text.splitlines())
                    if leaked:
                        st.error("🚨 This password has been leaked in data breaches!")
                    else:
                        st.success("✅ Not found in known breaches.")
                except:
                    st.error("Could not connect.")

with tab2:
    st.subheader("Generate a Strong Password")
    length = st.slider("Password Length", 12, 32, 16)
    
    c1, c2, c3, c4 = st.columns(4)
    upper = c1.checkbox("Uppercase (A-Z)", True)
    lower = c2.checkbox("Lowercase (a-z)", True)
    digits = c3.checkbox("Numbers (0-9)", True)
    special = c4.checkbox("Special (!@#$...)", True)
    
    if st.button("Generate Strong Password", type="primary"):
        chars = ""
        if lower: chars += string.ascii_lowercase
        if upper: chars += string.ascii_uppercase
        if digits: chars += string.digits
        if special: chars += "!@#$%^&*()_+-=[]{}|;:,.<>/?"
        
        if chars:
            password = ''.join(random.choice(chars) for _ in range(length))
            st.code(password, language=None)
            st.success("✅ Password generated! Use a password manager to store it.")
            
            # Optional: Analyze the generated password
            if st.button("Analyze this generated password"):
                res = zxcvbn(password)
                st.info(f"Strength: {['Very Weak','Weak','Medium','Strong','Very Strong'][res['score']]}")
        else:
            st.error("Please select at least one character type.")

st.divider()
st.caption("Password Fortress — Cybersecurity Portfolio Project | Built with zxcvbn & Have I Been Pwned")
