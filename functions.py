import os
import time
import subprocess
import webbrowser

def returnToDocuments(dvs):
    if dvs == 1: 
            os.chdir('/Users/fhva/Documents')
    elif dvs == 2:
            os.chdir(r'C:/Users/ferva/Documents')

def readyconf(dvs):
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
    return totalProgramas