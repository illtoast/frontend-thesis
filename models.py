from sqlalchemy import Column, Integer, String, Date, DateTime
from database import Base

class Students(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(String, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    course = Column(String)
    year_level = Column(String)
    section = Column(String)
    gender = Column(String)

class Events(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String, index=True)
    event_date = Column(Date, index=True)

class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    event_id = Column(Integer)
    student_id = Column(String)
    barcode_in = Column(DateTime)
    barcode_out = Column(DateTime)
    sensor_in = Column(DateTime)
    sensor_in = Column(DateTime)
    
