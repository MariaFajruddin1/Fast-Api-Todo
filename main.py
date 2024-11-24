# main.py

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Todo

app: FastAPI = FastAPI()

# Dependency
@app.post("/todos")
async def create_todo(text: str, is_complete: bool = False):
    todo = Todo(text=text, is_done=is_complete)
    SessionLocal.add(todo)
    SessionLocal.commit()
    SessionLocal.refresh(todo)
    return {"todo added": todo.text}

@app.put("/todos/{todo_id}")
async def update_todo(
    id: int,
    text: str = "",
    is_complete: bool = False
):
    todo_query = SessionLocal.query(Todo).filter(Todo.id==id)
    todo = todo_query.first()
    if text:
        todo.text = text
    todo.is_done = is_complete
    SessionLocal.add(todo)
    SessionLocal.commit()
    return {'todo update': todo.text}

@app.delete("/todos/{todo_id}")
async def delete_todo(id: int):
    todo = SessionLocal.query(Todo).filter(Todo.id==id).first()
    SessionLocal.delete(todo)
    SessionLocal.commit()
    return {"todo deleted": todo.text}
