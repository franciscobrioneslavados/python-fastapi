from fastapi import FastAPI

from app.routes.user_routes import router as UserRouter

app = FastAPI(
    title="REST API with FastAPI and MongoDB",
    description="this is a simple REST API using fastapi and moongodb",
    version="0.0.1"
)

app.include_router(UserRouter, prefix="/api/users", tags=["Users"])

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001, log_level="debug")