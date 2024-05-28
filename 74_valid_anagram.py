class Solution:
    """Class representing a solution to the anagram check problem."""

    def isAnagram(self, s: str, t: str) -> bool:
        """Checks if two strings are anagrams of each other.

        Args:
            s (str): The first string.
            t (str): The second string.

        Returns:
            bool: True if `s` and `t` are anagrams, False otherwise.

        """
        if len(s) != len(t):
            return False
        s_dict = {}
        t_dict = {}

        for _s, _t in zip(s, t):
            s_dict[_s] = s_dict.get(_s, 0) + 1
            t_dict[_t] = t_dict.get(_t, 0) + 1
        return True if s_dict == t_dict else False
