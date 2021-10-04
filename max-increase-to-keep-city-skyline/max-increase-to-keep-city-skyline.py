class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        west = [max(i) for i in grid]
        south = [max(i) for i in zip(*grid)]
        
        n = len(grid[0])
        ans = 0
        for i in range(n):
            for j in range(n):
                a = south[j] - grid[i][j]
                b = west[i] - grid[i][j]
                if a>=0 and b>=0:
                    ans += min(a, b)
        return ans