import tkinter as tk
from tkinter import messagebox
import math

class ResolucionEcuacionCuadratica:
    def __init__(self, coef_a, coef_b, coef_c):
        self.coef_a = coef_a
        self.coef_b = coef_b
        self.coef_c = coef_c

    def obtener_discriminante(self):
        return math.pow(self.coef_b, 2) - 4 * self.coef_a * self.coef_c

    def resolver_ecuacion(self):
        discriminante = self.obtener_discriminante()
        if discriminante > 0:
            raiz1 = (-self.coef_b + math.sqrt(discriminante)) / (2 * self.coef_a)
            raiz2 = (-self.coef_b - math.sqrt(discriminante)) / (2 * self.coef_a)
            return f"X₁ = {raiz1}, X₂ = {raiz2}"
        elif discriminante == 0:
            raiz = -self.coef_b / (2 * self.coef_a)
            return f"La única solución es: {raiz}"
        else:
            return "No hay solución en los números reales."

def procesar_raices():
    try:
        coef_a = float(entrada_a.get())
        coef_b = float(entrada_b.get())
        coef_c = float(entrada_c.get())

        ecuacion = ResolucionEcuacionCuadratica(coef_a, coef_b, coef_c)
        resultado = ecuacion.resolver_ecuacion()

        area_resultados.delete(1.0, tk.END)
        area_resultados.insert(tk.END, resultado)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para los coeficientes.")

def limpiar_campos():
    entrada_a.delete(0, tk.END)
    entrada_b.delete(0, tk.END)
    entrada_c.delete(0, tk.END)
    area_resultados.delete(1.0, tk.END)

ventana = tk.Tk()
ventana.title("Ecuación Cuadrática: Cálculo de Raíces")
ventana.geometry("400x400")

tk.Label(ventana, text="Coeficiente A").pack(pady=5)
entrada_a = tk.Entry(ventana)
entrada_a.pack(pady=5)

tk.Label(ventana, text="Coeficiente B").pack(pady=5)
entrada_b = tk.Entry(ventana)
entrada_b.pack(pady=5)

tk.Label(ventana, text="Coeficiente C").pack(pady=5)
entrada_c = tk.Entry(ventana)
entrada_c.pack(pady=5)

tk.Button(ventana, text="Calcular", command=procesar_raices).pack(pady=10)
tk.Button(ventana, text="Limpiar", command=limpiar_campos).pack(pady=10)

area_resultados = tk.Text(ventana, height=5, width=40)
area_resultados.pack(pady=20)

ventana.mainloop()
