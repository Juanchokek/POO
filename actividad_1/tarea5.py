import numpy as np  # Importar la biblioteca numpy

# Leer el radio del círculo ingresado por el usuario
radio = float(input("Ingrese el radio del círculo en cm: "))

# Calcular el área y la circunferencia
area = np.round(np.pi * radio ** 2, 2)
circunferencia = np.round(2 * np.pi * radio, 2)

# Mostrar los resultados con unidades de cm
print("El área del círculo es:", area, "cm²")
print("La circunferencia del círculo es:", circunferencia, "cm")