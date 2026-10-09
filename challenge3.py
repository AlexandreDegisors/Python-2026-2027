import secrets
import string

from challenge1 import check_password


def generate_password(length=16):

    # Refuse une longueur inférieure à 12
    if length < 12:
        raise ValueError("longueur minimale : 12")
    # Catégories de caractères
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*_-+=?"

    # Garantit au moins un caractère de chaque catégorie
    password = [
        secrets.choice(uppercase),
        secrets.choice(lowercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Regroupe tous les caractères possibles
    all_characters = uppercase + lowercase + digits + special

    # Complète jusqu'à la longueur demandée
    while len(password) < length:
        password.append(secrets.choice(all_characters))

    # Mélange les caractères
    secrets.SystemRandom().shuffle(password)

    # Transforme la liste en texte
    return "".join(password)


if __name__ == "__main__":

    # Tests avec différentes longueurs
    print(generate_password())
    print(generate_password(24))

    # Test d'une longueur interdite
    try:
        generate_password(8)

    except ValueError as error:
        print("ValueError:", error)

    # Vérification de 1000 mots de passe avec le challenge 1
    invalid_count = 0

    for i in range(1000):

        password = generate_password()

        valid, errors = check_password(password)

        if not valid:
            invalid_count += 1

    print("Mots de passe invalides sur 1000 :", invalid_count)