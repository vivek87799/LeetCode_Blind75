from typing import List

class Solution:
    def listSubSequences(self, s: List[str]) -> List[str]:
        output = []
        def listSubSequencesHelper(ind: int, arr: List[str]) -> List[str]:
            if ind >= len(s):
                output.append(''.join(arr))
            else:
                listSubSequencesHelper(ind+2, arr+[s[ind]])
                listSubSequencesHelper(ind+1, arr)
                
                
        listSubSequencesHelper(0, [])
        return output

sequence = "abcdefg"
solution = Solution()
result = solution.listSubSequences(sequence)
print(result)

