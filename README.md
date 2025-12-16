# Sistema de gestión de carga

## Keywords

### Principales
#while, #match_case, #if_else, #listas, #diccionarios, #listas_comprimidas, #diccionarios_comprimidos, 
### Secundarios
#append, #insert, #remove, #pop, #colores_ansi


## Conceptos a trabajar

En este ejercicio pondrás a prueba los siguientes conocimientos:

- **Estructuras de datos:** manipulación de listas que contienen diccionarios.
- **Control de flujo:** uso de `while`, `match`, `if/else`.
- **Algoritmia básica:** búsqueda de máximos y mínimos en una colección.
- **Métodos de listas:** uso práctico de `.append()`, `.insert()`, `.remove()` y `.pop()`.
- **Comprehensions:** list comprehension y dict comprehension.
- **Formato de salida:** uso de colores ANSI en la terminal.

## Objetivo

Vas a programar el sistema de gestión de carga de una nave o bodega espacial.   Tu programa deberá mostrar un menú en bucle para:

- Añadir nuevos elementos de carga (normales y prioritarios).
- Eliminar y expulsar carga cuando sea necesario.
- Analizar el peso total, los elementos más pesados y más ligeros.
- Generar pequeños reportes a partir de la carga actual usando *comprehensions*.

Todo esto respetando siempre un peso máximo permitido y mostrando mensajes informativos con colores en la consola.

Trabajarás en un archivo llamado `gestion_carga.py`.

---

## Nuevo concepto: colores en la consola

Para mejorar la visualización, usaremos códigos de escape ANSI. Son variables que cambian el color del texto. Copia estas constantes al inicio de tu código. Funcionan como un interruptor: activas el color, imprimes el texto y luego restableces el color original.


```python
# Constantes de color
ROJO = "\033[31m"      # Para errores
VERDE = "\033[32m"     # Para éxitos
AMARILLO = "\033[33m"  # Para información
AZUL = "\033[34m"      # Para títulos
RESET = "\033[0m"      # Para volver al color por defecto
```

**Ejemplo de uso en código:**

```python
print(ROJO + "Error: el sistema ha fallado" + RESET)
```

---

## Datos iniciales

Copia esta estructura al inicio de tu programa. Representa el estado actual de la bodega.

```python
carga = [
    {"nombre": "Combustible", "peso": 2000, "tipo": "Propulsión"},
    {"nombre": "Comida", "peso": 500, "tipo": "Consumible"},
    {"nombre": "Oxígeno", "peso": 1000, "tipo": "Vital"},
]

PESO_MAXIMO = 5000
```

---

## Requisitos del programa

El programa debe ejecutarse en un bucle infinito (`while True`) mostrando un menú de gestión.

### A. Cabecera del menú

En cada vuelta del bucle, antes de mostrar las opciones, el programa debe imprimir:

1. El título del sistema en color **AZUL**.
2. El peso total actual (suma de todos los pesos).
3. El espacio disponible (`PESO_MAXIMO` - peso actual).

**Ejemplo de salida en consola:**

```bash
--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 3500 kg
Espacio libre: 1500 kg
```

### B. Opciones del menú (usar `match`)

#### Opción 1: agregar carga (`append`)

Solicita al usuario: nombre, peso y tipo.

- **Validación:** comprueba si la suma del peso actual más el nuevo peso supera el `PESO_MAXIMO`.
- **Si supera el límite:** muestra un mensaje en **ROJO** y no añadas el ítem.
- **Si hay espacio:** añade el diccionario al final de la lista y muestra un mensaje en **VERDE**.
    

**Ejemplo de salida (éxito):**

```bash
Nombre: Agua
Peso: 200
Tipo: Consumible
[VERDE] Éxito: Agua añadido a la carga.
```

**Ejemplo de salida (error):**

```bash
Nombre: Plomo
Peso: 3000
Tipo: Material
[ROJO] Error: sobrecarga detectada. No se ha añadido el ítem.
```

#### Opción 2: agregar carga prioritaria (`insert`)

Funciona igual que la opción 1 (pide datos y valida peso), pero el ítem debe añadirse en la **posición 0** de la lista (al principio).

- Usa los mismos colores para error (**ROJO**) y éxito (**VERDE**).

#### Opción 3: eliminar carga por nombre (`remove`)

Solicita al usuario el nombre del ítem a eliminar.

- **Lógica:** la lista contiene diccionarios, por lo que no puedes hacer `remove("Nombre")` directamente. Debes buscar el diccionario que contenga ese nombre.
- **Si existe:** elimínalo de la lista y muestra mensaje en **AMARILLO**.
- **Si no existe:** muestra un mensaje de error indicando que no se encuentra.

**Ejemplo de salida:**

```bash
Nombre a eliminar: Comida
[AMARILLO] Comida eliminado correctamente.
```

#### Opción 4: expulsión de emergencia (`pop`)

Elimina el **último** elemento de la lista.

- Muestra por pantalla el nombre del ítem eliminado.

**Ejemplo de salida:**

```bash
[AMARILLO] Alerta: se ha expulsado Oxígeno de la bodega.
```

#### Opción 5: análisis de carga (máximo y mínimo)

En lugar de ordenar, la tripulación necesita saber cuáles son los extremos. Debes recorrer la lista y encontrar:

1. El artículo que más pesa.
2. El artículo que menos pesa.

Muestra el nombre y el peso de ambos.

**Ejemplo de salida:**

```bash
Artículo más pesado: Combustible (2000 kg)
Artículo más ligero: Comida (500 kg)
```

#### Opción 6: reportes (comprehensions)

Sin modificar la lista original, genera e imprime:

1. **List comprehension:** una lista solo con los nombres de los artículos de tipo "Vital".
2. **Dict comprehension:** un diccionario `{nombre: estado}` donde el estado es "LIGERO" (si peso < 1000) o "PESADO" (si peso >= 1000).

**Ejemplo de salida:**


```bash
Ítems vitales: ['Oxígeno', 'Agua']
Estado de peso: {'Combustible': 'PESADO', 'Comida': 'LIGERO', 'Oxígeno': 'PESADO'}
```

#### Opción 7: salir

Finaliza el programa.

---

## Ejemplos de ejecución

A continuación tienes ejemplos de sesiones completas para que veas el flujo típico del programa.

### Ejemplo 1: agregar carga, agregar prioritaria y salir

```bash
--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 3500 kg
Espacio libre: 1500 kg

1. Agregar carga
2. Agregar carga prioritaria
3. Eliminar carga por nombre
4. Expulsión de emergencia
5. Análisis de carga
6. Reportes
7. Salir

Opción: 1
Nombre: Agua
Peso: 200
Tipo: Consumible
[VERDE] Éxito: Agua añadido a la carga.

--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 3700 kg
Espacio libre: 1300 kg

1. Agregar carga
2. Agregar carga prioritaria
3. Eliminar carga por nombre
4. Expulsión de emergencia
5. Análisis de carga
6. Reportes
7. Salir

Opción: 2
Nombre: Medicinas
Peso: 300
Tipo: Vital
[VERDE] Éxito: Medicinas añadido como carga prioritaria.

--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 4000 kg
Espacio libre: 1000 kg

1. Agregar carga
2. Agregar carga prioritaria
3. Eliminar carga por nombre
4. Expulsión de emergencia
5. Análisis de carga
6. Reportes
7. Salir

Opción: 1
Nombre: Plomo
Peso: 2000
Tipo: Material
[ROJO] Error: sobrecarga detectada. No se ha añadido el ítem.

--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 4000 kg
Espacio libre: 1000 kg

1. Agregar carga
2. Agregar carga prioritaria
3. Eliminar carga por nombre
4. Expulsión de emergencia
5. Análisis de carga
6. Reportes
7. Salir

Opción: 7
Saliendo del sistema...
```

> Nota: el peso inicial de 3500 kg corresponde a Combustible (2000) + Comida (500) + Oxígeno (1000).

---

### Ejemplo 2: eliminar por nombre, expulsión de emergencia, análisis y reportes

En este ejemplo partimos de la **lista inicial**, sin Agua ni Medicinas añadidas.

```bash
--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 3500 kg
Espacio libre: 1500 kg

1. Agregar carga
2. Agregar carga prioritaria
3. Eliminar carga por nombre
4. Expulsión de emergencia
5. Análisis de carga
6. Reportes
7. Salir

Opción: 5
Artículo más pesado: Combustible (2000 kg)
Artículo más ligero: Comida (500 kg)

--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 3500 kg
Espacio libre: 1500 kg

1. Agregar carga
2. Agregar carga prioritaria
3. Eliminar carga por nombre
4. Expulsión de emergencia
5. Análisis de carga
6. Reportes
7. Salir

Opción: 6
Ítems vitales: ['Oxígeno']
Estado de peso: {'Combustible': 'PESADO', 'Comida': 'LIGERO', 'Oxígeno': 'PESADO'}

--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 3500 kg
Espacio libre: 1500 kg

1. Agregar carga
2. Agregar carga prioritaria
3. Eliminar carga por nombre
4. Expulsión de emergencia
5. Análisis de carga
6. Reportes
7. Salir

Opción: 3
Nombre a eliminar: Comida
[AMARILLO] Comida eliminado correctamente.

--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 3000 kg
Espacio libre: 2000 kg

1. Agregar carga
2. Agregar carga prioritaria
3. Eliminar carga por nombre
4. Expulsión de emergencia
5. Análisis de carga
6. Reportes
7. Salir

Opción: 4
[AMARILLO] Alerta: se ha expulsado Oxígeno de la bodega.

--- SISTEMA DE GESTIÓN DE CARGA ---
Peso actual: 2000 kg
Espacio libre: 3000 kg

1. Agregar carga
2. Agregar carga prioritaria
3. Eliminar carga por nombre
4. Expulsión de emergencia
5. Análisis de carga
6. Reportes
7. Salir

Opción: 7
Saliendo del sistema...
```

Aquí se ve claramente:
 
- Cómo se calcula el peso total tras eliminar elementos.
- Cómo funcionan los mensajes en AMARILLO para acciones de eliminación/expulsión.   
- Cómo deben verse los reportes de análisis y comprehensions.
