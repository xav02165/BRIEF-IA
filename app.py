import pandas as pd
import plotly.express as px
import streamlit as st

# Configuration de la page
st.set_page_config(
    page_title="Tableau de bord - Salaires", page_icon="💼", layout="wide"
)

st.title("💼 Dashboard des Salaires par Filiale")

# 1. Chargement des CSV générés par brief.py
try:
    df_employes = pd.read_csv("employes_resultats.csv")
    df_stats = pd.read_csv("statistiques.csv")
except FileNotFoundError:
    st.error(
        "⚠️ Fichiers CSV introuvables. Exécute d'abord le script 'brief.py' !"
    )
    st.stop()

# 2. Barre latérale : filtres
st.sidebar.header("🔍 Filtres d'analyse")

entreprises_dispo = df_employes["Entreprise"].unique().tolist()
entreprises_sel = st.sidebar.multiselect(
    "Filiales :", options=entreprises_dispo, default=entreprises_dispo
)

postes_dispo = df_employes["Poste"].unique().tolist()
postes_sel = st.sidebar.multiselect(
    "Postes :", options=postes_dispo, default=postes_dispo
)

# 3. Filtrage du DataFrame
df_filtre = df_employes[
    (df_employes["Entreprise"].isin(entreprises_sel))
    & (df_employes["Poste"].isin(postes_sel))
]

# 4. Affichage principal
if df_filtre.empty:
    st.warning("Aucun résultat ne correspond aux filtres.")
else:
    # Indicateurs (KPIs)
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Nombre d'employés", len(df_filtre))
    col2.metric(
        "Moyenne salariale", f"{round(df_filtre['Salaire (€)'].mean(), 2)} €"
    )
    col3.metric("Salaire Minimum", f"{df_filtre['Salaire (€)'].min()} €")
    col4.metric("Salaire Maximum", f"{df_filtre['Salaire (€)'].max()} €")

    st.divider()

    # Onglets
    tab_graph, tab_details, tab_stats = st.tabs(
        [
            "📊 Visualisations",
            "👥 Liste des employés",
            "📈 Statistiques pré-calculées",
        ]
    )

    with tab_graph:
        c1, c2 = st.columns(2)
        with c1:
            fig_box = px.box(
                df_filtre,
                x="Entreprise",
                y="Salaire (€)",
                color="Entreprise",
                title="Distribution des salaires",
            )
            st.plotly_chart(fig_box, use_container_width=True)
        with c2:
            df_poste = (
                df_filtre.groupby("Poste")["Salaire (€)"]
                .mean()
                .reset_index()
            )
            fig_bar = px.bar(
                df_poste,
                x="Poste",
                y="Salaire (€)",
                color="Poste",
                title="Salaire moyen par Poste",
            )
            st.plotly_chart(fig_bar, use_container_width=True)

    with tab_details:
        st.dataframe(df_filtre, use_container_width=True)

    with tab_stats:
        st.dataframe(df_stats, use_container_width=True)



   #     python -m streamlit run app.py