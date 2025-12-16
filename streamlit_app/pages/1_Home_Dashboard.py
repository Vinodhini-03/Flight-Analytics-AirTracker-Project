import streamlit as st
import pandas as pd
import mysql.connector

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Flight Analytics Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
/* Sidebar gradient */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #87CEEB 0%, #0B1D3A 100%);
    color: white;
}

/* Sidebar text */
[data-testid="stSidebar"] * {
    color: white;
}

/* Hero section */
.hero {
    padding: 2.5rem 2rem;
    background: linear-gradient(135deg, #0B1D3A, #1F4E79);
    border-radius: 16px;
    color: white;
    margin-bottom: 2rem;
}

/* KPI cards */
.kpi-card {
    background: white;
    padding: 1.5rem;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    text-align: center;
}

.kpi-title {
    font-size: 0.9rem;
    color: #6b7280;
}

.kpi-value {
    font-size: 2rem;
    font-weight: 700;
    color: #0B1D3A;
}
</style>
""", unsafe_allow_html=True)

# ---------- DB CONNECTION ----------
def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Vino@123",
        database="flight_analytics"
    )

conn = get_connection()

# ---------- DATA ----------
total_flights = pd.read_sql(
    "SELECT COUNT(*) AS total FROM flights", conn
).iloc[0, 0]

cancelled_flights = pd.read_sql(
    "SELECT COUNT(*) AS cancelled FROM flights WHERE status = 'Cancelled'", conn
).iloc[0, 0]

top_airline = pd.read_sql("""
    SELECT airline, COUNT(*) AS cnt
    FROM flights
    GROUP BY airline
    ORDER BY cnt DESC
    LIMIT 1
""", conn)

busiest_route = pd.read_sql("""
    SELECT departure_airport, arrival_airport, COUNT(*) AS cnt
    FROM flights
    GROUP BY departure_airport, arrival_airport
    ORDER BY cnt DESC
    LIMIT 1
""", conn)

conn.close()

# ---------- HERO HEADER ----------
st.markdown("""
<div class="hero">
    <h1>✈️ Flight Analytics Dashboard</h1>
    <p>Real-time flight insights powered by AeroDataBox & MySQL</p>
</div>
""", unsafe_allow_html=True)

# ---------- KPI SECTION ----------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">✈ Total Flights</div>
        <div class="kpi-value">{total_flights}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">❌ Cancelled Flights</div>
        <div class="kpi-value">{cancelled_flights}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🏢 Top Airline</div>
        <div class="kpi-value">{top_airline.iloc[0]['airline']}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">🛫 Busiest Route</div>
        <div class="kpi-value">
            {busiest_route.iloc[0]['departure_airport']} → {busiest_route.iloc[0]['arrival_airport']}
        </div>
    </div>
    """, unsafe_allow_html=True)
