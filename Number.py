# The Idea behind this class is to create an object which
# holds a list of bits ( 0 || 1)
class Number:
    def __init__(self, num):
       self.bin_num = self.convert_2Bin(num)

    def __str__(self):
        return f'{self.bin_num}'

    @staticmethod
    def invert_list(raw_bin):

        # Define start and end of list(index-wise)
        start = 0
        end = len(raw_bin) - 1

        # when start == end (middle of list)
        while start < end:
            # Swap start and finish and move towards middle index
            raw_bin[start], raw_bin[end] = raw_bin[end], raw_bin[start]

            # Increment and decrement to move towards middle index(s)
            start += 1
            end -= 1

        # Return modified list
        return raw_bin

    @staticmethod
    def convert_2Bin(num):
        # Raw binary representation (needs to be inverted)
        raw_bin = []

        while num > 0:
            # Modulo will return 1 or 0 depending on if there is a remainder
            raw_bin.append(num % 2)
            # Ensure integer division is performed
            num //= 2

        return Number.invert_list(raw_bin)


