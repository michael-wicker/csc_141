# 03_08 Seeing the World
# Store places to visit, print in original and sorted orders.

places = ["Tokyo", "Paris", "New York", "Rome", "Sydney"]

print("Original order:")
print(places)

print("\nAlphabetical order without changing the list:")
print(sorted(places))

print("\nOriginal order again:")
print(places)

print("\nReverse alphabetical order without changing the list:")
print(sorted(places, reverse=True))

print("\nOriginal order after sorting tests:")
print(places)

places.reverse()
print("\nReversed list:")
print(places)

places.reverse()
print("\nList back to original order:")
print(places)

places.sort()
print("\nSorted list in alphabetical order:")
print(places)

places.sort(reverse=True)
print("\nSorted list in reverse alphabetical order:")
print(places)
