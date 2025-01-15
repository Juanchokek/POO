import tkinter as tk
from tkinter import messagebox

class ComparadorNumeros:
    def __init__(self, numero1, numero2):
        self.numero1 = numero1
        self.numero2 = numero2
    
    def determinar_mayor(self):
        if self.numero1 > self.numero2:
            return f"{self.numero1} es mayor que {self.numero2}"
        elif self.numero1 == self.numero2:
            return f"{self.numero1} es igual a {self.numero2}"
        else:
            return f"{self.numero2} es mayor que {self.numero1}"
    
    def __str__(self):
        return self.determinar_mayor()

def calcular_mayor():
    try:
        valor1 = float(input_num1.get())
        valor2 = float(input_num2.get())
        
        comparador = ComparadorNumeros(valor1, valor2)
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, str(comparador))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos.")

def limpiar_entradas():
    input_num1.delete(0, tk.END)
    input_num2.delete(0, tk.END)
    texto_resultado.delete(1.0, tk.END)

# Parámetros de la ventana
ventana = tk.Tk()
ventana.title("Comparador de Números")
ventana.geometry("400x300")

tk.Label(ventana, text="Número 1").pack(pady=5)
input_num1 = tk.Entry(ventana)
input_num1.pack(pady=5)

tk.Label(ventana, text="Número 2").pack(pady=5)
input_num2 = tk.Entry(ventana)
input_num2.pack(pady=5)

tk.Button(ventana, text="Calcular Mayor", command=calcular_mayor).pack(pady=10)
tk.Button(ventana, text="Limpiar", command=limpiar_entradas).pack(pady=10)

texto_resultado = tk.Text(ventana, height=5, width=40)
texto_resultado.pack(pady=20)




ventana.mainloop()