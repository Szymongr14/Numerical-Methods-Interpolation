from plot_functions import generate_plot_from_data
from interpolations import interpolate_lagrange, interpolate_spline

START_INDEX, END_INDEX = 0, 511
NUMBER_OF_NODES = 50

# generate_plot_from_data("tracks/MountEverest.csv", "Mount Everest")
# generate_plot_from_data("tracks/GlebiaChallengera.csv", "Głębia Challenger")
# generate_plot_from_data("tracks/SpacerniakGdansk.csv", "Specerniak Gdańsk")
# generate_plot_from_data("tracks/stale.txt", "Stałe wzniesienie")

# interpolate_lagrange("tracks/MountEverest.csv", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Mount Everest", use_chebychev_nodes=True)
# interpolate_lagrange("tracks/GlebiaChallengera.csv", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Głębia Challenger", True)
interpolate_lagrange("tracks/Obiadek.csv", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Obiadek", True)
# interpolate_lagrange("tracks/SpacerniakGdansk.csv", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Specerniak Gdańsk", True)
# interpolate_lagrange("tracks/stale.txt", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Stałe wzniesienie", True)
# interpolate_spline("tracks/MountEverest.csv", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Mount Everest")
# interpolate_spline("tracks/GlebiaChallengera.csv", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Głębia Challenger")
interpolate_spline("tracks/Obiadek.csv", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Obiadek")
# interpolate_spline("tracks/SpacerniakGdansk.csv", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Specerniak Gdańsk")
# interpolate_spline("tracks/stale.txt", START_INDEX, END_INDEX, NUMBER_OF_NODES, "Stałe wzniesienie")

