# Constantes de color
ROJO = "\033[31m"  # Para errores
VERDE = "\033[32m"  # Para éxitos
AMARILLO = "\033[33m"  # Para información
AZUL = "\033[34m"  # Para títulos
RESET = "\033[0m"  # Para volver al color por defecto

# Valores iniciales
carga = [
    {"nombre": "Combustible", "peso": 2000, "tipo": "Propulsión"},
    {"nombre": "Comida", "peso": 500, "tipo": "Consumible"},
    {"nombre": "Oxígeno", "peso": 1000, "tipo": "Vital"},
]

PESO_MAXIMO = 5000


def peso_total(carga) -> int:
    return sum(item["peso"] for item in carga)


while True:
    print(f"{AZUL} --- SISTEMA DE GESTIÓN DE CARGA ---{RESET}")
    print(f"{AMARILLO}Peso actual: {sum(item["peso"] for item in carga)}{RESET}")
    print(f"{AMARILLO}Espacio disponible: {PESO_MAXIMO - peso_total(carga)}")
    break
