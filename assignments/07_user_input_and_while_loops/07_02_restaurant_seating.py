# 7-2. Restaurant Seating

party_size = input("How many people are in your dinner group? ")
party_size = int(party_size)

if party_size > 8:
    print("You will have to wait for a table.")
else:
    print("Your table is ready.")
