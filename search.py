import random
from datetime import datetime
import bisect


class Search:

    def __init__(self, maze):
        self.maze = maze
        random.seed(datetime.now())

    def a_star_search(self, position):
        self.maze.reset_state()

        queue = [self.maze.grid[position[0], position[1]]]
        visited = []
        distance = 0

        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node != self.maze.target:
                if current_node not in visited:
                    visited.append(current_node)
                    neighbours = current_node.get_neighbours()
                    for neighbour in neighbours:
                        if neighbour not in visited:
                            neighbour.set_parent(current_node)
                            score = int(neighbour.get_distance()) + neighbour.manhattan_distance(self.graph.target)
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

        print("The number of visited nodes is: {}".format(len(visited)))
