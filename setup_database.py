from database import connection, cursor

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
print("Initial airport data added successfully")