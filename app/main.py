from typing import Optional
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.controllers.todoController import router as todo

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo, tags=["TODO"], prefix='/api/todo')

@app.get("/api/healthz")
def root():
    return {"message": "Welcome to FastAPI with MongoDB"}