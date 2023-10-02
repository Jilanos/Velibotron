import random
import numpy as np
import matplotlib.pyplot as plt
import os
import gc
import sys 
import pandas as pd



chemin_fichier = r'C:\THESE_PAUL\Bureau\finance\Data Hackathon\14-Hackathon\01_Courses_usagers\2023_02'

# Lire le fichier Excel
data = pd.read_excel(chemin_fichier + "\\" + "2023-02-01_Courses_usagers.xlsx")

#%%

sorted_data = data.sort_values(by='Durée en secondes')

# Prendre les 100 premières lignes
top_100_faibles_temps = sorted_data.head(20)

# Afficher les résultats
print(top_100_faibles_temps[['ID utilisateur', 'Durée en secondes', 'Distance parcourue en mètres', 'Vitesse maximum']])