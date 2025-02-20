"""
This class represents a Number object that stores
a list of bits (0 or 1), representing its binary form.
"""
class Number:
    # Constructor: Initializes a Number object with its binary representation.
    def __init__(self, num):
        self.num = self.convert_2Bin(num)

    # Allows the object to be printed directly, returning its binary form as a string.
    def __str__(self):
        return f'{self.num}'

    # Converts a positive integer into its binary representation.
    # This is a static method since it acts as a utility function.
    @staticmethod
    def convert_2Bin(num):
        # Handle the special case where num is zero.
        if num == 0:
            return [0]

        raw_bin = []  # Stores the binary digits in reverse order.

        while num > 0:
            raw_bin.append(num % 2)  # Get the least significant bit.
            num //= 2  # Perform integer division to shift right.

        return raw_bin[::-1]  # Reverse the list to get the correct order.
