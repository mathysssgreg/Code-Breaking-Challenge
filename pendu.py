# La liste des mots possibles
mots = ["chat", "chien", "souris", "ordinateur", "voiture", "avion"]

# Choisir un mot aléatoirement
mot_a_trouver = random.choice(mots)

# Initialiser les variables
lettres_devinees = []
erreurs = 0

# Boucle de jeu
while erreurs < 6:
    mot_masque = ""
    for lettre in mot_a_trouver:
        if lettre in lettres_devinees:
            mot_masque += lettre
        else:
            mot_masque += "_"

    if "_" not in mot_masque:
        print("Félicitations ! Vous avez trouvé le mot :", mot_masque)
        break

    print("Mot à deviner :", mot_masque)
    lettre_devinee = input("Devinez une lettre : ").lower()

    if lettre_devinee in mot_a_trouver:
        lettres_devinees.append(lettre_devinee)
    else:
        erreurs += 1
        print("La lettre ne se trouve pas dans le mot. Il vous reste", 6 - erreurs, "erreur(s) avant de perdre.")

if erreurs == 6:
    print("Désolé, vous avez perdu. Le mot était", mot_a_trouver + ".")
