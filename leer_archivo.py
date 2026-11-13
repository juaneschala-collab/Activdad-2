class LeerArchivo:
    @staticmethod
    def main():
        nombre_archivo = "prueba.txt"  # Ajustar a la ruta deseada
        try:
            # open con 'r' lee texto y gestiona eficientemente el buffer
            with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
                for linea in archivo:
                    print(linea.strip())
        except IOError:
            print("No se pudo leer el archivo.")

if __name__ == '__main__':
    LeerArchivo.main()
