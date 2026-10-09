# 7-8. Deli

sandwich_orders = ['tuna', 'turkey', 'ham', 'club']
finished_sandwiches = []

while sandwich_orders:
    current_order = sandwich_orders.pop(0)
    print(f"I made your {current_order} sandwich.")
    finished_sandwiches.append(current_order)

print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
