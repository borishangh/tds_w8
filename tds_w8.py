import streamlit as st


def main():
    st.title("TDS W8 Assgn : Greatest of 3 numbers")
    st.write("Borishan Ghosh \n 22f2000824")

    st.write("Enter three Numbers : ")
    a = st.number_input("a = ")
    b = st.number_input("b = ")
    c = st.number_input("c = ")

    st.write("The largest number is : " + str(max(a, b, c)))


if __name__ == "__main__":
    main()
