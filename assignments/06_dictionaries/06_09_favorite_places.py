# 6-9. Favorite Places

favorite_places = {
    'Maya': ['Seattle', 'Paris', 'Kyoto'],
    'Leo': ['Austin', 'New York'],
    'Ava': ['Tokyo', 'Barcelona']
}

for person, places in favorite_places.items():
    print(f"{person}'s favorite places are: {', '.join(places)}")
