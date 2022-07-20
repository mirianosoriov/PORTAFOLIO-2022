#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 24 17:30:39 2021
UNIVERSIDAD NACIONAL DE SAN AGUSTÍN

Escuela Profesional de Ingeniería en Telecomunicaciones

PRÁCTICA 03 
Curso: Computacion 1
Ing.: Renzo Bolívar 

@author: Mirian Lucero Osorio Valencia
"""
PYTHON ‐ Estructuras Condicionales 

# - LISTAS

# 1. INTRODUCCIÓN A LISTAS.

cadena = "Si quieres aprender, enseña. Marco Tulio Ciceron"

print ('La frase inicia con la letra:',cadena[0])
print ('La frase termina con la letra: ',cadena [-1])

# 1.1. Divida una cadena en una lista donde cada palabra sea 
# un elemento de la lista:
    lista_de_cadena = cadena.split()
    print (lista_de_cadena)
    
# 1.2. Los elemento de la lista pueden ser de cualquier tipo:
lista_de_nombres = ["Antony","Fernando","Luciana",'Kassandra','Brayan']

print (lista_de_nombres)
lista_numeros = [20,30,40,50,60,70,80,90]

print (lista_numeros)

print (lista_numeros[0])

print (lista_numeros[-1]*5)

print(lista_numeros[2])

print ('\n')

print(lista_de_nombres)

print(lista_de_nombres[0].title())
print(lista_de_nombres[-1].upper())
print(lista_de_nombres[2])

# 1.3. Modificando elementos en una lista, porque la lista es mutable:
celulares = ['iphone','sansung','huavei','motorola','xiaomi']
print(celulares)
    
celulares[1]= 'samsung'
celulares[2]= 'huawei'

print (celulares)

# 1.4. Adicionando elementos a una lista:
celulares = ['iphone','samsung','motorola','xiaomi']

celulares.append ('lg')

print(celulares)

cel =['zte','logic']
cel2 = celulares + cel 

print(cel2)

# 1.5. Borrando elementos de una lista:
celulares = ['iphone','samsung','huawei','motorola','xiaomi','lg','zte','logic']

print("\nLista de celulares original")
print (celulares)

del celulares[-1] # borramos 01 elemento con el comando"del" indicando posicion del elemento
print("\nLista borrando el ultimo celular")
print(celulares)

b_celular = celulares.pop(4)   #metodo "pop" borra posicion "4" de la lista, se puede almacenar el valor
print("\nLista borrando celular nuevamente")
print (celulares)
print("\n equipo celular borrado")

c_celular = 'lg'        # metodo que borra el celular llamado"lg"
celulares.remove(c_celular)
print(f"\nLista de celular {c_celular.upper()}")
print (celulares)
print(f"\nLista de celular {c_celular.upper()} es muy malo para mi.")

# 1.6. Ordenamos una lista :
autos = ['mazda','audi','toyota','subaru','bmw','lamborghini']
print ('\n lista original')
print(autos)

print('\n lista ordenada')
autos.sort()
print (autos)

print('\nlista ordenada a la inversa')
autos.reverse()
print (autos)


num = [200,600,10,2000,-5,50,1500]
print('\nlista Original')
print(num)

print('\nlista Ordenada temporal')
print(sorted(num))

print ('\nlista Original de nuevo')
print(num)

# 1.7. Longitud de una lista:
print ('Cantidad de autos')
print(len(autos))

print ('\n Cantidad de numeros')
print (len(num))

# 2. ESTRUCTURA CONDICIONAL

# 2.1 Condiciones Simples:
x= 'Guido'

print('i' in x)
print('i' not in x)


lista = ['uva','naranja', 'pera','manzana']

print('uva' in lista)


x =100 
y = 100

print (x, 'es igual a' ,y,' ====>> ', x == y)


print ('1 < 7 = ',1<7)
print ('2 > 9 =' , 2>=9)
print ('10 == 20 = ', 10== 20)
print ('escuela == casa = ',"escuela" == "casa")
print ('Python ! = Java = ',"Python" != "Java")

# 2.2 Comando if - condicional simple:
x = 20
if x > 0 : 
    print(' El numero ',x, 'es valido')
    print(' El cuadrado del numero',x, 'es:', x*x )
    
# 2.3 Comando if - else - Condicional:
n = 15
m = 20

if n > m: 
    print('El numero MAYOR es : '+str(n))
else:
    print ('El numero MAYOR es: ' +str(m))
    
# 2.4 Comando if -else - Condicional anidado:
a = int(input(' Ingrese el primer Numero:'))
b = int(input(' Ingrese el segundo Numero:'))
c = int(input(' Ingrese el tercer Numero:'))

if a > b:
    if a > c:
        m = a
    else:
        m = c
else: 
    if b > c:
        m = b
    else:
        m = c

print(" El numero MAYOR es : " +str(m))
print ("El numero MAYOR es : {}".format(m))

# 2.5 comando if - elif - else - Condicional encadenado:
nombre = input ('Ingrese su nombre:')
if 'a' in nombre:
    print(nombre. title()+' contiene la vocal a')
elif 'e' in nombre:
    print(nombre. title()+' contiene la vocal e')
elif 'i' in nombre:
    print(nombre. title()+' contiene la vocal i')
elif 'o' in nombre:
    print(nombre. title()+' contiene la vocal o')
elif 'u' in nombre:
    print(nombre. title()+' contiene la vocal u')
else:
    print('¡Que nombre tan extraño!!!!!!')
    

# 3. EJEMPLOS:
# Listas.
# 3.1. Operadores con varias listas:
lista1 = [10,20,30]
lista2 = [40,50,60]
print(lista1 + lista2)

# 3.2. Mejorando la impresión de varias listas:
listaA = ['audi','toyota','mazda']
puerta = [2,4]​
print("Mi auto es: " + listaA[-1].title())
print(f"Mi auto {listaA[-2].title()} tiene {puerta[-2]} puertas")

# 3.3. Operadores matemáticos de una lista:
lista3 = [100,500,200,7000,-200,]
print(sum(lista3))
print(max(lista3))
print(min(lista3))
lista3 = [100,500,200,7000,-200,]
print(sum(lista3))
print(max(lista3))
print(min(lista3))

lista1 = list(range(7))
lista2 = list(range(1,10))
lista3 = list(range(-10,2))
lista4 = list(range(200,100,-20))
lista5 = list(range(200,100,20))

print(lista1)
print(lista2)
print(lista3)
print(lista4)
print(lista5)

# 3.4. Error comun en una lista:
autos = ['mazda', 'audi', 'toyota', 'subaru', 'bmw', 'lamborghini']
print(autos[6].upper())

autos = ['mazda', 'audi', 'toyota', 'subaru', 'bmw', 'lamborghini']
print(autos[4].upper())

# Condicionales.
# 3.5. Hacer un programa que determine si un numero ingresado por 
#pantalla es positivo o negativo.

#METODO1:Utilizando if Anidado
x = int(input("Ingrese un numero entero, positivo o negativo:"))
if x > 0:
    y = "positivo"
else:
    if x < 0:
        y = "negativo"
    else :
        if x == 0:
            y = "cero"
print("\nEl numero : {}".format(x))
print("Es un numero : {}".format(y))

#METODO 2:Utilizando elif
#******************FUNCIÓN detecta POSITIVOS NEGATIVOS ****************
def det(xx):
    if xx < 0:
        p = 'negativo'
    elif xx > 0:
        p = 'positivo'
    else:
        p = 'cero'
        print(p)
    return p
###Ingresamos NUMERO ****************************************************
num = int(input("Ingrese un numero entero, positivo o negativo : "))  

###LAMAMOS A LA FUNCION ***********************************************
#FUNCION devuelve un resultado capturado en variable "resp"
resp = det(num)
#Imprimo RESULTADO
print("\nEl numero : {}".format(num))
print("Es un numero : {}".format(resp))

# 3.6. Hacer un programa que pueda ingresar radio del Circulo y 
# calcule: Perímetro, Área y Diámetro.

#METODO1 : Utilizando if Anidado
from math import pi
radio = float(input("Ingrese el radio de un círculo: "))
#Menú
print("Seleccione una opción: ")
print("a) Calcular el diámetro.")
print("b) Calcular el perímetro.")
print("c) Calcular el área.")
opcion = input("Digita a, b, o c y presiona enter: ")
if opcion == "a":
    diametro = 2 * radio
    print("\nEl diámetro del Círculo es {0}.".format(diametro))
else:
    if opcion == "b":
        perimetro = 2 * pi * radio
        print("\nEl perímetro del Círculo es {0}.".format(perimetro))
    else:
        if opcion == "c":
            area = pi * radio ** 2
            print("\nEl área del Círculo es {0}.".format(area))
        else:
            print("\nSolo hay tres opciones: a, b, c.")
            print('Tu has tecleado "{0}".'.format(opcion))
            
#METODO 2 : Utilizando elif
from math import pi
radio = float(input("Ingrese el radio de un círculo: "))
#Menú
print("Seleccione una opción: ")
print("a) Calcular el diámetro.")
print("b) Calcular el perímetro.")
print("c) Calcular el área.")
opcion = input("Digita a, b, o c y presiona enter: ")
if opcion == "a":
    diametro = 2 * radio
    print("El diámetro del Círculo es {0}.".format(diametro))
elif opcion == "b":
    perimetro = 2 * pi * radio
    print("El perímetro del Círculo es {0}.".format(perimetro))
elif opcion == "c":
    area = pi * radio ** 2
    print("El área del Círculo es {0}.".format(area))
else:
    print("Solo hay tres opciones: a, b, c.")
    print('Tu has tecleado "{0}".'.format(opcion))
    
# 3.7. Hacer un programa que verifique si se ha comprado carne en la 
# lista del mercado para hacer Parrillada.

# Lista de Alimentos
alimento = ['arroz', 'papas', 'camotes', 'leche', 'carne', 'cebolla', 'tomate', 'lechuga']
if 'carne' in alimento: 
    print('Hoy comemos rica Parrilla!!!!')
else:
    print('Hoy comemos Verduras')
    
    
# 3.8. Hacer un programa que verifique en una jugeria si tienen la 
#fruta que deseas y te prepare un jugo.

#**********FUNCION JUGUERIA*************************************************
def preparar (fruit):
    if fruit in fruta:
        print(f'\nSi tenemos {antojo.upper()} !!!, te prepararemos un Jugo')
    else:
        print(f'\nHoy no tenemos {antojo.upper()}, pero regresa Mañana')
# *********** LISTA DE FRUTAS********************************************
fruta = ['platano', 'manzana', 'pera', 'naranja', 'mandarina', 'uva']
antojo = input('Ingresa la fruta que deseas comer hoy : ')
preparar(antojo)
print('\nGracias por tu Preferencia !!!, Vuelve Pronto')

# 3.9. Hacer un programa que verifique mayoría de edad.
#************* FUNCIÓN que detecte la mayoria de edad ************
def mayoria(nom,xx):
    if xx >= 18:
        print(f'\n{nom.upper()} es Mayor de Edad con {xx} años de edad')
    else:
        print(f'\n{nom.upper()} es Menor de Edad con {xx} años de edad')
#************** INGRESA DATOS ************************************ 
nombre = input('Ingresa tu Nombre : ')
edad = int(input('Ingrese su edad : '))
mayoria(nombre,edad) #Probar varias veces con mayores y menores de edad, hombres y mujeres







