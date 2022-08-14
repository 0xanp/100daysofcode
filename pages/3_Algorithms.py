import streamlit as st

def page_config():
    # ---- PAGE CONFIG ----
    st.set_page_config(
        page_title="Algorithms",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # ---- HIDING DEFAUT WATERMARK ----
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden; }
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)