import streamlit as st
import pandas as pd

def home():
    c_title, c_bear = st.columns([1, 4])
    with c_title:
        st.title("Welcome!")
    with c_bear:
        st.image("images/welcome_bear.png", width=80)
        
    st.header("- My Personal Homepage -")
    st.divider()

    col_photo, col_info = st.columns(2)
    with col_photo:
        st.image("images/me.png", caption="My Photo", width=220)

    with col_info:
        st.subheader("Personal Information")
        st.write("Name: Fiona")
        st.write("Student ID: 250580203")
        st.write("Major: Higher Diploma in Data Science and Artificial Intelligence")
        st.write("School: Hong Kong Institute of Information Technology")
        
    st.subheader("My Skill Proficiency")
    skill_data = {
        "Tech Skill": ["Python", "Java", "Hadoop", "Oracle SQL", "Streamlit"],
        "Level": ["Learning", "Intermediate", "Intermediate", "Intermediate", "Learning"]
    }
    df_skill = pd.DataFrame(skill_data)
    st.table(df_skill)

    st.subheader("Hobbies")
    h1, h2, h3, h4 = st.columns(4)
    with h1: st.write("📖 Reading")
    with h2: st.write("✈️ Traveling")
    with h3: st.write("🎨 Painting")
    with h4: st.write("✍️ Handwriting")

    st.divider()
    st.markdown("# 📥 Download My Profile Document")
    full_profile_text = """
==================== PERSONAL PROFILE ====================
Name: Fiona
Student ID: 250580203
Major: Higher Diploma in Data Science and Artificial Intelligence
School: Hong Kong Institute of Information Technology

---------------- SKILL PROFICIENCY ----------------
Python: Learning
Java: Intermediate
Hadoop: Intermediate
Oracle SQL: Intermediate
Streamlit: Learning

---------------- HOBBIES ----------------
Reading, Traveling, Painting, Handwriting

================ HOMETOWN INTRO =================
Sichuan is a beautiful and culturally diverse province in southwest China.
It boasts breathtaking natural landscapes, world-famous delicacies, and profound multi-ethnic traditions.
Various ethnic minorities inhabit this land, inheriting gorgeous hand-made traditional costumes and unique folk customs.
"""
    st.download_button(
        label="Download Profile as TXT File",
        data=full_profile_text,
        file_name="My_Profile_Document.txt",
        mime="text/plain"
    )

def my_hometown():
    st.title("My Hometown — Sichuan")
    st.write("""
Sichuan is a beautiful and culturally diverse province in southwest China.
It boasts breathtaking natural landscapes, world-famous delicacies, and profound multi-ethnic traditions.
Various ethnic minorities inhabit this land, inheriting gorgeous hand-made traditional costumes and unique folk customs.
""")
    st.divider()
    c1, c2, c3 = st.columns(3)
    with c1:
        st.image("images/sichuan1.png")
    with c2:
        st.image("images/sichuan2.png")
    with c3:
        st.image("images/sichuan3.png", caption="Traditional Ethnic Costume")
        st.caption("Exquisite ethnic costume with local cultural features")

    st.divider()
    feeling = st.selectbox(
        "How do you feel about these hometown photos?",
        ["Surprised", "Wonderful", "Amazing", "Beautiful", "Impressive"]
    )
    st.write(f"My feeling: {feeling}")

def my_album():
    st.title("My Album")
    a1, a2, a3, a4 = st.columns(4)

    with a1:
        st.image("images/album1.png")
    with a2:
        st.image("images/album2.png")
    with a3:
        st.image("images/album3.png")
    with a4:
        st.image("images/album4.png")

def leave_message():
    st.title("Leave a Message")
    name = st.text_input("Your Name")
    content = st.text_area("Your Message")
    if st.button("Submit Message"):
        if name and content:
            st.success("Message submitted successfully!")
        else:
            st.error("Please fill in both name and message!")

st.set_page_config(page_title="Personal Homepage", layout="wide")

bg_style = """
<style>
[data-testid="stAppViewContainer"] {
background-color: #eef8f3 !important;
}
[data-testid="stHeader"] {
background-color: #eef8f3 !important;
}
[data-testid="stToolbar"] {
background-color: #eef8f3 !important;
}
</style>
"""
st.markdown(bg_style, unsafe_allow_html=True)

def main():
    nav_home, nav_hometown, nav_album, nav_msg = st.columns(4)
    with nav_home:
        btn_home = st.button("Home")
    with nav_hometown:
        btn_hometown = st.button("My Hometown")
    with nav_album:
        btn_album = st.button("My Album")
    with nav_msg:
        btn_msg = st.button("Leave a Message")

    if "current_page" not in st.session_state:
        st.session_state.current_page = "Home"

    if btn_home:
        st.session_state.current_page = "Home"
    elif btn_hometown:
        st.session_state.current_page = "My Hometown"
    elif btn_album:
        st.session_state.current_page = "My Album"
    elif btn_msg:
        st.session_state.current_page = "Leave a Message"

    st.divider()
    active_page = st.session_state.current_page
    if active_page == "Home":
        home()
    elif active_page == "My Hometown":
        my_hometown()
    elif active_page == "My Album":
        my_album()
    elif active_page == "Leave a Message":
        leave_message()

if __name__ == "__main__":
    main()