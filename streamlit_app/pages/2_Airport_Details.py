import streamlit as st
import mysql.connector
import pandas as pd

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="Airport Details",
    layout="wide"
)

# ---------- CSS (reuse same theme) ----------
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
.hero {
    padding: 2.5rem 2rem;
    background: linear-gradient(135deg, #0B1D3A, #1F4E79);
    border-radius: 16px;
    color: white;
    margin-bottom: 2rem;
}

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

# ---------- DB ----------
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vino@123",
    database="flight_analytics"
)

query = """
SELECT
    a.iata_code,
    a.name,
    a.country,
    COUNT(f.flight_id) AS total_flights,
    SUM(CASE WHEN f.status = 'Cancelled' THEN 1 ELSE 0 END) AS cancelled
FROM airports a
LEFT JOIN flights f
ON a.iata_code = f.departure_airport
GROUP BY a.iata_code, a.name, a.country
"""

df = pd.read_sql(query, db)
db.close()

# ---------- HERO ----------
st.markdown("""
<div class="hero">
    <h1>🛫 Airport Details</h1>
    <p>Flight activity and cancellation overview by airport</p>
</div>
""", unsafe_allow_html=True)

# ---------- AIRPORT SELECT ----------
airport = st.selectbox(
    "✈ Select an Airport",
    df["iata_code"].sort_values()
)

selected = df[df["iata_code"] == airport].iloc[0]

# ---------- KPI ROW ----------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Airport</div>
        <div class="kpi-value">{selected['iata_code']}</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Total Flights</div>
        <div class="kpi-value">{int(selected['total_flights'])}</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div class="kpi-card">
        <div class="kpi-title">Cancelled Flights</div>
        <div class="kpi-value">{int(selected['cancelled'])}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------- DETAILS TABLE ----------
st.subheader("📋 Airport Summary")
st.dataframe(
    selected.to_frame().T.reset_index(drop=True),
    use_container_width=True
)
