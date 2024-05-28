import heapq
class MedianFinder:

    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def addNum(self, num: int) -> None:
        #  add ele to min_heap
        heapq.heappush(self.min_heap, -1*num)
        # check for consistency
        if self.min_heap and self.max_heap and -1*self.min_heap[0] > self.max_heap[0]:
            heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))
        # uneven size
        if len(self.min_heap) > len(self.max_heap)+1:
            heapq.heappush(self.max_heap, -1*heapq.heappop(self.min_heap))
        if len(self.max_heap) > len(self.min_heap)+1:
            heapq.heappush(self.min_heap, -1*heapq.heappop(self.max_heap))

    def findMedian(self) -> float:
        # if max_heap > min_heap:
        if len(self.max_heap) > len(self.min_heap):
        #   get ele from max_heap
            return self.max_heap[0]
        # elif min_heap > max_heap:
        elif len(self.min_heap) > len(self.max_heap):
        #   get ele from min_heap
            return -1*self.min_heap[0]
        # else:
        else:
        #   get ele1 from min_heap
        #   get  ele2 from max_heap
        #   (ele1+ele2) / 2
            return (-1*self.min_heap[0]+(self.max_heap[0]))/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()