from fastapi import APIRouter, HTTPException
from typing import Optional, List
from app.models.todoModel import TodoModel
from app.services.todoService import (fetch_all_todos, create_todo, update_todo, fetch_one_todo, remove_todo)
router = APIRouter()

@router.get('/')
async def get_todo():
    response = await fetch_all_todos()
    return response

@router.post("/", response_model=TodoModel)
async def post_todo(todo: TodoModel):
    response = await create_todo(todo.dict())
    if response:
        return response
    raise HTTPException(400, "Something went wrong")


@router.put("/{title}/", response_model=TodoModel)
async def put_todo(title: str, desc: str):
    response = await update_todo(title, desc)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@router.get("/{title}", response_model=TodoModel)
async def get_todo_by_title(title):
    response = await fetch_one_todo(title)
    if response:
        return response
    raise HTTPException(404, f"There is no todo with the title {title}")


@router.delete("/{title}")
async def delete_todo(title):
    response = await remove_todo(title)
    if response:
        return "Successfully deleted todo"
    raise HTTPException(404, f"There is no todo with the title {title}")