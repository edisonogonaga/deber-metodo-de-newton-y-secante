# Edison Ogonaga deber métodos newton y secante
import numpy as np
import matplotlib.pyplot as plt
from ejercicio6_sin_raiz import newton_raphson_residuo


def s(t):
    return 1.2 * np.exp(-t / 2.0) + np.exp(-t / 2.0) * np.cos(2.0 * t)


def ds(t):
    return np.exp(-t / 2.0) * (-0.6 - 0.5 * np.cos(2.0 * t) - 2.0 * np.sin(2.0 * t))


if __name__ == "__main__":
    for t0 in [0.0, 2.0, 3.0, 4.0]:
        t_gorro, hist = newton_raphson_residuo(s, ds, t0, TOL=1e-6, N0=50)
        s_izq = s(t_gorro - 0.01)
        s_cen = s(t_gorro)
        s_der = s(t_gorro + 0.01)
        print(
            f"t0 = {t0:.1f} -> t_hat = {t_gorro:10.6f} | "
            f"s(t_hat - 0.01) = {s_izq:.3e}, "
            f"s(t_hat) = {s_cen:.3e}, "
            f"s(t_hat + 0.01) = {s_der:.3e}"
        )

    t = np.linspace(0, 12, 600)
    st = s(t)
    st_escalada = 1.2 + np.cos(2.0 * t)

    fig, axes = plt.subplots(1, 2, figsize=(12, 5))

    ax1 = axes[0]
    ax1.plot(t, st, color="steelblue", linewidth=2, label=r"$s(t) = 1.2e^{-t/2} + e^{-t/2}\cos(2t)$")
    ax1.axhline(0, color="black", linestyle="--", linewidth=1, label=r"$y = 0$")
    ax1.set_title(r"Señal $s(t)$ en $[0, 12]$ (los mínimos se acercan al eje)")
    ax1.set_xlabel("t")
    ax1.set_ylabel("s(t)")
    ax1.legend()
    ax1.grid(True, alpha=0.35)

    ax2 = axes[1]
    ax2.plot(t, st_escalada, color="darkorange", linewidth=2, label=r"$s(t)e^{t/2} = 1.2 + \cos(2t)$")
    ax2.axhline(0.2, color="crimson", linestyle="--", linewidth=1.8, label=r"Recta $y = 0.2$ (mínimo)")
    ax2.axhline(0, color="black", linestyle=":", linewidth=1, label=r"$y = 0$")
    ax2.set_ylim(-0.1, 2.4)
    ax2.set_title(r"$s(t)e^{t/2} = 1.2 + \cos(2t)$ en $[0, 12]$ (nunca baja de $0.2$)")
    ax2.set_xlabel("t")
    ax2.set_ylabel(r"$s(t)e^{t/2}$")
    ax2.legend(loc="upper right")
    ax2.grid(True, alpha=0.35)

    plt.tight_layout()
    ruta_img = "grafica_senal_sensor.png"
    plt.savefig(ruta_img, dpi=150)
