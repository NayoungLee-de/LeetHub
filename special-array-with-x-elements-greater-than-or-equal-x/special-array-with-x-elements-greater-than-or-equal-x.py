class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        cnt = 0
        l = len(nums)
        
        for i in range(1,l+1):
            idx = bisect.bisect_left(nums, i)
            if l-idx == i:
                return i
        return -1