import math

class CalculosNumericos:
    @staticmethod
    def calcular_logaritmo_neperiano(valor_str):
        try:
            valor = float(valor_str)
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            resultado = math.log(valor)
            print(f"Resultado = {resultado}")
        except ArithmeticError:
            print("El valor debe ser un número positivo para calcular el logaritmo")
        except ValueError:
            print("El valor debe ser numérico para calcular el logaritmo")

    @staticmethod
    def calcular_raiz_cuadrada(valor_str):
        try:
            valor = float(valor_str)
            if valor < 0:
                raise ArithmeticError("El valor debe ser un número positivo")
            resultado = math.sqrt(valor)
            print(f"Resultado = {resultado}")
        except ArithmeticError:
            print("El valor debe ser un número positivo para calcular la raíz cuadrada")
        except ValueError:
            print("El valor debe ser numérico para calcular la raíz cuadrada")

if __name__ == '__main__':
    valor_ingresado = input("Valor numérico = ")
    CalculosNumericos.calcular_logaritmo_neperiano(valor_ingresado)
    CalculosNumericos.calcular_raiz_cuadrada(valor_ingresado)
