
#CRUD OPERATIONS
#1) CREATE  (INSERTING DATA INTO THE TABLE)

from database import connection, cursor

airport_id=int(input("Enter the airport id: "))
name=input("Enter the airport name: ")
code=input("Enter the airport code: ")
city=input("Enter the airport city: ")

cursor.execute("""
INSERT INTO airport(airport_id,name,code,city)
VALUES (%s,%s,%s,%s)
""",(airport_id,name,code,city))
connection.commit()
print("DATA ADDED SUCCESSFULLY")