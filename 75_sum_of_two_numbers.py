class Solution:
    """Class representing a solution to the sum of two integers problem."""

    def getSum(self, a: int, b: int) -> int:
        """Returns the sum of two integers.

        Args:
            a (int): The first integer.
            b (int): The second integer.

        Returns:
            int: The sum of `a` and `b`.
        """
        # Python does not have a fixed size (32bit) for integers. 
        mask = 0b11111111111111111111111111111111
        # Iterate until there is no carry
        while (b & mask) != 0:
            # Carry now contains common set bits of a and b
            carry = a & b

            # Sum of bits of a and b where at least one of the bits is not set
            a = a ^ b

            # Carry is shifted by one so that adding it to a gives the required sum
            b = carry << 1

        return a&mask if b > 0 else a