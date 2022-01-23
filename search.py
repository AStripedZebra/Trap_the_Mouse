import random
from datetime import datetime
import bisect

class Search:

    def __init__(self, maze):
        random.seed(datetime.now())
        self.maze = maze


    def greedy(self, position):
        self.maze.reset_state()

        queue = [self.maze.start]
        visited = []
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node != self.maze.target:
                #if current_node not in visited:
                    visited.append(current_node)
                    neighbours = current_node.get_neighbours()
                    for neighbour in neighbours:
                        if neighbour not in visited:
                            neighbour.set_parent(current_node)
                            neighbour.set_score(neighbour.manhattan_distance(self.maze.target))
                            bisect.insort_left(queue, neighbour)
            else:
                break
        current_node = self.maze.target.parent

        while current_node is not None and current_node != self.maze.start:
            current_node.set_color((255, 200, 30))
            current_node = current_node.parent

        print("The number of visited nodes is: {}".format(len(visited)))

    def a_star(self, position):
        self.maze.reset_state()
        queue = [self.maze.start]
        visited = []
        distance = 0

        while len(queue) > 0:
            current_node = queue.pop(0)
            print(current_node)
            if current_node != self.maze.target:
                if current_node not in visited:
                    visited.append(current_node)
                    neighbours = current_node.get_neighbours()
                    for neighbour in neighbours:
                        print("kaas")
                        if neighbour not in visited:
                            neighbour.set_parent(current_node)
                            score = int(neighbour.get_distance()) + neighbour.manhattan_distance(self.maze.target)
                            if neighbour not in queue:
                                neighbour.set_score(score)
                                distance = neighbour.score
                                bisect.insort_left(queue, neighbour)
                            elif neighbour.score < distance:
                                neighbour.set_score(score)
                                distance = neighbour.score
                                queue.remove(neighbour)
                                bisect.insort_left(queue, neighbour)
            else:
                break

        current_node = self.maze.target.parent

        while current_node is not None and current_node != self.maze.start:
            current_node.set_color((255, 200, 30))
            current_node = current_node.parent

        print("The number of visited nodes is: {}".format(len(visited)))
