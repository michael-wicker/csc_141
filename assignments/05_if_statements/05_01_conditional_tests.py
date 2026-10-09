# 5-1. Conditional Tests:

car = 'subaru'
topping = 'mushrooms'
age = 25
is_student = False

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print("\nIs car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car != 'audi'? I predict True.")
print(car != 'audi')

print("\nIs car == 'Subaru'? I predict False.")
print(car == 'Subaru')

print("\nIs age == 25? I predict True.")
print(age == 25)

print("\nIs age > 30? I predict False.")
print(age > 30)

print("\nIs age < 18? I predict False.")
print(age < 18)

print("\nIs age >= 25 and is_student == False? I predict True.")
print(age >= 25 and is_student == False)

print("\nIs topping == 'pepperoni'? I predict False.")
print(topping == 'pepperoni')

print("\nIs topping != 'mushrooms'? I predict False.")
print(topping != 'mushrooms')

print("\nIs 'sub' in car? I predict True.")
print('sub' in car)

print("\nIs 'a' not in car? I predict False.")
print('a' not in car)
