# Vamos a encontrar el elemento mas frecuente en una lista 
# Utilizamos la funcion max()
# Si solo se le pasa u argumento, retorna el elemento mayor.

numbers = [1,2,3,7,5,4,6,8,7,5,2,1,4,6,8,0,7,5,3,6,9,0,8,5]
most_fr = max(numbers, key=numbers.count)
print(most_fr)
print(type(most_fr))