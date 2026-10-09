# 6-7. People

people = [
    {
        'first_name': 'Maya',
        'last_name': 'Johnson',
        'age': 20,
        'city': 'Seattle'
    },
    {
        'first_name': 'Leo',
        'last_name': 'Martinez',
        'age': 22,
        'city': 'Austin'
    },
    {
        'first_name': 'Ava',
        'last_name': 'Nguyen',
        'age': 18,
        'city': 'Boston'
    }
]

for person in people:
    print(f"{person['first_name']} {person['last_name']} is {person['age']} years old and lives in {person['city']}.")
