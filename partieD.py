import random

mots = ["PYTHON", "RESEAU", "TELECOM"]

mot = random.choice(mots)

masque = ["_"] * len(mot)

lettres_proposees = []

erreurs = 0
max_erreurs = 7

while erreurs < max_erreurs and "_" in masque:

    print("\nMot :", " ".join(masque))
    print("Erreurs :", erreurs)
    print("Lettres :", lettres_proposees)

    lettre = input("Lettre : ").upper()

    if lettre in lettres_proposees:
        print("Déjà proposée")
        continue

    lettres_proposees.append(lettre)

    if lettre in mot:

        for i in range(len(mot)):
            if mot[i] == lettre:
                masque[i] = lettre

        print("Bonne lettre")

    else:
        erreurs += 1
        print("Mauvaise lettre")

if "_" not in masque:
    print("Gagné")
else:
    print("Perdu")
    print("Le mot était", mot)

    input("Appuie sur Entrée pour quitter...")