#!/usr/bin/env python3

# Uključivanje modula za geometriju
from geom import *

# Definisanje potrebnih transformacija
t1 = trans(-204, -132)
t2 = refl(90)
t3 = skal(1/7, 1/7)

# Matrica prelaza sa platna na koord. sistem
plat_u_koord = t3 * t2 * t1
print(plat_u_koord)
print()

# Definisanje inverznih transformacija
t1 = trans(204, 132)
t2 = refl(90)
t3 = skal(7, 7)

# Matrica prelaza sa koord. sistema na platno
koord_u_plat = t1 * t2 * t3
print(koord_u_plat)
print()

# Definisanje tačke platna
tac_plat = tacka(202, 129)
print(tac_plat)
print()

# Prelazak u koord. sistem
tac_koord = plat_u_koord * tac_plat
print(tac_koord)
print()

# Skaliranje u koord. sistemu
tac_skal_koord = skal(2,2) * tac_koord
print(tac_skal_koord)
print()

# Vraćanje u platno
tac_skal_plat = koord_u_plat * tac_skal_koord
print(tac_skal_plat)
print()
