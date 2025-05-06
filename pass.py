import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title('🔐Password Strenght Checker')
st.markdown("""
## Welcome to the ultimate password strength checker! 👋
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
            we will give you helpful tips to create a ''Strong Password''🔒 """)

def check_password_strength(password):
    score = 0
    feedback = []


    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be ""atleast 8 characters long"".")

    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("❌Password should include ""both uppercase (A-Z) and lowercase (a-z) letters"".")

    if re.search(r"\d", password):
        score += 1
    else:
        feedback.append("❌Password should include ""at least one number (0-9) "".")

    if re.search(r"[!@#$%&*]", password):
        score += 1
    else:
        feedback.append("❌Password should contain at least one special character(!@#$%&*).")

        #display password strenght results
    if score == 4 :
        st.success("✅ ""Strong Password"" - Your password is secure.")
    elif score == 3 :
        st.info("⚠️""Moderate Password"" - Considerimproving security by adding more feature.")

    else:
        st.error("❌ ""Week Password"" - follow the suggestion below to strength it. ")
    
    if  feedback:
        with st.expander("🔍"" Improve Your Password"" "):
            for item in feedback: 
                st.write(item)                                     
            
password = st.text_input("Enter Your Password:", type="password", help="Ensure your password is strong 🔐")

#Button working
if st.button("Check Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password first!")