class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        column=len(grid[0])
        island=0
        def dfs(row,col):
            if row < 0 or row >= rows or col < 0 or col >= column: # outisde the grid
                return
            if grid[row][col] !='1':
                return 
            grid[row][col]='0'
            dfs(row,col-1)
            dfs(row-1,col)
            dfs(row+1,col)
            dfs(row,col+1)




        for i in range(rows):
            for j in range(column):
                if grid[i][j]=='1':
                    dfs(i,j)
                    island+=1

        return island