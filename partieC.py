import random

mots = [
    "python",
    "ordinateur",
    "reseau",
    "telecom"
]

def choisir_mot(liste):
    return random.choice(liste).upper()


def creer_masque(mot):
    return ["_"] * len(mot)


mot = choisir_mot(mots)

print("Mot :", mot)
print("Masque :", creer_masque(mot))
input("Appuie sur Entrée pour quitter...")