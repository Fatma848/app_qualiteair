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


st.header("Conclusion ")
st.write("""
Au cours de cette exploration de la qualité de l’air à la station **Saint-Germain-des-Prés** en 2025, **nous avons observé** plusieurs éléments clés :  

- **Évolution quotidienne de PM10 :** nous avons constaté que la concentration de particules fines varie tout au long de l’année, avec un **pic notable le 5 août**, correspondant à une journée particulièrement polluée.  
- **Relations avec les facteurs météorologiques :** grâce à la matrice de corrélation, **nous avons vu** qu’il existe une forte corrélation positive entre la température et PM10, tandis que l’humidité semble avoir une influence moins marquée.  
- **Indicateurs clés et distributions :** en examinant les histogrammes et les KPI, **nous avons observé** la moyenne, la médiane, le minimum et le maximum pour chaque variable, ce qui nous permet de mieux comprendre la variabilité des mesures.  

**En résumé :** cette application nous a permis de visualiser de manière interactive les tendances de la pollution de l’air, d’identifier les journées à forte concentration de PM10 et de mieux comprendre l’impact des facteurs climatiques sur la qualité de l’air.  
""")
