# Interactive Llama Chat

Interactive Llama Chat is a Python-based application that allows users to interact with the Llama model through a Streamlit interface. The project provides an easy-to-use platform for sending messages to the Llama server and receiving responses in real time.

---

## Features
- **Streamlit Interface**: A user-friendly web interface for communication.
- **Backend Integration**: Communicates with the Llama server using REST APIs.
- **Extensibility**: Modular code structure for easy customization and extension.

---

## Project Structure
```plaintext
tameronline-interactive_llama_chat/
├── requirements.txt
└── src/
    ├── chat_interface.py
    ├── main.py
    └── ollama.py
```

### Files Overview
- **`requirements.txt`**: Lists the dependencies required for the project.
- **`src/chat_interface.py`**: Contains the main Streamlit application logic.
- **`src/main.py`**: The entry point for the application.
- **`src/ollama.py`**: Handles communication with the Llama server.

---

## Installation

### Prerequisites
Ensure you have the following installed on your system:
- Python 3.8 or later
- pip (Python package manager)
- [Download Ollama](https://www.ollama.com/download)
- [Download Llama3.2](https://www.ollama.com/library/llama3.2)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/TamerOnLine/interactive_llama_chat.git
   cd interactive_llama_chat
   ```

2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   python src/main.py
   ```

---

## Usage
1. Open the application in your web browser (default URL: `http://localhost:8501`).
2. Enter your message in the text input field and submit.
3. View the response from the Llama server in real time.

---

## Configuration
- **Llama Server URL**: The URL is defined in `src/ollama.py` under the variable `url`. Update it to point to your Llama server if needed.

---

## Dependencies
- **Streamlit**: For building the web interface.
- **Requests**: For making HTTP requests to the Llama server.

---

## Contribution
Contributions are welcome! Please follow these steps:
1. Fork the repository.
2. Create a feature branch.
3. Submit a pull request.

---

## License
This project is licensed under the [MIT License](https://github.com/TamerOnLine/Interactive_Llama_Chat/blob/main/LICENSE
).

---

## Acknowledgments
Special thanks to the creators of Streamlit and the Llama model for making this project possible.
