class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        nums_len = len(nums)
        output = []
        freq_box = {}
        for key, val in counter.items():
            freq_box[val] = freq_box.get(val, []) + [key]
        
        freq_list = list(freq_box.keys())
        freq_list.sort(reverse=True)

        i = 0
        while len(output) < k:
            for r in freq_box[freq_list[i]]:
                output.append(r)
            i+=1
                
        return output
