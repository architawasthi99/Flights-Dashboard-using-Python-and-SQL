import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

# Connect to the database server
try:
    connection = mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME")
    )
    cursor=connection.cursor()
    print("Connected to the database")
except:
    print("Error connecting to the database") 