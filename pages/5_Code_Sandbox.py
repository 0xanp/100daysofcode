import streamlit as st
from streamlit_ace import st_ace, KEYBINDINGS, LANGUAGES, THEMES

def page_config():
    # ---- PAGE CONFIG ----
    st.set_page_config(
        page_title="The Code Sandbox",
        page_icon=":computer:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # ---- TITLE AND HEADER ----
    st.title("The Code Sandbox")

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
    with st.container():
        c1, c2 = st.columns([3, 1])

        c2.subheader("Parameters")

        with c1:
            content = st_ace(
                placeholder=c2.text_input("Editor placeholder", value="Write your code here"),
                language=c2.selectbox("Language mode", options=LANGUAGES, index=121),
                theme=c2.selectbox("Theme", options=THEMES, index=35),
                keybinding=c2.selectbox("Keybinding mode", options=KEYBINDINGS, index=3),
                font_size=c2.slider("Font size", 5, 24, 14),
                tab_size=c2.slider("Tab size", 1, 8, 4),
                show_gutter=c2.checkbox("Show gutter", value=True),
                show_print_margin=c2.checkbox("Show print margin", value=False),
                wrap=c2.checkbox("Wrap enabled", value=False),
                auto_update=c2.checkbox("Auto update", value=False),
                readonly=c2.checkbox("Read-only", value=False),
                min_lines=45,
                key="ace",
            )

            if content:
                st.subheader("Content")
                st.text(content.language)


if __name__ == "__main__":
    main()