✈️ Flight Analytics & AirTracker Dashboard

📌 Project Overview

This project is an end-to-end Flight Analytics & AirTracker Dashboard built using real-time aviation data from the AeroDataBox API. The system collects airport and flight data, stores it in a MySQL database, performs SQL-based analysis, and visualizes insights using an interactive Streamlit web application.

The project demonstrates an end-to-end data engineering and analytics workflow using real-world aviation APIs.

The main objectives of this project are to analyze:

* Flight movements and operational status
* Airport activity and traffic distribution
* Route popularity and busiest connections
* Delay and cancellation patterns

---

🛠 Tech Stack

* Language: Python
* API: AeroDataBox (via RapidAPI)
* Database: MySQL
* Application / Dashboard: Streamlit
* Data Processing: Pandas
* Version Control: GitHub

---

🧱 Project Structure

```
flight-analytics-project/
│
├── src/
│   ├── api/
│   │   ├── fetch_airports.py
│   │   ├── fetch_flights.py
│   │   └── fetch_delays.py
│   │
│   └── database/
│       ├── schema.sql
│       └── insert_flights.py
│
├── streamlit_app/
│   ├── app.py
│   └── pages/
│       ├── 1_Home_Dashboard.py
│       ├── 2_Flight_Search.py
│       ├── 3_Airport_Details.py
│       ├── 4_Delay_Analysis.py
│       └── 5_Routes_Insights.py
│
├── sql/
│   ├── create_tables.sql
│   └── queries.sql
│
├── requirements.txt
└── README.md
```

---

✈️ Airport Selection

The project includes both Indian and international airports to enable meaningful domestic and global comparisons.

Indian Airports:

* DEL – Delhi
* BOM – Mumbai
* BLR – Bengaluru
* MAA – Chennai
* HYD – Hyderabad
* CCU – Kolkata
* COK – Kochi

International Airports:

* LHR – London Heathrow
* JFK – New York (JFK)
* DXB – Dubai
* SIN – Singapore
* CDG – Paris Charles de Gaulle
* FRA – Frankfurt
* HND – Tokyo Haneda

These airports were selected based on:

* High passenger traffic
* Global connectivity
* Availability of consistent real-time flight data

---

🌐 API Data Collection

All data is fetched using the AeroDataBox API via RapidAPI.

Airport Data:

* Endpoint used: `/airports/iata/{code}`
* Stored fields:

  * IATA code
  * ICAO code
  * Airport name
  * City
  * Country
  * Latitude & Longitude
  * Timezone

Flight Data:

* Flights are collected using airport arrivals and departures endpoints
* Past-time window data is used (not future-only data)
* Stored details include:

  * Flight number
  * Airline
  * Departure airport
  * Arrival airport
  * Departure and arrival times
  * Flight status (On Time / Delayed / Cancelled)

---

🗄 Database Design

The database is created manually using SQL scripts.

Key tables:

* airports
* flights

Design features:

* Primary keys for entity uniqueness
* Logical relationships between tables using airport codes
* Proper data types for time, text, and numeric fields
* Only real API data is stored (no mock data)

---

📊 SQL Analysis

All analytical SQL queries are documented in:

```
sql/queries.sql
```

The queries cover:

* Flight counts grouped by airline and status
* Busiest routes and most active airports
* Cancelled flight analysis
* Domestic vs international flight classification
* Delay percentage analysis by destination airport

Note:
Aircraft-level analytics were limited due to API quota and project scope constraints; therefore, some insights are derived at the airline and route level instead of individual aircraft models.

---

📈 Streamlit Application

The Streamlit application provides an interactive dashboard with the following pages:

🏠 Home Dashboard

* Total flights
* Cancelled flights
* Top airline by number of flights
* Busiest route

🔍 Flight Search

* Search flights by departure airport
* View flight status and timings

🛫 Airport Details

* Airport information
* Total flights associated with the airport
* Cancellation count

⏱ Delay Analysis

* Delay and cancellation summary by airline
* Bar chart visualization

🛣 Routes Insights

* Top busiest routes
* Route-based flight count visualization

---

⚠️ Error Handling

* Basic API request error handling and response validation
* Database connection safety checks
* Duplicate-safe insert logic
* Graceful error prevention within Streamlit components

---

▶️ How to Run the Project

1️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

2️⃣ Create database and tables

```sql
Run the SQL scripts inside:
sql/create_tables.sql
```

3️⃣ Fetch and insert data

```bash
python src/api/fetch_airports.py
python src/api/fetch_flights.py
python src/database/insert_flights.py
```

4️⃣ Run the Streamlit application

```bash
streamlit run streamlit_app/app.py
```

---

✅ Project Status

✔ Real-time API data collected
✔ SQL database populated
✔ Analytical SQL queries implemented
✔ Streamlit dashboard running
✔ GitHub version control used

---

👤 Author

Vinodhini S
Flight Analytics & AirTracker Project
