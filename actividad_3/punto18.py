import tkinter as tk
from tkinter import messagebox

class DatosEmpleado:
    def __init__(self, codigo, nombre_completo, horas_trabajadas, tarifa_hora, porcentaje_retencion):
        self.codigo = codigo
        self.nombre_completo = nombre_completo
        self.horas_trabajadas = horas_trabajadas
        self.tarifa_hora = tarifa_hora
        self.porcentaje_retencion = porcentaje_retencion
    
    def calcular_salario_bruto(self):
        return self.horas_trabajadas * self.tarifa_hora
    
    def calcular_salario_neto(self):
        return self.calcular_salario_bruto() * (1 - self.porcentaje_retencion / 100)
    
    def __str__(self):
        return (f"Código: {self.codigo} - Nombre: {self.nombre_completo} - Salario Bruto: ${self.calcular_salario_bruto():.2f} - "
                f"Salario Neto: ${self.calcular_salario_neto():.2f}")

def procesar_salario():
    try:
        codigo = entrada_codigo.get()
        nombre_completo = entrada_nombre.get()
        horas_trabajadas = float(entrada_horas.get())
        tarifa_hora = float(entrada_tarifa.get())
        porcentaje_retencion = float(entrada_retencion.get())
        
        empleado = DatosEmpleado(codigo, nombre_completo, horas_trabajadas, tarifa_hora, porcentaje_retencion)
        area_resultado.delete(1.0, tk.END)  # Limpiar el cuadro de texto
        area_resultado.insert(tk.END, str(empleado))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para horas trabajadas, tarifa por hora y porcentaje de retención.")

def limpiar_campos():
    entrada_codigo.delete(0, tk.END)
    entrada_nombre.delete(0, tk.END)
    entrada_horas.delete(0, tk.END)
    entrada_tarifa.delete(0, tk.END)
    entrada_retencion.delete(0, tk.END)
    area_resultado.delete(1.0, tk.END)


# Parámetros de la ventana

ventana = tk.Tk()
ventana.title("Cálculo de Salarios")
ventana.geometry("400x550")

tk.Label(ventana, text="Código del Empleado").pack(pady=5)
entrada_codigo = tk.Entry(ventana)
entrada_codigo.pack(pady=5)

tk.Label(ventana, text="Nombre del Empleado").pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="Horas Trabajadas").pack(pady=5)
entrada_horas = tk.Entry(ventana)
entrada_horas.pack(pady=5)

tk.Label(ventana, text="Tarifa por Hora").pack(pady=5)
entrada_tarifa = tk.Entry(ventana)
entrada_tarifa.pack(pady=5)

tk.Label(ventana, text="Porcentaje de Retención").pack(pady=5)
entrada_retencion = tk.Entry(ventana)
entrada_retencion.pack(pady=5)

tk.Button(ventana, text="Calcular", command=procesar_salario).pack(pady=10)
tk.Button(ventana, text="Limpiar", command=limpiar_campos).pack(pady=10)

area_resultado = tk.Text(ventana, height=5, width=40)
area_resultado.pack(pady=20)

ventana.mainloop()