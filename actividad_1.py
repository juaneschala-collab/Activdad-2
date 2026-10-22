import math
import tkinter as tk
from tkinter import messagebox


class FiguraGeometrica:
    def __init__(self):
        self.volumen = 0.0
        self.superficie = 0.0

class Cilindro(FiguraGeometrica):
    def __init__(self, radio, altura):
        super().__init__()
        self.radio = radio
        self.altura = altura
    
    def calcular_volumen(self):
        self.volumen = math.pi * (self.radio ** 2) * self.altura
        return self.volumen
    
    def calcular_superficie(self):
        area_ladoA = 2.0 * math.pi * self.radio * self.altura
        area_ladoB = 2.0 * math.pi * (self.radio ** 2)
        self.superficie = area_ladoA + area_ladoB
        return self.superficie

class Esfera(FiguraGeometrica):
    def __init__(self, radio):
        super().__init__()
        self.radio = radio

    def calcular_volumen(self):
        self.volumen = (4.0 / 3.0) * math.pi * (self.radio ** 3)
        return self.volumen
    
    def calcular_superficie(self):
        self.superficie = 4.0 * math.pi * (self.radio ** 2)
        return self.superficie

class Piramide(FiguraGeometrica):
    def __init__(self, base, altura, apotema):
        super().__init__()
        self.base = base
        self.altura = altura
        self.apotema = apotema

    def calcular_volumen(self):
        self.volumen = (math.pow(self.base, 2.0) * self.altura) / 3.0
        return self.volumen
    
    def calcular_superficie(self):
        area_base = math.pow(self.base, 2.0)
        area_lado = 2.0 * self.base * self.apotema
        self.superficie = area_base + area_lado
        return self.superficie



# interfaz

class Principal(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Figuras Geométricas")
        self.geometry("350x160")
        
        btn_cilindro = tk.Button(self, text="Cilindro", command=self.abrir_cilindro)
        btn_cilindro.pack(pady=10)
        
        btn_esfera = tk.Button(self, text="Esfera", command=self.abrir_esfera)
        btn_esfera.pack(pady=10)
        
        btn_piramide = tk.Button(self, text="Pirámide", command=self.abrir_piramide)
        btn_piramide.pack(pady=10)
        
    def abrir_cilindro(self):
        VentanaCilindro(self)

    def abrir_esfera(self):
        VentanaEsfera(self)

    def abrir_piramide(self):
        VentanaPiramide(self)

class VentanaCilindro(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Cilindro")
        self.geometry("280x210")
        
        tk.Label(self, text="Radio (cms):").pack(pady=5)
        self.ent_radio = tk.Entry(self)
        self.ent_radio.pack()
        
        tk.Label(self, text="Altura (cms):").pack(pady=5)
        self.ent_altura = tk.Entry(self)
        self.ent_altura.pack()
        
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        btn_calcular.pack(pady=10)
        
        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): ")
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): ")
        self.lbl_superficie.pack()

    def calcular(self):
        try:
            r = float(self.ent_radio.get())
            h = float(self.ent_altura.get())
            cilindro = Cilindro(r, h)
            self.lbl_volumen.config(text=f"Volumen (cm3): {cilindro.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {cilindro.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")

class VentanaEsfera(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Esfera")
        self.geometry("280x200")
        
        tk.Label(self, text="Radio (cms):").pack(pady=5)
        self.ent_radio = tk.Entry(self)
        self.ent_radio.pack()
        
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        btn_calcular.pack(pady=10)
        
        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): ")
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): ")
        self.lbl_superficie.pack()

    def calcular(self):
        try:
            r = float(self.ent_radio.get())
            esfera = Esfera(r)
            self.lbl_volumen.config(text=f"Volumen (cm3): {esfera.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {esfera.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")

class VentanaPiramide(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)
        self.title("Pirámide")
        self.geometry("280x250")
        
        tk.Label(self, text="Base (cms):").pack(pady=2)
        self.ent_base = tk.Entry(self)
        self.ent_base.pack()
        
        tk.Label(self, text="Altura (cms):").pack(pady=2)
        self.ent_altura = tk.Entry(self)
        self.ent_altura.pack()

        tk.Label(self, text="Apotema (cms):").pack(pady=2)
        self.ent_apotema = tk.Entry(self)
        self.ent_apotema.pack()
        
        btn_calcular = tk.Button(self, text="Calcular", command=self.calcular)
        btn_calcular.pack(pady=10)
        
        self.lbl_volumen = tk.Label(self, text="Volumen (cm3): ")
        self.lbl_volumen.pack()
        self.lbl_superficie = tk.Label(self, text="Superficie (cm2): ")
        self.lbl_superficie.pack()

    def calcular(self):
        try:
            b = float(self.ent_base.get())
            h = float(self.ent_altura.get())
            a = float(self.ent_apotema.get())
            piramide = Piramide(b, h, a)
            self.lbl_volumen.config(text=f"Volumen (cm3): {piramide.calcular_volumen():.2f}")
            self.lbl_superficie.config(text=f"Superficie (cm2): {piramide.calcular_superficie():.2f}")
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos")

if __name__ == "__main__":
    app = Principal()
    app.mainloop()