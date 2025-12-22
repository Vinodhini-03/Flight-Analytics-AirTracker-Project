/* =====================================================
   QUERY 1
   Total number of flights for each aircraft model
   ===================================================== */
SELECT
    a.model,
    COUNT(*) AS flight_count
FROM flights f
JOIN aircraft a ON f.aircraft_id = a.aircraft_id
GROUP BY a.model
ORDER BY flight_count DESC;


/* =====================================================
   QUERY 2
   Aircraft assigned to more than 5 flights
   ===================================================== */
SELECT
    a.registration,
    a.model,
    COUNT(f.flight_id) AS total_flights
FROM aircraft a
JOIN flights f ON a.aircraft_id = f.aircraft_id
GROUP BY a.aircraft_id, a.registration, a.model
HAVING total_flights > 5;


/* =====================================================
   QUERY 3
   Airports with more than 5 outbound flights
   ===================================================== */
SELECT
    ap.name AS airport_name,
    COUNT(f.flight_id) AS outbound_flights
FROM airports ap
JOIN flights f ON ap.iata_code = f.departure_airport
GROUP BY ap.iata_code, ap.name
HAVING outbound_flights > 5;


/* =====================================================
   QUERY 4
   Top 3 destination airports by arriving flights
   ===================================================== */
SELECT
    ap.name,
    ap.city,
    COUNT(f.flight_id) AS arrival_count
FROM airports ap
JOIN flights f ON ap.iata_code = f.arrival_airport
GROUP BY ap.iata_code, ap.name, ap.city
ORDER BY arrival_count DESC
LIMIT 3;


/* =====================================================
   QUERY 5
   Domestic vs International flights
   ===================================================== */
SELECT
    f.flight_number,
    dep.country AS origin_country,
    arr.country AS destination_country,
    CASE
        WHEN dep.country = arr.country THEN 'Domestic'
        ELSE 'International'
    END AS flight_type
FROM flights f
JOIN airports dep ON f.departure_airport = dep.iata_code
JOIN airports arr ON f.arrival_airport = arr.iata_code;


/* =====================================================
   QUERY 6
   5 most recent arrivals at DEL airport
   ===================================================== */
SELECT
    f.flight_number,
    a.model AS aircraft_model,
    dep.name AS departure_airport,
    f.arrival_time
FROM flights f
JOIN aircraft a ON f.aircraft_id = a.aircraft_id
JOIN airports dep ON f.departure_airport = dep.iata_code
WHERE f.arrival_airport = 'DEL'
ORDER BY f.arrival_time DESC
LIMIT 5;


/* =====================================================
   QUERY 7
   Airports with no arriving flights
   ===================================================== */
SELECT
    ap.iata_code,
    ap.name
FROM airports ap
LEFT JOIN flights f ON ap.iata_code = f.arrival_airport
WHERE f.flight_id IS NULL;


/* =====================================================
   QUERY 8
   Flight count by airline and status
   ===================================================== */
SELECT
    airline,
    SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END) AS on_time,
    SUM(CASE WHEN status = 'Delayed' THEN 1 ELSE 0 END) AS delayed,
    SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled
FROM flights
GROUP BY airline;


/* =====================================================
   QUERY 9
   All cancelled flights with aircraft and airports
   ===================================================== */
SELECT
    f.flight_number,
    a.model AS aircraft_model,
    dep.name AS departure_airport,
    arr.name AS arrival_airport,
    f.departure_time
FROM flights f
JOIN aircraft a ON f.aircraft_id = a.aircraft_id
JOIN airports dep ON f.departure_airport = dep.iata_code
JOIN airports arr ON f.arrival_airport = arr.iata_code
WHERE f.status = 'Cancelled'
ORDER BY f.departure_time DESC;


/* =====================================================
   QUERY 10
   Routes with more than 2 aircraft models
   ===================================================== */
SELECT
    f.departure_airport,
    f.arrival_airport,
    COUNT(DISTINCT a.model) AS aircraft_models
FROM flights f
JOIN aircraft a ON f.aircraft_id = a.aircraft_id
GROUP BY f.departure_airport, f.arrival_airport
HAVING aircraft_models > 2;


/* =====================================================
   QUERY 11
   Percentage of delayed flights per destination airport
   ===================================================== */
SELECT
    arr.name AS destination_airport,
    ROUND(
        SUM(CASE WHEN f.status = 'Delayed' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*),
        2
    ) AS delayed_percentage
FROM flights f
JOIN airports arr ON f.arrival_airport = arr.iata_code
GROUP BY arr.iata_code, arr.name
ORDER BY delayed_percentage DESC;
