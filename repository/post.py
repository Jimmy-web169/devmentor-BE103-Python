from sqlalchemy.orm import Session

from database.post import Post
from schema.database.post import PostCreate, PostUpdate


def lists(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Post).offset(skip).limit(limit).all()


def create(db: Session, post: PostCreate):
    db_user = Post(title=post.title, content=post.content)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()

def update(db: Session, post_id: int, post: PostUpdate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        for var, value in vars(post).items():
            setattr(db_post, var, value) if value else None
        db.add(db_post)
        db.commit()
        db.refresh(db_post)
        return db_post