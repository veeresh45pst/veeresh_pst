# def test_pass():
#     assert 1 + 1 == 2

# test_pass()    



# def test_fail():
#     assert 1 + 1 == 5

# test_fail()  




from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test creating a to-do item
def test_create_todo():
    response = client.post("/todos", json={"title": "Sample Todo", "description": "Sample description"})
    assert response.status_code == 200
    assert response.json()["title"] == "Sample Todo"

# Test retrieving all to-do items
def test_get_todos():
    response = client.get("/todos")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test updating a to-do item
def test_update_todo():
    # First, create a new todo
    response = client.post("/todos", json={"title": "Todo to Update", "description": "To be updated"})
    todo_id = response.json()["id"]

    # Now, update the created todo
    response = client.put(f"/todos/{todo_id}", json={"title": "Updated Todo", "description": "Updated description", "completed": True})
    assert response.status_code == 200
    assert response.json()["title"] == "Updated Todo"
    assert response.json()["completed"] is True

# Test deleting a to-do item
def test_delete_todo():
    # First, create a new todo
    response = client.post("/todos", json={"title": "Todo to Delete", "description": "To be deleted"})
    todo_id = response.json()["id"]

    # Now, delete the created todo
    response = client.delete(f"/todos/{todo_id}")
    assert response.status_code == 200
    assert response.json()["message"] == "Todo deleted successfully"