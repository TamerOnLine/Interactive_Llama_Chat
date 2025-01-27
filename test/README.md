# Test Suite for Interactive Llama Chat

This folder contains the test cases designed to ensure the functionality, reliability, and robustness of the `Interactive Llama Chat` application. The tests primarily validate the behavior of the API interaction and application logic.

---

## Test Files

- **`test_ollama.py`**
  - Verifies the functionality of the `get_response_from_llama` function in `ollama.py`.
  - Ensures that the API returns valid responses and handles errors gracefully.

---

## Setup Instructions

### Prerequisites

Ensure you have the following:

- Python 3.8 or later.
- All dependencies listed in `requirements.txt`.

### Running the Tests

1. Navigate to the root directory of the project:
   ```bash
   cd /path/to/project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Execute the tests using `pytest`:
   ```bash
   pytest tests/
   ```

   Replace `tests/` with the relative path to the `test` folder if required.

---

## Contributing

- Ensure new tests cover edge cases and error handling scenarios.
- Follow the existing test structure for consistency.
- Submit pull requests with detailed descriptions for any enhancements.

---

## Notes

- Use `mock` or similar libraries to simulate API responses for robust and isolated testing.
- Keep the tests updated with any changes to the core application logic.
