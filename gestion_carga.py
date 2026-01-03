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
OPCIONES: list = [
    "Agregar carga",
    "Agregar carga prioritaria",
    "Eliminar carga por nombre",
    "Expulsión de emergencia",
    "Análisis de carga",
    "Reportes",
    "Salir",
]


def buscar_elemento(nombre) -> dict:
    # Implementación de dictionary comprehension
    return {i["nombre"]: i for i in carga if i["nombre"] == nombre}


def peso_total(carga) -> int:
    return sum(item["peso"] for item in carga)


# TODO: Refactorizar agregar_carga() y agregar_carga_prioritaria(). Se repite demasiado codigo


def agregar_carga() -> None:
    try:
        nombre: str = input("Nombre: ").capitalize()
        peso: int = int(input("Peso: "))
        tipo: str = input("Tipo: ").capitalize()

        if peso_total(carga) + peso >= PESO_MAXIMO:
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
    nombre: str = input("Nombre del elemento: ").capitalize()
    if buscar_elemento(nombre):
        # Iterar sobre una copia de carga
        for i in carga[:]:
            if i["nombre"] == nombre:
                carga.remove(i)
        print(f"{AMARILLO}{nombre} eliminado correctamente {RESET}")
    else:
        print(f"{ROJO}Elemento no encontrado{RESET}")


def expulsion_emergencia() -> None:
    nombre_elemento = carga[-1]
    carga.pop()
    print(
        f"{AMARILLO}Alerta: Se ha expulsado {nombre_elemento["nombre"]} de la bodega{RESET}"
    )


# Eliminar el None una vez esta hecha la funcion
def analisis_carga() -> None:
    # Verificar que la lista no esté vacía POR LO QUE SEA
    if not carga:
        print(f"{ROJO}No hay carga para analizar{RESET}")
        return None

    mas_pesado = carga[0]
    for articulo in carga:
        if articulo["peso"] > mas_pesado["peso"]:
            mas_pesado = articulo

    mas_ligero = carga[0]
    for articulo in carga:
        if articulo["peso"] < mas_ligero["peso"]:
            mas_ligero = articulo

    print(f"Artículo más pesado: {mas_pesado['nombre']} ({mas_pesado['peso']} kg)")
    print(f"Artículo más ligero: {mas_ligero['nombre']} ({mas_ligero['peso']} kg)")


def reportes() -> None:  # En la medida de lo posible, siempre se retornara una lista
    if not carga:
        print(f"{ROJO}No hay carga para generar reportes{RESET}")
        return None

    # List comprehension: lista con nombres de artículos de tipo "Vital"
    items_vitales = [
        articulo["nombre"] for articulo in carga if articulo["tipo"] == "Vital"
    ]

    # Dict comprehension: diccionario con nombre y estado según peso
    estado_peso = {
        articulo["nombre"]: "LIGERO" if articulo["peso"] < 1000 else "PESADO"
        for articulo in carga
    }

    # Mostrar resultados
    print(f"Ítems vitales: {items_vitales}")
    print(f"Estado de peso: {estado_peso}")


while True:
    print(f"{AZUL} --- SISTEMA DE GESTIÓN DE CARGA ---{RESET}")
    print(f"{AMARILLO}Peso actual: {peso_total(carga)}")
    print(f"{AMARILLO}Espacio disponible: {PESO_MAXIMO - peso_total(carga)}{RESET}")

    # Imprimir las diferentes opciones
    for tarea in OPCIONES:
        print(f"{OPCIONES.index(tarea)} {tarea}")

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
                analisis_carga()
            case 5:
                reportes()
            case 6:
                break
            case _:
                print(f"{ROJO}Opción no encontrada{RESET}")
    except ValueError:
        print(f"{ROJO}Debes introducir el numero de la acción a realizar{RESET}")
