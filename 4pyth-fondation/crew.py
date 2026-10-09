from person import Operator, Mentalist
from spaceship import Spaceship
from fleet import Fleet

# Liste des rôles autorisés
ROLES = ["commandant", "pilote", "technicien", "armurier", "marchand", "entretien"]


def add_member(crew):
    """Ajoute un membre à l'équipage après validation des informations."""

    print("\n===== AJOUT D'UN MEMBRE =====")

    # Demande un prénom entre 3 et 15 caractères
    while True:
        first_name = input("Prénom : ").strip()

        if 3 <= len(first_name) <= 15:
            break

        print("Erreur : le prénom doit contenir entre 3 et 15 caractères.")

    # Demande un nom entre 3 et 15 caractères, qui n'existe pas déjà
    while True:
        last_name = input("Nom : ").strip()

        if not 3 <= len(last_name) <= 15:
            print("Erreur : le nom doit contenir entre 3 et 15 caractères.")
            continue

        # Vérifie si le nom existe déjà dans l'équipage
        duplicate = any(
            member["last_name"].lower() == last_name.lower()
            for member in crew
        )

        if duplicate:
            print("Erreur : ce nom existe déjà dans l'équipage.")
            continue

        break

    # Accepte uniquement F ou M
    while True:
        gender = input("Genre (F/M) : ").strip().upper()

        if gender in ["F", "M"]:
            break

        print("Erreur : saisissez F ou M.")

    # Vérifie que l'âge contient uniquement des chiffres
    while True:
        age_input = input("Âge : ").strip()

        if age_input.isdigit():
            age = int(age_input)
            break

        print("Erreur : saisissez un âge en chiffres.")

    # Vérifie que le rôle fait partie des rôles autorisés
    while True:
        role = input("Rôle : ").strip().lower()

        if role in ROLES:
            break

        print("Erreur : rôle invalide.")
        print("Rôles disponibles :", ", ".join(ROLES))

    # Crée le dictionnaire du nouveau membre
    member = {
        "first_name": first_name,
        "last_name": last_name,
        "gender": gender,
        "age": age,
        "role": role
    }

    # Ajoute le membre à la liste
    crew.append(member)

    print(f"\n{first_name} {last_name} a été ajouté à l'équipage !")
    return crew

def remove_member(crew):
    """Supprime un membre de l'équipage à partir de son nom."""

    print("\n===== SUPPRESSION D'UN MEMBRE =====")

    # Demande le nom du membre à supprimer
    last_name = input("Nom du membre à supprimer : ").strip()

    # Parcourt les membres de l'équipage
    for member in crew:

        # Compare les noms sans tenir compte des majuscules
        if member["last_name"].lower() == last_name.lower():

            # Supprime le membre trouvé
            crew.remove(member)

            print(f"{member['first_name']} {member['last_name']} a été supprimé.")
            return True  # Suppression réussie

    # Aucun membre ne correspond au nom saisi
    print("Erreur : aucun membre trouvé avec ce nom.")
    return False

def display_crew(crew):
    # Vérifie si la liste de l'équipage est vide
    if not crew:
        print("L'équipage est vide.")
        return

    # Affiche le nombre total de membres
    print("\n===== LISTE DE L'ÉQUIPAGE =====")
    print(f"Nombre de membres : {len(crew)}")

    # Parcourt et affiche chaque membre
    for index, member in enumerate(crew, start=1):
        print(f"\nMembre n°{index}")
        print(f"Prénom : {member['first_name']}")
        print(f"Nom : {member['last_name']}")
        print(f"Genre : {member['gender']}")
        print(f"Âge : {member['age']} ans")
        print(f"Rôle : {member['role']}")

    print("==============================")
    
def check_crew(crew):
    """Vérifie si l'équipage est prêt pour la mission."""

    # Vérifie si l'équipage contient au moins 2 membres
    enough_members = len(crew) >= 2

    # Vérifie si un pilote est présent
    has_pilot = False

    # Vérifie si un technicien est présent
    has_technician = False

    # Parcourt tous les membres pour vérifier leurs rôles
    for member in crew:
        if member["role"] == "pilote":
            has_pilot = True

        if member["role"] == "technicien":
            has_technician = True

    # Vérifie si toutes les conditions sont respectées
    if enough_members and has_pilot and has_technician:
        print("L'équipage est prêt pour la mission !")
        return True

    # Affiche les conditions non respectées
    print("L'équipage n'est pas prêt pour la mission.")

    if not enough_members:
        print("- Il faut au moins 2 membres.")

    if not has_pilot:
        print("- Il manque un pilote.")

    if not has_technician:
        print("- Il manque un technicien.")

    return False

def build_fleet(data):
    """Transforme les dictionnaires en objets Fleet, Spaceship et Person."""

    # Crée la flotte avec son nom
    fleet = Fleet(data["name"])

    # Parcourt tous les vaisseaux présents dans les données
    for ship_data in data["spaceships"]:

        # Crée un objet Spaceship
        spaceship = Spaceship(
            ship_data["name"],
            ship_data["ship_type"],
            ship_data["condition"]
        )

        # Parcourt les membres du vaisseau
        for member_data in ship_data["crew"]:

            # Vérifie si le membre est un opérateur
            if member_data["type"] == "operator":

                member = Operator(
                    member_data["first_name"],
                    member_data["last_name"],
                    member_data["gender"],
                    member_data["age"],
                    member_data["role"]
                )

            # Vérifie si le membre est un mentaliste
            elif member_data["type"] == "mentalist":

                member = Mentalist(
                    member_data["first_name"],
                    member_data["last_name"],
                    member_data["gender"],
                    member_data["age"],
                    member_data["mana"]
                )

            else:
                # Refuse un type de membre inconnu
                raise ValueError("Type de membre inconnu.")

            # Ajoute le membre au vaisseau
            spaceship.add_member(member)

        # Ajoute le vaisseau complet à la flotte
        fleet.add_spaceship(spaceship)

    # Renvoie la flotte avec tous ses vaisseaux
    return fleet

def choose_spaceship(fleet):
    """Demande à l'utilisateur de choisir un vaisseau."""

    # Affiche les vaisseaux disponibles
    print("\n===== VAISSEAUX DISPONIBLES =====")

    for spaceship in fleet.spaceships:
        print(f"- {spaceship.name}")

    # Demande le nom du vaisseau
    name = input("Nom du vaisseau : ").strip()

    # Recherche le vaisseau dans la flotte
    spaceship = fleet.find_spaceship(name)

    if spaceship is None:
        print("Erreur : vaisseau introuvable.")

    return spaceship

def add_fleet_member(fleet):
    """Ajoute un opérateur ou un mentaliste à un vaisseau."""

    spaceship = choose_spaceship(fleet)

    # Arrête la fonction si le vaisseau n'existe pas
    if spaceship is None:
        return

    # Demande le type de membre
    member_type = input("Type (operator/mentalist) : ").strip().lower()

    if member_type not in ["operator", "mentalist"]:
        print("Erreur : type de membre invalide.")
        return

    # Informations communes aux deux types
    first_name = input("Prénom : ").strip()
    last_name = input("Nom : ").strip()
    gender = input("Genre (F/M) : ").strip().upper()

    # Vérifie le genre
    if gender not in ["F", "M"]:
        print("Erreur : genre invalide.")
        return

    # Vérifie que l'âge est un nombre
    age_input = input("Âge : ").strip()

    if not age_input.isdigit():
        print("Erreur : âge invalide.")
        return

    age = int(age_input)

    # Crée l'objet selon le type choisi
    if member_type == "operator":

        role = input("Rôle : ").strip().lower()

        member = Operator(
            first_name, last_name, gender, age, role
        )

    else:
        member = Mentalist(
            first_name, last_name, gender, age
        )

    # Ajoute le membre au vaisseau
    spaceship.add_member(member)

    print(f"{member.name} a été ajouté au vaisseau {spaceship.name}.")
    
def remove_fleet_member(fleet):
    """Supprime un membre d'un vaisseau."""

    spaceship = choose_spaceship(fleet)

    if spaceship is None:
        return

    # Nom de famille, ou prénom si le membre n'en possède pas
    name = input("Nom du membre à supprimer : ").strip()

    member = spaceship.remove_member(name)

    if member is None:
        print("Erreur : membre introuvable.")
    else:
        print(f"{member.name} a été supprimé de {spaceship.name}.")
        
def display_fleet(fleet):
    """Affiche tous les vaisseaux et leurs membres."""

    print(f"\n===== FLOTTE {fleet.name.upper()} =====")

    for spaceship in fleet.spaceships:
        print(f"\n{spaceship}")

        # Affiche les membres de chaque vaisseau
        for member in spaceship.crew:
            print(f"  - {member}")


def check_spaceship(fleet):
    """Vérifie si un vaisseau est prêt."""

    spaceship = choose_spaceship(fleet)

    if spaceship is None:
        return

    if spaceship.check_preparation():
        print(f"{spaceship.name} est prêt pour la mission !")
    else:
        print(f"{spaceship.name} n'est pas prêt : pilote ou technicien manquant.")