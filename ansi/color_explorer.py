for s, x in enumerate(range(1,100),1):
    print(f' \33[{x}m{x:02}\33[0m', end='')
    if s % 10 == 0: print()
print()
