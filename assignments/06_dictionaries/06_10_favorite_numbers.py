# 6-10. Favorite Numbers

favorite_numbers = {
    'Maya': [7, 13, 21],
    'Leo': [12, 42],
    'Ava': [3, 9, 27],
    'Noah': [11, 19],
    'Zoe': [5, 8, 15]
}

for name, numbers in favorite_numbers.items():
    print(f"{name}'s favorite numbers are: {', '.join(str(number) for number in numbers)}")
