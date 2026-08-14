import matplotlib.pyplot as plt
import numpy as np
import sympy as sp

x = sp.symbols('x')

eq = input("Enter the desired equation:")

try:
    expr = sp.sympify(eq)

    func = sp.lambdify(x, expr, modules=["numpy"])

    X = np.linspace(-10, 10, 500)

    Y = func(X)

    if np.isscalar(Y):
        Y = np.full_like(X, Y)

    plt.figure(figsize=(8,5))
    plt.plot(X,Y, color="blue")
    plt.title(f"y = {eq}")
    plt.grid(True)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

except Exception as e:
    print("Error:", e)