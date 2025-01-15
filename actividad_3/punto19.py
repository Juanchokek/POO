import tkinter as tk
from tkinter import messagebox

class PropiedadesTrianguloEquilatero:
    def __init__(self, longitud_lado):
        self.longitud_lado = longitud_lado

    def calcular_area(self):
        return (self.longitud_lado ** 2) * (3 ** 0.5) / 4

    def calcular_perimetro(self):
        return self.longitud_lado * 3

    def calcular_altura(self):
        return (self.longitud_lado * (3 ** 0.5)) / 2

    def __str__(self):
        return (f"Lado: {self.longitud_lado} - Área: {self.calcular_area():.2f} - "
                f"Perímetro: {self.calcular_perimetro():.2f} - Altura: {self.calcular_altura():.2f}")

def mostrar_resultados():
    try:
        lado = float(entrada_lado.get())  # Obtener el valor del lado
        
        triangulo = PropiedadesTrianguloEquilatero(lado)
        texto_resultados.delete(1.0, tk.END)  # Limpiar el área de resultados
        texto_resultados.insert(tk.END, str(triangulo))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido para el lado del triángulo.")

def limpiar_entradas():
    entrada_lado.delete(0, tk.END)  # Limpiar la entrada del lado
    texto_resultados.delete(1.0, tk.END)  # Limpiar el área de resultados

# Parámetros de la ventana
ventana = tk.Tk()
ventana.title("Propiedades de un Triángulo Equilátero")
ventana.geometry("400x300") 

tk.Label(ventana, text="Lado del Triángulo").pack(pady=5)
entrada_lado = tk.Entry(ventana)
entrada_lado.pack(pady=5)

tk.Button(ventana, text="Calcular", command=mostrar_resultados).pack(pady=10)
tk.Button(ventana, text="Limpiar", command=limpiar_entradas).pack(pady=10)

texto_resultados = tk.Text(ventana, height=5, width=40)
texto_resultados.pack(pady=20)

ventana.mainloop()