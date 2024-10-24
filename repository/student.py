from sqlalchemy.orm import Session

from database.student import Student  
from schema.database.student import StudentCreate  

def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Student).offset(skip).limit(limit).all()


def create(db: Session, student: StudentCreate):
    db_student = Student(name=student.name, age=student.age)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student
