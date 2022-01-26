import random
from datetime import datetime
import bisect

class Search:
    #this class controls the search algorythm used by the mouse object to move around.
    def __init__(self, maze):
        random.seed(datetime.now())
        self.maze = maze

    def greedy(self):
        #this method calculates a path accoring the the greedy search algorithm
        self.maze.reset_state() #remove all data from previous search form the maze
        queue = [self.maze.start]   # create a priority queue and add the starting node
        visited = []    #make a list to store visited nodes
        while len(queue) > 0:   #while there is somehting in the queue
            current_node = queue.pop(0) #get the first node from the queue
            if current_node != self.maze.target:    #if its not the destination, add it to visited and find its neighbours
                    visited.append(current_node)
                    neighbours = current_node.get_neighbours()
                    for neighbour in neighbours:    #go over all neighbours
                        if neighbour not in visited:    #if not visited before
                            neighbour.set_parent(current_node)  #set the current node as their parent
                            neighbour.set_score(neighbour.manhattan_distance(self.maze.target)) #set its score to the manhattan score
                            bisect.insort_left(queue, neighbour) #sort it into the queue
            else:   #if the destination has been found, break the loop
                break
        self.draw_path(visited) #draw the path to the destination


    def draw_path(self, visited):
        #self.maze.target.set_color((200, 50, 50))
        current_node = self.maze.target.parent

        while current_node is not None and current_node != self.maze.start:
            #current_node.set_color((50, 50, 50))
            current_node = current_node.parent


    def get_path(self):
        #this method computes the path and returns its nodes in a list
        path = []
        current_node = self.maze.target
        #start from the end of the route
        while current_node is not None and current_node != self.maze.start:
            #go through all parents to find the starting node
            path.append(current_node)
            current_node = current_node.parent
        return path