import streamlit as st
import mysql.connector
import pandas as pd

st.set_page_config(layout="wide")

st.title("⏱️ Delay Analysis")

# ---------- SIDEBAR STYLE (SAFE CSS) ----------
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
    airline,
    SUM(CASE WHEN status = 'On Time' THEN 1 ELSE 0 END) AS on_time,
    SUM(CASE WHEN status = 'Delayed' THEN 1 ELSE 0 END) AS delayed_flights,
    SUM(CASE WHEN status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled
FROM flights
GROUP BY airline;
"""

df = pd.read_sql(query, db)
db.close()

# ---------- LAYOUT ----------
col1, col2 = st.columns([2, 3])

with col1:
    st.subheader("📋 Delay Summary by Airline")
    st.dataframe(df, use_container_width=True)

with col2:
    st.subheader("📊 Flight Status Comparison")
    st.bar_chart(
        df.set_index("airline")[["on_time", "delayed_flights", "cancelled"]],
        use_container_width=True
    )
