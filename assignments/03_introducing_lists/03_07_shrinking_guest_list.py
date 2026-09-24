# 03_07 Shrinking Guest List
# Remove guests as the table size changes and print a message.

guests = ["Alice", "Bob", "Charlie", "Dana", "Evan"]

print("I can only invite two people to dinner.")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest}, I can't invite you to dinner.")

for guest in guests:
    print(f"Dear {guest}, you are still invited to dinner.")

del guests[:]
print(guests)
