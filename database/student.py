from sqlalchemy import Boolean, Column, Integer, String

from infrastructure.mysql import Base



class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(255), nullable=False, index=True)
    age = Column(Integer, nullable=False)
