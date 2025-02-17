class Binary_Ops:
    @staticmethod
    def binary_addition(a, b):

        # Reverse for easier addition (LSB to MSB)
        a = Binary_Ops.reverse_list(a)
        b = Binary_Ops.reverse_list(b)

        # Pad both lists to equal length
        max_length = max(len(a), len(b))
        a = Binary_Ops.pad_bin_list(a, max_length)
        b = Binary_Ops.pad_bin_list(a, max_length)

        c = []
        # Initially the carry will be zero at the first addition
        carry = 0

        for i in range(max_length):
            # Add corresponding bits and carry
            sum_value = a[i] + b[i] + carry

            if sum_value == 2:  # 1 + 1
                c.append(0)
                carry = 1
            elif sum_value == 3:  # 1 + 1 + carry
                c.append(1)
                carry = 1
            else:
                c.append(sum_value) # 0 + 1 || 1 + 0
                carry = 0

        # If there's a carry left, append it
        if carry:
            c.append(1)

        return Binary_Ops.reverse_list(c)


    @staticmethod
    def pad_bin_list(x, length):
        """Pads a binary list with leading zeros to match the required length."""
        while len(x) < length:
            x.insert(0, 0)  # Add leading zeros
        return x

    # The purpose of the repeated reverse_list function
    # is to show prep the binary list for addition
    @staticmethod
    def reverse_list(x):
        # Define start and end of list(index-wise)
        start = 0
        end = len(x) - 1

        # when start == end (middle of list)
        while start < end:
            # Swap start and finish and move towards middle index
            x[start], x[end] = x[end], x[start]
            # Increment and decrement to move towards middle index(s)
            start += 1
            end -= 1

        # Return modified list
        return x



