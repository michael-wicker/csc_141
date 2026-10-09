# 7-6. Three Exits

# Version 1: conditional test in the while statement
print("Version 1: conditional test in while")
topping = ""
while topping.lower() != 'quit':
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping.title()} to your pizza.")

# Version 2: active variable controls the loop
print("\nVersion 2: active variable")
active = True
while active:
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        active = False
    else:
        print(f"I'll add {topping.title()} to your pizza.")

# Version 3: break statement
print("\nVersion 3: break statement")
while True:
    topping = input("Enter a topping (or 'quit' to finish): ")
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping.title()} to your pizza.")
