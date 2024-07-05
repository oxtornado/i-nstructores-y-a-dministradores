from Classes.clases import *
import os

# Nombramos una funcion que limpie la consola
def clear():
  os.system('cls' if os.name == 'nt' else 'clear')

# Creamos una funcion que se encargara de continuar con la clase que corresponda
def continuar(funcion):
    #Bucle de control
    while True:
        #Input que se encargar de saber si continuar o no
        respuesta = input("¿Desea continuar? S/N: ").upper() #Upper para que no haya confusion
        if respuesta == 'N': # Caso en el que se terminara la operacion
            print('Hasta luego')
            exit()
        else: # Cualquier otra opcion continuara ejecutandose
            clear()
            break
