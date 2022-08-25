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

# ---- DAY 1 ----
def day_1():
    with st.expander("Day 1 - Array", expanded=False):
        tab1, tab2, tab3 = st.tabs(["Concepts", "Code examples","LeetCode"])
        with tab1:
            st.write("""
            ### Readings
            - [Array cheatsheet for coding interviews](https://www.techinterviewhandbook.org/algorithms/array/[), Tech Interview Handbook
            - [Array in Data Structure: What is, Arrays Operations](https://www.guru99.com/array-data-structure.html), Guru99
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
        with tab3:
            st.write("""
            - [Two Sum](https://leetcode.com/problems/two-sum/)
            - [Best Time to Buy and Sell Stock](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)
            - [Product of Array Except Self](https://leetcode.com/problems/product-of-array-except-self/)
            - [Maximum Subarray](https://leetcode.com/problems/maximum-subarray/)
            """)
        
# ---- DAY 2 ----     
def day_2():
    with st.expander("Day 2 - String"):
        tab1, tab2= st.tabs(["Concepts", "Code examples"])
        with tab1:
            st.title("Concepts")
        with tab2:
            st.title("Code examples")   

def page_layout():
    # ---- TITLE AND HEADER ----
    st.title("The Basics")

    # ---- HIDING DEFAUT WATERMARK ----
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
    day_1()
    day_2()


def main():
    page_config()
    page_layout()

if __name__ == "__main__":
    main()