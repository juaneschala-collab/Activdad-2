class Vendedor:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos
        self.edad = 0

    def imprimir(self):
        print(f"Nombre del vendedor = {self.nombre}")
        print(f"Apellidos del vendedor = {self.apellidos}")
        print(f"Edad del vendedor = {self.edad}")

    def verificar_edad(self, edad):
        if 0 <= edad < 18:
            raise ValueError("El vendedor debe ser mayor de 18 años.")
        elif 18 <= edad <= 120:
            self.edad = edad
        else:
            raise ValueError("La edad no puede ser negativa ni mayor a 120.")

if __name__ == '__main__':
    try:
        nombre = input("Nombre del vendedor = ")
        apellidos = input("Apellidos del vendedor = ")
        vendedor = Vendedor(nombre, apellidos)
        
        edad = int(input("Edad del vendedor = "))
        vendedor.verificar_edad(edad)
        vendedor.imprimir()
    except ValueError as e:
        print(f"Excepción: {e}")
