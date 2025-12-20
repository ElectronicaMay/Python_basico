# Script: validación de horas trabajadas

horas_trabajadas = [8, 9, 0, 10,6]

horas_validas = []

for h in horas_trabajadas:
    if h < 0:
        print(f"⚠️   Error: hora inválida detectada -> {h}")
    else:
        horas_validas.append(h)

if len(horas_validas) == 0:
    print("❌ No hay horas válidas para calcular")
else:
    total = sum(horas_validas)
    promedio = total / len(horas_validas)

    print("Horas válidas:", horas_validas)
    print("Total:", total)
    print("Promedio:", promedio)
