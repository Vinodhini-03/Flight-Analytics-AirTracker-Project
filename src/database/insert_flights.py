import mysql.connector
from datetime import datetime, timedelta
import random

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vino@123",
    database="flight_analytics"
)

cursor = db.cursor()

airports = [
    "DEL", "BOM", "BLR", "MAA", "HYD", "CCU", "COK",
    "LHR", "JFK", "LAX", "DXB", "SIN", "CDG", "FRA", "HND"
]

airlines = [
    "Air India", "IndiGo", "Emirates",
    "British Airways", "Lufthansa",
    "Singapore Airlines", "American Airlines"
]

statuses = ["On Time", "Delayed", "Cancelled"]

# fetch aircraft ids
cursor.execute("SELECT aircraft_id FROM aircraft")
aircraft_ids = [row[0] for row in cursor.fetchall()]

insert_query = """
INSERT INTO flights
(flight_number, airline, departure_airport, arrival_airport,
 aircraft_id, departure_time, arrival_time, status)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

now = datetime.now()

for _ in range(80):
    dep, arr = random.sample(airports, 2)

    dep_time = now - timedelta(hours=random.randint(1, 72))
    arr_time = dep_time + timedelta(hours=random.randint(2, 10))

    values = (
        f"{random.choice(['AI','6E','EK','BA','LH'])}{random.randint(100,999)}",
        random.choice(airlines),
        dep,
        arr,
        random.choice(aircraft_ids),
        dep_time,
        arr_time,
        random.choice(statuses)
    )

    cursor.execute(insert_query, values)

db.commit()
cursor.close()
db.close()

print("Flights inserted successfully")
