import math
import tkinter as tk
from tkinter import messagebox

class Notas:
    def __init__(self):
        self.lista_notas = []
    
    def agregar_nota(self, nota):
        self.lista_notas.append(nota)

    def calcular_promedio(self):
        if not self.lista_notas: return 0
        return sum(self.lista_notas) / len(self.lista_notas)
    
    def calcular_desviacion(self):
        prom = self.calcular_promedio()
        suma = 0
        for nota in self.lista_notas:
            suma += math.pow(nota - prom, 2)
        return math.pow(suma / len(self.lista_notas), 0.5)

    def calcular_menor(self):
        return min(self.lista_notas)

    def calcular_mayor(self):
        return max(self.lista_notas)

    def limpiar_notas(self):
        self.lista_notas.clear()

# interfaz
class VentanaPrincipal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Notas")
        self.geometry("300x380")
        self.notas = Notas()

        # Entradas
        self.entries = []
        for i in range(5):
            tk.Label(self, text=f"Nota {i+1}:").pack(pady=2)
            ent = tk.Entry(self)
            ent.pack()
            self.entries.append(ent)
            
        # Botones
        frame_btns = tk.Frame(self)
        frame_btns.pack(pady=10)
        
        btn_calcular = tk.Button(frame_btns, text="Calcular", command=self.calcular)
        btn_calcular.pack(side=tk.LEFT, padx=5)
        
        btn_limpiar = tk.Button(frame_btns, text="Limpiar", command=self.limpiar)
        btn_limpiar.pack(side=tk.LEFT, padx=5)
        
        # Resultados
        self.lbl_promedio = tk.Label(self, text="Promedio = ")
        self.lbl_promedio.pack()
        self.lbl_desviacion = tk.Label(self, text="Desviación estándar = ")
        self.lbl_desviacion.pack()
        self.lbl_mayor = tk.Label(self, text="Nota mayor = ")
        self.lbl_mayor.pack()
        self.lbl_menor = tk.Label(self, text="Nota menor = ")
        self.lbl_menor.pack()

    def calcular(self):
        self.notas.limpiar_notas()
        try:
            for ent in self.entries:
                valor = float(ent.get())
                self.notas.agregar_nota(valor)
                
            self.lbl_promedio.config(text=f"Promedio = {self.notas.calcular_promedio():.2f}")
            self.lbl_desviacion.config(text=f"Desviación estándar = {self.notas.calcular_desviacion():.2f}")
            self.lbl_mayor.config(text=f"Nota mayor = {self.notas.calcular_mayor():.2f}")
            self.lbl_menor.config(text=f"Nota menor = {self.notas.calcular_menor():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Por favor, asegúrese de ingresar números válidos en todos los campos.")

    def limpiar(self):
        self.notas.limpiar_notas()
        for ent in self.entries:
            ent.delete(0, tk.END)
        self.lbl_promedio.config(text="Promedio = ")
        self.lbl_desviacion.config(text="Desviación estándar = ")
        self.lbl_mayor.config(text="Nota mayor = ")
        self.lbl_menor.config(text="Nota menor = ")


if __name__ == "__main__":
    app = VentanaPrincipal()
    app.mainloop()