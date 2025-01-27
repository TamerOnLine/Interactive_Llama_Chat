import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))


import pytest
from ollama import get_response_from_llama

def test_get_response_from_llama_valid_input():
    input_message = "Hello, how are you?"
    response = get_response_from_llama(input_message)
    assert isinstance(response, dict), "Response should be a dictionary"
    assert 'choices' in response, "Response should contain 'choices' key"
