#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 21:19:08 2021

UNIVERSIDAD NACIONAL DE SAN AGUSTÍN
@author: Mirian Osorio
"""

# EJERCICIOS

# 1. Variables

x="Bienvenidos a Python"
y="en minusculas"
lowcase=x.lower()
uppcase=x.upper()
titcase=y.title()
print("\n",lowcase)
print("\n",uppcase)
print("\n",titcase)

x="Bienvenidos a Python"
y="en minusculas"
lowcase=x.lower()
uppcase=x.upper()
titcase=y.title()
print("\t",lowcase,"\t",uppcase,"\t", titcase)

nom="Milo"
age=25
print("Hola, me llamo: ",nom,"\n y tengo: ",age,"años")

x=10*3.25
y=200*200
z="El valor de x es: " + repr(x) + ", y el valor de y es: " + repr(y) + "..."
print(z)
print("El valor de x es: ",x,", y el valor de y es: ",y,"...")

# 2. Formatear cadenas
# f-strings

import math
print (f"El valor de pi es aproximadamente: {math.pi:.3f}")

nom="Milo"
age=25
print(f"Hola, \n Me llamo: {nom} \n y tengo: {age} años.")


# str.format()

nom="Milo"
age=25
print("Hola, \n Me llamo: {0} \n y tengo: {1} años.".format(nom,age))

# 3. Función Input

print("Ingrese su Nombre")
nom= input()
print(f"Un gusto conocerte ,{nom} ")

# 4. Funciones
# Hacer un programa que utilice la función que calcule el importe de un producto.
def valor(precio):
    igv=precio*0.18
    importe=precio+igv
    return(importe)
producto=input("Ingrese el nombre del Producto: ")
imp=float(input("Ingrese el precio del Producto: "))
print("El importe total de {0} es: {1} ".format(producto,valor(imp)))




