import random
from datetime import datetime
import bisect

class Search:

    def __init__(self, maze):
        random.seed(datetime.now())
        self.maze = maze


    def bfs(self, position):

        self.maze.reset_state()

        queue = [self.maze.start]
        visited = []

        while len(queue) > 0:
            current_node = queue.pop(0)

            if current_node != self.maze.target:
                if current_node not in visited:
                    visited.append(current_node)
                    for next_node in current_node.get_neighbours():
                        if next_node not in visited:
                            next_node.set_parent(current_node)
                            queue.append(next_node)
            else:
                break
        self.draw_path(visited)

    def greedy(self, position):
        self.maze.reset_state()

        queue = [self.maze.start]
        visited = []
        while len(queue) > 0:
            current_node = queue.pop(0)
            if current_node != self.maze.target:
                    visited.append(current_node)
                    neighbours = current_node.get_neighbours()
                    for neighbour in neighbours:
                        if neighbour not in visited:
                            neighbour.set_parent(current_node)
                            neighbour.set_score(neighbour.manhattan_distance(self.maze.target))
                            bisect.insort_left(queue, neighbour)
            else:
                break
        self.draw_path(visited)

    def a_star(self, position):
        self.maze.reset_state()
        queue = [self.maze.start]
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
        self.draw_path(visited)

    def draw_path(self, visited):
        self.maze.target.set_color((200, 50, 50))
        current_node = self.maze.target.parent

        while current_node is not None and current_node != self.maze.start:
            current_node.set_color((50, 50, 50))
            current_node = current_node.parent

        print("Visited nodes: {}".format(len(visited)))

    def get_path(self):
        path = []
        current_node = self.maze.target

        while current_node is not None and current_node != self.maze.start:
            path.append(current_node)
            current_node = current_node.parent
        return path