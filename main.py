from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, schemas
import database

app = FastAPI()

# Dependency
def get_db():
	db = database.SessionLocal()
	try:
		yield db
	finally:
		db.close()

						# HANDLERS FOR MANIPULATING INTERNS

# handler for GET request to get list of interns
@app.get("/api/interns/")
def get_interns(db: Session = Depends(get_db)):
	interns = crud.get_interns(db)
	return interns 


# handler for POST to create a new intern
@app.post("/api/interns/", response_model=schemas.Intern)
def create_intern(new_intern: schemas.InternCreate, db: Session = Depends(get_db)):
	db_intern = crud.get_intern_by_email(db, email=new_intern.email)
	if db_intern:
		raise HTTPException(status_code=400, detail="Email already registered")
	return crud.create_intern(db=db, new_intern=new_intern)

# handler for PUT to update an intern
@app.put("/api/intern/{id}", response_model=schemas.Intern)
def update_intern(id: int, intern: schemas.InternCreate, db: Session = Depends(get_db)):
	return crud.update_intern(db=db, intern=intern, id=id)	

# handler for DELETE to delete an intern
@app.delete("/api/intern/{id}", response_model=schemas.Intern)
def del_intern(id: int, db: Session = Depends(get_db)):
	return crud.del_intern(db, intern_id=id)


						# HANDLERS FOR MANIPULATING ASSIGNMENTS

# handler for GET to get all assignments of specific intern
@app.get("/api/intern/{id}/assignments")
def get_intern_assignments(id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
	return crud.get_intern_assignments(db=db, id=id, skip=skip, limit=limit)

# handler for POST to create a new assignment
@app.post("/api/intern/{id}/new_assignment", response_model=schemas.Assignment)
def create_assignment(id: int, new_assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
	return crud.create_assignment(db=db, assignment=new_assignment, intern_id=id)

# handler for PUT to update an assignment
@app.put("/api/intern/{id}/assignment/{assignment_id}", response_model=schemas.Assignment)
def update_assignment(id: int, assignment_id: int, assignment: schemas.AssignmentCreate, db: Session = Depends(get_db)):
	return crud.update_assignment(assignment=assignment, db=db, id=id, assignment_id=assignment_id)	

# handler for DELETE to delete an assignment
@app.delete("/api/intern/{id}/assignment/{assignment_id}", response_model=schemas.Assignment)
def del_assignment(id: int, assignment_id: int, db: Session = Depends(get_db)):
	return crud.del_assignment(db, id=id, assignment_id=assignment_id)