import pandas as pd
import plotly.express as px
import streamlit as st

# ==============================================================================
# 1. CONFIGURATION DE LA PAGE
# ==============================================================================
# IMPACT VISUEL : Pleine largeur d'écran pour disposer les tableaux et graphiques côte à côte.
st.set_page_config(page_title="Rapport Salaires", layout="wide")

st.title("💼 Rapport Synthétique et Détaillé des Salaires")

# ==============================================================================
# 2. CHARGEMENT ET SÉCURISATION DES DONNÉES
# ==============================================================================
try:
    df_emp = pd.read_csv("employes_resultats.csv")
    df_stats = pd.read_csv("statistiques.csv")
except FileNotFoundError:
    st.error(
        "⚠️ Fichiers CSV introuvables. Exécute d'abord ton script 'brief.py'."
    )
    st.stop()


# ==============================================================================
# 3. SYNTHÈSE GLOBALE DE L'ENTREPRISE (KPIs)
# ==============================================================================
st.subheader("1. Indicateurs Globaux")

# IMPACT VISUEL : Extraction de la ligne 'Entreprise Globale' dans statistiques.csv
stats_globales = df_stats[df_stats["Entité"] == "Entreprise Globale"].iloc[0]

# IMPACT VISUEL : 3 cartes épurées en haut de page pour les chiffres clés
col_kpi1, col_kpi2, col_kpi3 = st.columns(3)
col_kpi1.metric(
    "Salaire Moyen Global", f"{stats_globales['Salaire Moyen (€)']} €"
)
col_kpi2.metric(
    "Salaire Minimum Global", f"{stats_globales['Salaire Minimum (€)']} €"
)
col_kpi3.metric(
    "Salaire Maximum Global", f"{stats_globales['Salaire Maximum (€)']} €"
)

st.divider()


# ==============================================================================
# 4. STATISTIQUES PAR FILIALE
# ==============================================================================
st.subheader("2. Comparatif des Filiales")

col_fil_tab, col_fil_graph = st.columns(2)

# Filtrage : On conserve uniquement les filiales (on exclut la ligne globale)
df_filiales = df_stats[df_stats["Entité"] != "Entreprise Globale"]

with col_fil_tab:
    # IMPACT VISUEL : Tableau synthétique issu directement de statistiques.csv
    st.write("**Données chiffrées par filiale**")
    st.dataframe(df_filiales, use_container_width=True, hide_index=True)

with col_fil_graph:
    # IMPACT VISUEL : Bar chart épuré comparant les moyennes par filiale
    fig_filiales = px.bar(
        df_filiales,
        x="Entité",
        y="Salaire Moyen (€)",
        text_auto=True,
        title="Salaire Moyen par Filiale (€)",
    )
    fig_filiales.update_layout(
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis_title=None,
        yaxis_title=None,
        yaxis_showticklabels=False,
    )
    fig_filiales.update_traces(
        marker_color="#2b5c8f", textposition="outside", cliponaxis=False
    )
    st.plotly_chart(fig_filiales, use_container_width=True)

st.divider()


# ==============================================================================
# 5. REGISTRE DÉTAILLÉ ET MOYENNE PAR MÉTIER
# ==============================================================================
st.subheader("3. Registre des Employés & Analyse par Métier")

col_emp_tab, col_emp_graph = st.columns(2)

with col_emp_tab:
    # IMPACT VISUEL : Liste intégrale de chaque employé (Entreprise, Nom, Poste, Salaire)
    st.write("**Liste complète des collaborateurs**")
    st.dataframe(df_emp, use_container_width=True, hide_index=True)

with col_emp_graph:
    # Calcul dynamique de la moyenne salariale par métier sur la base du fichier individuel
    df_metier = df_emp.groupby("Poste")["Salaire (€)"].mean().reset_index()
    df_metier["Salaire (€)"] = df_metier["Salaire (€)"].round(2)

    # IMPACT VISUEL : Bar chart épuré par poste
    fig_metier = px.bar(
        df_metier,
        x="Poste",
        y="Salaire (€)",
        text_auto=True,
        title="Salaire Moyen par Métier (€)",
    )
    fig_metier.update_layout(
        margin=dict(l=10, r=10, t=30, b=10),
        xaxis_title=None,
        yaxis_title=None,
        yaxis_showticklabels=False,
    )
    fig_metier.update_traces(
        marker_color="#4183c4", textposition="outside", cliponaxis=False
    )
    st.plotly_chart(fig_metier, use_container_width=True)
   #     python -m streamlit run app.py