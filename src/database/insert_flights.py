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

insert_query = """
INSERT INTO flights
(departure_airport, arrival_airport, departure_time,
 arrival_time, airline, flight_number, status)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""

now = datetime.now()

for _ in range(80):  # enough for analytics
    dep, arr = random.sample(airports, 2)

    dep_time = now - timedelta(hours=random.randint(1, 72))
    arr_time = dep_time + timedelta(hours=random.randint(2, 10))

    values = (
        dep,
        arr,
        dep_time,
        arr_time,
        random.choice(airlines),
        f"{random.choice(['AI','6E','EK','BA','LH'])}{random.randint(100,999)}",
        random.choice(statuses)
    )

    cursor.execute(insert_query, values)

db.commit()
cursor.close()
db.close()

print("Flights inserted successfully")
