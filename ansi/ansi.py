#!/usr/bin/env python3
# File: ansi.py
# Colorizing TUI Projects in Python: Strategy 01
# Version: 1.0
#
# The COLORS Key:
#   [cid]_[b|f][1|2]
#   cid = one of 7 color names (see COLOR_ORDER)
#   b   = background usage
#   f   = foreground usage
#   1   = standard intensity
#   2   = higher / brighter
#
# Source: https://github.com/TotalPythoneering/etc/tree/main/ansi
# Author: https://ko-fi.com/Post/Colorizing-Your-App--T-U-I-Style-C0C31JKS47
# Author: https://ko-fi.com/post/If-you-had-to-write-one-program-D1D61JSD5W

RESET = '\033[0m'

COLORS = {
"black_f1"      : "\033[30m",
"black_f2"      : "\033[90m",
"black_b1"      : "\033[40m",
"black_b2"      : "\033[100m",
"blue_f1"       : "\033[34m",
"blue_f2"       : "\033[94m",
"blue_b1"       : "\033[44m",
"blue_b2"       : "\033[104m",
"cyan_f1"       : "\033[36m",
"cyan_f2"       : "\033[96m",
"cyan_b1"       : "\033[46m",
"cyan_b2"       : "\033[106m",
"green_f1"      : "\033[32m",
"green_f2"      : "\033[92m",
"green_b1"      : "\033[42m",
"green_b2"      : "\033[102m",
"majenta_f1"    : "\033[35m",
"majenta_f2"    : "\033[95m",
"majenta_b1"    : "\033[45m",
"majenta_b2"    : "\033[105m",
"red_f1"        : "\033[31m",
"red_f2"        : "\033[91m",
"red_b1"        : "\033[41m",
"red_b2"        : "\033[101m",
"white_f1"      : "\033[37m",
"white_f2"      : "\033[97m",
"white_b1"      : "\033[47m",
"white_b2"      : "\033[107m",
"yellow_f1"     : "\033[33m",
"yellow_f2"     : "\033[93m",
"yellow_b1"     : "\033[43m",
"yellow_b2"     : "\033[103m",
}

COLOR_ORDER = {
'black'  :0,
'red'    :1,
'green'  :2,
'yellow' :3,
'blue'   :4,
'magenta':5,
'cyan'   :6,
'white'  :7,
}


def show():
    for ss, key in enumerate(COLORS,1):
        print(f'{COLORS[key]}{ss}.) {key}{RESET}')

def sort():
    for ss, key in enumerate(sorted(COLORS),1):
        print(f'{COLORS[key]}{ss}.) {key}{RESET}')


if __name__ == '__main__':
    show()

