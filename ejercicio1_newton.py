# Edison Ogonaga taller 3 newton y secante 


def newton_raphson(f, df, p0, TOL=1e-6, N0=50):
    """Algoritmo 2.3. Devuelve (p, historia), con historia = [p0, p1, ..., p]."""
    historia = [p0]
    i = 1
    while i <= N0:
        d = df(p0)
        if d == 0:
            raise ZeroDivisionError(f"f'(p0) = 0 en p0 = {p0}: la tangente es horizontal")
        p = p0 - f(p0) / d               
        historia.append(p)               
        if abs(p - p0) < TOL:           
            return p, historia
        i = i + 1
        p0 = p                           
    raise RuntimeError(f"El método fracasó después de {N0} iteraciones")


if __name__ == "__main__":
    # Prueba con f(x) = x^3 + 4x^2 - 10
    f = lambda x: x**3 + 4 * x**2 - 10
    df = lambda x: 3 * x**2 + 8 * x

    p, historia = newton_raphson(f, df, 1.5, TOL=1e-6)
    print(f"Raíz aproximada (Newton-Raphson): {p:.10f}")
    print(f"Iteraciones realizadas: {len(historia) - 1}")
    print(f"Historia: {historia}")
