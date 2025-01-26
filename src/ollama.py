# ollama.py
import requests

# Llama server URL
url = "http://localhost:11434/v1/chat/completions"


def get_response_from_llama(user_input):
    """
    Sends a message to the Llama server and retrieves the response.

    Args:
        user_input (str): The user's input message.

    Returns:
        dict or str: JSON response from the server or error message.
    """
    data = {
        "model": "llama3.2:latest",  # Model name
        "messages": [{"role": "user", "content": user_input}]
    }

    try:
        # Send the request to the server
        response = requests.post(url, json=data)
        response.raise_for_status()  # Check for HTTP errors
        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"  # Handle exceptions
