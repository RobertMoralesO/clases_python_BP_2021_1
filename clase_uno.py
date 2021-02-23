print('hello world')

a = 5
print(a)
# OPERACIONES

# Suma
a = 5
b = 2
c = a + b
print(c)

# Resta
a = 5
b = 2
c = a - b
print(c)

# Multiplicación
a = 5
b = 2
c = a * b
print(c)

# División
a = 5
b = 2
c = a / b
print(c)

# División parte entera
a = 5
b = 2
c = a // b
print(c)

# Potencia
a = 5
b = 2
c = a ** b
print(c)

# Raiz cuadrada

a = 16
b = a ** (1/2)
print(b)

# import math
# raiz = math.sqrt(25)
# print(raiz)

# TIPOS DE DATOS

a = 5
print(type(a))
print(a)
a = "hola"
print(type(a))
print(a)
a = 4.5
print(type(a))
print(a)
a = True
print(type(a))
print(a)

# String str
a = "hola mundo"
b = 'hola mundo'
c = "I can't do it"
d = 'Alias "Carlos"'

# Entero  int
a = 5

# Decimal float
x = 3.5

# Booleano bool
x = True
y = False

# Conversiones de String a entero
x = '3'
y = int(x)
print(y)

# Conversiones de entero a decimal
x = 3
y = float(x)
print(y)

# Conversiones de decimal a string
x = 3.5
y = str(x)
print(y)

# CONCATENACIONES

a = 'hola'
b = 'carlos'
c = a + ' ' + b
print(c)

a = 'Roberto'
b = 5
c = a * 5
print(c)

# CAPTURA DE DATOS POR PANTALLA

nombre = input('Digite su nombre: ')
print(nombre)

print('Digite su nombre: ')
nombre = input()
print(nombre)


# Hua que sume dos numeros e imprima
# su resultado

num_uno = float(input('Digite el número uno: '))
num_dos = float(input('Digite el número dos: '))
suma = num_uno + num_dos
# print('La suma es', suma)
# print(f'La suma es {suma}')
print(f'La suma es {suma}')

# HUA que lea un número y lo eleve al cuadrado

num = int(input('Digite el número a elevar: '))
cuadrado = num ** 2
print(f'El cuadrado de {num} es: {cuadrado}')

# HUAque tome el valor de un producto y le aplique
# el 20% de descuento, imprima el valor del
# producto inicial, el valor del producto con descuento
# y el valor ahorrado.

valor_producto = float(input('Digite el valor del producto $'))
descuento = valor_producto * 0.2
valor_final = valor_producto - descuento
valor_ahorrado = valor_producto - valor_final
print(f'El valor inical del producto es: ${valor_producto:,}')
print(f'El valor del descuento es: ${descuento:,}')
print(f'El valor final a pagar es: ${valor_final:,}')
print(f'El valor ahorrado es: ${valor_ahorrado:,}')

# CONDICIONALES

# Tabla de verdad del and
# v and v = v
# v and f = f
# f and v = f
# f and f = f

print(True and True)
print(True and False)
print(False and True)
print(False and False)

# Tabla de verdad del or
# v or v = v
# v or f = v
# f or v = v
# f or f = f

print(True or True)
print(True or False)
print(False or True)
print(False or False)

# Negación
print(not True)
print(not False)

# Mas de dos condiciones al mismo tiempo
print(True and False and True or False or True and True)
print(True and (False and True) or (False or True) and True)

# Jerarquía de Operaciones
# 1. Paréntesis y llaves
# 2. Potencias y Raices
# 3. Multiplicación y División
# 4. Sumas y Restas

# Jerarquia de operaciones booleana
# 1. Paréntesis y llaves
# 2. Tabla de verdad binaria

# Estructura de un if
if(x > 0):
    print('Positivo')
else:
    print('Negativo')
    print('Resultado')

# HUA que dada la edad de una persona diga si es mayor
# o menor de edad

edad = int(input('Digite la edad de la persona: '))
if edad >= 18:
    print('Es Mayor de edad')
else:
    print('Es Menor de edad')

# HUA que dado un numero n diga si es negativo, positivo
# o cero

numero = int(input('Digite el número '))
if numero == 0:
    print('El número es cero')
elif numero > 0:
    print('El número es positivo')
else:
    print('El número es negativo')
















