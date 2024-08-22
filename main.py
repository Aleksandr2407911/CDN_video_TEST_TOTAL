from fastapi import FastAPI
from src.handler.user_handler import user_router

# Creating the Fast_API of the application
app = FastAPI()
app.include_router(user_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

