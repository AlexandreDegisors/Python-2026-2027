# Liste des membres de l'équipage
# Chaque membre est représenté par un dictionnaire

crew = [
    {"first_name": "Bel", "last_name": "Riose", "gender": "M", "age": 48, "role": "commandant"},
    {"first_name": "Gaal", "last_name": "Dornick", "gender": "F", "age": 34, "role": "technicien"},
    {"first_name": "Hugo", "last_name": "Crast", "gender": "M", "age": 37, "role": "pilote"},
    {"first_name": "Salvor", "last_name": "Hardin", "gender": "F", "age": 28, "role": "armurier"},
    {"first_name": "Novi", "last_name": "Sura", "gender": "F", "age": 25, "role": "entretien"},
]

# Test temporaire pour afficher l'équipage
if __name__ == "__main__":
    for member in crew:
        print(member)