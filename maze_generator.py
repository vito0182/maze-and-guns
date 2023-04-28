import random
import numpy as np
import time

class Maze:
    def __init__(self, size_x=300, size_y=300):
        self.maze_size = (size_x,size_y)

        self.unvisited = "u"
        self.visited = " "
        self.wall = "X"

        self.maze_grid = ((self.maze_size[0] * 2 - 1), (self.maze_size[1] * 2 -1))
        self.maze = []

        for row in range(self.maze_grid[0]):
            line = []
            for cell in range(self.maze_grid[1]):
                line += self.unvisited if (cell % 2 == 0 and row % 2 == 0) else self.wall
            self.maze.append(line)

        self.x = random.randrange(1, self.maze_grid[0] + 1, 2) - 1
        self.y = random.randrange(1, self.maze_grid[1] + 1, 2) - 1
        self.path = []

    def track_unvisited(self):
        
        mx, my = self.x,self.y

        while any(self.unvisited in nested_list for nested_list in self.maze):

            list = []

            if (mx+1 < self.maze_grid[0]) and self.maze[mx + 2][my] == self.unvisited:
                list.append([mx + 2, my])

            if (my+1 < self.maze_grid[1]) and self.maze[mx][my + 2] == self.unvisited:
                list.append([mx, my + 2])

            if (mx-2 >= 0) and self.maze[mx - 2][my] == self.unvisited:
                list.append([mx - 2, my])

            if (my-2 >= 0) and self.maze[mx][my - 2] == self.unvisited:
                list.append([mx, my - 2])

            if list:
                
                self.maze[mx][my] = self.visited
                tracked_cell = random.choice(list)

                self.path.append(tracked_cell)

                self.maze[int((mx+tracked_cell[0])/2)][int((my+tracked_cell[1])/2)] = self.visited
                self.maze[tracked_cell[0]][tracked_cell[1]] = self.visited
        
            else:

                del self.path[-1]
                tracked_cell = self.path[-1]

            mx, my = tracked_cell[0], tracked_cell[1]

        return self.maze


print(time.time())
if __name__ == "__main__":
    maze = Maze()
    print(*maze.track_unvisited(), sep="\n")
print(time.time())