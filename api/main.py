from fastapi import FastAPI
from api.models import Todo

app = FastAPI()
todos = []

# Get the home page
@app.get("/")
async def home():
    return{"msg":"Hello"}

# Fetch all the todos
@app.get("/todos")
async def get_todos():
    return{"todos": todos}

# Fetch Particular todo
@app.get("/todos/{todo_id}")
async def get_one_todo(todo_id:int):
    for todo in todos:
        if todo.id == todo_id:
            return{"todo": todo}     
    return{"message":"No todo found"}

# Create Todos
@app.post("/todos")
async def create_todos(todo: Todo):
    todos.append(todo)
    return{"Success": "Todo Has Been Added"}

# Delete Todos
@app.delete("/todos/{todo_id}")
async def delete_todo(todo: Todo):
    todos.remove(todo)
    return{"message": "Todo is deleted"}
# Update the data
@app.put("/todos/{todo_id}")
async def update_todo(todo_id:int, todo_obj: Todo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return{"message":"Todo is updated"}

