# Microcursos-Python

- [Microcursos-Python](#microcursos-python)
  - [Repaso](#repaso)
    - [Descarga e instalación de Python](#descarga-e-instalación-de-python)
    - [Instalación de IDE](#instalación-de-ide)
    - [Impresión de datos en consola](#impresión-de-datos-en-consola)
  - [Operadores](#operadores)
    - [Relacionales](#relacionales)
    - [Lógicos](#lógicos)
  - [Condicionales](#condicionales)
    - [IF - ELSE - ELIF](#if---else---elif)
  - [Ciclos](#ciclos)
    - [WHILE](#while)
    - [FOR](#for)
  - [Cómo estructurar un código](#cómo-estructurar-un-código)
  - [Consejos y buenas prácticas](#consejos-y-buenas-prácticas)
  - [Aplicaciones](#aplicaciones)


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

## Operadores

### Relacionales

| Expresión | Significado |
|------|------|
| `a == b` | `a` es igual a `b` |
| `a != b` | `a` es diferente de `b` |
| `a > b` | `a` es mayor que `b` |
| `a < b` | `a` es menor que `b` |
| `a >= b` | `a` es mayor o igual que `b` |
| `a <= b` | `a` es menor o igual que `b` |

### Lógicos

| Expresión | Significado |
|------|------|
| `a and b` | `a` y `b` se cumplen |
| `a or b` | `a` o `b` se cumplen |
| `not a` | Inverso de `a` |

## Condicionales

### IF - ELSE - ELIF

```
if <expresión_1>:
    <instrucciones para expresión_1 = True>
elif <expresión_2>:
    <instrucciones para expresión_2 = True>
else:
    <instrucciones para todas las expresiones anteriormente evaluadas = False>
```

- 1 `if` obligatorio
- Múltiples `elif`
- 1 `else`

```python
a = input("Ingrese el primer numero 'a': ")
b = input("Ingrese el primer numero 'b': ")

# Python depende de las indentaciones/tabulaciones

if b > a:
    print("b es mayor que a")
elif a == b:
    print("a y b son iguales")
else:
    print("a es mayor que b")
```

## Ciclos

### WHILE

Ejecutar un bloque de código mientras una condición se cumpla.

```
while <expresión>:
    <instrucciones para expresión = True>
```

```python
i = 1

while i < 6:
    print(i)
    i += 1
```

### FOR

Ejecutar un bloque de código iterando en una secuencia.

```
for <iterador> in <colección>:
    <instrucciones para cada elemento>
```

```python
fruits = ["apple", "banana", "cherry"]

for x in fruits:
    print(x)
```

## Cómo estructurar un código

1. Importación de librerias
2. Definición de funciones
3. Código principal

## Consejos y buenas prácticas

- Usar nombres claros y descriptivos para variables.
- Leer y comprender los mensajes de consola.
- Documentar el trabajo.

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
