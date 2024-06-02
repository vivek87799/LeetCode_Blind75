"""
3. Longest Substring Without Repeating Characters

Given a string s, find the length of the longest
substring
without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<=1:
            return len(s)
        substirng_set = set()
        l,r = 0, 0
        output = float('-inf')
        while r<len(s):
            while s[r] in substirng_set:
                substirng_set.remove(s[l])
                l+=1
            output = max(output, r-l+1)
            substirng_set.add(s[r])
            print(l, r, substirng_set, output)
            r+=1
        return output