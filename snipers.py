import pandas as pd

# Lecture du classement individuel
df = pd.read_excel("classement_individuel.xlsx")

# Tri par nombre de scores exacts
snipers = df.sort_values(
    by="Scores exacts",
    ascending=False
)

# Top 10
snipers = snipers.head(10)

# Sauvegarde
snipers.to_excel(
    "snipers.xlsx",
    index=False
)

print()
print("Top 10 Snipers :")
print()

print(
    snipers[
        [
            "Rang",
            "Prénom",
            "Username",
            "Service",
            "Scores exacts"
        ]
    ]
)