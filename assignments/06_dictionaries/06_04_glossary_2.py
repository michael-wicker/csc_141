# 6-4. Glossary 2

# Original five terms plus five more
programming_glossary = {
    'variable': 'A named storage location used to hold data in a program.',
    'list': 'A collection of items that can be changed and accessed by index.',
    'dictionary': 'A collection of key-value pairs used to store related data.',
    'loop': 'A structure that repeats a block of code until a condition is met.',
    'function': 'A reusable block of code that performs a specific task.',
    'string': 'A sequence of characters used to represent text.',
    'boolean': 'A data type with only two values: True or False.',
    'tuple': 'An ordered, immutable collection of values.',
    'condition': 'A statement that checks whether something is true or false.',
    'module': 'A file containing Python code that can be imported and reused.'
}

for word, meaning in programming_glossary.items():
    print(f"{word.title()}: {meaning}\n")
