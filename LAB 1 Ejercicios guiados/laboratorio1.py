# ====================================
# Módulo A — Funciones y Métodos
# ====================================

# A.1 – Funciones como valores
def saludar(nombre):
    return f"Hola, {nombre}"

def despedir(nombre):
    return f"Adiós, {nombre}"

def aplaudir(nombre):
    return f"👏 Muy bien, {nombre}!"

acciones = {
    "saludar": saludar,
    "despedir": despedir,
    "aplaudir": aplaudir
}

def ejecutar(accion, *args, **kwargs):
    if accion not in acciones:
        raise KeyError(f"La acción '{accion}' no está disponible.")
    return acciones[accion](*args, **kwargs)


# A.2 – Funciones internas y closures
def crear_descuento(porcentaje):
    def aplicar_descuento(precio):
        return precio * (1 - porcentaje)
    return aplicar_descuento

descuento10 = crear_descuento(0.10)
descuento25 = crear_descuento(0.25)


# ====================================
# Módulo B — Excepciones
# ====================================

# B.1 – Validación de entrada
def parsear_enteros(entradas: list[str]):
    valores = []
    errores = []
    for e in entradas:
        try:
            valores.append(int(e))
        except ValueError:
            errores.append(f"No se pudo convertir '{e}' a entero.")
    return valores, errores


# B.2 – Excepciones personalizadas
class CantidadInvalida(Exception):
    pass

def calcular_total(precio_unitario, cantidad):
    if cantidad <= 0:
        raise CantidadInvalida("La cantidad debe ser mayor a 0.")
    if precio_unitario < 0:
        raise ValueError("El precio unitario no puede ser negativo.")
    return precio_unitario * cantidad


# ====================================
# Módulo C — Decoradores
# ====================================

# C.1 – Decorador de validación
def requiere_positivos(func):
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if isinstance(arg, (int, float)) and arg <= 0:
                raise ValueError(f"Argumento inválido ({arg}). Todos los números deben ser > 0.")
        return func(*args, **kwargs)
    return wrapper

@requiere_positivos
def calcular_descuento(precio, porcentaje):
    return precio * (1 - porcentaje)

@requiere_positivos
def escala(valor, factor):
    return valor * factor


# ====================================
# PRUEBAS
# ====================================
if __name__ == "__main__":
    # A.1
    print(ejecutar("saludar", "Ana"))    # Hola, Ana
    print(ejecutar("despedir", "Luis"))  # Adiós, Luis
    print(ejecutar("aplaudir", "Karla")) # 👏 Muy bien, Karla!

    # A.2
    print(descuento10(100))  # 90.0
    print(descuento25(80))   # 60.0

    # B.1
    valores, errores = parsear_enteros(["10", "x", "3"])
    print("Valores:", valores)   # [10, 3]
    print("Errores:", errores)   # ["No se pudo convertir 'x' a entero."]

    # B.2
    try:
        print(calcular_total(10, 3))  # 30
        print(calcular_total(10, 0))  # Lanza CantidadInvalida
    except CantidadInvalida as e:
        print("Error:", e)
    except ValueError as e:
        print("Error:", e)

    # C.1
    print(calcular_descuento(100, 0.2))  # 80
    try:
        print(calcular_descuento(-1, 0.2))  # Lanza ValueError
    except ValueError as e:
        print("Error:", e)

    print(escala(10, 5))  # 50
