COMMON_PASSWORDS = [
    "123456", "password", "azerty", "qwerty", "motdepasse",
    "admin", "letmein", "iloveyou", "000000", "azertyuiop",
    "Password123!", "Azerty123456!",
]


def check_password(password, is_admin=False):
    errors = []

    # Longueur minimale
    min_length = 16 if is_admin else 12

    if len(password) < min_length:
        errors.append(f"au moins {min_length} caractères")

    # Vérification des différents caractères
    has_upper = False   #majuscule
    has_lower = False   #minuscule
    has_digit = False   #chiffre
    has_special = False #special

    for char in password:
        if char.isupper():
            has_upper = True

        if char.islower():
            has_lower = True

        if char.isdigit():
            has_digit = True

        if not char.isalnum():
            has_special = True

    if not has_upper:
        errors.append("au moins une majuscule")

    if not has_lower:
        errors.append("au moins une minuscule")

    if not has_digit:
        errors.append("au moins un chiffre")

    if not has_special:
        errors.append("au moins un caractère spécial")
    
    # Vérification des mots de passe courants
    common_lower = []

    for common_password in COMMON_PASSWORDS:
        common_lower.append(common_password.lower())

    if password.lower() in common_lower:
        errors.append("ne doit pas être un mot de passe courant")

    return len(errors) == 0, errors

print(check_password("Tr0ub4dour&Co"))
print(check_password("Azerty123456!"))
print(check_password("azerty"))
print(check_password("correct horse battery staple"))
print(check_password("Tr0ub4dour&Co", is_admin=True))