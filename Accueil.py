import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from math import pi
from matplotlib.cm import get_cmap

import streamlit as st
import pandas as pd
import plotly.express as px

# --- Chargement des données ---
df = pd.read_csv('air_qualité.csv', sep=';')
df.columns = df.columns.str.strip()

# --- Création de la date complète ---
df['date'] = pd.to_datetime(df[['day', 'month', 'year']])

# --- Configuration page ---
st.set_page_config(
    page_title="Analyse Qualité de l'air 2025 - Saint-Germain-des-Prés",
    layout="wide"
)
st.title("Analyse de la qualité de l'air en 2025")
st.subheader("Étude des particules fines PM10 et facteurs associés")
st.markdown("#### Veuillez regarder les différentes pages pour **explorez l'analyse !!**")
# --- Titre principal et introduction ---
st.write("""
Cette analyse porte sur la qualité de l’air en 2025 dans la station située à la gare **Saint-Germain-des-Prés**, à Paris.  
La base de données contient des mesures quotidiennes comprenant :  

- **PM10 :** particules fines de diamètre inférieur ou égal à 10 µm, exprimées en µg/m³. Ces particules peuvent pénétrer profondément dans les poumons et affecter la santé respiratoire.  
- **TEMP :** température en degrés Celsius, qui peut influencer la dispersion des polluants dans l’air.  
- **HUMI :** humidité relative en pourcentage, un facteur pouvant moduler la concentration de particules fines.  
- **day, month, year :** informations permettant de situer chaque mesure dans le temps.  

Cette base permet d’examiner les variations quotidiennes de la pollution et d’étudier les relations entre PM10, température et humidité sur l’ensemble de l’année 2025.  
Les données sont représentées sous forme de séries temporelles, indicateurs statistiques, matrices de corrélation et tableaux filtrés pour faciliter l’analyse et la compréhension.
""")



