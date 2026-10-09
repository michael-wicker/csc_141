# 6-3. Glossary

glossary = {
    'variable': 'A named storage location used to hold data in a program.',
    'list': 'A collection of items that can be changed and accessed by index.',
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'loop': 'A structure that repeats a block of code until a condition is met.',
    'function': 'A reusable block of code that performs a specific task.'
}

for word, meaning in glossary.items():
    print(f"{word.title()}: {meaning}\n")
