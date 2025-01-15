import tkinter as tk
from tkinter import messagebox
import math

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * math.pow(self.radio, 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

class Cuadrado:
    def __init__(self, lado):
        self.lado = lado

    def calcular_area(self):
        return self.lado * self.lado

    def calcular_perimetro(self):
        return 4 * self.lado

class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * self.base + 2 * self.altura

class TrianguloRectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2

    def calcular_perimetro(self):
        return self.base + self.altura + self.calcular_hipotenusa()

    def calcular_hipotenusa(self):
        return math.sqrt(math.pow(self.base, 2) + math.pow(self.altura, 2))

    def clasificar_triangulo(self):
        if ((self.base == self.altura) and 
            (self.base == self.calcular_hipotenusa()) and 
            (self.altura == self.calcular_hipotenusa())):
            return "Es un triángulo equilátero"
        elif ((self.base != self.altura) and 
              (self.base != self.calcular_hipotenusa()) and 
              (self.altura != self.calcular_hipotenusa())):
            return "Es un triángulo escaleno"
        else:
            return "Es un triángulo isósceles"

def calcular_circulo():
    try:
        radio_valor = float(entry_radio.get())
        figura_circulo = Circulo(radio_valor)
        area = figura_circulo.calcular_area()
        perimetro = figura_circulo.calcular_perimetro()
        result_area_circulo.config(state=tk.NORMAL)
        result_area_circulo.delete(1.0, tk.END)
        result_area_circulo.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}")
        result_area_circulo.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido para el radio.")

def calcular_cuadrado():
    try:
        lado_valor = float(entry_lado.get())
        figura_cuadrado = Cuadrado(lado_valor)
        area = figura_cuadrado.calcular_area()
        perimetro = figura_cuadrado.calcular_perimetro()
        result_area_cuadrado.config(state=tk.NORMAL)
        result_area_cuadrado.delete(1.0, tk.END)
        result_area_cuadrado.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}")
        result_area_cuadrado.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa un valor numérico válido para el lado.")

def calcular_rectangulo():
    try:
        base_valor = float(entry_base.get())
        altura_valor = float(entry_altura.get())
        figura_rectangulo = Rectangulo(base_valor, altura_valor)
        area = figura_rectangulo.calcular_area()
        perimetro = figura_rectangulo.calcular_perimetro()
        result_area_rectangulo.config(state=tk.NORMAL)
        result_area_rectangulo.delete(1.0, tk.END)
        result_area_rectangulo.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}")
        result_area_rectangulo.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para la base y la altura.")

def calcular_triangulo():
    try:
        base_valor = float(entry_base_triangulo.get())
        altura_valor = float(entry_altura_triangulo.get())
        figura_triangulo = TrianguloRectangulo(base_valor, altura_valor)
        area = figura_triangulo.calcular_area()
        perimetro = figura_triangulo.calcular_perimetro()
        clasificacion = figura_triangulo.clasificar_triangulo()
        result_area_triangulo.config(state=tk.NORMAL)
        result_area_triangulo.delete(1.0, tk.END)
        result_area_triangulo.insert(tk.END, f"Área: {area}\nPerímetro: {perimetro}\nClasificación: {clasificacion}")
        result_area_triangulo.config(state=tk.DISABLED)
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para la base y la altura.")

def limpiar_campos():
    entry_radio.delete(0, tk.END)
    entry_lado.delete(0, tk.END)
    entry_base.delete(0, tk.END)
    entry_altura.delete(0, tk.END)
    entry_base_triangulo.delete(0, tk.END)
    entry_altura_triangulo.delete(0, tk.END)
    result_area_circulo.config(state=tk.NORMAL)
    result_area_circulo.delete(1.0, tk.END)
    result_area_circulo.config(state=tk.DISABLED)
    result_area_cuadrado.config(state=tk.NORMAL)
    result_area_cuadrado.delete(1.0, tk.END)
    result_area_cuadrado.config(state=tk.DISABLED)
    result_area_rectangulo.config(state=tk.NORMAL)
    result_area_rectangulo.delete(1.0, tk.END)
    result_area_rectangulo.config(state=tk.DISABLED)
    result_area_triangulo.config(state=tk.NORMAL)
    result_area_triangulo.delete(1.0, tk.END)
    result_area_triangulo.config(state=tk.DISABLED)

root = tk.Tk()
root.title("Calculadora de Figuras Geométricas")
root.geometry("700x450")

# Circulo
frame_circulo = tk.LabelFrame(root, text="Círculo", padx=10, pady=10)
frame_circulo.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")
tk.Label(frame_circulo, text="Radio").grid(row=0, column=0)
entry_radio = tk.Entry(frame_circulo)
entry_radio.grid(row=0, column=1)
tk.Button(frame_circulo, text="Calcular", command=calcular_circulo).grid(row=1, column=0, columnspan=2)
result_area_circulo = tk.Text(frame_circulo, height=5, width=30, state=tk.DISABLED)
result_area_circulo.grid(row=2, column=0, columnspan=2)

# Cuadrado
frame_cuadrado = tk.LabelFrame(root, text="Cuadrado", padx=10, pady=10)
frame_cuadrado.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")
tk.Label(frame_cuadrado, text="Lado").grid(row=0, column=0)
entry_lado = tk.Entry(frame_cuadrado)
entry_lado.grid(row=0, column=1)
tk.Button(frame_cuadrado, text="Calcular", command=calcular_cuadrado).grid(row=1, column=0, columnspan=2)
result_area_cuadrado = tk.Text(frame_cuadrado, height=5, width=30, state=tk.DISABLED)
result_area_cuadrado.grid(row=2, column=0, columnspan=2)

# Rectangulo
frame_rectangulo = tk.LabelFrame(root, text="Rectángulo", padx=10, pady=10)
frame_rectangulo.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")
tk.Label(frame_rectangulo, text="Base").grid(row=0, column=0)
entry_base = tk.Entry(frame_rectangulo)
entry_base.grid(row=0, column=1)
tk.Label(frame_rectangulo, text="Altura").grid(row=1, column=0)
entry_altura = tk.Entry(frame_rectangulo)
entry_altura.grid(row=1, column=1)
tk.Button(frame_rectangulo, text="Calcular", command=calcular_rectangulo).grid(row=2, column=0, columnspan=2)
result_area_rectangulo = tk.Text(frame_rectangulo, height=5, width=30, state=tk.DISABLED)
result_area_rectangulo.grid(row=3, column=0, columnspan=2)

# Triangulo Rectangulo
frame_triangulo = tk.LabelFrame(root, text="Triángulo Rectángulo", padx=10, pady=10)
frame_triangulo.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")
tk.Label(frame_triangulo, text="Base").grid(row=0, column=0)
entry_base_triangulo = tk.Entry(frame_triangulo)
entry_base_triangulo.grid(row=0, column=1)
tk.Label(frame_triangulo, text="Altura").grid(row=1, column=0)
entry_altura_triangulo = tk.Entry(frame_triangulo)
entry_altura_triangulo.grid(row=1, column=1)
tk.Button(frame_triangulo, text="Calcular", command=calcular_triangulo).grid(row=2, column=0, columnspan=2)
result_area_triangulo = tk.Text(frame_triangulo, height=5, width=30, state=tk.DISABLED)
result_area_triangulo.grid(row=3, column=0, columnspan=2)

tk.Button(root, text="Limpiar Campos", command=limpiar_campos).grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
