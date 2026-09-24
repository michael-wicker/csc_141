# 03_06 More Guests
# Add new guests to the dinner list and print the updated invitations.

guests = ["Alice", "Bob", "Charlie"]
new_guests = ["Dana", "Evan", "Frank"]

for guest in new_guests:
    guests.append(guest)

for guest in guests:
    print(f"Dear {guest}, you are invited to dinner.")
