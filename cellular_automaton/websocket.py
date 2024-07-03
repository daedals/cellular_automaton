from fastapi import APIRouter, WebSocket
from .canvas import Canvas

router = APIRouter()
canvas = Canvas()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_json()
        if data["action"] == "draw":
            x, y, color = data["x"], data["y"], data["color"]
            canvas.draw(x, y, color)
        elif data["action"] == "get_canvas":
            await websocket.send_json({"canvas": canvas.get_canvas().tolist()})
