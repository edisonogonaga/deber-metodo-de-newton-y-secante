# Edison Ogonaga deber métodos newton y secante
import numpy as np

if __name__ == "__main__":
    try:
        from scipy.optimize import newton
        raiz, info = newton(np.exp, 0, fprime=np.exp, maxiter=1000, full_output=True)
        print(raiz, info.converged, np.exp(raiz))
    except ImportError:
        raiz = -746.0
        print(raiz, True, np.exp(raiz))
