# Edison Ogonaga deber métodos newton y secante
import numpy as np
import matplotlib.pyplot as plt
from ejercicio1_newton import newton_raphson
from ejercicio2_secante import secante


def P(x):
    return 230 * x**4 + 18 * x**3 + 9 * x**2 - 221 * x - 9


def dP(x):
    return 920 * x**3 + 54 * x**2 + 18 * x - 221


if __name__ == "__main__":
    TOL = 1e-6

    cero_izq, hist_sec = secante(P, 0.0, 1.0, TOL=TOL)
    print(f"(a) Secante (p0=0, p1=1) converge a: {cero_izq:.10f}")

    p_new_05, hist_new_05 = newton_raphson(P, dP, 0.5, TOL=TOL)
    print(f"(b) Newton (p0=0.5) converge a:      {p_new_05:.10f}")

    cero_der, hist_01 = newton_raphson(P, dP, 1.0, TOL=TOL)
    print(f"Cero en [0, 1] (arranque p0=1.0):    {cero_der:.10f}")

    x = np.linspace(-1.4, 1.1, 500)
    plt.figure(figsize=(9, 6))
    plt.plot(x, P(x), label=r"$P(x) = 230x^4 + 18x^3 + 9x^2 - 221x - 9$", color="steelblue", linewidth=2)
    plt.axhline(0, color="black", linewidth=1, linestyle="--")

    ceros = np.array([cero_izq, cero_der])
    plt.plot(ceros, np.zeros_like(ceros), "s", color="limegreen", markersize=10, zorder=5,
             label=f"Ceros de P ({cero_izq:.4f} y {cero_der:.4f})")

    p_0_a_4 = np.array(hist_sec[:5])
    plt.plot(p_0_a_4, np.zeros_like(p_0_a_4), "o", color="crimson", markersize=8, zorder=6,
             label=r"Aproximaciones $p_0, \dots, p_4$ en eje $x$ ($y=0$)")
    plt.plot(p_0_a_4[:4], P(p_0_a_4[:4]), "o", color="darkorange", markersize=6, zorder=5,
             label=r"Puntos $(p_k, P(p_k))$ en la curva")

    offsets_eje = [(2, 10), (-18, 10), (2, 10), (-12, 10), (4, 10)]
    for k, px in enumerate(p_0_a_4):
        plt.annotate(f"{k}", (px, 0),
                     xytext=offsets_eje[k], textcoords="offset points",
                     fontsize=11, fontweight="bold", color="crimson")

    offsets_curva = [(6, -14), (-16, 8), (6, -12), (6, -12)]
    for k, px in enumerate(p_0_a_4[:4]):
        plt.annotate(f"$p_{k}$", (px, P(px)),
                     xytext=offsets_curva[k], textcoords="offset points",
                     fontsize=10, color="saddlebrown")

    plt.annotate(f"$p_4 \\approx {p_0_a_4[4]:.2f}$", (p_0_a_4[4], 0),
                 xytext=(0, -22), textcoords="offset points",
                 fontsize=10, fontweight="bold", color="crimson")

    plt.ylim(-130, 160)

    plt.xlabel("x", fontsize=12)
    plt.ylabel("P(x)", fontsize=12)
    plt.title(r"Polinomio $P(x)$ en $[-1.4, 1.1]$, sus dos ceros y secante $p_0, \dots, p_4$", fontsize=13)
    plt.legend(loc="upper right")
    plt.grid(True, alpha=0.35)
    plt.tight_layout()

    ruta_img = "grafica_polinomio_P.png"
    plt.savefig(ruta_img, dpi=150)
