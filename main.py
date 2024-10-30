# from fastapi import FastAPI
# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def first_example():
# # '''
# # 	FG Example First Fast API Example 
# # '''
# 	return {"GFG Example": "FastAPI"}


from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from uuid import uuid4

app = FastAPI()

# Sample database in memory
todos = {}

# Data model for a To-Do item
class TodoItem(BaseModel):
    id: str = None
    title: str
    description: str
    completed: bool = False

# Route to list all tasks
@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return list(todos.values())

# Route to create a new task
@app.post("/todos", response_model=TodoItem)
def create_todo(todo: TodoItem):
    todo.id = str(uuid4())  # Generate unique ID
    if todo.title != "":

        todos[todo.id] = todo
        return todo
    else :
        raise HTTPException(status_code=400, detail="Invalid request")

# Route to update an existing task
@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: str, updated_todo: TodoItem):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    updated_todo.id = todo_id
    todos[todo_id] = updated_todo
    return updated_todo

# Route to delete a task
@app.delete("/todos/{todo_id}", response_model=dict)
def delete_todo(todo_id: str):
    if todo_id not in todos:
        raise HTTPException(status_code=404, detail="Todo not found")
    del todos[todo_id]
    return {"message": "Todo deleted successfully"}




