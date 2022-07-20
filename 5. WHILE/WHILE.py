#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 08:50:48 2021

Universidad  Nacional de San Agustín de Arequipa

Facultad de Ingeniería de Producción y Servicios

Escuela Profesional de Ingeniería en Telecomunicaciones

Práctica 5 : Estructura Iterativa - While

@author: Osorio Valencia Mirian Lucero                   CUI: 20210713

Arequipa - 2021
"""

## 1. Estructura Iterativa - Bucle "While"

### Usamos While

##### Hacer un programa que imprima la tabla del 3.

# 'While' imprimiendo tabla del número 3

contador = 0
print('Tabla del número 3')

#bucle white

while contador <= 10:
    print(f'3 x {contador} ==> {contador*3}')
    contador += 1
    
print('Fin de la tabla')

print('\n')

##### Hacer un programa que repita una frase las veces que se desee, use funciones.

#frase a repetir
frase = "Debo escribir mi propio código y comentarlo"
#Contador
cont = 0

#función recibe n veces
def repetir (n,cont) :
    while cont < n:
        print(frase)
        cont +=1
        
num = int(input('Ingrese el número de veces a repetir la frase: '))
print('\n\n')


#llamar la función
repetir(num,cont)

print('\n')

##### Hacer un programa que solicite ingreso de contraseña.

#Ingreso password

password = ''

while password != '12345':
    print('Por favor ingrese su contraseña')
    password = input()
    
print('Por fin.....!')

print('\n')

## 2. Modificando la finalización del bucle while: break y continue

### Uso de break

##### Hacer un programa que valide ingreso nombre Mirian.

while True:
    print('Por favor ingrese su nombre: ')
    name = input()
    if name.lower() == 'mirian':
        break
        
print(' Hasta luego !!!!')

print('\n')

### Uso de continue

##### Hacer un programa que valide nombre y contraseña de dos listas respectivamente.

#listas de nombre y números
nombre = ['María','Solange','Milagros','Pamela','Cinthia']
contra = ['1234','4321','abcd','dcba','4567']

#while

while True:
    name = input('Ingrese su nombre: ')
    if name not in nombre:
        continue
    print(f'\n Hola {name.title()}, por favor ingresa tu contraseña: ')
    password = input()
    if password in contra:
        print('\n Bienvenido a su cuenta Bancaria')
        break
    else:
        print('\n Acceso Negado')
        break
    
print('\n')

############################### EJEMPLOS ##################################

# Estructura Iterativa while

## 1. Hacer un programa que busque el número 2 dentro de una lista de números, si se encuentra, que imprima el índice dentro de la lista.

valores = [5, 1, 9, 2, 7, 4]
encontrado = False
indice = 0
longitud = len(valores)
while not encontrado and indice < longitud:
    valor = valores[indice]
    if valor == 2:
        encontrado = True
    else:
        indice += 1
if encontrado:
    print(f'El número 2 ha sido encontrado en el índice {indice}')
else:
    print('El número 2 no se encuentra en la lista de valores')
    
print('\n')

## 2. Hacer un programa que solicite ingreso de contraseña con intentos limitados.

#Ingreso password
password = ''

#sino tengo contador while True:

cont = 0
while password != '20210713':
    cont += 1
    print('Por favor igrese su contraseña: ')
    password = input()
    if cont == 5:
        print('Finalizo los intentos...!')
        break
if cont != 5:
    print('Por fin...!')
    
print('\n')

## 3. Imprime la secuencia 3n+1 desde un número n, terminando cuando llegue a 1.

def seq3np1(n):
    while n != 1:
        print(n, end=", ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
    print(n, end = ".\n")
    
num = int(input('Ingrese número de inicio n : ==> '))
seq3np1(num)

print('\n')

## 4. Hacer un pograma con función que cuenta el número de dígitos que son 0 o 5 en un entero positivo.

#Creamos la función
def num_digi(n):
    count = 0
    while n > 0:
        digit = n % 10
        if digit == 0 or digit == 5:
            count = count + 1
        n = n // 10
    return count

#solicitamos número
num = int(input('Ingrese un número que contenga los dígitos "0" y "5" : ==> '))

#Asignamos la cantidad que retorna
cantidad = num_digi(num)

#imprimir resultado
print('\n\nLa cantidad de dígitos "0" y "5" en el número ',num,'es: ==>',cantidad)