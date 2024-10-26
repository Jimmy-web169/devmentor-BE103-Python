from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import service.post
import service.student
from infrastructure.mysql import get_db
from schema.database.post import PostCreate, PostUpdate
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

@router.get("/{post_id}")
def get_post(post_id: int, db: Session = Depends(get_db)):
    post = service.post.get(db, post_id=post_id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}")
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    updated_post = service.post.update(db=db, post_id=post_id, post=post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post
