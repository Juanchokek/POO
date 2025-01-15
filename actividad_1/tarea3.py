# Definimos las variables
horas_trabajadas = 48
pago_por_hora = 5000
retencion_porcentaje = 12.5 / 100  # Convertir el porcentaje a decimal

# Cálculo del salario bruto, retención de fuente y salario neto
salario_bruto = horas_trabajadas * pago_por_hora
retencion_fuente = salario_bruto * retencion_porcentaje
salario_neto = salario_bruto - retencion_fuente

# Imprimimos los resultados
print("Salario Bruto: $" + str(salario_bruto))
print("Retención en la Fuente: $" + str(retencion_fuente))
print("Salario Neto: $" + str(salario_neto))