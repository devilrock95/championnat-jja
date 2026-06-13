import pandas as pd

# ==========================
# Lecture du classement individuel
# ==========================
df = pd.read_excel("classement_individuel.xlsx")

# Les points vides deviennent 0
df["Points"] = df["Points"].fillna(0)

# On retire les joueurs sans service
df = df[df["Service"].notna()]

# ==========================
# Calcul par service
# ==========================
classement_services = (
    df.groupby("Service")
      .agg(
          Joueurs=("Username", "count"),
          Points_totaux=("Points", "sum"),
          Moyenne=("Points", "mean")
      )
      .reset_index()
)

# Tri du meilleur au moins bon
classement_services = classement_services.sort_values(
    by="Moyenne",
    ascending=False
)

# Création du rang
classement_services.insert(
    0,
    "Rang",
    range(1, len(classement_services) + 1)
)

# Arrondi de la moyenne
classement_services["Moyenne"] = (
    classement_services["Moyenne"]
    .round(2)
)

# ==========================
# Sauvegarde
# ==========================
classement_services.to_excel(
    "classement_services.xlsx",
    index=False
)

print()
print("Classement des services mis à jour.")
print()
print(classement_services)