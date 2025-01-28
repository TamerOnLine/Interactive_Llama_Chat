# Interactive Llama Chat

Interactive Llama Chat is a Python-based application that facilitates communication with the Llama model through a streamlined Streamlit interface. It enables users to send messages to the Llama server and receive responses in real time via REST APIs.

---

## Features

- **Intuitive Interface**: Built with Streamlit for easy interaction.
- **Seamless Integration**: Communicates with Llama server using RESTful APIs.
- **Modular Design**: Structured for straightforward customization and scalability.

---

## Installation Guide

### Requirements

Ensure you have the following installed:

- Python 3.8 or later
- pip
- [Ollama](https://www.ollama.com/download)
- [Llama3.2 Model](https://www.ollama.com/library/llama3.2)

### Setup Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/TamerOnLine/interactive_llama_chat.git
   cd interactive_llama_chat
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # For Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Start the Ollama server:
   - Open your terminal.
   - Navigate to the folder where Ollama is installed.
   - Run the following command:
     ```bash
     ollama start
     ```
5. Launch the application:
   ```bash
   streamlit run main.py
   ```

---

## Usage Instructions

1. Open the application in your browser (default URL: `http://localhost:8501`).
2. Input your message and submit it.
3. View the real-time response from the Llama model.

---

## Project Structure

```plaintext
project-directory/
├── requirements.txt
└── src/
    ├── chat_interface.py  # Streamlit app logic
    ├── main.py            # Application entry point
    └── ollama.py          # Handles Llama server communication
```

---

## Configuration

- Modify the Llama server URL in `src/ollama.py` if needed.

---

## Contributions

We welcome contributions to enhance the project:

- Fork the repository.
- Create a feature branch.
- Submit a pull request.

---

## License

This project is distributed under the [MIT License](https://github.com/TamerOnLine/Interactive_Llama_Chat/blob/main/LICENSE).

---

## Credits

Thanks to the teams behind Streamlit and the Llama model for their tools and resources.

## Future Enhancements

We are considering the following enhancements to improve the project:

1. **Comprehensive Testing**:
   - Add tests to cover edge cases such as invalid input and server unavailability.
   - Ensure the project is stable under different scenarios.

2. **Settings Management**:
   - Use `.env` files for managing configuration, such as server URL, model name, etc., for better flexibility.

3. **Improved Documentation**:
   - Add detailed comments to the code for better readability and understanding.
   - Enhance README.md with example use cases and troubleshooting tips.

4. **Interface Customization**:
   - Add options in the Streamlit interface to customize model settings (e.g., model name, number of responses).
   - Allow users to upload configurations directly.

5. **Performance Optimization**:
   - Explore using `asyncio` or other libraries to handle high traffic efficiently.


