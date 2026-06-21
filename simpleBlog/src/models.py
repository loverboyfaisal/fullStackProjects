from src import mysql_connection
from flask_login import UserMixin


# This class which get data from mysql database 
class User(UserMixin):
    def __init__(self,user_id,user_name,user_email,user_password):
        self.id = user_id
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password
    @staticmethod
    def get(user_id :int):
        db = mysql_connection()
        curr = db.cursor(dictionary=True,buffered=True)

        curr.execute("select * from users where id = %s;",(user_id,))
        row = curr.fetchone()

        curr.close()
        db.close()

        if row:
            return User(
                row.get("id"), 
                row.get("user_name"), 
                row.get("user_email"), 
                row.get("user_password_hash")
            )
        
        return None
    @staticmethod
    def get_by_email(user_email :int):
        db = mysql_connection()
        curr = db.cursor(dictionary=True,buffered=True)

        curr.execute("select * from users where user_email = %s;",(user_email,))
        row = curr.fetchone()

        curr.close()
        db.close()

        if row:
            return User(
            row.get("id"), 
            row.get("user_name"), 
            row.get("user_email"), 
            row.get("user_password_hash")
            )

        return None
    


def create_blog_db():
    db = mysql_connection()
    curr = db.cursor()
    
    query = "create database if not exists blog;"
    curr.execute(query)

    curr.close()
    db.close()


def create_users_table():
    db = mysql_connection()
    curr = db.cursor()
    
    query = "create table if not exists users (id int primary key auto_increment unique,user_name varchar(255),user_email varchar(255),user_password_hash varchar(255));"
    curr.execute(query)

    curr.close()
    db.close()


def create_user(user_name,user_email,password):
    db = mysql_connection()
    curr = db.cursor()

    query = "insert into users (user_name,user_email,user_password_hash) values (%s,%s,%s)"
    curr.execute(query,(user_name,user_email,password))
    db.commit()
    curr.close()
    db.close()






