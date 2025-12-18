
-- Database: flight_analytics

CREATE DATABASE IF NOT EXISTS flight_analytics;
USE flight_analytics;


-- Airports Table

CREATE TABLE airports (
    airport_id INT AUTO_INCREMENT PRIMARY KEY,
    iata_code VARCHAR(10) UNIQUE NOT NULL,
    name VARCHAR(255),
    city VARCHAR(255),
    country VARCHAR(255)
);


-- Aircraft Table

CREATE TABLE aircraft (
    aircraft_id INT AUTO_INCREMENT PRIMARY KEY,
    registration VARCHAR(20) UNIQUE NOT NULL,
    model VARCHAR(100) NOT NULL
);


-- Flights Table

CREATE TABLE flights (
    flight_id INT AUTO_INCREMENT PRIMARY KEY,
    flight_number VARCHAR(20),
    airline VARCHAR(100),

    departure_airport VARCHAR(10),
    arrival_airport VARCHAR(10),

    aircraft_id INT,

    departure_time DATETIME,
    arrival_time DATETIME,
    status VARCHAR(50),

    FOREIGN KEY (departure_airport) REFERENCES airports(iata_code),
    FOREIGN KEY (arrival_airport) REFERENCES airports(iata_code),
    FOREIGN KEY (aircraft_id) REFERENCES aircraft(aircraft_id)
);
