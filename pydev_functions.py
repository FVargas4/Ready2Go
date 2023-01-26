import os
import webbrowser

def startVirtualenv(envLocation, envName):
    if envLocation == os.chdir('pwd'):
        try:
            os.system(f'source {envName}/bin/activate')
        except:
            print('Env does not exist')
        finally:
            os.chdir('ls')
    else:
        breakpoint

def django(dvs):
    print('Lanzando sus programas...')
    webbrowser.open_new_tab('https://www.youtube.com/watch?v=JT80XhYJdBw')
    webbrowser.open_new_tab('http://127.0.0.1:8000/')
    if dvs is True:
        os.chdir('DjangoP')
    elif dvs is False:
        os.chdir(r'C:/Users/ferva/Documents/DjangoP')
    os.system('code .')
    if dvs is True:
        os.chdir('/Users/fhva/Documents')
    elif dvs is False:
        os.chdir(r'C:/Users/ferva/Documents')