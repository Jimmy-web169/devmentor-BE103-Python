from sqlalchemy.orm import Session

from database.post import Post
from schema.database.post import PostCreate, PostUpdate
import repository.post


def lists(db: Session, skip: int = 0, limit: int = 100):
    return repository.post.lists(db, skip=skip, limit=limit)


def create(db: Session, post: PostCreate):
    return repository.post.create(db=db, post=post)

def get(db: Session, post_id: int):
    return repository.post.get(db=db, post_id=post_id)

def update(db: Session, post_id: int, post: PostUpdate):
    return repository.post.update(db=db, post_id=post_id, post=post)