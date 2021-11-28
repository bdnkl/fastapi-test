import io

from fastapi import FastAPI
from fastapi.responses import Response, StreamingResponse
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from uvicorn import Server, Config
import matplotlib.pyplot as plt


app = FastAPI()

@app.get('/')
async def get_plot():
    fig = Figure(figsize=(4.5, 6))
    ax = fig.subplots()
    ax.plot([1, 2, 3], [2, 3, 4])


    with io.BytesIO() as pseudo_file:
        FigureCanvas(fig).print_png(pseudo_file)
        content = pseudo_file.getvalue()

    return Response(content, media_type="image/png")


if __name__ == '__main__':
    config = Config(app, timeout_keep_alive=1, hostname='0.0.0.0', port=5000)
    server = Server(config)
    server.run()
