import requests
import pandas as pd

# ==========================
# Lecture du token
# ==========================
with open("token.txt", "r", encoding="utf-8") as f:
    TOKEN = f.read().strip()

headers = {
    "Authorization": TOKEN
}

url = "https://api.mpp.football/challenge-standings/users-standings"

# ==========================
# Récupération MPP
# ==========================
tous_les_joueurs = []

offset = 0
limit = 100

while True:

    params = {
        "challengeId": "mpp_challenge_UCB9B893",
        "offset": offset,
        "limit": limit
    }

    response = requests.get(
        url,
        headers=headers,
        params=params
    )

    if response.status_code != 200:
        print("Erreur API :", response.status_code)
        break

    data = response.json()

    standings = data.get("standings", [])

    if len(standings) == 0:
        break

    for joueur in standings:

        user = joueur.get("user", {})
        ranking = joueur.get("ranking", {})

        tous_les_joueurs.append({

            "Rang": ranking.get("rank"),

            "Points": ranking.get("points"),

            "Bons pronostics": ranking.get("goodForecasts"),

            "Scores exacts": ranking.get("exactForecasts"),

            "Pronostics joués": ranking.get("calculatedForecasts"),

            "Prénom": user.get("firstName"),

            "Username": user.get("username")

        })

    print(f"Offset {offset} : {len(standings)} joueurs")

    if not data.get("hasNext", False):
        break

    offset += limit

# ==========================
# Création dataframe MPP
# ==========================
df_mpp = pd.DataFrame(tous_les_joueurs)

df_mpp.drop_duplicates(
    subset=["Username"],
    inplace=True
)

# ==========================
# Lecture du fichier services
# ==========================
try:

    df_services = pd.read_excel(
        "joueurs_services.xlsx"
    )

except:

    df_services = pd.DataFrame(
        columns=["Username", "Service"]
    )

# ==========================
# Fusion avec les services
# ==========================
df_final = df_mpp.merge(
    df_services[["Username", "Service"]],
    on="Username",
    how="left"
)

# Tri par classement
df_final = df_final.sort_values(
    by="Rang"
)

# ==========================
# Sauvegarde
# ==========================
df_final.to_excel(
    "classement_individuel.xlsx",
    index=False
)

print()
print(f"{len(df_final)} joueurs dans le fichier.")
print("Mise à jour terminée.")