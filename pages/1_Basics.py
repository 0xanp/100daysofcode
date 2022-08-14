import streamlit as st

def page_config():
    # ---- PAGE CONFIG ----
    st.set_page_config(
        page_title="Basics",
        page_icon=":computer:",
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
        tab1, tab2, tab3 = st.tabs(["Concepts", "Code examples", "Notes"])
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
            python_code = '''>>> fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
>>> fruits.count('apple')
2
>>> fruits.count('tangerine')
0
>>> fruits.index('banana')
3
>>> fruits.index('banana', 4)  # Find next banana starting a position 4
6
>>> fruits.reverse()
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange']
>>> fruits.append('grape')
>>> fruits
['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape']
>>> fruits.sort()
>>> fruits
['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear']
>>> fruits.pop()
'pear'
            '''
            java_code = '''class ArrayDemo {
    public static void main(String[] args) {
        // declares an array of integers
        int[] anArray;

        // allocates memory for 10 integers
        anArray = new int[10];
           
        // initialize first element
        anArray[0] = 100;
        // initialize second element
        anArray[1] = 200;
        // and so forth
        anArray[2] = 300;
        anArray[3] = 400;
        anArray[4] = 500;
        anArray[5] = 600;
        anArray[6] = 700;
        anArray[7] = 800;
        anArray[8] = 900;
        anArray[9] = 1000;

        System.out.println("Element at index 0: "
                           + anArray[0]);
        System.out.println("Element at index 1: "
                           + anArray[1]);
        System.out.println("Element at index 2: "
                           + anArray[2]);
        System.out.println("Element at index 3: "
                           + anArray[3]);
        System.out.println("Element at index 4: "
                           + anArray[4]);
        System.out.println("Element at index 5: "
                           + anArray[5]);
        System.out.println("Element at index 6: "
                           + anArray[6]);
        System.out.println("Element at index 7: "
                           + anArray[7]);
        System.out.println("Element at index 8: "
                           + anArray[8]);
        System.out.println("Element at index 9: "
                           + anArray[9]);
    }
} 
            '''
            java_output = '''Element at index 0: 100
Element at index 1: 200
Element at index 2: 300
Element at index 3: 400
Element at index 4: 500
Element at index 5: 600
Element at index 6: 700
Element at index 7: 800
Element at index 8: 900
Element at index 9: 1000
'''
            with python:
                st.code(python_code, language='python')
            with java:
                st.write("""The following program, `ArrayDemo`, creates an array of integers, puts some values in the array, and prints each value to standard output.""")
                st.code(java_code, language='java')
                st.write('The output from this program is:')
                st.code(java_output, language='java')
        with tab3:
            st.write("Notes")
        
# ---- DAY 2 ----     
def day_2():
    with st.expander("Day 2 - String"):
        tab1, tab2, tab3 = st.tabs(["Concepts", "Code examples", "Notes"])
        with tab1:
            st.title("Concepts")
        with tab2:
            st.title("Code examples")
        with tab3:
            st.title("Notes")

def main():
    page_config()
    day_1()
    day_2()

if __name__ == "__main__":
    main()