#!/usr/bin/env python
import platform,os

sysstr = platform.system()
os.putenv('FLASK_CONFIG','development')

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
    task = ['db init','db migrate','db upgrade','clear']
    for t in task:
        task_cmd = 'python start.py '+t
        os.system(task_cmd)
    print('----------------A sqlite database has been inintialized.')

def start_server():
    print('----------------Start applicaton in production mode...')
    os.system('python start.py runserver --host 0.0.0.0')

if __name__ == "__main__":
    pip_install()
    db_init()
    start_server()