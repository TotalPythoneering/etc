# File: cbanner.py
# Colorized Console Message

COLORS = {
    'BLACK'  :'\033[30m','BLUE'  :'\033[34m',
    'CYAN'   :'\033[36m','GREEN' :'\033[32m',
    'MAGENTA':'\033[35m','RED'   :'\033[31m',
    'WHITE'  :'\033[37m','YELLOW':'\033[33m',
    'RESET'  :'\033[0m'
    }

prefix = \
   {1:["DEBUG",   COLORS['BLUE']],
    2:["WARNING", COLORS['YELLOW']],
    3:["ERROR", COLORS['RED']],
    4:["INFO", COLORS['BLACK']]}
           
def message(which, message):
    # "sanity checking"
    if which < 1 or which > len(prefix)+1:
        which = 1
    print(prefix[which][1],prefix[which][0]+': ',
        message, COLORS['RESET'])

if __name__ == "__main__":
    for which in prefix.keys():
        message(which, "This is "
            + prefix[which][0].lower())

