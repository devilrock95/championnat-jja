import pandas as pd

# ========================================
# Lecture des fichiers
# ========================================

services = pd.read_excel("classement_services.xlsx")
mvp = pd.read_excel("mvp.xlsx")
snipers = pd.read_excel("snipers.xlsx")
classement = pd.read_excel("classement_individuel.xlsx")

try:
    progressions = pd.read_excel("progressions.xlsx")
except:
    progressions = pd.DataFrame()

try:
    chutes = pd.read_excel("chutes.xlsx")
except:
    chutes = pd.DataFrame()

# ========================================
# Informations principales
# ========================================

leader_service = services.iloc[0]["Service"]
leader_moyenne = round(services.iloc[0]["Moyenne"], 2)

leader_joueur = mvp.iloc[0]["Prénom"]
leader_points = int(mvp.iloc[0]["Points"])

# ========================================
# Construction HTML
# ========================================

html = f"""
<!DOCTYPE html>
<html lang="fr">

<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Championnat des Services JJA</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

<header>
    <div class="header-content">
        <h1>CHAMPIONNAT DES SERVICES JJA</h1>
        <p>Coupe du Monde 2026 - Mon Petit Prono</p>
    </div>
</header>

<nav class="menu">
    <a href="index.html">🏆 Accueil</a>
    <a href="actualites.html">📰 Actualités</a>
</nav>

<div class="container">

    <div class="hero-card">

        <h2>🏆 À LA UNE</h2>

        <h1>{leader_joueur}</h1>

        <p>
            MVP actuel avec <strong>{leader_points} points</strong>
        </p>

        <hr>

        <p>
            🥇 Service leader :
            <strong>{leader_service}</strong>
            ({leader_moyenne} points de moyenne)
        </p>

    </div>

    <div class="grid">

        <div class="card">
            <h2>⭐ MVP</h2>

            {mvp.to_html(index=False)}
        </div>

        <div class="card">
            <h2>🎯 Snipers</h2>

            {snipers.to_html(index=False)}
        </div>

    </div>
"""

# ========================================
# Progressions
# ========================================

if len(progressions) > 0:

    html += f"""
    <div class="card full-width">

        <h2>📈 Plus fortes progressions</h2>

        {progressions.to_html(index=False)}

    </div>
    """

# ========================================
# Chutes
# ========================================

if len(chutes) > 0:

    html += f"""
    <div class="card full-width">

        <h2>📉 Plus grosses chutes</h2>

        {chutes.to_html(index=False)}

    </div>
    """

# ========================================
# Classement services
# ========================================

html += f"""

    <div class="card full-width">

        <h2>🏢 Classement des services</h2>

        {services.to_html(index=False)}

    </div>

    <div class="card full-width">

        <h2>👥 Classement individuel complet</h2>

        {classement.to_html(index=False)}

    </div>

</div>

</body>
</html>
"""

# ========================================
# Sauvegarde
# ========================================

with open(
    "index.html",
    "w",
    encoding="utf-8"
) as f:

    f.write(html)

print()
print("🌐 Site web créé : index.html")