import os
import webbrowser
import time
import functions as fun
import tec_functions as tec

totalProgramas = 0
interruptor = 0
exit = 0
dvs = 0
print("El programa inicia a las " + time.ctime())
device = str(input('Estas en Mac o PC? ', ))
if device == 'mac' or device == 'Mac' or device == '1':
    dvs = 1
    interruptor = str(input('¿Qué vamos a hacer hoy? '))
elif device == 'pc' or device == 'PC' or device == '2':
    dvs = 2
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
        if dvs ==1:
            os.system('open -a "/Applications/Spotify.app"')
        elif dvs ==2:
            print('Falta investigar como abrir Spotify desde PC')
        webbrowser.open_new('https://www.youtube.com')
        webbrowser.open_new('https://www.twitch.tv')
        totalProgramas = 2    


    elif interruptor == 'ldaw' or interruptor == 'Ldaw':
        print('Lanzando sus programas...')
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=bmVKaAV_7-A')
        if dvs == 1:
            os.chdir('LDAW')
        elif dvs == 2:
            os.chdir(r'C:/Users/ferva/Documents/LDAW')
        os.system('code .')
        if dvs ==1:
            os.chdir('/Users/fhva/Documents')
        elif dvs ==2:
            os.chdir(r'C:/Users/ferva/Documents')
        totalProgramas = 3

    elif interruptor == 'verano' or interruptor == 'Verano' or interruptor == 'porvenir':
        print('Lanzando sus programas...')
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=bmVKaAV_7-A')
        webbrowser.open_new_tab('https://drive.google.com/drive/u/2/folders/15ooSk6lyx34iuYV2k-WEvrinTOLzwtrQ')
        if dvs == 1:
            os.chdir('ProyectoVerano')
        elif dvs == 2:
            os.chdir(r'C:/Users/ferva/Documents/ProyectoVerano')
        os.system('code .')
        if dvs ==1:
            os.chdir('/Users/fhva/Documents')
        elif dvs ==2:
            os.chdir(r'C:/Users/ferva/Documents')
        totalProgramas = 3 

    elif interruptor == 'spotify' or interruptor == 'spotify':
        if dvs == 1:
            print('Lanzando Spotify')
            os.chdir('../../../..')
            os.chdir('Applications/')
            os.system('open Spotify.app')

    #https://www.youtube.com/playlist?list=PLmNaBlhoxd8ncktaL4G9X7MPBUnJTf-Pj
    elif interruptor == 'django' or interruptor == 'Django' or interruptor == 'dj'or interruptor == 'Dj':
        print('Lanzando sus programas...')
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=JT80XhYJdBw')
        webbrowser.open_new_tab('http://127.0.0.1:8000/')
        if dvs == 1:
            os.chdir('DjangoP')
        elif dvs == 2:
            os.chdir(r'C:/Users/ferva/Documents/DjangoP')
        os.system('code .')
        if dvs ==1:
            os.chdir('/Users/fhva/Documents')
        elif dvs ==2:
            os.chdir(r'C:/Users/ferva/Documents')
        totalProgramas = 3 


    else:
        print('Comando no reconocido por el sistema, intente otra vez.')
        breakpoint
    totalProgramas = str(totalProgramas)

    print("Se han abierto " + totalProgramas + " programas" )

    print("El programa termina a las " + time.ctime())


    newint = str(input('Algo más? '))
    interruptor = newint
