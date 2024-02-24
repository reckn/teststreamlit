import streamlit as st

def square_number(num):
    return num ** 2

def main():
    st.title('Simple Square Calculator')
    
    # User input
    user_input = st.number_input('Enter a number:')
    
    # Calculate square
    if st.button('Calculate'):
        result = square_number(user_input)
        st.write(f"The square of {user_input} is {result}")

if __name__ == "__main__":
    main()
