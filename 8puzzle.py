class Solver:
    def __init__(self):
        self.side = 3
        self.problem = [4, 1, 3, 6, 5, 9, 8, 7, 2]
    
    def manhattan(self, start, goal):
        start_x, start_y = start % self.side, start // self.side
        goal_x, goal_y = goal % self.side, goal // self.side
        return abs(goal_x - start_x) + abs(goal_y - start_y)

    def heuristic(self):
        sum = self.manhattan(9, self.problem[0])
        for i in range(1, 9):
            sum = sum + self.manhattan(i, self.problem[i])
        return sum

game = Solver()
print(game.heuristic())