from sqlalchemy.orm import Session
import models
import schemas

def get_student(db: Session, student_id: str):
    return db.query(models.Students).filter(models.Students.id == student_id).first()

def get_students(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Students).offset(skip).limit(limit).all()

def create_student(db: Session, student: schemas.StudentCreate):
    db_student = models.Students(**student.dict())
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
