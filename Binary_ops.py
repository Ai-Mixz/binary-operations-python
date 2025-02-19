from Number import Number as num

class Binary_Ops:
    @staticmethod
    def addition_two_positive(a, b):

        # Reverse for easier addition (LSB to MSB)
        a = num.Reverse_list(a)
        b = num.Reverse_list(b)

        # Pad both lists to equal length
        max_length = max(len(a), len(b))
        a = Binary_Ops.pad_bin_list(a, max_length)
        b = Binary_Ops.pad_bin_list(b, max_length)

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
                c.append(sum_value) # 0 + 1 || 1 + 0 || 0 + 0
                carry = 0

        # If there's a carry left, append it
        if carry:
            c.append(1)

        return num.Reverse_list(c)

    @staticmethod
    def pad_bin_list(x, length):
        # Pads a binary list with leading zeros to match the required length.
        while len(x) < length:
            x.insert(0, 0)  # Add leading zeros
        return x


