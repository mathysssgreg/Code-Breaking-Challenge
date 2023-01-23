import random

# Liste des lettres disponibles pour les codes
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Fonction pour générer un code aléatoire
def generate_code(difficulty):
    code = ""
    for i in range(difficulty):
        code += random.choice(LETTERS)
    return code

# Fonction pour déchiffrer le code
def decrypt_code(code, guess):
    decrypted = ""
    for i in range(len(code)):
        decrypted += chr((ord(guess[i]) - ord(code[i])) % 26 + ord("A"))
    return decrypted

# Niveau de difficulté
difficulty = 4

# Code à déchiffrer
code = generate_code(difficulty)

# Boucle de jeu
while True:
    # Demander au joueur de deviner le code
    guess = input("Devinez le code (4 lettres majuscules): ").upper()

    # Vérifier si le code deviné est correct
    if guess == code:
        print("Félicitations ! Vous avez déchiffré le code.")
        break
    else:
        print("Code erroné. Voici un indice :", decrypt_code(code, guess))
