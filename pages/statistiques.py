import streamlit as st
import pandas as pd

from data.loader import charger_parties


st.title("Statistiques")

parties = charger_parties()

df = pd.DataFrame(parties)

st.write("Nombre de parties par serveur")

nombre_par_serveur = df["serveur_id"].value_counts().sort_index()

st.bar_chart(nombre_par_serveur)