from Number import Number as num
from Binary_Ops import Binary_Ops as Bops

# This script is for testing the functionality of the Number and Binary_Ops classes.

# Prompt the user to enter two integers.
x = int(input("Please enter the first number: "))
y = int(input("Please enter the second number: "))

# Convert the integers to their binary representation using the Number class.
# Note: The objects a and b store instances of the Number class, not just the binary lists.
a = num(x)
b = num(y)

# Display the original numbers and their binary representations.
print(f'First number: {x}')
print(a.num)  # Binary representation of x
print(f'Second number: {y}')
print(b.num)  # Binary representation of y

# Perform binary addition using Binary_Ops.
result = Bops.addition_two_positive(a.num, b.num)

# Display the result of the binary addition.
print(f'\nResult:\n{result}')
