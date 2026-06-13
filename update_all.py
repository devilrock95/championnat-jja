import os

print()
print("🏆 MISE À JOUR DU CHAMPIONNAT JJA")
print("=" * 40)

scripts = [
    "maj_mpp.py",
    "calcul_classements.py",
    "mvp.py",
    "snipers.py",
    "historique.py",
    "progression.py",
    "chutes.py",
    "dashboard.py"
]

for script in scripts:

    print()
    print(f"▶ Exécution de {script}")

    resultat = os.system(f"python {script}")

    if resultat != 0:
        print(f"❌ Erreur dans {script}")
    else:
        print(f"✅ {script} terminé")

print()
print("=" * 40)
print("🎉 Mise à jour terminée")
print("🌐 Pense à actualiser index.html")
print()