from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from .websocket import router as websocket_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(websocket_router)

@app.get("/")
def read_root():
    """  read_root """
    return {"message": "Welcome to the Falling Sands Simulation!"}
