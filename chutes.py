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

    # Les deux dernières dates
    date_hier = dates[-2]
    date_aujourdhui = dates[-1]

    df_hier = df[df["Date"] == date_hier]
    df_aujourdhui = df[df["Date"] == date_aujourdhui]

    # Fusion sur Username
    chutes = pd.merge(
        df_hier[["Username", "Prénom", "Service", "Rang"]],
        df_aujourdhui[["Username", "Rang"]],
        on="Username",
        suffixes=("_hier", "_aujourdhui")
    )

    # Calcul de la perte de places
    chutes["Chute"] = (
        chutes["Rang_aujourdhui"]
        - chutes["Rang_hier"]
    )

    # Tri du plus mauvais au moins mauvais
    chutes = chutes.sort_values(
        by="Chute",
        ascending=False
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