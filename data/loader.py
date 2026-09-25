import sqlite3
import streamlit as st


@st.cache_data
def charger_parties():
    connexion = sqlite3.connect("parties.db")
    connexion.row_factory = sqlite3.Row

    cursor = connexion.execute("""
        SELECT *
        FROM parties
        LIMIT 100
    """)

    parties = [dict(row) for row in cursor.fetchall()]

    connexion.close()

    return parties