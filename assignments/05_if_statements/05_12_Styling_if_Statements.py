# 5-12. Styling if Statements

# Good style examples for simple conditional tests
age = 18
color = 'green'

if age >= 18:
    print("You are old enough to vote.")

if color == 'green':
    print("The light is green.")

# Multi-condition test with a clear comparison structure
if age >= 18 and color == 'green':
    print("You are allowed to go and the light is green.")

# A slightly longer condition is broken across lines for readability
if (
    age >= 18
    and color == 'green'
    and True
):
    print("This condition is readable and well styled.")
