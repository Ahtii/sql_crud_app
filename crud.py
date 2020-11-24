from sqlalchemy.orm import Session
import models, schemas

# function to get a specific intern by id from the database
def get_intern(db: Session, intern_id: int):
	return db.query(models.Intern).filter(models.Intern.id == intern_id).first()


# funtion to get a specific intern by email from the database
def get_intern_by_email(db: Session, email: str):
	return db.query(models.Intern).filter(models.Intern.email == email).first()

# funtion to get interns in range
def get_interns(db: Session):
	return db.query(models.Intern).all()


# function to create an new intern
def create_intern(db: Session, new_intern: schemas.InternCreate):
	fake_hashed_password = "notreallyhashed"
	db_intern = models.Intern(name=new_intern.name, email=new_intern.email, hashed_password=fake_hashed_password)
	db.add(db_intern)
	db.commit()
	db.refresh(db_intern)
	return db_intern

# function to update an intern
def update_intern(db: Session, intern: schemas.InternCreate, id: int):	
	db_intern = db.query(models.Intern).filter(models.Intern.id==id).first()
	db_intern.name = intern.name
	db_intern.email = intern.email
	db.commit()	
	return db_intern

# function to del an intern
def del_intern(db: Session, intern_id: int):
	db_intern = db.query(models.Intern).filter(models.Intern.id==intern_id).first()
	db.delete(db_intern)
	db.commit()
	return db_intern		

# function to get all assignments of intern
def get_intern_assignments(db: Session, id: int, skip: int = 0, limit: int = 100):
	return db.query(models.Assignment).filter(models.Assignment.owner_id==id).offset(skip).limit(limit).all()

# function to create a new assignment
def create_assignment(intern_id: int, assignment: schemas.AssignmentCreate, db: Session):
	param = assignment.dict()
	param.update({'owner_id': intern_id})	
	db_assignment = models.Assignment(**param)
	db.add(db_assignment)
	db.commit()
	db.refresh(db_assignment)
	return db_assignment

def update_assignment(assignment: schemas.AssignmentCreate, db: Session, id: int, assignment_id: int):
	db_assignment = db.query(models.Assignment).filter((models.Assignment.owner_id==id) & (models.Assignment.id==assignment_id)).first()
	db_assignment.title = assignment.title
	db_assignment.assigned_by = assignment.assigned_by
	db.commit()
	return db_assignment

# function to delete an assignment
def del_assignment(db: Session, id: int, assignment_id: int):
	db_assignment = db.query(models.Assignment).filter(models.Assignment.id==assignment_id and models.Assignment.owner_id==id).first()
	db.delete(db_assignment)
	db.commit()
	return db_assignment

