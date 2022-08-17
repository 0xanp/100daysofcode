import streamlit as st

def page_config():
    # ---- PAGE CONFIG ----
    st.set_page_config(
        page_title="100 days of code",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def page_layout():
    st.image("100days.png")
    # ---- HIDING DEFAUT WATERMARK AND ADDING SOCIALS ----
    css_example ="""
             <style>
            #MainMenu {visibility: hidden; }
            footer {visibility: hidden; }
            a:link,
            a:visited {
            color: white;
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
    st.sidebar.markdown(css_example, unsafe_allow_html=True)
    st.write("Week 1 to Week 4: Basics, Data Structures and Algorithms")
    st.write("Week 5 to Week 12: In-depth Practice with Leetcode")

def main():
    page_config()
    page_layout()

if __name__ == "__main__":
    main()