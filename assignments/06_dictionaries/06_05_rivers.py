# 6-5. Rivers

rivers = {
    'nile': 'Egypt',
    'amazon': 'Brazil',
    'mississippi': 'United States'
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through {country}.")

print("\nRivers:")
for river in rivers:
    print(river.title())

print("\nCountries:")
for country in rivers.values():
    print(country)
