## Inprimir un calendario con Python 

import calendar

#print(calendar.month(2020, 6))

"""
OUTPUT

     June 2020
Mo Tu We Th Fr Sa Su
 1  2  3  4  5  6  7
 8  9 10 11 12 13 14
15 16 17 18 19 20 21
22 23 24 25 26 27 28
29 30
"""

# calendar.esleap(ear): Devuelve True si el año especificado es bisiesto
print(calendar.isleap(2020))

