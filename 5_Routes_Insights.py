import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(layout="wide")

st.title("🛣️ Routes Insights")

# ---------- SIDEBAR STYLE ----------
st.markdown("""
<style>
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #87CEEB 0%, #1E3A8A 100%);
}

[data-testid="stSidebar"] * {
    color: white;
}
</style>
""", unsafe_allow_html=True)

# ---------- DATABASE ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vino@123",
    database="flight_analytics"
)

query = """
SELECT
    departure_airport,
    arrival_airport,
    COUNT(*) AS total_flights
FROM flights
GROUP BY departure_airport, arrival_airport
ORDER BY total_flights DESC
LIMIT 10
"""

df = pd.read_sql(query, db)
db.close()

# Route column
df["route"] = df["departure_airport"] + " → " + df["arrival_airport"]

# ---------- LAYOUT ----------
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("📋 Top 10 Busiest Routes")
    st.dataframe(
        df[["route", "total_flights"]],
        use_container_width=True
    )

with col2:
    st.subheader("📊 Busiest Routes Visualization")
    st.bar_chart(
        df.set_index("route")[["total_flights"]],
        use_container_width=True
    )
