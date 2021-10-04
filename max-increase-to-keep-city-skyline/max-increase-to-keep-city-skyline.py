class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        west = []
        south = []
        for i in grid:
            west.append(max(i))
        
        n = len(grid[0])
        
        for i in range(n):
            m = 0
            for j in range(n):
                m = max(m, grid[j][i])
            south.append(m)
        
        ans = 0
        for i in range(n):
            for j in range(n):
                a = south[j] - grid[i][j]
                b = west[i] - grid[i][j]
                if a>=0 and b>=0:
                    ans += min(a, b)
        return ans
                
                