import pandas as pd

# Lecture de l'historique
df = pd.read_excel("historique_joueurs.xlsx")

# Suppression des lignes sans rang
df = df[df["Rang"].notna()]

# Vérification qu'il y a au moins deux journées
dates = sorted(df["Date"].unique())

if len(dates) < 2:

    print()
    print("Pas encore assez de données pour calculer les chutes.")

else:

    # Deux dernières journées
    date_hier = dates[-2]
    date_aujourdhui = dates[-1]

    # Données d'hier
    df_hier = (
        df[df["Date"] == date_hier]
        .drop_duplicates(subset=["Username"], keep="last")
    )

    # Données d'aujourd'hui
    df_aujourdhui = (
        df[df["Date"] == date_aujourdhui]
        .drop_duplicates(subset=["Username"], keep="last")
    )

    # Fusion
    chutes = pd.merge(
        df_hier[["Username", "Prénom", "Service", "Rang"]],
        df_aujourdhui[["Username", "Rang"]],
        on="Username",
        suffixes=("_hier", "_aujourdhui")
    )

    # Calcul des pertes de places
    chutes["Chute"] = (
        chutes["Rang_aujourdhui"]
        - chutes["Rang_hier"]
    )

    # Ne garder que les chutes
    chutes = chutes[
        chutes["Chute"] > 0
    ]

    # Tri du pire au moins pire
    chutes = chutes.sort_values(
        by="Chute",
        ascending=False
    )

    # Suppression des doublons
    chutes = chutes.drop_duplicates(
        subset=["Username"]
    )

    # Top 10
    top_chutes = chutes.head(10)

    # Sauvegarde
    top_chutes.to_excel(
        "chutes.xlsx",
        index=False
    )

    print()
    print("Top 10 des chutes :")
    print()

    print(
        top_chutes[
            [
                "Prénom",
                "Service",
                "Rang_hier",
                "Rang_aujourdhui",
                "Chute"
            ]
        ]
    )