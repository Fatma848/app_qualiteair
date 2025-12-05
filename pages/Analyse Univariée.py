import streamlit as st
import pandas as pd
import plotly.express as px

# --- Chargement des données ---
df = pd.read_csv('air_qualité.csv', sep=';')
df.columns = df.columns.str.strip()
df['date'] = pd.to_datetime(df[['day','month','year']])

# --- Titre principal ---

st.subheader("Analyse Univariée ")

st.write("""
Cette analyse porte sur la qualité de l’air en 2025 dans la station **Saint-Germain-des-Prés**.  
Les variables disponibles sont :  

- **PM10 :** particules fines ≤10 µm (µg/m³)  
- **TEMP :** température en °C  
- **HUMI :** humidité relative en %  
- **day, month, year** : date de la mesure  

Ces histogrammes permettent de visualiser la **distribution des mesures** pour chaque variable et de mieux comprendre leur variabilité.
""")




st.header("Histogrammes des variables")
    
    # Choix de la variable
var_choice = st.selectbox(
        "Choisissez la variable à afficher :",
        ["PM10", "TEMP", "HUMI"]
    )
    
    # Création de l'histogramme avec Plotly
fig_hist = px.histogram(
        df,
        x=var_choice,
        nbins=30,
        title=f"Distribution de {var_choice}",
        labels={var_choice: f"{var_choice}"},
        color_discrete_sequence=['#0b3d91']
    )
fig_hist.update_layout(
        xaxis_title=var_choice,
        yaxis_title="Nombre de mesures",
        title_font_size=20,
        font=dict(size=14)
    )
    
st.plotly_chart(fig_hist, use_container_width=True)
    
    # Statistiques de base
st.write(f"Statistiques pour **{var_choice}** :")
st.write(df[var_choice].describe().to_frame())

