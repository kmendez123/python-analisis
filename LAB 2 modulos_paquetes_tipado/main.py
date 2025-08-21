from matematicas import operaciones
from utilidades import saludos

def main():
    print(saludos.saludar("Karla"))
    
    print("Suma:", operaciones.suma(10, 5))
    print("Resta:", operaciones.resta(10, 5))
    print("Multiplicación:", operaciones.multiplicacion(10, 5))
    print("División:", operaciones.division(10, 5))
    
    print(saludos.despedir("Karla"))

if __name__ == "__main__":
    main()
