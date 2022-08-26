import streamlit as st
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

def page_config():
    # ---- PAGE CONFIG ----
    st.set_page_config(
        page_title="The Code Sandbox",
        page_icon=":closed_book:",
        layout="wide",
        initial_sidebar_state="expanded",
    )

def page_layout():
    # ---- TITLE AND HEADER ----
    st.title("The Code Sandbox")

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

    # ---- CODE EDITOR ----
    with st.container():
            c1, c2 = st.columns([3, 1])

            c2.subheader("Parameters")

            with c1:
                content = st_ace(
                    language=c2.selectbox("Language mode", options=LANGUAGES, index=121),
                    theme=c2.selectbox("Theme", options=THEMES, index=35),
                    keybinding=c2.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
                    font_size=c2.slider("Font size", 5, 24, 14),
                    tab_size=c2.slider("Tab size", 1, 8, 4),
                    show_gutter=c2.checkbox("Show gutter", value=True),
                    show_print_margin=c2.checkbox("Show print margin", value=False),
                    wrap=c2.checkbox("Wrap enabled", value=False),
                    auto_update=c2.checkbox("Auto update", value=True),
                    readonly=c2.checkbox("Read-only", value=False),
                    min_lines=45,
                    key="ace",
                )

def main():
    page_config()
    page_layout()


if __name__ == "__main__":
    main()