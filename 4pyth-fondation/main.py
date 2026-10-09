from crew import (
    build_fleet,
    add_fleet_member,
    remove_fleet_member,
    display_fleet,
    check_spaceship
)

from fleet_data import FLEET_DATA
from spaceship import Spaceship


def main():
    """Lance le menu interactif de gestion de la flotte."""

    # Construit les 5 vaisseaux et les 24 membres
    fleet = build_fleet(FLEET_DATA)

    # Répète le menu jusqu'à ce que l'utilisateur quitte
    while True:

        print("\n===== FLOTTE GALACTICA =====")
        print("1 - Ajouter un membre")
        print("2 - Retirer un membre")
        print("3 - Afficher la flotte")
        print("4 - Vérifier un vaisseau")
        print("5 - Ajouter un vaisseau")
        print("6 - Statistiques de la flotte")
        print("0 - Quitter")

        # Récupère le choix de l'utilisateur
        choice = input("Votre choix : ").strip()

        # Intercepte les erreurs envoyées par les classes
        try:
            match choice:

                case "1":
                    add_fleet_member(fleet)

                case "2":
                    remove_fleet_member(fleet)

                case "3":
                    display_fleet(fleet)

                case "4":
                    check_spaceship(fleet)

                case "5":
                    print("\n===== AJOUT D'UN VAISSEAU =====")

                    name = input("Nom du vaisseau : ").strip()
                    ship_type = input(
                        "Type (transport/guerre/marchand) : "
                    ).strip().lower()

                    if not name:
                        print("Erreur : le nom ne peut pas être vide.")
                        continue

                    if ship_type not in ["transport", "guerre", "marchand"]:
                        print("Erreur : type de vaisseau invalide.")
                        continue

                    # Crée et ajoute le nouveau vaisseau
                    spaceship = Spaceship(name, ship_type)
                    fleet.add_spaceship(spaceship)

                    print(f"Vaisseau {name} ajouté à la flotte !")

                case "6":
                    fleet.statistics()

                case "0":
                    print("Fermeture du programme.")
                    break

                case _:
                    print("Choix invalide, veuillez réessayer.")

        except ValueError as error:
            # Affiche l'erreur sans arrêter le programme
            print(f"Erreur : {error}")


# Lance le menu uniquement si ce fichier est exécuté directement
if __name__ == "__main__":
    main()