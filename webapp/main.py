from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

class ConnectionManager:
    def __init__(self):
        self.active_connections: dict[str, WebSocket] = {}    #Rewrite using dict, add 'username' to make sure no duplicate username

    async def connect(self, username: str, websocket: WebSocket):
        await websocket.accept()
        if username in self.active_connections:
            await websocket.send_text("Username already in use. Please refresh to choose a different username.")
            await websocket.close()
        else:
            self.active_connections[username] = websocket

    def disconnect(self, username: str):
        del self.active_connections[username]

    async def broadcast(self, message: str):
        for connection in self.active_connections.values():
            await connection.send_text(message)

manager = ConnectionManager()

# Mount the static directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve the index.html file at the root URL
@app.get("/")
async def get():
    return FileResponse('static/index.html')


@app.websocket("/ws/{username}")
async def websocket_endpoint(websocket: WebSocket, username: str):
    await manager.connect(username, websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client {username}: {data}")
    except WebSocketDisconnect:
        manager.disconnect(username)
        await manager.broadcast(f"Client {username} left the chat room")
