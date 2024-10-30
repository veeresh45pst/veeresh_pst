import pytest
import requests

# Example API endpoint for creating a task
API_URL = "http://127.0.0.1:8000/todos"

# Define the test cases with different input datasets
test_cases = [
    ("valid_task", 200),  # Valid task name
    ("", 400),             # Empty task name
    ("task_with_special_#@!", 201),  # Task name with special characters
    ("   ", 400),         # Whitespace only
    ("task_with_very_long_name_" + "x" * 255, 201),  # Very long task name
    ("task_with_newline\n", 400),  # Task name with newline
]

@pytest.mark.parametrize("task_name, expected_status", test_cases)
def test_create_task(task_name, expected_status):
    # Create the payload for the API request
    payload = {
        "id": None,
        "title": str,
        "description": str,
        "completed": False
    }
    
    # Make the API request
    response = requests.post(API_URL, json=payload)
    
    # Assert the response status code
    if expected_status == 200:
        assert response.status_code != 200  # Fail for 200
    else:
        assert response.status_code == 200  # Pass for 400 or other non-200