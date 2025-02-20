"""
This class represents a Number object that stores
a list of bits (0 or 1), representing its binary form.
"""
class Number:
    # Constructor: Initializes a Number object with its binary representation.
    def __init__(self, num):
        if num >= 0:
            self.num = self.Binary(num)
        if num < 0:
            self.num = self.twos_compliment(num)
    # Allows the object to be printed directly, returning its binary form as a string.
    def __str__(self):
        return f'{self.num}'

    # Converts a positive integer into its binary representation.
    # This is a static method since it acts as a utility function.
    @staticmethod
    def Binary(num):
        # Handle the special case where num is zero.
        if num == 0:
            return [0]

        raw_bin = []  # Stores the binary digits in reverse order.

        while num > 0:
            raw_bin.append(num % 2)  # Get the least significant bit.
            num //= 2  # Perform integer division to shift right.

        return raw_bin[::-1]  # Reverse the list to get the correct order.

    @staticmethod
    def twos_compliment(num):
        """
        Compute the two's complement representation of a given integer.

        This method takes an integer `num`, computes its binary representation,
        inverts the bits to find the one's complement, and adds 1 to the result
        to obtain the two's complement. The result is returned as a list of bits,
        with the least significant bit (LSB) first.
        """

        # Obtain the absolute value of the number to handle negative inputs
        num = abs(num)

        # Initialize an empty list to store binary digits in reverse order
        raw_bin = []

        # Convert the absolute value of the number to binary
        while num > 0:
            # Append the least significant bit (LSB) to the list
            raw_bin.append(num % 2)
            # Shift the number to the right (integer division by 2)
            num //= 2

        # Determine the maximum length of the binary list
        max_length = len(raw_bin)

        # Compute the one's complement by inverting each bit
        one_comp = [1 - bit for bit in raw_bin]

        # Initialize the list for the two's complement and set the initial carry to 1
        two_comp = []
        carry = 1

        # Perform bit-wise addition to compute the two's complement
        for i in range(max_length):
            # Sum the current bit and the carry value
            sum_value = one_comp[i] + carry

            if sum_value == 2:
                # If the sum is 2 (1 + 1), append 0 and keep the carry as 1
                two_comp.append(0)
                carry = 1
            elif sum_value == 3:
                # If the sum is 3 (1 + 1 + carry), append 1 and keep the carry as 1
                two_comp.append(1)
                carry = 1
            else:
                # For cases where sum is 0 + 1, 1 + 0, or 0 + 0, append the sum and reset carry
                two_comp.append(sum_value)
                carry = 0

        # If there's a remaining carry after processing all bits, append it to the result
        if carry:
            two_comp.append(1)

        # Reverse the list to restore the correct bit order (most significant bit first)
        return two_comp[::-1]

