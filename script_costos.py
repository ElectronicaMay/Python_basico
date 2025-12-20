# Script: cálculo de costos operativos

horas_trabajadas = [9, 9, 8, 10, 7]
costo_por_hora = 30000  # COP

costo_total = sum(horas_trabajadas) * costo_por_hora
promedio_horas = sum(horas_trabajadas) / len(horas_trabajadas)

print("Horas trabajadas:", horas_trabajadas)
print("Costo por hora:", costo_por_hora)
print("Costo total:", costo_total)
print("Promedio de horas:", promedio_horas)

if costo_total > 1_000_000:
    print("⚠️ Alerta: costo operativo alto")
