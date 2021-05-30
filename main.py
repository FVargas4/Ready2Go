import os
import subprocess
import webbrowser
import time

totalProgramas = 0
interruptor = 0
exit = 0
print("El programa inicia a las " + time.ctime())
device = str(input('Estas en Mac o PC? ', ))
if device == 'mac' or device == 'Mac' or device == '1':
    dvs = 1
elif device == 'pc' or device == 'PC' or device == '2':
    dvs = 2
interruptor = str(input('¿Qué vamos a hacer hoy? '))
while(exit == 0):

    if dvs ==1:
            os.chdir('/Users/fhva/Documents')
    elif dvs ==2:
            os.chdir(r'C:/Users/ferva/Documents')

            
    if interruptor == 'Salir' or interruptor == 'No' or interruptor == 'no':
        print('Gracias por usar Ready 2 Go')
        exit = 1
        break
    else:
        print('Buena suerte con ' + interruptor)
        totalProgramas = 0


    if interruptor == 'bloque' or interruptor == 'Bloque':
        print('Lanzando sus programas...')
        webbrowser.open_new("https://drive.google.com/drive/u/1/folders/0ABfuvAAzZODCUk9PVA")
        time.sleep(2)
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=bmVKaAV_7-A')
        if dvs == 1:
            os.chdir('ProyectoBloqueII')
            os.chdir('Ninosyninas')
        elif dvs == 2:
            os.chdir(r'C:/Users/ferva/Documents/ProyectoBloqueII/Ninosyninas')
        os.system('code .')
        if dvs ==1:
            os.chdir('/Users/fhva/Documents')
        elif dvs ==2:
            os.chdir(r'C:/Users/ferva/Documents')
        totalProgramas = 3
        

    elif interruptor == 'R2G':
        print('Lanzando sus programas...')
        
        if dvs ==1:
            os.system('open -a "/Applications/Notion.app"')
        elif dvs ==2:
            print('Falta investigar como abrir Notion desde PC')
        time.sleep(2)
        webbrowser.open_new('https://www.youtube.com/watch?v=bmVKaAV_7-A')
        webbrowser.open_new('https://www.google.com/')
        if dvs ==1:
            os.chdir('/Users/fhva/Documents/Ready2Go')
        elif dvs ==2:
            os.chdir(r'C:/Users/ferva/Documents/Ready2Go')
        os.system('code .')
        totalProgramas = 4

    elif interruptor == 'Relax' or interruptor == 'relax':
        if dvs ==1:
            os.system('open -a "/Applications/Spotify.app"')
        elif dvs ==2:
            print('Falta investigar como abrir Spotify desde PC')
        webbrowser.open_new('https://www.youtube.com')
        webbrowser.open_new('https://www.twitch.tv')
        totalProgramas = 2    


    if interruptor == 'ldaw' or interruptor == 'Ldaw':
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

    else:
        print('Comando no reconocido por el sistema, intente otra vez.')
        breakpoint
    totalProgramas = str(totalProgramas)

    print("Se han abierto " + totalProgramas + " programas" )

    newint = str(input('Algo más? '))
    interruptor = newint
