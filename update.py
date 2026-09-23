#UPDATE THROUGH SQL/NORMAL PYTHON 
from database import connection, cursor

cursor.execute("""
UPDATE airport
SET city = 'BOMBAY'
WHERE airport_id = 2
""")
connection.commit()

print("Airport city updated successfully")


# UPDATE THEOUGH WEB APPLICATION

from fastapi import FastAPI
app = FastAPI()

@app.put("/airports/{airport_id}")
def update_airport(
    airport_id:int,
    name:str,
    code:str,
    city:str
):
    cursor.execute("""
    UPDATE airport
    SET name=%s, code=%s, city=%s
    WHERE airport_id=%s
    """,(name, code, city, airport_id)
)
    connection.commit()
    return {"message": "Airport updated successfully"}

   
