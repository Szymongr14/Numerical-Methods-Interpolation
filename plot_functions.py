import pandas as pd
import matplotlib.pyplot as plt


def generate_plot_from_data(file_name, title):
    df = pd.read_csv(file_name)
    x = df["Dystans (m)"]
    y = df["Wysokość (m)"]
    plt.figure()
    plt.plot(x, y)
    plt.xlabel("Odgległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.title(title)
    plt.show()


def plot_nodes(x, y, title):
    plt.figure()
    plt.plot(x, y, 'bx')
    plt.xlabel("Odgległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.title(title)
    plt.show()


def plot_interpolated_function(x, y_interpolated, y_original, chosen_nodes,  title):
    plt.figure(figsize=(10, 6))
    plt.plot(x, y_interpolated, 'g')
    plt.plot(x, y_original, 'r--')
    plt.scatter(chosen_nodes[0], chosen_nodes[1], s=10, color='blue')

    plt.xlabel("Odgległość [m]")
    plt.ylabel("Wysokość [m]")
    plt.legend(["Funkcja interpolująca", "Oryginalna funkcja", "Wybrane węzły"])
    plt.title(title)
    plt.show()
