# chat_interface.py
import streamlit as st
from ollama import get_response_from_llama  # Import the function from ollama.py


def streamlit_app():
    """
    Streamlit application to interact with Llama.
    """
    st.title("Chat with Llama")  # Page title

    # User interaction input
    user_input = st.text_input("Enter your message:")

    if user_input:
        # Get response from server
        response = get_response_from_llama(user_input)

        # Extract textual content from the JSON response
        if isinstance(response, dict) and 'choices' in response:
            content = response['choices'][0]['message']['content']
            st.write("Response from Llama:", content)  # Display the text from the response
        else:
            st.write("Error in response:", response)  # Display an error message for invalid responses
