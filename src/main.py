# main.py
import streamlit as st
from chat_interface import streamlit_app  # Import streamlit_app function from streamlit.py


if __name__ == "__main__":
    """
    Entry point for the Streamlit application.
    """
    st.title("Welcome to Llama Chat!")  # Welcome message

    # Call the application from chat_interface.py
    streamlit_app()
