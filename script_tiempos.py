# Script: cálculo de horas trabajadas

horas = [18, 9, 7, 10, 6]

total = sum(horas)
promedio = total / len(horas)

print("Horas registradas:", horas)
print("Total semanal:", total)
print("Promedio diario:", promedio)

if total > 45:
    print("⚠️    Alerta: exceso de horas trabajadas")
