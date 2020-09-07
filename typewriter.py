from colorama import Fore, Style, init
import sys, time

init(autoreset=True)

def typewriter(s, colour: Fore = None):
    
    if (colour):
      prefix = colour
    else:
      prefix = ''
    for c in s:
        sys.stdout.write(prefix + c)
        sys.stdout.flush()
        time.sleep(0.06)