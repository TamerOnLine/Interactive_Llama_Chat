# main.py
import streamlit as st
from chat_interface import streamlit_app  # استيراد دالة streamlit_app من streamlit.py

if __name__ == "__main__":
    # عرض رسالة ترحيبية
    st.title("Welcome to Llama Chat!")
    
    # استدعاء التطبيق من streamlit.py
    streamlit_app()
