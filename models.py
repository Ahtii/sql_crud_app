from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# import database

# initializing base model
Base = declarative_base()

class Intern(Base):
	__tablename__ = "intern"

	id = Column(Integer, primary_key=True, index=True)
	name = Column(String(50))
	email = Column(String(50), unique=True, index=True)
	hashed_password = Column(String(500))
	is_active = Column(Boolean, default=True)
	qualification = Column(String(100))

	assignment = relationship("Assignment", back_populates="owner")


class Assignment(Base):
	__tablename__ = "assignment"

	id = Column(Integer, primary_key=True, index=True)
	title = Column(String(100))
	assigned_by = Column(String(50))
	completed = Column(Boolean, default=False)	

	owner_id = Column(Integer, ForeignKey("intern.id"))

	owner = relationship("Intern", back_populates="assignment")


