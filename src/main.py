# src/main.py
from .operaciones import sumar, dividir

def run():
    print("Suma 5+10 =", sumar(5, 10))
    print("División 10/2 =", dividir(10, 2))
    try:
        print("División 10/0 =", dividir(10, 0))
    except ZeroDivisionError as e:
        print("Error controlado en dividir:", e)

if __name__ == "__main__":
    run()
