import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="swordfish1",
)

my_cursor = mydb.cursor() #robo that does command for you on the db

#my_cursor.execute("CREATE DATABASE our_users")

my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)