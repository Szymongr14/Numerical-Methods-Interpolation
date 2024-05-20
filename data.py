import pandas as pd


def return_all_nodes(filename) -> [[], []]:
    df = pd.read_csv(filename)
    x = df["Dystans (m)"]
    y = df["Wysokość (m)"]
    return x, y
