# Edison Ogonaga deber métodos newton y secante
import numpy as np
from ejercicio1_newton import newton_raphson


def f(x):
    return np.exp(x)


def df(x):
    return np.exp(x)


def newton_raphson_residuo(f, df, p0, TOL=1e-6, N0=50):
    historia = [p0]
    i = 1
    while i <= N0:
        d = df(p0)
        if d == 0:
            raise ZeroDivisionError(f"f'(p0) = 0 en p0 = {p0}: la tangente es horizontal")
        p = p0 - f(p0) / d
        historia.append(p)
        if abs(f(p)) < TOL:
            return p, historia
        i = i + 1
        p0 = p
    raise RuntimeError(f"El método fracasó después de {N0} iteraciones")


if __name__ == "__main__":
    p0 = 0.0
    print(f"Si p0 = 0, p_50 = {p0 - 50}")

    try:
        p, hist = newton_raphson(f, df, 0.0, TOL=1e-6, N0=50)
        print(f"Devolvió: {p}")
    except Exception as e:
        print(f"Lanzó {type(e).__name__}: {e}")

    p_res, hist_res = newton_raphson_residuo(f, df, 0.0, TOL=1e-6, N0=50)
    print(f"Valor devuelto como «raíz»: {p_res}")
