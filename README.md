# sql_crud_app

**Required:**

You must have mysql already installed and setup with user and database created if you haven't just follow the instructions: 
https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing

**How to run:**

Step 1: Open `database.py` file and populate the DB credentials with your database credentials and the database name

Step 2: Activate your virtual environment and install all the required dependecies with:

        pip install -r requirements.txt
  
Step 2: Go inside the project directory and run the server with:
        
        uvicorn main:app --reload
        
Step 3: Go to ***localhost:8000/docs*** to do crud operations with mysql.

Happy coding. :)
