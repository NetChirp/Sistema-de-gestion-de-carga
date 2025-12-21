# Constantes de color
ROJO = "\033[31m"  # Para errores
VERDE = "\033[32m"  # Para éxitos
AMARILLO = "\033[33m"  # Para información
AZUL = "\033[34m"  # Para títulos
RESET = "\033[0m"  # Para volver al color por defecto

# Valores iniciales
carga: list = [
    {"nombre": "Combustible", "peso": 2000, "tipo": "Propulsión"},
    {"nombre": "Comida", "peso": 500, "tipo": "Consumible"},
    {"nombre": "Oxígeno", "peso": 1000, "tipo": "Vital"},
]

PESO_MAXIMO: int = 5000
opciones: list = [
    "Agregar carga",
    "Agregar carga prioritaria",
    "Eliminar carga por nombre",
    "Expulsión de emergencia",
    "Análisis de carga",
    "Reportes",
    "Salir",
]


def peso_total(carga) -> int:
    return sum(item["peso"] for item in carga)


def agregar_carga(carga) -> None:
    pass


def agregar_carga_prioritaria(carga) -> None:
    pass


def eliminar_carga_nombre(nombre_carga) -> None:
    pass


def expulsion_emergencia() -> None:
    pass


# Eliminar el None una vez esta hecha la funcion
def analisis_carga() -> list | None:
    pass


# Eliminar el none una vez esta hecha la funcion
def reportes() -> list | dict | None:
    pass


while True:
    print(f"{AZUL} --- SISTEMA DE GESTIÓN DE CARGA ---{RESET}")
    print(f"{AMARILLO}Peso actual: {peso_total(carga)}")
    print(f"{AMARILLO}Espacio disponible: {PESO_MAXIMO - peso_total(carga)}{RESET}")

    # Imprimir las diferentes opciones
    for tarea in opciones:
        print(f"{opciones.index(tarea)} {tarea}")

    try:
        realizar_opcion: int = int(input("Opción: "))
        match realizar_opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case _:
                print(f"{ROJO}Opción no encontrada{RESET}")
    except ValueError:
        print(f"{ROJO}Debes introducir el numero de la acción a realizar{RESET}")
