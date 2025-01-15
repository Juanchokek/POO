import tkinter as tk
from tkinter import messagebox

class CalculoMatricula:
    def __init__(self, numero_inscripcion, nombres_estudiante, patrimonio, estrato):
        self.numero_inscripcion = numero_inscripcion
        self.nombres_estudiante = nombres_estudiante
        self.patrimonio = patrimonio
        self.estrato = estrato
    
    def calcular_pago(self):
        pago_base = 50000
        if self.patrimonio > 2000000 and self.estrato > 3:
            pago_base += 0.03 * self.patrimonio
        return (f"El estudiante con número de inscripción {self.numero_inscripcion} y nombre {self.nombres_estudiante} "
                f"debe pagar ${pago_base:.2f}")
    
    def __str__(self):
        return self.calcular_pago()

def ejecutar_calculo():
    try:
        numero_inscripcion = entrada_inscripcion.get()
        nombres_estudiante = entrada_nombres.get()
        patrimonio = float(entrada_patrimonio.get())
        estrato = int(entrada_estrato.get())
        
        estudiante = CalculoMatricula(numero_inscripcion, nombres_estudiante, patrimonio, estrato)
        texto_resultado.delete(1.0, tk.END)
        texto_resultado.insert(tk.END, str(estudiante))
    except ValueError:
        messagebox.showerror("Error", "Por favor, ingresa valores numéricos válidos para Patrimonio y Estrato.")

def limpiar_campos():
    entrada_inscripcion.delete(0, tk.END)
    entrada_nombres.delete(0, tk.END)
    entrada_patrimonio.delete(0, tk.END)
    entrada_estrato.delete(0, tk.END)
    texto_resultado.delete(1.0, tk.END)

# Parámetros de la ventana
ventana = tk.Tk()
ventana.title("Cálculo de Matrícula")
ventana.geometry("400x450") 

tk.Label(ventana, text="Número de Inscripción").pack(pady=5)
entrada_inscripcion = tk.Entry(ventana)
entrada_inscripcion.pack(pady=5)

tk.Label(ventana, text="Nombre del Estudiante").pack(pady=5)
entrada_nombres = tk.Entry(ventana)
entrada_nombres.pack(pady=5)

tk.Label(ventana, text="Patrimonio").pack(pady=5)
entrada_patrimonio = tk.Entry(ventana)
entrada_patrimonio.pack(pady=5)

tk.Label(ventana, text="Estrato").pack(pady=5)
entrada_estrato = tk.Entry(ventana)
entrada_estrato.pack(pady=5)

tk.Button(ventana, text="Calcular Matrícula", command=ejecutar_calculo).pack(pady=10)
tk.Button(ventana, text="Limpiar", command=limpiar_campos).pack(pady=10)

texto_resultado = tk.Text(ventana, height=5, width=40)
texto_resultado.pack(pady=20)

ventana.mainloop()
