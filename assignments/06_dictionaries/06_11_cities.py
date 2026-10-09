# 6-11. Cities

cities = {
    'Seattle': {
        'country': 'United States',
        'population': 749256,
        'fact': 'It is known for coffee shops and the Space Needle.'
    },
    'Paris': {
        'country': 'France',
        'population': 2161000,
        'fact': 'It is home to the Eiffel Tower.'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': 37400068,
        'fact': 'It is one of the largest cities in the world.'
    }
}

for city, info in cities.items():
    print(f"\n{city}:")
    print(f"Country: {info['country']}")
    print(f"Population: {info['population']}")
    print(f"Fact: {info['fact']}")
