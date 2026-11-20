# Edison Ogonaga deber métodos newton y secante
import numpy as np
import matplotlib.pyplot as plt
from ejercicio1_newton import newton_raphson
from ejercicio2_secante import secante


def f(x):
    return 3.0 * x - np.exp(x)



def df(x):
    return 3.0 - np.exp(x)


def biseccion_30(f, a, b, N0=30):
    FA = f(a)
    historia = []
    for _ in range(N0):
        p = (a + b) / 2.0
        FP = f(p)
        historia.append(p)
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    return historia[-1], historia


if __name__ == "__main__":
    p_ref, _ = secante(f, 1.0, 2.0, TOL=1e-15, N0=100)
    p_exacta, _ = newton_raphson(f, df, p_ref, TOL=1e-16, N0=50)
    print(f"Raíz p en [1, 2]: {p_exacta:.16f}")

    _, hist_bis = biseccion_30(f, 1.0, 2.0, N0=30)
    _, hist_new = newton_raphson(f, df, 1.5, TOL=1e-14, N0=50)
    _, hist_sec = secante(f, 1.0, 2.0, TOL=1e-14, N0=50)

    n_bis = [i + 1 for i, pn in enumerate(hist_bis) if abs(pn - p_exacta) > 0]
    err_bis = [abs(pn - p_exacta) for pn in hist_bis if abs(pn - p_exacta) > 0]

    n_new = [i for i, pn in enumerate(hist_new) if abs(pn - p_exacta) > 0]
    err_new = [abs(pn - p_exacta) for pn in hist_new if abs(pn - p_exacta) > 0]

    n_sec = [i for i, pn in enumerate(hist_sec) if abs(pn - p_exacta) > 0]
    err_sec = [abs(pn - p_exacta) for pn in hist_sec if abs(pn - p_exacta) > 0]

    plt.figure(figsize=(9, 6))
    plt.semilogy(n_bis, err_bis, "o-", label="Bisección en [1, 2]", markersize=5, color="steelblue")
    plt.semilogy(n_new, err_new, "s-", label=r"Newton ($p_0 = 1.5$)", markersize=6, color="limegreen")
    plt.semilogy(n_sec, err_sec, "^-", label=r"Secante ($p_0 = 1, p_1 = 2$)", markersize=6, color="crimson")

    n_cota = np.arange(1, 31)
    cota_bis = (2.0 - 1.0) / (2.0 ** n_cota)
    plt.semilogy(n_cota, cota_bis, "--", color="navy", alpha=0.7, label=r"Cota bisección $(b - a)/2^n$")

    plt.axhline(1e-8, color="black", linestyle=":", linewidth=1.5, label=r"Tolerancia $10^{-8}$")

    plt.xlabel("Iteración n", fontsize=12)
    plt.ylabel(r"Error absoluto $|p_n - p|$", fontsize=12)
    plt.title(r"Convergencia de Bisección, Newton y Secante en $3x - e^x = 0$ ($[1, 2]$)", fontsize=13)
    plt.legend(loc="upper right")
    plt.grid(True, which="both", alpha=0.35)
    plt.tight_layout()

    ruta_img = "grafica_convergencia.png"
    plt.savefig(ruta_img, dpi=150)
