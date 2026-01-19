import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vino@123",
    database="flight_analytics"
)

cursor = db.cursor()

aircraft_data = [
    ("VT-ABC", "Airbus A320"),
    ("VT-DEF", "Boeing 737"),
    ("VT-GHI", "Airbus A321"),
    ("VT-JKL", "Boeing 787"),
    ("VT-MNO", "Airbus A350")
]

insert_query = """
INSERT IGNORE INTO aircraft (registration, model)
VALUES (%s, %s)
"""

for aircraft in aircraft_data:
    cursor.execute(insert_query, aircraft)

db.commit()
cursor.close()
db.close()

print("Aircraft inserted successfully")
