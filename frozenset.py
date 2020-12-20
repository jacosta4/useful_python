## FROZENSET()
# Con este modulo, podemos convertir un modelo mutable en inmutable. Basicamente lo que 
# hace es restringir el objeto para que este no pueda cambiar su valor. 

list_1 = [1,2,3,4,5,6]
list_1 = frozenset(list_1)
print(list_1)
list_1[2] = 9
print(list_1)

"""
OUTPUT
    frozenset({1, 2, 3, 4, 5, 6})
    Traceback (most recent call last):
    File "frozenset.py", line 8, in <module>
        list_1[2] = 9
    TypeError: 'frozenset' object does not support item assignment
"""