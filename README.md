# Microcursos-Python

- [Microcursos-Python](#microcursos-python)
  - [Repaso](#repaso)
    - [Descarga e instalación de Python](#descarga-e-instalación-de-python)
    - [Instalación de IDE](#instalación-de-ide)
    - [Impresión de datos en consola](#impresión-de-datos-en-consola)
  - [Cómo estructurar un código](#cómo-estructurar-un-código)
  - [Lógica](#lógica)
    - [Operadores de comparación](#operadores-de-comparación)
    - [Operadores lógicos](#operadores-lógicos)
  - [Condicionales](#condicionales)
    - [IF - ELSE - ELIF](#if---else---elif)
  - [Ciclos](#ciclos)
    - [FOR](#for)
    - [WHILE](#while)
  - [Aplicaciones](#aplicaciones)
  - [Consejos](#consejos)


## Repaso

### Descarga e instalación de Python

[Sitio oficial de Python](https://www.python.org/downloads/)

### Instalación de IDE

- Visual Studio Code
- PyCharm
- Spyder

### Impresión de datos en consola

```python
name = input("Ingrese su nombre: ")
print("Hola " + name)
```

## Cómo estructurar un código

1. Importación de librerias
2. Definición de funciones
3. Código principal

## Lógica

### Operadores de comparación

| Expresión | Significado |
|------|------|
| `a == b` | `a` es igual a `b` |
| `a != b` | `a` es diferente de `b` |
| `a > b` | `a` es mayor que `b` |
| `a < b` | `a` es menor que `b` |
| `a >= b` | `a` es mayor o igual que `b` |
| `a <= b` | `a` es menor o igual que `b` |

### Operadores lógicos

| Expresión | Significado |
|------|------|
| `a and b` | `a` y `b` se cumplen |
| `a or b` | `a` o `b` se cumplen |
| `not a` | Inverso de `a` |

## Condicionales

### IF - ELSE - ELIF

```python
a = input("Ingrese el primer numero 'a': ")
b = input("Ingrese el primer numero 'b': ")

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")
```

## Ciclos

### FOR

Ejecutar un bloque de código iterando en una secuencia

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
```

### WHILE

Ejecutar un bloque de código mientras una condición se cumpla

```python
i = 1

while i < 6:
    print(i)
    i += 1
```

## Aplicaciones

Usando MatPlotLib y Numpy

> [!NOTE]
> 
> ```console
> pip install matplotlib
> pip install numpy
> ```
>
> ```python
> import matplotlib
> import numpy
> print(matplotlib.__version__)
> print(numpy.__version__)
> ```

```python
print("Hello World")
```

## Consejos

- Usar nombres claros y descriptivos para variables.
- No subestimar la utilidad de los mensajes de consola.
- Documentar el trabajo.
