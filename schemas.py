from typing import List
from pydantic import BaseModel

# model for assignment

class AssignmentBase(BaseModel):
	title: str
	assigned_by: str
	completed: bool

class AssignmentCreate(AssignmentBase):
	pass

class Assignment(AssignmentBase):
	id: int
	owner_id: int

	class Config:
		orm_mode = True

# model for intern

class InternBase(BaseModel):
	name: str
	email: str

class InternCreate(InternBase):
	pass

class Intern(InternBase):
	id: int
	is_active: bool
	assignments: List[Assignment] = []

	class Config:
		orm_mode = True


