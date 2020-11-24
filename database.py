from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = "root"           # your db username
DB_PASSWORD = "ahtisham"   # your db password
DB = "applied_informatics"  # your database name

# connecting to mysql database
SQLALCHEMY_DATABASE_URL = "mysql+mysqlconnector://"+DB_USER+":"+DB_PASSWORD+"@localhost/"+DB

# creating a connection between database and sqlalchemy
engine = create_engine(
	SQLALCHEMY_DATABASE_URL
)

# create a database session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

