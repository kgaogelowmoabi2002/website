import streamlit as st
import json
from streamlit_lottie import st_lottie
# ----configuring page
st.set_page_config(page_title="My Webpage", page_icon="👨‍💻", layout="wide")
st.subheader("Hi, I am Kgaogelo Moela")
st.title("Diploma In Financial Information Systems(FIS) Alumni")
st.write("I am passionate about using VBA and Python in finance to be efficient")
button1 = st.button("About Me")
#----everything about me
# Initialize session state (only once)
if 'show_about_me' not in st.session_state:
    st.session_state.show_about_me = False

# Button to toggle visibility
if button1:
    st.session_state.show_about_me = not st.session_state.show_about_me

# Display information if the button is toggled on
if st.session_state.show_about_me:
    st.write("""I am eager to contribute my skills and passion for accounting and information technology and further develop skills in a dynamic environment with communication and IT skills.
    Throughout my studies in Financial Information Systems, I have developed a keen interest in
    accounting principles and practices. My coursework included modules on financial accounting,
    cost and management accounting, and the use of information systems in financial analysis.
    
SKILLS:

- Programming languages such as (VBA,Python and SQL) 
- Ability to work independently
- Ability to work under pressure 
- Eager to learn
- Cost accounting system
- Generally Accepted Accounting Principles (GAAP)
- General ledger preparation
- Report-writing skills
- Ability to Analyze and recommend costs and cost savings,
- Detailed oriented
- Knowledgeable on statistics
- Attention to details
- Sage accounting software experience
""")
st.subheader("JOBS I CAN DO:")
st.write("""
- Junior Financial Accountant
- Business Analyst
- Junior Cost Accountant
- Data Capturer
- Accounts Payable Clerk
- Junior Financial Analyst
- Payroll Administrator
- Bookkeeper/Secretary
- Data Analyst
- Database Administrator
""")

st.link_button("Connect on LinkedIn", "https://www.linkedin.com/in/kgaogelo-moela-260aab255")
st.caption("Email me here:")

import streamlit as st
import smtplib


contact_form = """
<form action="https://formsubmit.co/moelakgaogelow@gmail.com" method="POST">
    <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="your name" required>
     <input type="email" name="email" placeholder="your email" required>
     <textarea name="message" placeholder="Write a message"></textarea>
     <button type="submit">Send</button>
</form>
"""

st.markdown(contact_form,unsafe_allow_html=True)
def local_css(file_name):
    with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css(r"C:\Users\defaultuser0\Documents/style.css.txt")
