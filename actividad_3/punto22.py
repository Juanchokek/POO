import tkinter as tk
from tkinter import messagebox

class DatosEmpleado:
    def __init__(self, nombre_empleado, tarifa_horaria, horas_mensuales):
        self.nombre_empleado = nombre_empleado
        self.tarifa_horaria = tarifa_horaria
        self.horas_mensuales = horas_mensuales

    def calcular_salario_total(self):
        return self.tarifa_horaria * self.horas_mensuales

    def generar_comentario(self):
        salario_total = self.calcular_salario_total()
        if salario_total > 450000:
            return f"{self.nombre_empleado}: ${salario_total:.2f}"
        else:
            return f"{self.nombre_empleado} tiene un salario por debajo del límite."

def procesar_salario():
    try:
        nombre_empleado = entrada_nombre.get()
        tarifa_horaria = float(entrada_tarifa.get())
        horas_mensuales = float(entrada_horas.get())

        empleado = DatosEmpleado(nombre_empleado, tarifa_horaria, horas_mensuales)
        resultado = empleado.generar_comentario()

        texto_resultados.delete(1.0, tk.END)
        texto_resultados.insert(tk.END, resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para la tarifa y las horas trabajadas.")

def limpiar_entradas():
    entrada_nombre.delete(0, tk.END)
    entrada_tarifa.delete(0, tk.END)
    entrada_horas.delete(0, tk.END)
    texto_resultados.delete(1.0, tk.END)

ventana = tk.Tk()
ventana.title("Cálculo de Salario Mensual")
ventana.geometry("400x400")

tk.Label(ventana, text="Nombre del Empleado").pack(pady=5)
entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack(pady=5)

tk.Label(ventana, text="Tarifa por Hora").pack(pady=5)
entrada_tarifa = tk.Entry(ventana)
entrada_tarifa.pack(pady=5)

tk.Label(ventana, text="Horas Trabajadas en el Mes").pack(pady=5)
entrada_horas = tk.Entry(ventana)
entrada_horas.pack(pady=5)

tk.Button(ventana, text="Calcular", command=procesar_salario).pack(pady=10)
tk.Button(ventana, text="Limpiar", command=limpiar_entradas).pack(pady=10)

texto_resultados = tk.Text(ventana, height=5, width=40)
texto_resultados.pack(pady=20)

ventana.mainloop()
