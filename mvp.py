import pandas as pd

# ==========================
# Lecture du classement individuel
# ==========================
df = pd.read_excel("classement_individuel.xlsx")

# On enlève les joueurs sans points
df = df[df["Points"].notna()]

# Tri du meilleur au moins bon
mvp = df.sort_values(
    by="Points",
    ascending=False
)

# On garde le top 10
mvp = mvp.head(10)

# Sauvegarde
mvp.to_excel(
    "mvp.xlsx",
    index=False
)

print()
print("Top 10 MVP :")
print()

print(
    mvp[
        [
            "Rang",
            "Prénom",
            "Username",
            "Service",
            "Points"
        ]
    ]
)