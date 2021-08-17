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
   $ flask db migrate
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
    
12. DEPLOYMENT

    Follow the directions to install [the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)  :

   ```
   $ brew tap heroku/brew && brew install heroku

   ```

   This command runs two separate commands. The `&&` joins them into one convenient copy/paste-able unit.

   The first command `brew tap heroku/brew` tells Homebrew to add an additional source of software packages (termed a *tap* in Homebrew-speak). The second command `brew install heroku` uses Homebrew to install the Heroku CLI, which it will be able to find with the tap we just configured.

   ### **Log In to the Heroku CLI**

   The Heroku CLI needs to authenticate our user account. Follow the directions to [log into the Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#getting-started)  :

   ```
   $ heroku login

   ```

   We'll be prompted to press any key to go to a web browser to complete our login. The CLI will then log us in automatically.

   # **Configure Our Flask App for Heroku**

   Although Heroku will do a lot of the work of hosting, running, and maintaining our API server, we need to add a small amount of configuration to our project.

   ### **Check Dependencies for `gunicorn`**

   We will use a Python package named [gunicorn](https://pypi.org/project/gunicorn/)  to launch our Flask API on Heroku.

   `gunicorn` is capable of running Flask apps so that they can handle multiple simultaneous requests, which is very important for production web applications.

   We should confirm that the package `gunicorn` is in the project's `requirements.txt` file.

   If `gunicorn` does *not* appear in our `requirement.txt`, we can add it by installing it locally with:

   ```
   (venv) $ pip install gunicorn

   ```

   After it has installed, we can update our `requirements.txt` by running:

   ```
   (venv) $ pip freeze > requirements.txt

   ```

   Heroku makes use of our `requirements.txt` file to install our app dependencies, so it is very important to ensure that all of our dependencies are properly listed.

   If we needed to update our `requirements.txt`, we should be sure to add and commit this change.

   ### **Create a Procfile for Heroku**

   `[Procfile`](https://devcenter.heroku.com/articles/procfile)  is a file specifically used in codebases deployed on Heroku.

   We'll use our Procfile to define how to start our Flask web server.

   First, create a `Procfile` inside the project root. This file *must be named exactly `Procfile`, **with no file extension***.

   ```
   $ touch Procfile

   ```

   Then, fill the Procfile with this content:

   ```
   web: gunicorn 'app:create_app()'

   ```

   # **Commit**

   Save this file. Then, create a Git commit that contains this change.

   # **Create a Heroku App**

   For each project we deploy, we will need to create and manage a Heroku app. Our Heroku app will give us visibility, access, and tools to manage our deployed app.

   After `cd`ing to our project root, we can create a Heroku app using the Heroku CLI. From the command line we should pick **either** of these options:

   1. We can create a Heroku app with an automatically generated app name using:

   ```
   $ heroku create

   ```

   1. We can create our app with the name `your-app-name` using:

   ```
   $ heroku create your-app-name

   ```

   Replace `your-app-name` with the desired name of the app.

   Our Heroku app doesn't have access to our Flask API code yet, so we'll see a default Heroku message.

   ### **Our New Heroku App**

   We have officially created a Heroku app that is accessible online! We can follow the link from the `heroku create` output.

   ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/ebc0c97b-0da5-4559-aca8-5d615e7a42ad/Untitled.png)

   ### **Verify the New Heroku Remote**

   Creating a Heroku app will add a new Git remote to our project! A Git remote is a destination to which we can `git push`!

   The new Git remote will be named `heroku`. This Git remote points exactly to where Heroku keeps and serves our code!

   Confirm that we have a `heroku` remote by running this command:

   ```
   $ git remote -v

   ```

   We should see the `heroku` remote listed alongside our `origin` remote.

   ### **Verify in the Dashboard**

   Creating a Heroku app will associate this app to our Heroku account.

   Visit the Heroku dashboard and see your new app listed! We'll visit this dashboard whenever we need details about our Heroku app.

   ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/7cff8f3e-3146-4e5f-a36c-11d1e289b360/Untitled.png)

   # **Push Code to the Heroku Remote**

   We should send our project codebase to our `heroku` remote.

   This command will push our project's Git history to a remote named `heroku`. It will push the default `master` branch on our computer to Heroku's default `main` branch on our new Heroku virtual computer.

   ```
   $ git push heroku master:main

   ```

   Every time we want to push our Git history to our Heroku app, we will need to push to the `heroku` remote.

   # **Create a Database in Heroku**

   Now that we've created our Heroku app for the first time, we need to tell the app that we're interested in adding a Postgres database to our deployed Heroku app.

   This command uses the Heroku CLI to add a Postgres database to the app.

   ```
   $ heroku addons:create heroku-postgresql:hobby-dev

   ```

   ### **Verify in the Dashboard**

   We can verify that our Heroku app has added a Postgres database by checking the [Heroku dashboard](https://dashboard.heroku.com/)  .

   We can use the Heroku dashboard to view our Heroku app. In the "Overview" tab, in the "Installed add-ons" section, we should see "Heroku Postgres."

   ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/19acc83d-070a-4d35-9be4-34644d139415/Untitled.png)

   Alternatively, in the "Resources" tab, in the "Add-ons" section, we should see "Heroku Postgres."

   ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/669eb422-b1c6-4517-938a-f3766142f5d1/Untitled.png)

   # **Set Environment Variables in Heroku**

   Our current app sets the `SQLALCHEMY_DATABASE_URI` environment variable using our `.env` file. Our Flask code accesses this environment variable with the code `os.environ.get("SQLALCHEMY_DATABASE_URI")`.

   Instead of giving Heroku our `.env` file, we need to add our environment variables to Heroku using the Heroku dashboard.

   ### **Find the Database URL in Heroku**

   First, let's find the connection string that will connect to our Heroku database, instead of a local database.

   When we added the Postgres database add-on above, Heroku created this connection string.

   In the Heroku dashboard, in the "Settings" tab, there is a section titled "Config Vars."

   ![Untitled](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/71c40f36-c307-4b2a-9d57-12039277f804/Untitled.png)

   Once we locate this section, we should:

   1. Click "Reveal Config Vars"
   2. Find the automatically generated variable named "DATABASE_URL"
   3. Copy the value of this connection string

   # **Setup and Initialize the Database in Heroku**

   Now that our Flask app is on Heroku and can connect to a database, we need to initialize the database in Heroku once.

   We can run the following:

   ```
   $ heroku run flask db upgrade

   ```

   This will migrate the empty database in our remote Postgres connection to the latest schema configuration we have generated from our models.

   # **Verify**

   Our Flask project is on a Heroku machine, running, and connected to an initialized database. Now is the time to verify whether our API is accessible by web!

   As a convenient shortcut, the Heroku CLI gives us this command to automatically open our Heroku app in the browser:

   ```
   $ heroku open

   ```

   This command needs to be run inside of our project folder.

   ### **Use Postman**

   We can use Postman to make and verify all sorts of HTTP requests to our API!

   ### **Use Heroku Logs**

   During local development on our own machines, when we ran `$ flask run`, the server's logs were output into our terminal. We could see the details about every HTTP request our server received and every HTTP response it returned. We could also see output for any errors.

   We can access the server logs of our Heroku app from the Heroku dashboard by finding the "More" menu and selecting "View logs."
