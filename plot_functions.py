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
