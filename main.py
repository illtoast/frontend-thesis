from fastapi import FastAPI, Form, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.responses import HTMLResponse ,FileResponse
import os
import crud
import models
import schemas
from database import SessionLocal, engine


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

@app.get("/logout.html")
async def readroot():
    # Get the directory of the current script
    current_directory = os.path.dirname(__file__)
    # Construct the full path to the HTML file
    file_path = os.path.join(current_directory, "logout.html")

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

# API
models.Base.metadata.create_all(bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
        
# @app.post("/students/", response_model=schemas.Student)
# def create_student(student: schemas.StudentCreate, db: Session = Depends(get_db)):
#     return crud.create_student(db=db, student=student)

@app.post("/students/", response_model=schemas.Student)
def create_student(first_name: str = Form(...), last_name: str = Form(...), 
    student_id: str = Form(...), section: str = Form(...), course: str = Form(...),
    year_level: str = Form(...), gender: str = Form(...),
    db: Session = Depends(get_db)):
    student = schemas.StudentCreate(student_id=student_id, first_name=first_name,
        last_name=last_name, section=section, year_level=year_level, course=course,
        gender=gender)
    return crud.create_student(db=db, student=student)

@app.get("/students/{item_id}", response_model=schemas.Student)
def read_item(student_id: str, db: Session = Depends(get_db)):
    db_student = crud.get_student(db, student_id=student_id)
    if db_student is None:
        raise HTTPException(status_code=404, detail="Student not found")
    return db_student




@app.get("/students/", response_model=list[schemas.Student])
def read_students(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    students = crud.get_students(db, skip=skip, limit=limit)
    return students  
        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)