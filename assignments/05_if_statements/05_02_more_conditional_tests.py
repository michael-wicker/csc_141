# 5-2. More Conditional Tests

car = 'subaru'
name = 'Maya'
age = 25
is_student = False
favorite_foods = ['pizza', 'tacos', 'pasta']

print("String equality and inequality")
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print("\nIs name != 'Maya'? I predict False.")
print(name != 'Maya')
print("\nIs name == 'maya'? I predict False.")
print(name == 'maya')

print("\nTests using the lower() method")
print("Is car.lower() == 'subaru'? I predict True.")
print(car.lower() == 'subaru')
print("\nIs name.lower() == 'maya'? I predict True.")
print(name.lower() == 'maya')
print("\nIs 'SUBARU'.lower() == 'subaru'? I predict True.")
print('SUBARU'.lower() == 'subaru')

print("\nNumerical tests")
print("Is age == 25? I predict True.")
print(age == 25)
print("\nIs age != 25? I predict False.")
print(age != 25)
print("\nIs age > 30? I predict False.")
print(age > 30)
print("\nIs age < 30? I predict True.")
print(age < 30)
print("\nIs age >= 25? I predict True.")
print(age >= 25)
print("\nIs age <= 20? I predict False.")
print(age <= 20)

print("\nTests using and and or")
print("Is age >= 25 and is_student == False? I predict True.")
print(age >= 25 and is_student == False)
print("\nIs age > 25 and is_student == False? I predict False.")
print(age > 25 and is_student == False)
print("\nIs age > 25 or is_student == True? I predict False.")
print(age > 25 or is_student == True)
print("\nIs age < 30 or is_student == True? I predict True.")
print(age < 30 or is_student == True)

print("\nTests for list membership")
print("Is 'pizza' in favorite_foods? I predict True.")
print('pizza' in favorite_foods)
print("\nIs 'burger' in favorite_foods? I predict False.")
print('burger' in favorite_foods)
print("\nIs 'burger' not in favorite_foods? I predict True.")
print('burger' not in favorite_foods)
print("\nIs 'pizza' not in favorite_foods? I predict False.")
print('pizza' not in favorite_foods)
