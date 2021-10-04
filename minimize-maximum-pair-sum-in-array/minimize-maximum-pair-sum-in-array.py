class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        pair = []
        nums = sorted(nums)
        n = len(nums)
        for i in range(n//2):
            a = [nums[i],nums[n-i-1]]
            pair.append(a)
        ans = []
        for i,j in pair:
            ans.append(i+j)
        return max(ans)