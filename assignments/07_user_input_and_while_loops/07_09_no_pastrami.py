# 7-9. No Pastrami

sandwich_orders = ['tuna', 'pastrami', 'turkey', 'pastrami', 'ham', 'pastrami']
finished_sandwiches = []

print("The deli has run out of pastrami.")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
