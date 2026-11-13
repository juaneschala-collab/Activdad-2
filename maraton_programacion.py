class Programador:
    def __init__(self, nombre, apellidos):
        self.nombre = nombre
        self.apellidos = apellidos

class EquipoMaratonProgramacion:
    def __init__(self, nombre_equipo, universidad, lenguaje_programacion):
        self.nombre_equipo = nombre_equipo
        self.universidad = universidad
        self.lenguaje_programacion = lenguaje_programacion
        self.programadores = []
        self.tamano_equipo = 0
        self.capacidad_maxima = 3

    def esta_lleno(self):
        return self.tamano_equipo == self.capacidad_maxima

    def anadir(self, programador):
        if self.esta_lleno():
            raise Exception("El equipo está completo. No se pudo agregar programador.")
        self.programadores.append(programador)
        self.tamano_equipo += 1

    @staticmethod
    def validar_campo(campo):
        for char in campo:
            if char.isdigit():
                raise Exception("El nombre no puede tener dígitos.")
        if len(campo) > 20:
            raise Exception("La longitud no debe ser superior a 20 caracteres.")

if __name__ == '__main__':
    try:
        nombre_eq = input("Nombre del equipo = ")
        universidad = input("Universidad = ")
        lenguaje = input("Lenguaje de programación = ")
        
        equipo = EquipoMaratonProgramacion(nombre_eq, universidad, lenguaje)
        
        print("Datos de los integrantes del equipo")
        for i in range(3):
            nombre_prog = input("Nombre del integrante = ")
            EquipoMaratonProgramacion.validar_campo(nombre_prog)
            
            apellidos_prog = input("Apellidos del integrante = ")
            EquipoMaratonProgramacion.validar_campo(apellidos_prog)
            
            programador = Programador(nombre_prog, apellidos_prog)
            equipo.anadir(programador)
    except Exception as e:
        print(f"Excepción: {e}")
