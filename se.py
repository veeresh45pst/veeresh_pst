from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests

API_URL = "http://127.0.0.1:8000/todos"

def test_add_task():
    # Set up the WebDriver (make sure to specify the path to your WebDriver)
    driver = webdriver.Chrome()
    
    try:
        # Open the HTML interface
        driver.get("http://127.0.0.1:5500/index.html")

        # Add a task
        task_title = "Test Task"
        driver.find_element(By.ID, 'task-title').send_keys(task_title)
        driver.find_element(By.ID, 'add-task').click()

        # Wait for a moment to ensure the task is added
        time.sleep(2)

        # Prepare the task data for the POST request
        task_data = {
            "title": task_title,
            "description": "",
            "completed": False
        }
        print("Sending task data:", task_data)

        # Send a POST request to add the task
        post_response = requests.post(API_URL, json=task_data)
        print("POST response status code:", post_response.status_code)
        print("POST response body:", post_response.json())

        # Use GET to retrieve tasks
        get_response = requests.get(API_URL)
        print("GET response status code:", get_response.status_code)
        tasks = get_response.json()  
        print("Retrieved tasks:", tasks)

        # Check if the task was added
        assert any(task['title'] == task_title for task in tasks), "Task was not added successfully."
        
    finally:
        # Close the WebDriver
        driver.quit()

def test_update_task(task_id, new_title):
    # First, retrieve the current task to confirm it exists
    get_response = requests.get(API_URL)
    current_tasks = get_response.json()
    print("Current tasks before update:", current_tasks)

    # Update a task
    update_data = {
        "title": new_title,
        "description": "",
        "completed": False
    }
    update_response = requests.put(f"{API_URL}/{task_id}", json=update_data)
    print("PUT response status code:", update_response.status_code)
    print("PUT response body:", update_response.json())

    # Use GET to retrieve the updated tasks
    get_response = requests.get(API_URL)
    updated_tasks = get_response.json()
    print("Updated tasks:", updated_tasks)

    # Check if the update was successful
    if not any(task['title'] == new_title for task in updated_tasks):
        print(f"Update failed for task ID {task_id}. Expected title: '{new_title}'")
        print("Available titles after update:", [task['title'] for task in updated_tasks])

    assert any(task['title'] == new_title for task in updated_tasks)
    print("Update verified successfully.")

def test_delete_task(task_id):
    # Delete a task
    delete_response = requests.delete(f"{API_URL}/{task_id}")
    print("DELETE response status code:", delete_response.status_code)
    print("DELETE response body:", delete_response.json())

    # Verify the deletion
    get_response = requests.get(API_URL)
    remaining_tasks = get_response.json()
    assert not any(task['id'] == task_id for task in remaining_tasks)

# Call the test functions
test_add_task()

task_id = "1dff79a0-47c7-48c7-b176-e8d399a6ced6"  # Replace with the actual task ID returned from the add task operation
test_update_task(task_id=task_id, new_title="Test Task")
test_delete_task(task_id="1dff79a0-47c7-48c7-b176-e8d399a6ced6")