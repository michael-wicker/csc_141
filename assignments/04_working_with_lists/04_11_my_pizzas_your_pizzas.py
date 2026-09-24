# 04_11 My Pizzas, Your Pizzas
# Copy a list of pizzas and add a new favorite.

my_pizzas = ["pepperoni", "margherita", "veggie"]
your_pizzas = my_pizzas[:]

my_pizzas.append("hawaiian")
your_pizzas.append("bbq chicken")

print("My favorite pizzas are:")
for pizza in my_pizzas:
    print(pizza)

print("\nYour favorite pizzas are:")
for pizza in your_pizzas:
    print(pizza)
