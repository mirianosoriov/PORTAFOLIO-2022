#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 11 10:07:47 2021

Universidad Nacional de San Agustín de Arequipa

Facultad de Ingeniería de Producción y Servicios

Escuela Profesional de Ingeniería en Telecomunicaciones

Práctica 6: Python - Funciones y Excepciones

@author: Osorio Valencia, Mirian Lucero       CUI: 20210713

Arequipa - 2021
"""

####Estructura Excepciones####

#Se utiliza pra evitar cortes en la ejecución del programa
try:
    <código>
    <código>
    ..........

except:
    <código>
    <código>
    ..........

## Típicos Errores

# ZeroDivisionError.
Se genera cuando el segundo argumento de una operación de división o módulo es cero. El valor asociado es una cadena que indica el tipo de operandos y la operación.
# ValueError.
Se genera cuando se aplica una operación o función a un objeto de tipo inadecuado. El valor asociado es una cadena que proporciona detalles sobre la falta de coincidencia de tipos.

## Validación de Números

#validar ingreso de números enteros
while True:
    try:
        x = int(input('Ingresar tu DNI: '))
        break
    except ValueError:
        print('Error!!! no es un número válido')
        
print('\n')

## Validación de números y otra condición

#Validar ingreso de números enteros positivos
while True:
    try:
        x = int(input('Ingresar un número positivo: '))
    except ValueError:
        print('Error!!! no es un número positivo válido')
        continue
    if x < 0:
        print('\t Por favor ingrese un número positivo')
        continue
    break

print('\n')

####Estructura Funciones####

## Función principal main

#Inicio mis programas con varias funciones
def uno():
    print('Inicio de Programa')
    
def dos():
    pass

def fin():
    print('\n\n\n Fin de programa')
    
#Programa MAIN principal
if __name__ == '__main__':
    uno()
    dos()
    uno()
    dos()
    fin()
    
print('\n')

# Hacer un programa que solicite ingreso de CUI correctamente

#Mi primera función validar dni
def validar_cui():
    while True:
        try:
            cui = int(input('Ingresar CUI: '))
            if len(str(cui)) == 8:
                print('\n\tCUI VÁLIDO')
                break
            else:
                print('\tError: Longitud de CUI no Válido ... Intente de nuevo')
                continue
                
        except ValueError:
            print('\tError!!! No es un CUI válido... Intente de Nuevo')
            
    return cui


#Programa MAIN principal

if __name__ == '__main__':
    titulo = ('   BENEFICIO PARA EL COMEDOR UNIVERSITARIO   ')
    print(titulo.center(50,'*'))
    print('\n\n')
    
    val_cui = validar_cui()
    
    print('\n\n El CUI Ingresado es: ==>',val_cui)
    
print('\n')

#################################EJEMPLOS####################################

# Hacer un programa que imprima un menú de opciones y que valide correctamente los ingresos:
    
#librería del sistema operativo

import os

def menu():
    """
    Función que limpia la pantalla y muestra nuevamente el menú
    """
    os.system('clear') # Borra pantalla en un terminal, en Jupyter no funciona
    titulo = (" Menú General ")
    print (titulo.center(50,'*'))
    print ('\n\n')
    print ("Selecciona una Opción")
    print ("\t1 - Primera Opción")
    print ("\t2 - Segunda Opción")
    print ("\t3 - Tercera Opción")
    print ("\t9 - salir")
    
def validar():
    while True:
        # Mostramos el menu
        menu()
        
        # Solicitamos una opción al usuario
        opcionMenu = input("Inserta un numero valor >> ")
        
        if opcionMenu=="1":
            print("")
            input("Has pulsado la opción 1...\npulsa una tecla para continuar")
        elif opcionMenu=="2":
            print("")
            input("Has pulsado la opción 2...\npulsa una tecla para continuar")
        elif opcionMenu=="3":
            print("")
            input("Has pulsado la opción 3...\npulsa una tecla para continuar")
        elif opcionMenu=="9":
            break
        else:
            print ("")
            input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")
    return opcionMenu

if __name__ == '__main__':
    validar()
    
    print('\tFINALIZO EL PROGRAMA!!!!!')




