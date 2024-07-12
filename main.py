from fastapi import FastAPI
from fastapi.responses import HTMLResponse ,FileResponse
import os

app = FastAPI()

@app.get("/")
async def readroot():
    # Get the directory of the current script
    current_directory = os.path.dirname(__file__)
    # Construct the full path to the HTML file
    file_path = os.path.join(current_directory, "index.html")

    # Read the HTML file content
    with open(file_path, "r") as file:
        html_content = file.read()

    return HTMLResponse(content=html_content)

@app.get("/index.js", include_in_schema=False)
def get_bg_tile():
    """
    Serve the tiled background
    """
    return FileResponse("index.js")

@app.get("/style.css", include_in_schema=False)
def get_bg_tile():
    """
    Serve the tiled background
    """
    return FileResponse("style.css")
@app.get("/event.css", include_in_schema=False)
def get_bg_tile():
    """
    Serve the tiled background
    """
    return FileResponse("event.css")
@app.get("/register.css", include_in_schema=False)
def get_bg_tile():
    """
    Serve the tiled background
    """
    return FileResponse("register.css")
@app.get("/login.css", include_in_schema=False)
def get_bg_tile():
    """
    Serve the tiled background
    """
    return FileResponse("login.css")

@app.get("/login.html")
async def readroot():
    # Get the directory of the current script
    current_directory = os.path.dirname(__file__)
    # Construct the full path to the HTML file
    file_path = os.path.join(current_directory, "login.html")

    # Read the HTML file content
    with open(file_path, "r") as file:
        html_content = file.read()

   
    return HTMLResponse(content=html_content)

@app.get("/index.html")
async def readroot():
    # Get the directory of the current script
    current_directory = os.path.dirname(__file__)
    # Construct the full path to the HTML file
    file_path = os.path.join(current_directory, "index.html")

    # Read the HTML file content
    with open(file_path, "r") as file:
        html_content = file.read()

   
    return HTMLResponse(content=html_content)

@app.get("/create_event.html")
async def readroot():
    # Get the directory of the current script
    current_directory = os.path.dirname(__file__)
    # Construct the full path to the HTML file
    file_path = os.path.join(current_directory, "create_event.html")

    # Read the HTML file content
    with open(file_path, "r") as file:
        html_content = file.read()

    return HTMLResponse(content=html_content)

@app.get("/register.html")
async def readroot():
    # Get the directory of the current script
    current_directory = os.path.dirname(__file__)
    # Construct the full path to the HTML file
    file_path = os.path.join(current_directory, "register.html")

    # Read the HTML file content
    with open(file_path, "r") as file:
        html_content = file.read()

    return HTMLResponse(content=html_content)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)