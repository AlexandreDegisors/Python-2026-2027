from spaceship import Spaceship
from person import Operator, Mentalist


class Fleet:
    """Représente une flotte composée de plusieurs vaisseaux."""

    # Nombre maximum de vaisseaux autorisés
    MAX_SPACESHIPS = 15

    def __init__(self, name):
        """Initialise une flotte avec un nom et une liste vide."""

        self.name = name
        self.spaceships = []

    def find_spaceship(self, name):
        """Recherche un vaisseau par son nom."""

        # Parcourt tous les vaisseaux
        for spaceship in self.spaceships:

            # Compare les noms sans tenir compte des majuscules
            if spaceship.name.lower() == name.strip().lower():
                return spaceship

        return None  # Aucun vaisseau trouvé

    def add_spaceship(self, spaceship):
        """Ajoute un vaisseau à la flotte."""

        # Vérifie que l'objet est bien un vaisseau
        if not isinstance(spaceship, Spaceship):
            raise ValueError("L'objet doit être un vaisseau.")

        # Vérifie la capacité maximale de la flotte
        if len(self.spaceships) >= self.MAX_SPACESHIPS:
            raise ValueError("La flotte est pleine.")

        # Vérifie si le nom du vaisseau existe déjà
        if self.find_spaceship(spaceship.name) is not None:
            raise ValueError("Ce nom de vaisseau existe déjà.")

        # Ajoute le vaisseau à la flotte
        self.spaceships.append(spaceship)

    def statistics(self):
        """Affiche les statistiques de la flotte."""

        # Compteurs des membres et des vaisseaux prêts
        total_members = 0
        ready_ships = 0
        mentalists = 0

        # Dictionnaire pour compter les rôles
        roles_count = {}

        # Liste pour calculer l'expérience moyenne
        experiences = []

        # Parcourt tous les vaisseaux
        for spaceship in self.spaceships:

            # Compte les membres du vaisseau
            total_members += len(spaceship.crew)

            # Vérifie si le vaisseau est prêt
            if spaceship.check_preparation():
                ready_ships += 1

            # Parcourt les membres du vaisseau
            for member in spaceship.crew:

                if isinstance(member, Operator):

                    # Compte les opérateurs selon leur rôle
                    role = member.role
                    roles_count[role] = roles_count.get(role, 0) + 1

                    # Enregistre leur expérience
                    experiences.append(member.experience)

                elif isinstance(member, Mentalist):

                    # Compte les mentalistes séparément
                    mentalists += 1

        # Calcule l'expérience moyenne sans division par zéro
        if experiences:
            average_experience = sum(experiences) / len(experiences)
        else:
            average_experience = 0.0

        # Affiche les résultats
        print(f"\nFlotte {self.name} : "
              f"{len(self.spaceships)} vaisseaux, {total_members} membres")

        for role, count in roles_count.items():
            print(f"  {role} : {count}")

        print(f"  mentaliste : {mentalists}")

        print(f"Expérience moyenne des opérateurs : {average_experience:.1f}")

        print(f"Vaisseaux prêts : {ready_ships} / {len(self.spaceships)}")