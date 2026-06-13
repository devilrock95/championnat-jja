import pandas as pd

# ==========================
# Lecture des articles
# ==========================

articles = pd.read_excel("articles.xlsx")

# Tri du plus récent au plus ancien
articles = articles.sort_values(
    by="Date",
    ascending=False
)

# ==========================
# Dernier article
# ==========================

une = articles.iloc[0]

# ==========================
# Début HTML
# ==========================

html = f"""
<!DOCTYPE html>
<html lang="fr">

<head>

<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>Actualités - Championnat des Services JJA</title>

<link rel="stylesheet" href="style.css">

</head>

<body>

<header>
    <h1>CHAMPIONNAT DES SERVICES JJA</h1>
    <p>Coupe du Monde 2026 - Actualités</p>
</header>

<nav class="menu">
    <a href="index.html">🏆 Accueil</a>
    <a href="actualites.html">📰 Actualités</a>
</nav>

<div class="container">

<div class="hero-card">

<h2>📰 À LA UNE</h2>

<h1>{une['Titre']}</h1>

<p>{une['Résumé']}</p>

<p>
<a href="articles/{une['Fichier']}">
➜ Lire l'article complet
</a>
</p>

</div>

<div class="card">

<h2>📰 Dernières actualités</h2>

"""

# ==========================
# Liste des articles
# ==========================

for _, article in articles.iterrows():

    html += f"""

    <h3>
    <a href="articles/{article['Fichier']}">
    {article['Titre']}
    </a>
    </h3>

    <p>
    <strong>{article['Date']}</strong>
    </p>

    <p>
    {article['Résumé']}
    </p>

    <p>
    <a href="articles/{article['Fichier']}">
    ➜ Lire l'article complet
    </a>
    </p>

    <hr>

    """

# ==========================
# Fin HTML
# ==========================

html += """

</div>

</div>

</body>

</html>

"""

# ==========================
# Sauvegarde
# ==========================

with open(
    "actualites.html",
    "w",
    encoding="utf-8"
) as f:

    f.write(html)

print()
print("📰 actualites.html généré")