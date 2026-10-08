import random

secret = random.randint(1, 100)

essais = 0
max_essais = 10

while essais < max_essais:

    proposition = int(input("Votre nombre : "))
    essais += 1

    if proposition < secret:
        print("Trop petit")

    elif proposition > secret:
        print("Trop grand")

    else:
        print("Gagné")
        break

if proposition != secret:
    print("Perdu")
    print("Le nombre était", secret)
    input("Appuie sur Entrée pour quitter...")