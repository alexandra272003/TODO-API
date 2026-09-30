from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Schema Definition ---
class Todo(BaseModel):
    id: int
    title: str
    description: str
    completed: bool = False

# --- In-Memory Storage ---
todos: list[dict] = []


# --- Health & Root Endpoints ---
@app.get("/")
def root():
    return {"message": "Welcome to the Todos API"}

@app.get("/ping")
def ping():
    return {"status": "ok"}


# --- Todo Endpoints ---

# 1. Fetch all todos
@app.get("/todos")
def get_todos():
    return todos


# 2. Fetch completed todos (MUST BE ABOVE /todos/{todo_id})
@app.get("/todos/completed")
def get_completed_todos():
    completed_list = [todo for todo in todos if todo.get("completed") is True]
    return completed_list


# 3. Create a todo
@app.post("/todos", response_model=None)
def create_todos(todo: Todo):
    # Check for duplicate ID
    if any(t["id"] == todo.id for t in todos):
        raise HTTPException(status_code=400, detail="Todo with this ID already exists")
    
    todo_dict = todo.model_dump()
    todos.append(todo_dict)
    return todo_dict


# 4. Fetch a specific todo by ID
@app.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")


# 5. Update a todo by ID
@app.put("/todos/{todo_id}")
def update_todos(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            todos[index] = updated_todo.model_dump()
            return todos[index]
    raise HTTPException(status_code=404, detail="Todo not found")


# 6. Delete a todo by ID
@app.delete("/todos/{todo_id}")
def delete_todos(todo_id: int):
    for index, todo in enumerate(todos):
        if todo["id"] == todo_id:
            deleted_todo = todos.pop(index)
            return {"message": "Todo deleted successfully", "todo": deleted_todo}
    raise HTTPException(status_code=404, detail="Todo not found")