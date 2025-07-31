
import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

mydb = None
mycursor = None

def get_connection():
    global mydb
    if mydb is None:
        mydb = mysql.connector.connect(

            host = os.getenv("HOST"),
            user = os.getenv("USER"),
            password = os.getenv("PASSWORD"),
            database = os.getenv("DATABASE")
        )
    return mydb

def get_cursor():
    global mycursor
    if mycursor is None:
     mycursor = get_connection().cursor()
    return mycursor
