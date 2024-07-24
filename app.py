import streamlit as st
# ----configuring page
st.set_page_config(page_title="My Webpage", page_icon="👨‍💻", layout="wide")
st.subheader("Hi, I am Kgaogelo Moela")
st.title("Financial Information Systems Alumni")
st.write("I am passionate about using VBA and Python in finance to be efficient")
button1 = st.button("About Me")
#----everything about me
if button1:
    text = ("""I am a Vaal University of Technology Alumni and throughout my studies in Financial Information Systems,
     I have developed a keen interest in
    accounting principles and practices. My coursework included modules on financial accounting,cost
    and management accounting,Data Analysis,IT Project Management, Business/System Analysis, and the use of information systems in financial analysis and also programming language such as VBA and Python""")
    st.write(text)
# Create a LinkedIn button
st.link_button("Connect on LinkedIn", "https://www.linkedin.com/in/kgaogelo-moela-260aab255")

# You can add more components to your app below!
