""" Optional Parameters """

# Valor default asignado al os parametros de la función 
# Si no se llama un argumento, toma por defecto el 1 en este caso. 
def func(x=1):
    return x**2

call = func()
print(call)

# Multiples valores opcionales
# Si deseo dejar add con su valor por defecto, es mejor dejarlo de ultimo en los parametros
def func(word, freq=1, add=5):
   print(word*(add+freq))

call = func('hello', 2)

# Aplicado en una clase 
class item():
    def __init__(self, room, price=100):
        self.room = room
        self.price = price

    def display(self, full_price=True):
        discount_price = self.price - (self.price * 0.01)
        if full_price:
            print(f"Your room number is {self.room} and it costs {self.price} usd.")
        else: 
            print(f"Your room number is {self.room} and it costs {discount_price} usd with the discount.")

client = item(403)
client.display(True)
