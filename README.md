# DineMine_Backend
DineMine capstone backend 

DineMine_Backend supports the CRUD routes for the Web-app

### ERD - ENTITY RELATIONSHIP DIAGRAM

<img width="790" alt="Screen Shot 2021-08-17 at 2 56 44 PM" src="https://user-images.githubusercontent.com/68921168/129805992-756715f4-9b6c-4771-a398-0fda8b8c5a19.png">


### CRUD ROUTES

<img width="1301" alt="Screen Shot 2021-08-17 at 2 53 49 PM" src="https://user-images.githubusercontent.com/68921168/129805705-3225a915-da4a-45b9-ba86-f7be132acbea.png">

### DEPENDENCIES
this app uses
1. Flask
2. Flask SQlAlchemy
3. Postgress db
4. Heroku


### SETUP

1. FORK AND CLONE THE REPO
   ```JSX
   git clone 'CLONED REPO CODE'
   ```
   
2. INSTALL FLASK
   
   ```JSX
   pip install flask
   ```
   Inside the Terminal enter your project root folder and run the following commands
   
3. ACTIVATE VIRTUAL ENVIRONMENT
   ```JSX
    $ python3 -m venv venv
    
    $ source venv/bin/activate
    
    (venv) $ # You're in activated virtual environment!
   ```
4. DOWNLOAD REQUIREMENTS
   
   ```JSX
   (venv) $ pip install -r requirements.txt
   ```

5. INSTALL FLASK-CORS

   ```JSX
   pip install flask-cors
   ```
   
6. INSTALL SQLALCHEMY

   ```JSX
   pip install sqlalchemy
   ```
7. IN THE POSTGRES -U PSQL
 
   ```JSX
   git clone 'CLONED REPO CODE'
   ```
8. Setting up development databases
  
   ```JSX
   git clone 'CLONED REPO CODE'
   ```
9. Run flask db init.
   
   ```JSX 
   flask db init
   ``` 
   
   After you make your first model, run the other commands 
   
   ```JSX 
   flask db migrate
   ```  
   and 
   
   ```JSX
   $ flask db upgrade
   ```

10. RUN FLASK

    ```$ flask run ``` and ```$ FLASK_ENV=development flask run ```
    
   
11. SETTING UP .ENV FILE 
    
    Create a file named .env.

    Create two environment variables that will hold your database URLs.

    SQLALCHEMY_DATABASE_URI to hold the path to your development database
    [OPTIONAL] SQLALCHEMY_TEST_DATABASE_URI to hold the path to your development database
    Your .env may look like this:
    
    ```JSX
    SQLALCHEMY_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/dinemine_backend_api_development
    SQLALCHEMY_TEST_DATABASE_URI=postgresql+psycopg2://postgres:postgres@localhost:5432/dinemine_backend_api_test
    ```
    
