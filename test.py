import os
import subprocess
import webbrowser
import time

totalProgramas = 0
interruptor = 0





print("El programa inicia a las " + time.ctime())

interruptor = int(input('Cual es el numero magico? '))

if(interruptor == 4):
    print('Le atinaste')
    time.sleep(1)
    """ webbrowser.open("https://drive.google.com/drive/u/1/folders/0ABfuvAAzZODCUk9PVA")
    webbrowser.open_new('https://www.youtube.com/channel/UCSM3FVwdCIJfU0OdjKZb94A') """
    #os.system('code')
    os.system('echo %cd%')
    os.chdir('..')
    os.chdir('ProyectoBloqueII/Ninosyninas')
    os.system('code')
    os.system('echo %cd%')
    
    

totalProgramas = str(totalProgramas)

print("Se han abierto " + totalProgramas + " programas" )
