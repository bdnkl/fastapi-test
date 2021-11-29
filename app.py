from fastapi import FastAPI
from fastapi.responses import Response, StreamingResponse
from uvicorn import Server, Config


app = FastAPI()

@app.get('/')
async def index():
    return "CI / CD Python FastAPI"


if __name__ == '__main__':
    config = Config(app, timeout_keep_alive=1, host='0.0.0.0', port=5000)
    server = Server(config)
    server.run()
