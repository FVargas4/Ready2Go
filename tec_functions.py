
import os
import time
import subprocess
import webbrowser
import functions as fun


def bloque2(dvs):
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
    fun.returnToDocuments(dvs)
    totalProgramas = 3
    return totalProgramas

def progra(dvs):
    print('Lanzando sus programas...')
    time.sleep(2)
    webbrowser.open_new_tab('https://experiencia21.tec.mx/courses/186016')
    if dvs == 1:
        os.chdir('ProgramacionAvanzada')
    elif dvs == 2:
        os.chdir(r'C:/Users/ferva/Documents/ProgramacionAvanzada')
    os.system('code .')
    if dvs ==1:
        os.chdir('/Users/fhva/Documents')
    elif dvs ==2:
        os.chdir(r'C:/Users/ferva/Documents')
    return(3)


def qmas(dvs):
    print('Lanzando sus programas...')
    time.sleep(2)
    webbrowser.open_new_tab('https://experiencia21.tec.mx/courses/186016')
    if dvs == 1:
        os.chdir('QuanitiativeMethodsandSimulations')
    elif dvs == 2:
        os.chdir(r'C:/Users/ferva/Documents/QuanitiativeMethodsandSimulations')
    os.system('code .')
    fun.returnToDocuments()
    return 3
def ldaw(dvs):
    print('Lanzando sus programas...')
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=bmVKaAV_7-A')
    if dvs is True:
        os.chdir('LDAW')
    elif dvs is False:
        os.chdir(r'C:/Users/ferva/Documents/LDAW')
    os.system('code .')
    if dvs is True:
        os.chdir('/Users/fhva/Documents')
    elif dvs is False:
        os.chdir(r'C:/Users/ferva/Documents')

