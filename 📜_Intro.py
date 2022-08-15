import streamlit as st

def page_config():
    # ---- PAGE CONFIG ----
    st.set_page_config(
        page_title="100 days of code",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # ---- TITLE AND HEADER ----
    st.title("100 days of code")
    
    # ---- HIDING DEFAUT WATERMARK ----
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden; }
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

def main():
    page_config()
    st.write("Week 1 to Week 4: Basics, Data Structures and Algorithms")
    st.write("Week 5 to Week 12: In-depth Practice with Leetcode")

if __name__ == "__main__":
    main()