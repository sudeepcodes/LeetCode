from typing import List


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        cur_dir = 0
        x, y = 0, 0
        dist = 0

        obstacles = set([tuple(obs) for obs in obstacles])

        for command in commands:
            if command == -2:
                cur_dir = (cur_dir - 1) % 4
            elif command == -1:
                cur_dir = (cur_dir + 1) % 4
            else:
                dx, dy = directions[cur_dir]
                for _ in range(command):
                    next_x, next_y = x + dx, y + dy
                    if (next_x, next_y) in obstacles:
                        break
                    x, y = next_x, next_y
            dist = max(dist, x ** 2 + y ** 2)

        return dist


print(Solution().robotSim([4,-1,4,-2,4], [[2,4]]))
