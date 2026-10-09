# Liste des rôles autorisés pour les opérateurs
ROLES = [
    "commandant",
    "pilote",
    "technicien",
    "armurier",
    "marchand",
    "entretien"
]

# Action correspondant à chaque rôle
ACTIONS = {
    "commandant": "donne ses ordres à l'équipage",
    "pilote": "pilote le vaisseau",
    "technicien": "répare les moteurs",
    "armurier": "vérifie les canons",
    "marchand": "négocie une cargaison",
    "entretien": "nettoie le vaisseau"
}

class Person:
    """Représente une personne de la flotte."""

    def __init__(self, first_name, last_name, gender, age):
        """Initialise les informations de la personne."""

        # Enregistre les informations dans l'objet
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    @property
    def name(self):
        """Renvoie le prénom et le nom sans espaces inutiles."""

        # strip() évite un espace en trop si le nom est vide
        return f"{self.first_name} {self.last_name}".strip()

    def introduce_yourself(self):
        """Renvoie une phrase de présentation."""

        # Détermine le texte selon le genre
        gender_text = "homme" if self.gender == "M" else "femme"

        return (
            f"Je m'appelle {self.name}, "
            f"je suis un{'e' if self.gender == 'F' else ''} "
            f"{gender_text} de {self.age} ans."
        )

    def __str__(self):
        """Définit l'affichage de la personne."""

        return f"{self.name} ({self.gender}, {self.age} ans)"
    
class Operator(Person):
    """Représente un opérateur avec un rôle et de l'expérience."""

    def __init__(self, first_name, last_name, gender, age, role, experience=0):
        """Initialise un opérateur."""

        # Récupère les attributs de la classe mère Person
        super().__init__(first_name, last_name, gender, age)

        # Passe par le setter pour vérifier le rôle
        self.role = role

        # Initialise l'expérience à 0 par défaut
        self.experience = experience

    @property
    def role(self):
        """Renvoie le rôle de l'opérateur."""
        return self._role

    @role.setter
    def role(self, value):
        """Vérifie que le rôle est autorisé."""

        # Convertit le rôle en minuscules
        value = value.strip().lower()

        if value not in ROLES:
            raise ValueError(f"Rôle inconnu : {value}")

        # Enregistre le rôle après validation
        self._role = value

    def gain_experience(self):
        """Augmente l'expérience de 1."""

        self.experience += 1

    def act(self):
        """Effectue l'action correspondant au rôle."""

        # Récupère l'action dans le dictionnaire ACTIONS
        action = ACTIONS[self.role]

        print(f"{self.name} {action}.")

        # Chaque action rapporte un point d'expérience
        self.gain_experience()

    def __str__(self):
        """Affiche les informations et le rôle de l'opérateur."""

        # Réutilise l'affichage de la classe Person
        return f"{super().__str__()} – {self.role}"
    
class Mentalist(Person):
    """Représente un mentaliste de la Seconde Fondation."""

    def __init__(self, first_name, last_name, gender, age, mana=100):
        """Initialise le mentaliste avec 100 points de mana par défaut."""

        # Récupère les attributs de Person
        super().__init__(first_name, last_name, gender, age)

        # Initialise le mana en passant par le setter
        self.mana = mana

    @property
    def mana(self):
        """Renvoie les points de mana."""
        return self._mana

    @mana.setter
    def mana(self, value):
        """Limite le mana entre 0 et 100."""

        # Empêche le mana de descendre sous 0 ou dépasser 100
        self._mana = max(0, min(value, 100))

    def act(self):
        """Le mentaliste se concentre et regagne 10 points de mana."""

        print(f"{self.name} se concentre.")
        self.mana += 10

    def recharge_mana(self):
        """Recharge 50 points de mana."""

        self.mana += 50

    def influence(self, operator):
        """Utilise 20 points de mana pour faire agir un opérateur."""

        # Vérifie si le mentaliste possède assez de mana
        if self.mana < 20:
            print(f"{self.name} n'a pas assez de mana pour influencer {operator.name}.")
            return False

        # Retire 20 points de mana
        self.mana -= 20

        print(f"{self.name} influence {operator.name}.")

        # Force l'opérateur à effectuer son action
        operator.act()

        return True

    def __str__(self):
        """Affiche les informations du mentaliste."""

        return f"{super().__str__()} – mentaliste, {self.mana} mana"