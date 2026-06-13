import pandas as pd

# Lecture de l'historique
df = pd.read_excel("historique_joueurs.xlsx")

# Suppression des lignes sans rang
df = df[df["Rang"].notna()]

# Vérification qu'il y a au moins deux journées
dates = sorted(df["Date"].unique())

if len(dates) < 2:

    print()
    print("Pas encore assez de données pour calculer les progressions.")

else:

    # Deux dernières journées
    date_hier = dates[-2]
    date_aujourdhui = dates[-1]

    # Données d'hier (1 seule ligne par joueur)
    df_hier = (
        df[df["Date"] == date_hier]
        .drop_duplicates(subset=["Username"], keep="last")
    )

    # Données d'aujourd'hui (1 seule ligne par joueur)
    df_aujourdhui = (
        df[df["Date"] == date_aujourdhui]
        .drop_duplicates(subset=["Username"], keep="last")
    )

    # Fusion des deux journées
    progression = pd.merge(
        df_hier[["Username", "Prénom", "Service", "Rang"]],
        df_aujourdhui[["Username", "Rang"]],
        on="Username",
        suffixes=("_hier", "_aujourdhui")
    )

    # Calcul du gain de places
    progression["Progression"] = (
        progression["Rang_hier"]
        - progression["Rang_aujourdhui"]
    )

    # Ne garder que les progressions positives
    progression = progression[
        progression["Progression"] > 0
    ]

    # Tri du plus gros gain au plus petit
    progression = progression.sort_values(
        by="Progression",
        ascending=False
    )

    # Sécurité supplémentaire contre les doublons
    progression = progression.drop_duplicates(
        subset=["Username"]
    )

    # Top 10
    top_progressions = progression.head(10)

    # Sauvegarde
    top_progressions.to_excel(
        "progressions.xlsx",
        index=False
    )

    print()
    print("Top 10 des progressions :")
    print()

    print(
        top_progressions[
            [
                "Prénom",
                "Service",
                "Rang_hier",
                "Rang_aujourdhui",
                "Progression"
            ]
        ]
    )