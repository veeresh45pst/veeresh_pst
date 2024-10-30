# FastAPI To-Do Application

This is a simple RESTful API built with FastAPI to manage a To-Do list. The application includes basic CRUD (Create, Read, Update, Delete) operations and demonstrates data validation, error handling, and testing.

## Features

- **Create** a new To-Do item.
- **List** all To-Do items.
- **Update** an existing To-Do item.
- **Delete** a To-Do item.
- Includes **validation** for task creation with FastAPI and **unit tests** with `pytest`.

## Requirements

- Python 3.8 or higher
- FastAPI
- Uvicorn (for running the FastAPI application)
- Pytest (for running tests)
- Requests (for making API requests in tests)

## Setup and Installation
**Start the FastAPI application:**
uvicorn main:app --reload
The API will be available at http://127.0.0.1:8000.

API Endpoints
GET /todos: Retrieves all To-Do items.
POST /todos: Creates a new To-Do item.
PUT /todos/{todo_id}: Updates an existing To-Do item by ID.
DELETE /todos/{todo_id}: Deletes a To-Do item by ID.
Running Tests
To run tests, first start the server and then execute the following command:

**To test the main file**
pytest test_main.py
This will run the defined tests, validating different task names and expected status codes.

Test Cases:
**The test cases cover various scenarios:**

1.Valid task name (expecting 200 status code).
2.Empty task name (expecting 400 status code).
3.Task name with special characters (expecting 201 status code).
4.Whitespace-only task name (expecting 400 status code).
5.Very long task name (expecting 201 status code).
6.Task name with a newline character (expecting 400 status code).

**Folder Structure**
├── main.py            # Main FastAPI application file
├── test_main.py       # Test file for API endpoints
├── requirements.txt   # Python dependencies
└── README.md          # Project documentation
