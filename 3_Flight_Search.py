import streamlit as st
import mysql.connector
import pandas as pd

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Flight Search",
    layout="wide"
)

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>
/* Sidebar gradient */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #6EC1E4, #0B1D3A);
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

/* Card */
.card {
    background: white;
    padding: 1.5rem;
    border-radius: 14px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# ---------- DB CONNECTION ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vino@123",
    database="flight_analytics"
)

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <h1>🔍 Flight Search</h1>
    <p>Search and explore flights departing from selected airports</p>
</div>
""", unsafe_allow_html=True)

# ---------- FILTER SECTION ----------
with st.container():
    st.markdown("<div class='card'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    airports = pd.read_sql("SELECT DISTINCT iata_code FROM airports", db)

    with col1:
        selected_airport = st.selectbox(
            "🛫 Departure Airport",
            airports["iata_code"].sort_values()
        )

    with col2:
        status_filter = st.selectbox(
            "📌 Flight Status",
            ["All", "On Time", "Delayed", "Cancelled"]
        )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------- QUERY ----------
query = f"""
SELECT
    flight_number,
    airline,
    departure_airport,
    arrival_airport,
    departure_time,
    arrival_time,
    status
FROM flights
WHERE departure_airport = '{selected_airport}'
"""

if status_filter != "All":
    query += f" AND status = '{status_filter}'"

df = pd.read_sql(query, db)
db.close()

# ---------- RESULTS ----------
st.subheader("📋 Matching Flights")

if df.empty:
    st.warning("No flights found for the selected filters.")
else:
    st.dataframe(
        df.sort_values("departure_time", ascending=False),
        use_container_width=True
    )
