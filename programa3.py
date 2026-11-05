# Calculadora de propinas
total_cuenta = float(input("Ingrese el total de la cuenta: $"))
porcentaje_propina = int(input("Ingrese el porcentaje de propina (ej. 10, 15): "))
personas = int(input("¿Entre cuántas personas se divide la cuenta?: "))

# Cálculos directos (sin repetir float)
monto_propina = total_cuenta * (porcentaje_propina / 100)
total_final = total_cuenta + monto_propina
pago_por_persona = total_final / personas

# Salida con formato de 2 decimales (:.2f)
print("\n--- RESUMEN DE LA CUENTA ---")
print(f"Propina ({porcentaje_propina}%): ${monto_propina:.2f}")
print(f"Monto total a pagar: ${total_final:.2f}")
print(f"Pago por persona: ${pago_por_persona:.2f}")