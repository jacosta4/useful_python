# Utilizando la función split()
# EL objetivo es separar las palabras de un string y obtener una lista con las mismas 
# Se establece como argument de la función spli() el separador que querramos que haya entre 
#   los elementos de la lista. 
string = "This is a new program to see split() function"
new_list = string.split(' ')
print(new_list)

"""
Output
['This', 'is', 'a', 'new', 'program', 'to', 'see', 'split()', 'function']
"""

## Utilizando la función join()
# Es el proceso contrario, convertimos una lista de palabras en una sola linea usando join()
# Syntaxis: " ".join(list)
my_list = ["This", "is", "a", "join()", "function"]
new_string = " ".join(my_list)
print(new_string)

"""
Output
This is a join() function
"""