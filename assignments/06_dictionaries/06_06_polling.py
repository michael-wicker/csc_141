# 6-6. Polling

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

poll_people = ['jen', 'mike', 'sarah', 'alex', 'phil']

for person in poll_people:
    if person in favorite_languages:
        print(f"Thank you, {person.title()}, for responding to the poll.")
    else:
        print(f"{person.title()}, would you like to take the favorite languages poll?")
