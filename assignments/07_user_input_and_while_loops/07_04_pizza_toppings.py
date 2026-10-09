# 7-4. Pizza Toppings

prompt = "Enter a topping to add to your pizza (or 'quit' to finish): "

while True:
    topping = input(prompt)
    if topping.lower() == 'quit':
        break
    print(f"I'll add {topping.title()} to your pizza.")
