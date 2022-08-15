import streamlit as st

def page_config():
    # ---- PAGE CONFIG ----
    st.set_page_config(
        page_title="References",
        page_icon=":books:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    # ---- TITLE AND HEADER ----
    st.title("References")

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
    st.write("""
    [1]: [Tech Interview Handbook](https://www.techinterviewhandbook.org/)

    [2]: [Python3 Official Language Docs](https://docs.python.org/3/contents.html)

    [3]: [Java Official Language Docs](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/index.html)
    """)

if __name__ == "__main__":
    main()