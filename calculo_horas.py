# Script para calcular horas trabajadas y costo total
# Versión con validación básica

try:
    horas_trabajadas = float(input("Ingrese horas trabajadas: "))
    costo_por_hora = float(input("Ingrese costo por hora: "))

    if horas_trabajadas < 0 or costo_por_hora < 0:
        print("Error: los valores no pueden ser negativos.")
    else:
        costo_total = horas_trabajadas * costo_por_hora
        print("Horas trabajadas:", horas_trabajadas)
        print("Costo por hora:", costo_por_hora)
        print("Costo total:", costo_total)

except ValueError:
    print("Error: debe ingresar solo números.")
