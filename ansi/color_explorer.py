# We're using W.S.L, a.k.a
# "Windows Subsystem for 
# Linux" - Debian.
# Video: https://ko-fi.com/post/Colorizing-Your-App--T-U-I-Style-C0C31JKS47

ESC = '\33[' # Escape 
RESET = ESC + '0m' # Yup

r = range(1,100)
for s,x in enumerate(r,1):
    print(f'{ESC}{x}m',
          f'{x:02}{RESET}',
          end='')
    if s % 10 == 0: print()
print()
