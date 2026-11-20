# Edison Ogonaga taller 3 newton y secante 


def secante(f, p0, p1, TOL=1e-6, N0=50):
    i = 2
    q0 = f(p0)
    q1 = f(p1)
    historia = [p0, p1]

    while i <= N0:
        if q1 == q0:
            raise ZeroDivisionError(f"f(p1) - f(p0) = 0 entre p0 = {p0} y p1 = {p1}: la secante es horizontal")

        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        historia.append(p)

        if abs(p - p1) < TOL:
            return p, historia

        i = i + 1

        p0, q0 = p1, q1
        p1, q1 = p, f(p)

    raise RuntimeError(f"El método fracasó después de {N0} iteraciones")


if __name__ == "__main__":
    llamadas = []

    def f(x):
        llamadas.append(x)
        return x**3 + 4 * x**2 - 10

    llamadas.clear()
    p, historia = secante(f, 1.0, 2.0, TOL=1e-6)
    print(p, len(historia) - 2, len(llamadas))

    for k, x in enumerate(historia):
        print(f"Iteración {k}: p = {x:.10f}")
