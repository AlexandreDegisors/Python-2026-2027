from fleet_data import FLEET_DATA
from crew import build_fleet

# Construit automatiquement la flotte
fleet = build_fleet(FLEET_DATA)

# Affiche tous les vaisseaux
print("\n===== VAISSEAUX DE LA FLOTTE =====")

for spaceship in fleet.spaceships:
    print(spaceship)

# Affiche les statistiques générales
print("\n===== STATISTIQUES =====")
fleet.statistics()