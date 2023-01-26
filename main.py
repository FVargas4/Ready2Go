# Importar las librerías y funciones de los documentos dentro de la carpeta
import os
import webbrowser
import time
import functions as fun
import tec_functions as tec
import pydev_functions as pd

"""
Variables:

interruptor (int): Variable que define cuál de los programas o procesos abrir
dvs (int): a

"""

interruptor = 0
exit = 0
dvs = True

print("El programa inicia a las " + time.ctime())
device = str(input('Estas en Mac o PC? ', ))
if device == 'mac' or device == 'Mac' or device == '1':
    dvs = True
    interruptor = str(input('¿Qué vamos a hacer hoy? '))
elif device == 'pc' or device == 'PC' or device == '2':
    dvs = False
    interruptor = str(input('¿Qué vamos a hacer hoy? '))
else:
    dvs = 3
    print("Introduzca una opcion válida")

while(exit == 0):

    fun.returnToDocuments(dvs)

    if interruptor == 'Salir' or interruptor == 'No' or interruptor == 'no' or interruptor == 'salir':
        print('Gracias por usar Ready 2 Go')
        exit = 1
        break
    else:
        print('Buena suerte con ' + interruptor)
        totalProgramas = 0


    if interruptor == 'bloque' or interruptor == 'Bloque':
        totalProgramas = fun.bloque2(dvs)
        
    elif interruptor == 'progra' or interruptor == 'Progra':
        totalProgramas = tec.progra(dvs)

    if interruptor == 'quantitative' or interruptor == 'quantum':
        totalProgramas = tec.qmas(dvs)

    elif interruptor == 'R2G':
        totalProgramas = fun.readyconf(dvs)

    elif interruptor == 'Relax' or interruptor == 'relax':
        fun.relax(dvs)  

    elif interruptor == 'ldaw' or interruptor == 'Ldaw':
        fun.ldaw(dvs)

    elif interruptor == 'spotify' or interruptor == 'spotify':
        if dvs is True:
            print('Lanzando Spotify')
            os.chdir('../../../..')
            os.chdir('Applications/')
            os.system('open Spotify.app')
        else:
            print('No es posible usar esta funcion en Windows por el momento')

    elif interruptor == 'django' or interruptor == 'Django' or interruptor == 'dj'or interruptor == 'Dj':
        pd.django(dvs)

    else:
        print('Comando no reconocido por el sistema, intente otra vez.')
        breakpoint

    print("El programa termina a las " + time.ctime())

    newint = str(input('Algo más? '))
    interruptor = newint
