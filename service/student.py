from sqlalchemy.orm import Session
import repository.student  
from schema.database.student import StudentCreate


def lists(db: Session, skip: int = 0, limit: int = 100):
    return repository.student.lists(db, skip=skip, limit=limit)


def create(db: Session, student: StudentCreate):
    return repository.student.create(db=db, student=student)
