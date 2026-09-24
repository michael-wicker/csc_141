# 03_05 Changing Guest List
# Replace one guest who cannot attend and invite the new guest.

guests = ["Alice", "Bob", "Charlie"]

print(f"Sorry, {guests[2]} cannot make it.")
guests[2] = "Dana"

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")
