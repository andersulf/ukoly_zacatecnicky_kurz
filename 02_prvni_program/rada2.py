"""
Tento program rozdává naivní rady do života.

Z prikladu v materialech, verze se zanorenym else
"""
print('Odpovídej "ano" nebo "ne".')
stastna_retezec = input('Jsi šťastná? ')
if stastna_retezec == 'ano':
    stastna = True
elif stastna_retezec == 'ne':
    stastna = False
else:
    print('Nerozumím!')

bohata_retezec = input('Jsi bohatá? ')
if bohata_retezec == 'ano':
    bohata = True
elif bohata_retezec == 'ne':
    bohata = False
else:
    print('Nerozumím!')


if bohata:
    if stastna:
        # Je bohatá a zároveň štǎstná, ta se má.
        print('Gratuluji!')
    else:
        # Je bohatá, ale není šťastná,
        # takže musí být jen bohatá.
        print('Zkus se víc usmívat.')
elif stastna:
    # Tady musí být jen šťastná.
    print('Zkus míň utrácet.')
else:
    # A tady víme, že není ani šťastná, ani bohatá.
    print('To je mi líto.')