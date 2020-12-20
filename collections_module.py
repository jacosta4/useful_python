## Modulo Collection
# Modulo para conocer la ocurrencia de los elementos de una lista 
# El método Counter retorna un diccionario con el par de elementos y ocurrencias en orden.

from collections import Counter

numbers = [1,2,3,7,5,4,6,8,7,5,2,1,4,6,8,0,7,5,3,6,9,0,8,5]
print(Counter(numbers))