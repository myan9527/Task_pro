#!/usr/bin/env python
import platform,os

sysstr = platform.system()
os.putenv('FLASK_CONFIG','production')

# build script for linux & windows.
def pip_install():
    print('----------------Start resolving dependencies...')
    with open('requirement.txt','r',buffering = 2048) as f:
        for line in f.readlines():
            try:
                pip_cmd = 'pip install '+ line
                os.system(pip_cmd)
            except:
                continue
    print('----------------All dependencies have been resolved succesfully.')

def db_init():
    print('----------------Start initialize sqlite database...')
    if os.path.exists('./migrations'):
        if sysstr == 'Windows':
            os.popen('rd /s/q migrations')
        elif sysstr == 'Linux':
            os.popen('rm -rf migrations')
    os.system('python start.py clear')
    os.system('python start.py db init')
    os.system('python start.py db migrate')
    os.system('python start.py db upgrade')
    print('----------------A sqlite database has been inintialized.')

def start_server():
    print('----------------Start applicaton in product mode...')
    os.system('python start.py runserver')

if __name__ == "__main__":
    pip_install()
    db_init()
    start_server()