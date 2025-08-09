#!/usr/bin/env python3
# File: alert.py
# Rev: 1.0
''' RUN FROM THE COMMAND LINE
The following colorizing codes always
work from POSIX / Linux operating command
line interfaces. Go for Google if otherwise.
'''

import argparse

colors = {
'black'   : '\033[30m',
'blue'    : '\033[34m',
'cyan'    : '\033[36m',
'green'   : '\033[32m',
'magenta' : '\033[35m',
'red'     : '\033[31m',
'white'   : '\033[37m',
'yellow'  : '\033[33m',
'reset'   : '\033[0m'
}

def print_colored(message: str, color: str):
    if not color in colors:
        color = colors['red']
    else:
        color = colors[color]
    if not message:
        message = ':-|'
    print(f"{color}{message}{colors['reset']}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Display ANSI Messages."
    )
    keys = sorted(list(colors))
    keys.remove('reset')
    parser.add_argument(
        "color",
        choices=keys,
        help="Message color."
    )
    parser.add_argument(
        "message",
        help="Message to display.",
        nargs='+'
    )

    args = parser.parse_args()
    message = ' '.join(args.message)
    print_colored(message, args.color)
