"""
191. Number of 1 Bits

Write a function that takes the binary representation of a positive integer and returns the number of
set bits
it has (also known as the Hamming weight).
"""
class Solution:
    def hammingWeight(self, n: int) -> int:
        output = 0
        while n:
            if n%2:
                output+=1
            n=n>>1
        return output
    