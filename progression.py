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

    # Les deux dernières dates
    date_hier = dates[-2]
    date_aujourdhui = dates[-1]

    df_hier = df[df["Date"] == date_hier]
    df_aujourdhui = df[df["Date"] == date_aujourdhui]

    # Fusion sur Username
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

    # Tri du meilleur au moins bon
    progression = progression.sort_values(
        by="Progression",
        ascending=False
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