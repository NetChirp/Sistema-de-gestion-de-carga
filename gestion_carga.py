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


def peso_total() -> int:
    return sum(item["peso"] for item in carga)


def agregar_carga() -> None:
    try:
        nombre: str = input("Nombre: ")
        peso: int = int(input("Peso: "))
        tipo: str = input("Tipo: ")

        if peso_total() + peso >= PESO_MAXIMO:
            print(f"{ROJO}Sobrecarga detectada, no se añadira el elemento.{RESET}")
        else:
            print(f"{VERDE}Carga añadida exitosamente{RESET}")
            carga.append(dict(nombre=nombre, peso=peso, tipo=tipo))
    except ValueError:
        print(
            f"{ROJO}El peso debe ser un numero entero, no un conjunto de letras.{RESET}"
        )


def agregar_carga_prioritaria() -> None:
    try:
        nombre: str = input("Nombre: ")
        peso: int = int(input("Peso: "))
        tipo: str = input("Tipo: ")

        if peso_total(carga) + peso >= PESO_MAXIMO:
            print(f"{ROJO}Sobrecarga detectada, no se añadira el elemento.{RESET}")
        else:
            print(f"{VERDE}Carga prioritaria añadida exitosamente{RESET}")
            carga.insert(0, dict(nombre=nombre, peso=peso, tipo=tipo))
    except ValueError:
        print(
            f"{ROJO}El peso debe ser un numero entero, no un conjunto de letras.{RESET}"
        )


def eliminar_carga_nombre() -> None:
    pass

def expulsion_emergencia() -> None:
    nombre_elemento = carga[-1]
    print(nombre_elemento)
    carga.pop()  # Por defecto elimina el ultimo elemento en la lista, siendo -1 su indice
    print(f"{AMARILLO}Alerta: Se ha expulsado  de la bodega{RESET}")


# Eliminar el None una vez esta hecha la funcion
def analisis_carga(carga) -> list | None:
    pass


# Eliminar el none una vez esta hecha la funcion
def reportes() -> list | dict | None:
    pass


while True:
    print(f"{AZUL} --- SISTEMA DE GESTIÓN DE CARGA ---{RESET}")
    print(f"{AMARILLO}Peso actual: {peso_total()}")
    print(f"{AMARILLO}Espacio disponible: {PESO_MAXIMO - peso_total()}{RESET}")

    # Imprimir las diferentes opciones
    for tarea in opciones:
        print(f"{opciones.index(tarea)} {tarea}")

    try:
        realizar_opcion: int = int(input("Opción: "))
        match realizar_opcion:
            case 0:
                agregar_carga()
            case 1:
                agregar_carga_prioritaria()
            case 2:
                eliminar_carga_nombre()
            case 3:
                expulsion_emergencia()
            case 4:
                pass
            case 5:
                pass
            case 6:
                break
            case _:
                print(f"{ROJO}Opción no encontrada{RESET}")
    except ValueError:
        print(f"{ROJO}Debes introducir el numero de la acción a realizar{RESET}")
