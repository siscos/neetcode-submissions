class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        rows, cols = len(grid), len(grid[0])

        def bfs(r: int, c: int) -> None:
            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                r, c = q.popleft()
                for dr, dc in directions:
                    curr_r, curr_c = r + dr, c + dc
                    if curr_r < 0 or curr_c < 0 or curr_c >= cols or curr_r >= rows or grid[curr_r][curr_c] == '0':
                        continue

                    q.append((curr_r, curr_c))
                    grid[curr_r][curr_c] = '0'
                

        num_islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    bfs(r, c)
                    num_islands += 1

        return num_islands




        