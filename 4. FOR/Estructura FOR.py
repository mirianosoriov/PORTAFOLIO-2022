#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 18:22:33 2021

Universidad Nacional de San Agustín

Facultad de Ingeniería de Producción y Servicios

Escuela Profesional de Ingeniería en Telecomunicaciones

Práctica 4 - Estructura iterativa - for

@author: Osorio Valencia Mirian Lucero

CUI: 20210713

Arequipa - 2021
"""

#####################Estructuras Iterativas##################################
 

## 1. Estructura Iterativa Bucle - For

### Usamos for

# 'for' iterando una lista
num = [6, 23, 89, 120]
for n in num:
    print(n)
    
print('\n')
    
# 'for' iterando un string
nom = "Bud Bunny"
for letra in nom:
    print(letra)
    
# 'for' hallando la longitud de los elementos de una lista
for nombre in ['Alfonsito', 'Pedrito', 'Juancito', 'Timoteo']:
    print ('Hola {0}, la longitud de tu nombre es de: {1} caracteres. '.format(nombre,len(nombre)))
    
print('\n')
    
###Hacer un programa que itere a lo largo de una lista que contenga colores y añada (appends) todos los colores que contengan la letra r a una nueva lista.

#lista de colores
color = ["amarillo", "rojo", "púrpura", "amarillo", "verde", "limón", "azul"]
#nueva lista
color_con_r = []

for m in color:
    if 'r' in m:
        color_con_r.append(m)

print(color_con_r)

print('\n')

## 2. Función range

# 'for' utilizando la función 'range' con 1 parámetro.
for i in range(12):
    print(i)
    
print('\n')
    
###Hacer un programa que imprima del número 1 al 10

# Podemos usar un argumento
# Añadiremos el parámetro end="" para que por defecto no genere una nueva lista

for i in range(10):
    print(i+1, "", end="")
    
print('\n')
    
# Podemos usar dos valores para definir el inicio y el final

for i in range(1,11):
    print(i, "", end="")
    
print('\n')
    
###Ejemplos de función rage

# Podemos usar 3 para definir un inicio, un final y una longitud de paso (en este caso 2)

for i in range(2,10,2):
    print(i, "", end="")
    
print('\n')
    
# inicio = 20, un final = 0 y una longitud de paso -2

for i in range(20,0,-2):
    print(i, "", end="")
    
print('\n')
    
# inicio = 40 , un final = -5 y una longitud de paso -5

for i in range(40,-5,-5):
    print(i, "", end="")
    
print('\n')
    
# inicio = 50 , un final = -1 y una longitud de paso 5

for i in range(50,-1,5):
    print(i, "", end="")
    
print('\n')

## 3. Función "break" y "continue"

### Uso de break

# Hacer un programa que de una lista de números y que imprima la posición del número 9

# Lista de número

lista = [2, 4, 5, 7, 8, 9, 3, 4]

# Utilizamos un contador, iniciamos en 0 o en -1??

cont = -1

for m in lista:
    cont = cont + 1
    if m == 9:
        break

print(cont)

print('\n')

contador = 1
#contador = contador + 1
contador                            #Hay abreviatuas similares para -=, *=, /=, //= 
contador /= 5
c=23
c/=5
print(c)

print('\n')

# Lista de números sin el número '9'


lista = [2, 4, 5, 7, 8, 19, 3, 4]

# Utilizamos un contador reducido

cont = -1

for m in lista:
    cont += 1
    if m == 9:
        break
else:   
## Usamos 'for' conjuntamente con 'else'
    cont = -1
    print("No se encontró el número 9")


## Usamos 'for' conjuntamente con 'else'

if cont >= 0:
    print(cont)
    
print('\n')

### Uso de continue

#lista de números
num = [12, 14, 15, 27, 108, 90, 33, 49, 200]

for p in num:
    if p % 2 != 0:
        continue
    print(p)
    
print('\n')

########################### Ejemplos #########################################

### Estructura Iterativa for

# 1. Hacer un programa y mostrar por pantalla los números pares del 0 al 10:
    
for num in range(0, 11, 2):
    print(num)
    
print('\n')

# 2. Hacer un programa que permita ingresar nombres a una lista, utilizando funciones:
    
#Inicializamos la lista vacía
nombres = []

#Función ingreso nombre
def ingreso(ele):
    for i in range(0,ele):
        m = input("Ingresar nombre de la posición {0} : ".format(i))
        nombres.append(m)

#Preguntamos de cuántos elementos conforman la lista

i = int(input("De cuántos elementos crearemos la lista de nombre : "))

ingreso (i)
print("\n la lista completa de nombres es :\n",nombres)

print('\n')

# 3. Método 2: Hacer un programa que de una lista de números e imprima la posición del número 9, utilizando función enumerate

#lista de números
lista = [2, 4, 5, 7, 8, 19, 3, 4]

#Utilizo la función 'enumerate' que devuelve una tupla (es igual a lista pero es inmutable)
#tupla de 2 elementos de una lista (posición, contenido)
for i,m in enumerate(lista):
    if m == 9:
        break
        
else:
## Usamos 'for' conjuntamente con 'else'
    #ponemos negativa la posición
    i = -1
    print('No se encontró el número 9')
    
if i >=0:
    print(i)
    
print('\n')

# 4. Hacer un programa que lea la lista de obras de Marcos Chicot e indique el orden de los libros

#Lista de libros de Marcos Chicot
obras_mch=["El asesinato de Pitágoras","El asesinato de Sócrates","El asesinato de PLatón"]
#Lista orden de los libros
orden=["primer","segundo","tercer"]

#Utilizamos 'enumerate'
for i, libro in enumerate(obras_mch):
    print("\nEl " + orden[i] +" libro de Marcos Chicot es: " + libro)
    
print('\n')

# 5. Hacer un programa que realice invitaciones de una lista de nombres

for f in ["Mirian", "Lucero", "Sofía", "Gabriela", "Eunice", "Estephany", "Angela", "Marjori"]:
    invitation = "Hola " + f + ". ¡Por favor, ven a mi fiesta el sábado!"
    print(invitation)
    
print('\n')

# 6. Hacer un programa que sume los elementos de una lista, utilizar funciones y for

#solicita usar for y funciones, NO SE PUEDE USAR función 'sum'
def mysum(xs):
    """ Suma todos los números de la lista xs, y devuelve el total. """
    running_total = 0
    for x in xs:
        running_total = running_total + x
    return running_total

# Add tests like these to your test suite ...
print (mysum([1, 2, 3, 4]))               # ==>> 10
print (mysum([1.25, 2.5, 1.75]))          # ==>> 5.5
print (mysum([1, -2, 3]))                 # ==>> 2
print (mysum([1, 2, 3, 4]))               # ==>> 10
print (mysum(range(11)))                  # ==>> 55
print (mysum([]))                         # ==>> 0

print('\n')

# 7. Hacer un programa que sume los elementos de una lista, usamos función sum

m = [1, 2, 3, 4]
sum(m)
print(sum(m))


m = [1, 2, 3, 4]
sum(m)

print ('\n')

# 8. Hacer un programa que imprima los múltiplos hasta el número 10 de cualquier número

# Creamos la función múltiplos
def multiplos(n):
    for i in range(1,11):
        print(n * i, end = "   ")
    print()
    
#Llamamos a la función con el número de múltiplo deseado
m = int(input("Ingrese un número: "))
print("\nLos múltiplos de ", m, "son: ")
multiplos(m)

print('\n')

# 9. Ejemplo de for anidado: Creación de tablas

for i in range (0,4):
    for j in range (0,4):
        for k in range (0,2):
            print(i,j,k)

print('\n')

# 10. Hacer un programa que permita hallar la raíz enésima de un número que se ingresará por teclado:
    
número = float(input("Ingrese un número: "))

for n in range(2, 101):
    print("la raíz {0}-ésima de {1} es {2}".format(n, número, número**(1/n)))
    
print('\n')

#Creo la lista de validación
num = ['1','2','3','4','5','6','7','8','9','0']
sim = ['?','!','$','%','&','/','ª','°']

#función
def validar(nomap):
    for x in nomap:
        if x in num:
            print('Nombre no valido!!!')
        elif x in sim:
            print('Nombre no valido!!!')
        else:
            print('Nombre correcto')
            
#Ingresar nombre
nom=input('Ingrese su nombre: ')

#Llamar a la función
validar(nom)

#Ingresar nombre
apell = input('Ingrese su apellido: ')

#Llamar a la función
validar (apell)



    
    
    
    




