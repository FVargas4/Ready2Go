import os
import time
import subprocess
import webbrowser

def returnToDocuments(dvs):
    if dvs is True: 
            os.system('cd /Users/fhva/Documents')
    elif dvs is False:
            os.chdir(r'C:/Users/ferva/Documents')

def readyconf(dvs):
    print('Lanzando sus programas...')
    if dvs is True:
        os.system('open -a "/Applications/Notion.app"')
    elif dvs is False:
        print('Falta investigar como abrir Notion desde PC')
    time.sleep(2)
    webbrowser.open_new('https://www.youtube.com/watch?v=bmVKaAV_7-A')
    webbrowser.open_new('https://www.google.com/')
    if dvs is True:
        os.chdir('/Users/fhva/Documents/Ready2Go')
    elif dvs is False:
        os.chdir(r'C:/Users/ferva/Documents/Ready2Go')
    os.system('code .')

def relax(dvs):
    if dvs is True:
            os.system('open -a "/Applications/Spotify.app"')
    elif dvs is False:
        print('Falta investigar como abrir Spotify desde PC')
    webbrowser.open_new('https://www.youtube.com')
    webbrowser.open_new('https://www.twitch.tv')

