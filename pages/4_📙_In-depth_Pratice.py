import streamlit as st

def page_config():
    # ---- PAGE CONFIG ----
    st.set_page_config(
        page_title="In-depth Practice",
        page_icon=":orange_book:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # ---- TITLE AND HEADER ----
    st.title("In-depth Practice")

    # ---- HIDING DEFAUT WATERMARK AND ADDING SOCIALS ----
    social_template ="""
             <style>
            #MainMenu {visibility: hidden; }
            footer {visibility: hidden; }
            a:link,
            a:visited {
            background-color: transparent;
            text-decoration: underline;
            }
            a:hover,
            a:active {
            color: red;
            background-color: transparent;
            text-decoration: underline;
            }
            </style>                                                                                                                                      
            <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css">
            <div style= 'text-align: center;'>
                <a target="_blank" href="https://apham.info/"><i class="fa-solid fa-window-maximize fa-xl"></i></a>                                                                                                                                                                                                                                                                                            
                <a target="_blank" href="https://twitter.com/0xAnP"><i class="fa-brands fa-twitter fa-xl"></i></a>
                <a target="_blank" href="https://github.com/0xanp"><i class="fa-brands fa-github fa-xl"></i></a>
                <a target="_blank" href="https://www.linkedin.com/in/binh-an-pham/"><i class="fa-brands fa-linkedin fa-xl"></i></a>
            </div>
            <br><br><br>
    """
    st.sidebar.markdown(social_template, unsafe_allow_html=True)


def main():
    page_config()

if __name__ == "__main__":
    main()