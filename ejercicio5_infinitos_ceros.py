# Edison Ogonaga deber métodos newton y secante
import numpy as np
import matplotlib.pyplot as plt
from ejercicio2_secante import secante


def f(x):
    return np.log(x**2 + 1) - np.exp(0.4 * x) * np.cos(np.pi * x)


if __name__ == "__main__":
    x = np.linspace(-1, 5, 600)
    plt.figure(figsize=(8, 5))
    plt.plot(x, f(x), label=r"$f(x) = \ln(x^2+1) - e^{0.4x}\cos(\pi x)$", color="navy")
    plt.axhline(0, color="black", linestyle="--")

    for n in range(1, 6):
        aprox = n - 0.5
        cero_n, _ = secante(f, aprox - 0.1, aprox + 0.1, TOL=1e-6)
        plt.plot(cero_n, 0, "ro")
        plt.annotate(f"n={n}", (cero_n, 0), xytext=(-10, 8), textcoords="offset points")

    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title(r"Gráfica de $f(x)$ en $[-1, 5]$")
    plt.legend()
    plt.grid(True, alpha=0.35)
    plt.tight_layout()
    plt.savefig("grafica_funcion_cos.png", dpi=150)

    n = 25
    p_aprox = n - 0.5
    cero_25, hist_25 = secante(f, p_aprox - 0.1, p_aprox + 0.1, TOL=1e-6)
    print(f"Aproximación inicial para n=25: n - 1/2 = {p_aprox}")
    print(f"25-ésimo cero positivo (con secante, TOL=1e-6): {cero_25:.10f}")
    print(f"Iteraciones: {len(hist_25) - 2}")
