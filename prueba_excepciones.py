def prueba_excepciones():
    # Primer bloque try
    try:
        print("Ingresando al primer try")
        cociente = 10000 / 0  # Lanza ZeroDivisionError
        print("Después de la división")  # Nunca se ejecuta
    except ZeroDivisionError:
        print("División por cero")
    finally:
        print("Ingresando al primer finally")

    # Segundo bloque try
    try:
        print("Ingresando al segundo try")
        objeto = None
        objeto.to_string()  # Lanza AttributeError (similar a NullPointerException)
        print("Imprimiendo objeto")
    except ZeroDivisionError:
        print("División por cero")
    except Exception:  # Captura excepción general
        print("Ocurrió una excepción")
    finally:
        print("Ingresando al segundo finally")

# Ejecución
if __name__ == '__main__':
    prueba_excepciones()
