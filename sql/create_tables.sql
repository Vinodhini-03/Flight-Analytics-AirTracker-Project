
-- Database: flight_analytics

CREATE DATABASE IF NOT EXISTS flight_analytics;
USE flight_analytics;


-- Airports Table

CREATE TABLE IF NOT EXISTS airports (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    iata_code VARCHAR(10) NOT NULL UNIQUE,
    icao_code VARCHAR(10),
    name VARCHAR(255),
    city VARCHAR(255),
    country VARCHAR(255),
    latitude DOUBLE,
    longitude DOUBLE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Flights Table

CREATE TABLE IF NOT EXISTS flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    departure_airport VARCHAR(10) NOT NULL,
    arrival_airport VARCHAR(10) NOT NULL,
    departure_time DATETIME,
    arrival_time DATETIME,
    airline VARCHAR(255),
    flight_number VARCHAR(50),
    status VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_departure_airport
        FOREIGN KEY (departure_airport)
        REFERENCES airports(iata_code)
        ON DELETE CASCADE,

    CONSTRAINT fk_arrival_airport
        FOREIGN KEY (arrival_airport)
        REFERENCES airports(iata_code)
        ON DELETE CASCADE
);


-- Indexes for Faster Analytics

CREATE INDEX idx_flights_status ON flights(status);
CREATE INDEX idx_flights_airline ON flights(airline);
CREATE INDEX idx_flights_route ON flights(departure_airport, arrival_airport);
