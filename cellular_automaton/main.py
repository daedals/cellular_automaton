import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from .canvas import Canvas

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

canvas = Canvas(1200,500)
connected_clients = []

@app.get("/")
async def get():
    """ defines get request from root path """
    return HTMLResponse(open("static/index.html", "r", encoding="utf-8").read())

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """ awaits and handles responses from websocket """
    await websocket.accept()
    connected_clients.append(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            if data["action"] == "draw":
                x, y, color = data["x"], data["y"], data["color"]
                canvas.draw(x, y, color)
            elif data["action"] == "get_canvas":
                await websocket.send_json({"canvas": canvas.get_canvas().tolist()})
    except WebSocketDisconnect:
        connected_clients.remove(websocket)

async def broadcast_canvas_state():
    """ handles broadcasting the same canvas to every client """
    while True:
        canvas_state = {"canvas": canvas.get_canvas().tolist()}
        for client in connected_clients:
            await client.send_json(canvas_state)
        await asyncio.sleep(.1)

@app.on_event("startup")
async def startup_event():
    """ creates async task on startup """
    asyncio.create_task(broadcast_canvas_state())
