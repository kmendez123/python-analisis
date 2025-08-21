# src/operaciones.py
# Versión corregida para que Mypy quede contento.

def sumar(a: int, b: int) -> int:
    return a + b

def dividir(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("b no puede ser 0")
    return a / b
