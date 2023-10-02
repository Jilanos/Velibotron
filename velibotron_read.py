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


#%%


chemin_fichier = r'C:\THESE_PAUL\Bureau\finance\Data Hackathon\14-Hackathon\02_Historique_remplissage_stations\2023_02'

# Lire le fichier Excel
data = pd.read_excel(chemin_fichier + "\\" + "2023-02-01_Historique_remplissage_stations.xlsx")

#%%

#on va créer une fonction qui va parcourir les lignes du fichier et va retourner les velibs qui ont été enlevé et direct rajoutés

data['Date mise à jour'] = pd.to_datetime(data['Date mise à jour'])

# Trier les données par station et par date de mise à jour
data = data.sort_values(['Code station', 'Date mise à jour'])

# Ajouter une colonne de différence temporelle en secondes
data['Diff temps (s)'] = data.groupby('Code station')['Date mise à jour'].diff().dt.total_seconds()

# Créer une condition pour les changements rapides
condition = (data['VM disponibles'].shift(1) == data['VM disponibles'] - 1) & (data['VM disponibles'].shift(2) == data['VM disponibles'] - 2) & (data['Diff temps (s)'] <= 60)

# Sélectionner les lignes qui satisfont la condition
velibs_retires_remis = data[condition]

# Afficher les résultats
pd.set_option('display.max_rows', None)  # Afficher toutes les lignes du DataFrame

with open('resultat.txt', 'w') as f:
    with pd.option_context('display.max_columns', None):
        sys.stdout = f
        print(velibs_retires_remis[['Diff temps (s)', 'Nom station',  'VM disponibles']])
        sys.stdout = sys.__stdout__  # Rétablir la sortie standard