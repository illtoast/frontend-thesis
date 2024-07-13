from pydantic import BaseModel

class StudentBase(BaseModel):
    student_id :str
    first_name: str
    last_name: str
    course:str
    year_level:str
    section:str
    gender:str

class StudentCreate(StudentBase):
    pass

class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
