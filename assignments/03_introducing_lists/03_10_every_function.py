# 03_10 Every Function
# Demonstrate common list functions and methods.

numbers = [3, 1, 4, 1, 5]

numbers.append(9)
print(f"After append: {numbers}")

numbers.insert(0, 2)
print(f"After insert: {numbers}")

numbers.remove(1)
print(f"After remove: {numbers}")

popped_value = numbers.pop()
print(f"Popped value: {popped_value}")
print(f"After pop: {numbers}")

numbers.sort()
print(f"After sort: {numbers}")

numbers.sort(reverse=True)
print(f"After reverse sort: {numbers}")

numbers.reverse()
print(f"After reverse: {numbers}")

print(f"Length: {len(numbers)}")
print(f"Minimum: {min(numbers)}")
print(f"Maximum: {max(numbers)}")
print(f"Sum: {sum(numbers)}")
