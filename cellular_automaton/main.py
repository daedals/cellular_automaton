from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .canvas import Canvas

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

canvas = Canvas(1500,600)

@app.get("/")
async def get():
    return HTMLResponse(open("static/index.html").read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        if data["action"] == "draw":
            x, y, color = data["x"], data["y"], data["color"]
            canvas.draw(x, y, color)
        elif data["action"] == "get_canvas":
            await websocket.send_json({"canvas": canvas.get_canvas().tolist()})
