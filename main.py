import os
import subprocess
import webbrowser
import time

totalProgramas = 0
interruptor = 0
exit = 0
print("El programa inicia a las " + time.ctime())

interruptor = str(input('¿Qué vamos a hacer hoy? '))
while(exit == 0):

    os.chdir('/Users/fhva/Documents')
    if interruptor == 'Salir' or interruptor == 'No' or interruptor == 'no':
        print('Gracias por usar Ready 2 Go')
        exit = 1
        break
    else:
        print('Buena suerte con ' + interruptor)


    if interruptor == 'bloque' or interruptor == 'Bloque':
        print('Lanzando sus programas...')
        webbrowser.open_new("https://drive.google.com/drive/u/1/folders/0ABfuvAAzZODCUk9PVA")
        time.sleep(2)
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=bmVKaAV_7-A')
        os.chdir('ProyectoBloqueII')
        os.chdir('Ninosyninas')
        os.system('code .')
        os.chdir('..')
        os.chdir('..')
        totalProgramas = 3
        

    elif interruptor == 'R2G':
        print('Lanzando sus programas...')
        os.system('open -a "/Applications/Notion.app"')
        time.sleep(2)
        webbrowser.open_new('https://www.youtube.com/watch?v=bmVKaAV_7-A')
        webbrowser.open_new('https://www.google.com/')
        os.chdir('Ready2Go')
        os.system('code .')
        os.chdir('..')
        totalProgramas = 4

    elif interruptor == 'Relax' or interruptor == 'relax':
        os.system('open -a "/Applications/Spotify.app"')
        webbrowser.open_new('https://www.youtube.com')
        totalProgramas = 2    

    totalProgramas = str(totalProgramas)

    print("Se han abierto " + totalProgramas + " programas" )

    newint = str(input('Algo más? '))
    interruptor = newint
