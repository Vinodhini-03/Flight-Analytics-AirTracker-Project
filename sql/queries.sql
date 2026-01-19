/* =====================================================
   QUERY 1
   Total number of flights for each aircraft model
   ===================================================== */
SELECT 
    a.model,
    COUNT(f.flight_id) AS total_flights
FROM flights f
JOIN aircraft a
    ON f.aircraft_registration = a.registration
GROUP BY a.model;


/* =====================================================
   QUERY 2
   Aircraft assigned to more than 5 flights
   ===================================================== */
SELECT 
    a.registration,
    a.model,
    COUNT(f.flight_id) AS flight_count
FROM flights f
JOIN aircraft a
    ON f.aircraft_registration = a.registration
GROUP BY a.registration, a.model
HAVING COUNT(f.flight_id) > 5;


/* =====================================================
   QUERY 3
   Airports with more than 5 outbound flights
   ===================================================== */
SELECT 
    ap.name,
    COUNT(f.flight_id) AS outbound_flights
FROM flights f
JOIN airports ap
    ON f.departure_airport = ap.iata_code
GROUP BY ap.name
HAVING COUNT(f.flight_id) > 5;


/* =====================================================
   QUERY 4
   Top 3 destination airports by arriving flights
   ===================================================== */
SELECT 
    ap.name,
    ap.city,
    COUNT(f.flight_id) AS arrival_count
FROM flights f
JOIN airports ap
    ON f.arrival_airport = ap.iata_code
GROUP BY ap.name, ap.city
ORDER BY arrival_count DESC
LIMIT 3;


/* =====================================================
   QUERY 5
   Domestic vs International flights
   ===================================================== */
SELECT 
    f.flight_number,
    f.departure_airport,
    f.arrival_airport,
    CASE
        WHEN ap1.country = ap2.country THEN 'Domestic'
        ELSE 'International'
    END AS flight_type
FROM flights f
JOIN airports ap1
    ON f.departure_airport = ap1.iata_code
JOIN airports ap2
    ON f.arrival_airport = ap2.iata_code;


/* =====================================================
   QUERY 6
   5 most recent arrivals at DEL airport
   ===================================================== */
SELECT 
    f.flight_number,
    f.aircraft_registration,
    ap.name AS departure_airport,
    f.arrival_time
FROM flights f
JOIN airports ap
    ON f.departure_airport = ap.iata_code
WHERE f.arrival_airport = 'DEL'
ORDER BY f.arrival_time DESC
LIMIT 5;


/* =====================================================
   QUERY 7
   Airports with no arriving flights
   ===================================================== */
SELECT 
    a.name,
    a.city
FROM airports a
LEFT JOIN flights f
    ON a.iata_code = f.arrival_airport
WHERE f.flight_id IS NULL;


/* =====================================================
   QUERY 8
   Flight count by airline and status
   ===================================================== */
SELECT
    airline,
    SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END) AS on_time,
    SUM(CASE WHEN status = 'Delayed' THEN 1 ELSE 0 END) AS delay,
    SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled
FROM flights
GROUP BY airline;


/* =====================================================
   QUERY 9
   All cancelled flights with aircraft and airports
   ===================================================== */
SELECT 
    f.flight_number,
    f.aircraft_registration,
    ap1.name AS departure_airport,
    ap2.name AS arrival_airport,
    f.departure_time
FROM flights f
JOIN airports ap1
    ON f.departure_airport = ap1.iata_code
JOIN airports ap2
    ON f.arrival_airport = ap2.iata_code
WHERE f.status = 'Cancelled'
ORDER BY f.departure_time DESC;


/* =====================================================
   QUERY 10
   Routes with more than 2 aircraft models
   ===================================================== */
SELECT 
    departure_airport,
    arrival_airport,
    COUNT(DISTINCT aircraft_registration) AS aircraft_used
FROM flights
GROUP BY departure_airport, arrival_airport
HAVING COUNT(DISTINCT aircraft_registration) > 2;


/* =====================================================
   QUERY 11
   Percentage of delayed flights per destination airport
   ===================================================== */
SELECT 
    ap.name AS destination_airport,
    ROUND(
        SUM(CASE WHEN f.status = 'Delayed' THEN 1 ELSE 0 END) * 100.0 
        / COUNT(f.flight_id),
        2
    ) AS delayed_percentage
FROM flights f
JOIN airports ap
    ON f.arrival_airport = ap.iata_code
GROUP BY ap.name
ORDER BY delayed_percentage DESC;
