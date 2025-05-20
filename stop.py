import os
import sys

def kill_process(name):
    if sys.platform.startswith('win'):
        os.system(f'taskkill /f /im {name}')
    else:
        os.system(f'pkill -f {name}')

kill_process("main")