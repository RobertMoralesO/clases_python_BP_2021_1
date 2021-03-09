#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 19:07:49 2021

@author: robertomorales
"""

# Ciclo  For en Python

for valor in range(10):
    print(valor)

for valor in range(1, 11):
    print(valor)

for valor in range(2, 100, 2):
    print(valor)
print("hola")

for i in range(1, 11):
    for j in range(1, 6):
        print(i, j)

# ciclo While

while True:
    print("hola")
    break

i = 2
while i <= 10:
    print(i)
    # i = i + 2
    i += 2

# HUA que imprima el ganador de una elección de
# dos candidatos
cant_uno = 0
cant_dos = 0
num_votos = int(input('Digite la cantidad de personas a votar: '))
for n in range(1, num_votos+1):
    while True:
        voto = int(input(f'Digite el voto {n} Candidato uno[1] o dos[2]: '))
        if (voto == 1 or voto == 2):
            break
    
    if voto == 1:
        cant_uno += 1
    else:
        cant_dos += 1
if(cant_uno > cant_dos):
    print(f'El ganador es Candidato Uno con {cant_uno} votos')
    print(f'El Candidato dos obtuvo solo {cant_dos} votos')
elif(cant_dos > cant_uno):
    print(f'El ganador es Candidato Dos con {cant_dos} votos')
    print(f'El Candidato Uno obtuvo solo {cant_uno} votos')
else:
    print(f'Se presentó un empate con {cant_uno} votos para cada uno')

# HUA que de las n notas de un estudiante calcule el promedio académico final

suma = 0
num_notas = int(input('Digite el número de notas a ingresar: '))
for n in range(1, num_notas+1):
    while True:
        nota = float(input(f'Digite la nota {n}: '))
        if nota >= 0 and nota <= 5:
            break
    suma += nota
prom = suma / num_notas
prom = round(prom, 2)
print(f'El promedio de las {num_notas} notas es: {prom}')

# Tipos de colecciones

# Listas o vectores
# Tipo de dato mutable y ordenado

a = [2, 3, 4]
b = [2, True, 'hola', 3.4]
c = [2, [True, False], ['hola', 'mundo'], [2.3, 3.4, 4.6, 7.8]]

for valor in a:
    print(valor)

for valor in b:
    print(valor)

for valor in c:
    print(valor)


a[0] = 7
print(b[2])

a = [2, 3, 4]
a.append(5)  # Agrega el elemento al final de la lista
a.remove(3)  # Elimina de la lista un elemento por su valor
a.pop()  # Elimina el último elemento del vector
a.pop(1)  # Elimina un elemento por posición
a.clear()  # Elimina todos los elementos del vector
# del a
4 in a  # Busca el elemento 4 dentro de a
len(a)  # Cantidad de elementos de la lista
b = a  # Asignación de b en el mismo espacio de memoria de a
id(a)  # Convierte en decimal la dirección en memoria de un objeto
b = a[:]  # Copia de los elementos de a
c = b[0:3]
c = b[:3]
c = b[2:]

# Tuplas
# Tipo de datos inmutable y ordenado

a = (1, 2, 3, 4)
print(a[1])
a = (1, 'hola', True, 4.5)
a = (1, ['hola', 'Mundo'], True, 4.5)
a = (1, ['hola', 'Mundo'], (True, False), 4.5)
b = a[:2]
4 in a


# Set
# Mutables y NO ordenados
a = {1, 2, 3, 4}
a = {7, 2, 1, 5, 9, 9}

# Diccionario
# Mutable pero no ordenado

a = {'nombre': 'Roberto', 'apellido': 'Morales'}
a = {1: 'Roberto', 2: 'Morales'}

a['nombre']
a['nombre'] = 'Carlos'

# Funciones


def nombre_funcion():
    pass


def hola_mundo():
    print('Hola Mundo')


def saludo(nombre='Mundo'):
    print(f'Hola {nombre}')


def suma(num1, num2):
    return num1 + num2


def operaciones(num1, num2):
    suma = num1 + num2
    resta = num1 - num2
    multip = num1 * num2
    div = round(num1 / num2, 2)
    return suma, resta, multip, div


resultados = operaciones(4, 5)
suma, resta, mul, div = resultados
_, _, _, div = resultados

_, _, _, div = operaciones(4, 5)






 