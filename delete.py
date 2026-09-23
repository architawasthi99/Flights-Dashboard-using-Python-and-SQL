#BASIC DELETE OPERATION
from database import connection, cursor

cursor.execute("""
  DELETE FROM airport
  WHERE airport_id=12
""")
connection.commit()
print("Airport deleted successfully")

#LET USER CHOSE THE AIRPORT ID TO DELETE
airport_id=int(input("Enter the airport id to delete: "))
cursor.execute("""
   DELETE FROM airport
   WHERE airport_id=%s
""",(airport_id,))

connection.commit()
print("Airport deleted successfully")

## DELETE THROUGH WEB APPLICATION FASTAPI
from fastapi import FastAPI
app=FastAPI()

@app.delete("/airports/{airport_id}")
def delete_airport(airport_id:int):
    cursor.execute("""
    DELETE FROM airport
    WHERE airport_id=%s
    """,(airport_id,))
    connection.commit()
    return {"message": "Airport deleted successfully"}