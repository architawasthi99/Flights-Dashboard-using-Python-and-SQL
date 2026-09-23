from database import connection, cursor

cursor.execute("SELECT * FROM airport")
airports=cursor.fetchall()

for airport in airports:
    print(f"Airport ID: {airport[0]}, Name: {airport[1]}, Code: {airport[2]}, City: {airport[3]}")