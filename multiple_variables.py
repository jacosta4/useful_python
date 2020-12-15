# Primera Asignacion
# Cuando las variables y los valores son iguales, cada valor se asignara a la correspondiente 
# variable según su posición. 
a, b = 2, 3
print(a, b) 
print(type(a))
print(type(b))

"""
Output
    2 3
    <class 'int'>
    <class 'int'>
"""

# Segunnda asignacion 
# Multiples valores pueden ser adignados a una misma variable, el * antes de la variable permitirá
# este proceso. Obtendremos como resultado una lista asignada a dicha variable, con los valores 
# que le correspondan según la asignación previamente descrita.  
a, *b = 2, 3, 4, 5
print(a, b) 
print(type(a))
print(type(b))

"""
Output
    2 [3, 4, 5]
    <class 'int'>
    <class 'list'>
"""

# Tercer tipo de asignacion 
# Asignación de un mismo valor a mas de una variable en una misma linea. 
a = b = c = 2
print(a, b, c)
print(type(a))
print(type(b))
print(type(c))

"""
Output
    2 2 2
    <class 'int'>
    <class 'int'>
    <class 'int'>
"""