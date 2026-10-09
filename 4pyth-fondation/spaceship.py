from person import Operator, Mentalist


class Spaceship:
    """Représente un vaisseau spatial et son équipage."""

    # Nombre maximum de membres par vaisseau
    MAX_CREW = 10

    def __init__(self, name, ship_type, condition="opérationnel"):
        """Initialise un nouveau vaisseau."""

        self.name = name
        self.ship_type = ship_type
        self.condition = condition

        # Liste vide au départ
        self.crew = []

    def find_member(self, name):
        """Recherche un membre par son nom."""

        # Parcourt les membres du vaisseau
        for member in self.crew:

            # Compare les noms sans tenir compte des majuscules
            member_name = member.last_name or member.first_name

            if member_name.lower() == name.strip().lower():
                return member

        return None  # Aucun membre trouvé

    def add_member(self, member):
        """Ajoute un membre à l'équipage."""

        # Vérifie que le membre est un Operator ou un Mentalist
        if not isinstance(member, (Operator, Mentalist)):
            raise ValueError("Le membre doit être un opérateur ou un mentaliste.")

        # Vérifie la capacité maximale
        if len(self.crew) >= self.MAX_CREW:
            raise ValueError("Le vaisseau est plein.")

        # Vérifie si ce nom existe déjà à bord
        member_name = member.last_name or member.first_name

        if self.find_member(member_name) is not None:
            raise ValueError("Ce nom existe déjà à bord.")

        # Ajoute le membre au vaisseau
        self.crew.append(member)

    def remove_member(self, name):
        """Supprime un membre et renvoie l'objet supprimé."""

        # Recherche le membre
        member = self.find_member(name)

        if member is not None:
            self.crew.remove(member)

        return member  # Renvoie None si introuvable

    def check_preparation(self):
        """Vérifie la présence d'un pilote et d'un technicien."""

        has_pilot = False
        has_technician = False

        # Parcourt l'équipage
        for member in self.crew:

            # Les mentalistes n'ont pas de rôle
            if isinstance(member, Operator):

                if member.role == "pilote":
                    has_pilot = True

                if member.role == "technicien":
                    has_technician = True

        return has_pilot and has_technician

    def watch_round(self):
        """Fait agir tous les membres de l'équipage."""

        for member in self.crew:
            member.act()

    def __str__(self):
        """Affiche les informations du vaisseau."""

        return (
            f"{self.name} ({self.ship_type}, {self.condition}) "
            f"– {len(self.crew)} membres"
        )