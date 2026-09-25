import streamlit as st

from data.loader import charger_parties


st.title("Parties")

parties = charger_parties()

# Filtre serveur
serveurs = sorted(set(partie["serveur_id"] for partie in parties))

serveur_selectionne = st.sidebar.selectbox(
    "Serveur",
    ["Tous"] + serveurs
)

if serveur_selectionne != "Tous":
    parties = [
        partie
        for partie in parties
        if partie["serveur_id"] == serveur_selectionne
    ]

# Pagination
lignes_par_page = 10

nombre_pages = max(1, (len(parties) + lignes_par_page - 1) // lignes_par_page)

page = st.sidebar.number_input(
    "Page",
    min_value=1,
    max_value=nombre_pages,
    value=1
)

debut = (page - 1) * lignes_par_page
fin = debut + lignes_par_page

parties_page = parties[debut:fin]

st.write(f"{len(parties)} parties trouvées.")
st.write(f"Page {page} / {nombre_pages}")

st.dataframe(parties_page)