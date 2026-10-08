def ajouter_etudiant(d, nom, note):
    d[nom] = float(note)


def moyenne_classe(d):
    if len(d) == 0:
        return 0

    return sum(d.values()) / len(d)


def meilleur_etudiant(d):
    if len(d) == 0:
        return None

    nom = max(d, key=d.get)
    return nom, d[nom]


def sauvegarder(d, fichier):
    try:
        with open(fichier, "w") as f:
            for nom, note in d.items():
                f.write(f"{nom}:{note}\n")
    except Exception as e:
        print("Erreur :", e)


def charger(fichier):
    d = {}

    try:
        with open(fichier, "r") as f:
            for ligne in f:
                try:
                    nom, note = ligne.strip().split(":")
                    d[nom] = float(note)
                except:
                    pass

    except FileNotFoundError:
        print("Fichier absent")

    return d


etudiants = {}

ajouter_etudiant(etudiants, "Alice", 12)
ajouter_etudiant(etudiants, "Bob", 15)
ajouter_etudiant(etudiants, "Claire", 9.5)

print("Moyenne :", moyenne_classe(etudiants))
print("Meilleur :", meilleur_etudiant(etudiants))

sauvegarder(etudiants, "notes.txt")

d = charger("notes.txt")
print(d)
input("Appuie sur Entrée pour quitter...")