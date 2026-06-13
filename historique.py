print("JE SUIS LE BON FICHIER")

import pandas as pd
from datetime import datetime

# ==========================
# Date du jour
# ==========================
date_du_jour = datetime.now().strftime("%Y-%m-%d")

# ==========================
# Lecture du classement individuel
# ==========================
df = pd.read_excel("classement_individuel.xlsx")

# Ajout de la date
df["Date"] = date_du_jour

# ==========================
# Colonnes à conserver
# ==========================
colonnes = [
    "Date",
    "Username",
    "Prénom",
    "Service",
    "Rang",
    "Points",
    "Bons pronostics",
    "Scores exacts"
]

df = df[colonnes]

# ==========================
# Lecture de l'historique existant
# ==========================
try:

    historique = pd.read_excel(
        "historique_joueurs.xlsx"
    )

    historique = pd.concat(
        [historique, df],
        ignore_index=True
    )

except:

    historique = df

# ==========================
# Sauvegarde
# ==========================
print("Avant sauvegarde")

historique.to_excel(
    "historique_joueurs.xlsx",
    index=False
)

print("Après sauvegarde")

print()
print("Historique mis à jour.")
print(f"{len(df)} lignes ajoutées.")