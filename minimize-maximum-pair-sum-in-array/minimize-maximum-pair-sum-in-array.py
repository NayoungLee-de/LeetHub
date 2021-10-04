class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pair = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n//2):
            a = [nums[i],nums[n-i-1]]
            pair.append(a)
            
        m = 0
        for i,j in pair:
            m = max(i+j, m)
        return m