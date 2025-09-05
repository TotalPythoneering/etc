## TUI Common Denominator
From forcing us to junk our non-broke computers to so many classic colorized console 'apps freedom, portability as well as hugely lower power, bios-efficient, secure & higher-performance options have ever 'been there' ... if 'ya know where to look!

(i.e. From Mainframes to POSIX - the colors never left!)

### Linux / WSL / ANSI Enabled O.S:
![](https://github.com/TotalPythoneering/etc/blob/main/ansi/color_sets.png)

### Educational Escape (* npi)
Today's console games & 'apps are a genre ... a handy go-to for educators? 🤠 

(* No pun intended)

The Videos:

[The Dump](https://ko-fi.com/Post/Colorizing-Your-App--T-U-I-Style-C0C31JKS47).

[The Possibilities](https://youtube.com/shorts/EYGPHQ_qCVQ?si=v6zZm1SQuDMKF8t2).

[The Idea](https://youtube.com/shorts/-2tGT4vkTRQ?si=7qeUUsgkrXN9PaDd).

## Ansi Possibilities?

### Common Escapes
These single-value codes are used to set basic text styling. 

    0: Reset all attributes to default.
    1: Bold or increased intensity.
    4: Underline.
    7: Inverse (swap foreground and background colors).
    22: Normal intensity (not bold).
    24: Not underlined.
    27: Not inverse. 

### 8-color (basic)
The most basic ANSI color set includes 8 colors for
foreground and background. On many terminals, the
bold attribute provides a brighter version
of these colors.

#### "Plus 10" Color Pallet
*Color, Foreground code, Background code*
```
Black,	30,	40
Red,	31,	41
Green, 32,	42
Yellow,	33,	43
Blue,	34,	44
Magenta,	35,	45
Cyan,	36,	46
White,	37,	47
```

### 16-color (bright)
This set includes the basic 8 colors
plus 8 "bright" variations, which are
typically used by combining the bold
attribute with the basic color codes.
Some terminals, however, have separate
codes for the bright colors.

### Use the m, Luke
```
RESET = '\033[0m'
for esc in range(30,38), range(40,48), range(90,98), range(100,108):
    for num in esc:
        print(f'\033[{num}m#{RESET}',end='')
    print()
```

#### Bright Color
Same "+10" strategy

*Color, Foreground code, Background code*

```
Bright Black,	90,	100
Bright Red,	91,	101
Bright Green,	92,	102
Bright Yellow,	93,	103
Bright Blue,	94,	104
Bright Magenta,	95,	105
Bright Cyan, 96,	106
Bright White,	97,	107
```


### 256-color (8-bit)
Modern terminals can use an 8-bit palette
to access 256 colors. The sequence is ESC[38;5;n
for foreground and ESC[48;5;n**m** for background,
where n is a number from 0 to 255. 

    0–7: Standard system colors
    
    8–15: High-intensity system colors
    
    16–231: A 6x6x6 RGB color cube
    
    232–255: A grayscale ramp 

#### Too Much!
```
RESET = '\033[0m'
for esc in range(8), range(8,16), range(16,232), range(232,256):
    for ss, num in enumerate(esc,1):
        if ss % 25 == 0:
            print()
        print(f'\033[38;5;{num}m#{RESET}',end='')
    print()
```

### True color (24-bit)
The most advanced terminals support 24-bit or
"true color" using 16 million RGB values. 

The sequence is ESC[38;2;r;g;b**m** for foreground
and ESC[48;2;r;g;b**m** for background, with r, g,
and b values ranging from 0 to 255. 

#### Waaaay too much!!
```
RESET = '\033[0m'
for esc in '\033[38;2;', '\033[48;2;':
    for r in range(256):
        for g in range(256):
            for bs, b in enumerate(range(256),1):
                print(f'{esc}{r};{g};{b}m#{RESET}',end='')
            print()
```
