import mysql.connector
from src.api.fetch_airports import fetch_airport

airport_codes = [
    "DEL", "BOM", "BLR", "MAA", "HYD", "CCU", "COK",
    "LHR", "JFK", "LAX", "DXB", "SIN", "CDG", "FRA", "HND"
]

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vino@123",
    database="flight_analytics"
)

cursor = db.cursor()

insert_query = """
INSERT INTO airports (
    icao_code,
    iata_code,
    name,
    city,
    country,
    continent
)
VALUES (%s, %s, %s, %s, %s, %s)
"""

for code in airport_codes:
    data = fetch_airport(code)

    values = (
        data.get("icao"),
        data.get("iata"),
        data.get("fullName"),
        data.get("municipalityName"),
        data["country"]["name"],
        data["continent"]["name"]
    )

    cursor.execute(insert_query, values)
    print(f"Inserted airport {code}")

db.commit()
cursor.close()
db.close()
