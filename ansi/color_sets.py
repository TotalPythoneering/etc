# Mission: Demonstrate
# TUI possibilities!
# We're using "Windows
# Subsystem for 
# Linux" - Debian.
# Video: (tbd)
# File: ansi/color_sets.py
print()
ESC = '\33[' # Escape 
RESET = ESC + '0m' # Yup

for r in range(30,38), range(90,98):
    for s,x in enumerate(r,1):
        for bk in range(40,48):
            print(f'{ESC}{x}m',
                  f'{ESC}{bk}mF{x}B{bk}{RESET}',
                  sep='',end='')
        print()
print('\nKEY: FnnBxx = Fore[nn] Back[xx]\n')

