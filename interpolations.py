import numpy as np
from matrix_operations import *

from data import return_all_nodes
from plot_functions import plot_interpolated_function


def lagrange_interpolation_internal(known_nodes, x) -> float:
    x_values = known_nodes[0]
    y_values = known_nodes[1]
    n = len(x_values)
    result = 0
    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if i != j:
                term *= (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term
    return result


def chebyshev_nodes(a, b, N):
    return a + 0.5 * (b - a) * (1 + np.cos(np.arange(N + 1) * np.pi / N))


def interpolate_lagrange(filename, start, end, number_of_nodes, title, use_chebychev_nodes=False):
    all_nodes = return_all_nodes(filename)
    if use_chebychev_nodes:
        indexes = chebyshev_nodes(start, end, number_of_nodes)
        indexes = np.round(indexes).astype(int)
        chosen_nodes = ([all_nodes[0][i] for i in indexes],
                        [all_nodes[1][i] for i in indexes])
    else:
        indexes = uniformly_choose_nodes(start, end, number_of_nodes)
        chosen_nodes = ([all_nodes[0][i] for i in indexes],
                        [all_nodes[1][i] for i in indexes])

    interpolated_values = []
    for i in range(end + 1):
        (interpolated_values.
         append(lagrange_interpolation_internal(chosen_nodes, all_nodes[0][i])))

    plot_interpolated_function(all_nodes[0],
                               interpolated_values,
                               all_nodes[1],
                               chosen_nodes,
                               f"Interpolacja Lagrange'a dla {title}, {number_of_nodes} węzłów, węzły Chebysheva")


def uniformly_choose_nodes(a, b, n):
    return [a + i * (b - a) // n for i in range(n + 1)]


def construct_spline_matrix(x, y):
    n = len(x) - 1  # number of intervals
    h = [x[i + 1] - x[i] for i in range(n)]  # lengths of intervals

    A = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    b = [0 for _ in range(n + 1)]

    for i in range(1, n):
        A[i][i] = 2 * (h[i - 1] + h[i])
        A[i][i + 1] = h[i]
        A[i][i - 1] = h[i - 1]
        b[i] = 6 * ((y[i + 1] - y[i]) / h[i] - (y[i] - y[i - 1]) / h[i - 1])

    A[0][0] = 1
    A[-1][-1] = 1

    return A, b


def construct_splines(x, y, m):
    n = len(x) - 1
    h = [x[i + 1] - x[i] for i in range(n)]

    splines = []
    for i in range(n):
        a = y[i]
        b = (y[i + 1] - y[i]) / h[i] - h[i] * (2 * m[i] + m[i + 1]) / 6
        c = m[i] / 2
        d = (m[i + 1] - m[i]) / (6 * h[i])
        splines.append((a, b, c, d, x[i]))

    return splines


def evaluate_spline(splines, x_eval):
    # looking for the right spline
    i = 0
    for i in range(len(splines)):
        if x_eval < splines[i][4]:
            i -= 1
            break

    a, b, c, d, x_i = splines[i]  # x_i is the starting point of the spline
    dx = x_eval - x_i  # distance from the starting point of the spline
    return a + b * dx + c * dx ** 2 + d * dx ** 3


def interpolate_spline(filename, start, end, number_of_nodes, title):
    all_nodes = return_all_nodes(filename)
    indexes = uniformly_choose_nodes(start, end, number_of_nodes)
    chosen_nodes = ([all_nodes[0][i] for i in indexes],
                    [all_nodes[1][i] for i in indexes])

    A, b = construct_spline_matrix(chosen_nodes[0], chosen_nodes[1])
    m = solve_linear_equation_with_lu_factorization(A, b)

    splines = construct_splines(chosen_nodes[0], chosen_nodes[1], m)

    interpolated_values = [evaluate_spline(splines, x) for x in all_nodes[0]]

    plot_interpolated_function(all_nodes[0],
                               interpolated_values,
                               all_nodes[1],
                               chosen_nodes,
                               f"Interpolacja Spline'a dla {title}, {number_of_nodes} węzłów")
