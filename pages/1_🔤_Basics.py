import streamlit as st
from streamlit_embedcode import github_gist

def page_config():
    # ---- PAGE CONFIG ----
    st.set_page_config(
        page_title="Basics",
        page_icon=":abc:",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    # ---- TITLE AND HEADER ----
    st.title("The Basics")

    # ---- HIDING DEFAUT WATERMARK ----
    hide_menu_style = """
            <style>
            #MainMenu {visibility: hidden; }
            footer {visibility: hidden;}
            </style>
            """
    st.markdown(hide_menu_style, unsafe_allow_html=True)

# ---- DAY 1 ----
def day_1():
    with st.expander("Day 1 - Array", expanded=False):
        tab1, tab2 = st.tabs(["Concepts", "Code examples"])
        with tab1:
            st.write("""
            Arrays hold values of the same type at contiguous memory locations. 
            
            In an array, we're usually concerned about two things: 
            - the position/index of an element (ordering)
            - the element itself (data types/values)
            \\
            In some languages, the size of the array is dynamic and you do not
            need to define before hand. Hence, people usually use these languages
            (Python, Javascript, Ruby) for interviews.

            **Advantages**
            - Store multiple elements of the same type with one single variable name
            - Accessing elements is fast as long as you have the index, as opposed to linked lists where you have to traverse from the head.
            \\
            **Disadvantages**
            - Addition and removal of elements into/from the middle of an array is slow because the remaining elements need to be shifted to accommodate the new/missing element. An exception to this is if the position to be inserted/removed is at the end of the array.
            - For certain languages where the array size is fixed, it cannot alter its size after initialization. If an insertion causes the total number of elements to exceed the size, a new array has to be allocated and the existing elements have to be copied over. The act of creating a new array and transferring elements over takes O(n) time.
            """)
        with tab2:
            python, java = st.tabs(["Python3", "Java"])
            python_code = "https://gist.github.com/0xanp/58bc11362ec85a713cdb4fefcf6ce357"
            java_code = "https://gist.github.com/0xanp/464cf4dbeb044c5e3f7a20e093581b54"
            java_output = "https://gist.github.com/0xanp/929dfe645ef9130d533ffaacfa6dddf3"
            with python:
                github_gist(python_code,height=500)
            with java:
                st.write("""The following program, `ArrayDemo`, creates an array of integers, puts some values in the array, and prints each value to standard output.""")
                github_gist(java_code,height=600)
                st.write('The output from this program is:')
                github_gist(java_output,height=300)
        
# ---- DAY 2 ----     
def day_2():
    with st.expander("Day 2 - String"):
        tab1, tab2= st.tabs(["Concepts", "Code examples"])
        with tab1:
            st.title("Concepts")
        with tab2:
            st.title("Code examples")

def main():
    page_config()
    day_1()
    day_2()

if __name__ == "__main__":
    main()