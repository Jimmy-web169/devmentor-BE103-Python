from pydantic import BaseModel


# 基礎的 Student 資料結構
class StudentBase(BaseModel):
    name: str
    age: int


# 用於創建新 Student 的資料結構
class StudentCreate(StudentBase):
    pass


class Student(StudentBase):
    id: int

    class Config:
        orm_mode = True
