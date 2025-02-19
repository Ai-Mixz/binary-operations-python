from Number import Number as num
from Binary_Ops import Binary_Ops as Bops

x = int(input("Please enter a first number: "))
y = int(input("Please enter second number: "))

# Note a (and b respectively) do not hold the list directly
a = num(x)
b = num(y)

print(f'Original: \n'
      f'{a.bin_num}\n'
      f'{b.bin_num}\n')

result = Bops.addition_two_positive(a.bin_num,b.bin_num)

print(f'Result: {result}')
