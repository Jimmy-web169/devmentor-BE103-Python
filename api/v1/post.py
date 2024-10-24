from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

import service.post
import service.student
from infrastructure.mysql import get_db
from schema.database.post import PostCreate
from schema.database.student import StudentCreate
router = APIRouter(
    tags=["post"],
    prefix="/posts"
)


@router.get("/")
def list_post(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    posts = service.post.lists(db, skip=skip, limit=limit)
    return posts


@router.post("/")
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return service.post.create(db=db, post=post)


@router.get("/students")
def list_students(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    students = service.student.lists(db, skip=skip, limit=limit)
    return students


@router.post("/students")
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    return service.student.create(db=db, student=student)