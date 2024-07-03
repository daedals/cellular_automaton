from fastapi import APIRouter, WebSocket
from .simulation import Simulation

router = APIRouter()

simulation = Simulation()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    """ websocket endpoint """
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        result = simulation.update(data)
        await websocket.send_text(result)
