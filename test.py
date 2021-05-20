import os
import subprocess
import webbrowser
import time

totalProgramas = 0
interruptor = 0





print("El programa inicia a las " + time.ctime())

interruptor = int(input('Que vamos a hacer hoy? '))


#with switch(interruptor) as s:
if interruptor == 4:
    print('Le atinaste')
    time.sleep(1)
    webbrowser.open("https://drive.google.com/drive/u/1/folders/0ABfuvAAzZODCUk9PVA")
    webbrowser.open_new('https://www.youtube.com/channel/UCSM3FVwdCIJfU0OdjKZb94A')
    webbrowser.open_new_tab("localhost")
    os.chdir('..')
    os.system('code -g ProyectoBloqueII/Ninosyninas')
    totalProgramas = 4

    

    
    
    

totalProgramas = str(totalProgramas)

print("Se han abierto " + totalProgramas + " programas" )


def switchPrograma(a):
    print('empieza el switch')
