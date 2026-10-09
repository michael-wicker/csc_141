# 7-10. Dream Vacation

responses = {}

poll_active = True

while poll_active:
    name = input("What is your name? ")
    place = input("If you could visit one place in the world, where would you go? ")
    responses[name] = place

    repeat = input("Would someone else like to answer? (yes/no) ")
    if repeat.lower() != 'yes':
        poll_active = False

print("\n--- Poll Results ---")
for name, place in responses.items():
    print(f"{name.title()} would like to visit {place.title()}.")
