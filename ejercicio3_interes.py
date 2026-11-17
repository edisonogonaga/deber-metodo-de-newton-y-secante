
# Edison Ogonaga taller 3 newton y secante 

from ejercicio2_secante import secante


def saldo_final(i, monto=20000.0, cuota=450.0, meses=60):
    """Saldo después de pagar todas las cuotas, con interés mensual i (0.01 es 1 %)."""
    saldo = monto
    for mes in range(meses):
        saldo = saldo * (1 + i) - cuota  
    return saldo


if __name__ == "__main__":
    
    saldo_cero = saldo_final(0)
    esperado_cero = 20000 - 60 * 450
    print(f"Prueba sin interés (i = 0): saldo_final(0) = {saldo_cero} (esperado: {esperado_cero})")

   
    i_mensual, historia = secante(saldo_final, 0.005, 0.02, TOL=1e-10)
    print(f"Tasa de interés mensual (i): {i_mensual:.10f} ({i_mensual * 100:.6f} %)")
    print(f"Iteraciones: {len(historia) - 2}")


    tasa_efectiva_anual = (1 + i_mensual)**12 - 1
    print(f"Tasa efectiva anual (TEA): {tasa_efectiva_anual:.10f} ({tasa_efectiva_anual * 100:.6f} %)")
