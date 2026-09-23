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


# Create a new database  on rhe db server if it doesn't exist  
cursor.execute("CREATE DATABASE IF NOT EXISTS indigo")
connection.commit() 

# Create a new table in the database if it doesn't exist
#table = airports and columns=id,name,code
cursor.execute("""
CREATE TABLE IF NOT EXISTS airport(
    airport_id INTEGER PRIMARY KEY,
    name VARCHAR(250) NOT NULL,
    code VARCHAR(10) NOT NULL,
    city VARCHAR(50) NOT NULL
)
""")
connection.commit()


#INSERTING DATA INTO THE TABLE
cursor.execute("""
INSERT IGNORE INTO airport (airport_id, name, code, city) VALUES
    (1, 'Indira Gandhi International Airport', 'DEL', 'Delhi'),
    (2, 'Chhatrapati Shivaji Maharaj International Airport', 'BOM', 'Mumbai'),
    (3, 'Kempegowda International Airport', 'BLR', 'Bengaluru'),
    (4, 'Chennai International Airport', 'MAA', 'Chennai'),
    (5, 'Rajiv Gandhi International Airport', 'HYD', 'Hyderabad'),
    (6, 'Netaji Subhas Chandra Bose International Airport', 'CCU', 'Kolkata'),
    (7, 'Sardar Vallabhbhai Patel International Airport', 'AMD', 'Ahmedabad'),
    (8, 'Cochin International Airport', 'COK', 'Kochi'),
    (9, 'Pune Airport', 'PNQ', 'Pune'),
    (10, 'Jaipur International Airport', 'JAI', 'Jaipur')
""")
connection.commit()


#CRUD OPERATIONS
#1) CREATE
cursor.execute("""
INSERT INTO airport(airport_id,name,code,city)
VALUES (%s,%s,%s,%s)
""",(11,"kanpur international airport","KNP","Kanpur"))
connection.commit()
print("DATA ADDED SUCCESSFULLY")