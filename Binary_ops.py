from Number import Number as num

class Binary_Ops:
    @staticmethod
    def addition_two_positive(a, b):
        """
        Performs binary addition of two positive numbers represented as lists of bits.
        """

        # Ensure both lists have the same length by padding with leading zeros.
        max_length = max(len(a), len(b))
        if len(a) < len(b):
            a = Binary_Ops.pad_bin_list(a, max_length)
        else:
            b = Binary_Ops.pad_bin_list(b, max_length)

        # Reverse the lists to align the least significant bits for addition.
        a.reverse()
        b.reverse()

        c = []  # Resultant binary sum list.
        carry = 0  # Initialize carry to zero.

        # Perform bit-wise addition.
        for i in range(max_length):
            sum_value = a[i] + b[i] + carry  # Sum current bits with carry.

            if sum_value == 2:  # Case: 1 + 1
                c.append(0)
                carry = 1
            elif sum_value == 3:  # Case: 1 + 1 + carry
                c.append(1)
                carry = 1
            else:  # Case: 0 + 1, 1 + 0, or 0 + 0
                c.append(sum_value)
                carry = 0

        # If there's a remaining carry, append it to the result.
        if carry:
            c.append(1)

        return c[::-1]  # Reverse to restore correct bit order.

    @staticmethod
    def pad_bin_list(x, length):
        """
        Pads a binary list with leading zeros to ensure it matches the given length.
        """
        return [0] * (length - len(x)) + x  # Prepend leading zeros.
