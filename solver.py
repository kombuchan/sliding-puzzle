#A* Algorithm
import sys
from tkinter import Event
from puzzle import *
from optparse import OptionParser
from pynput.keyboard import Key, Controller
import time

class Node:
    def __init__(self,G,H,F,values):
        self.H = H
        self.G = G
        self.F = F
        self.values = []
        self.neighbors = []
       

    def __lt__(self,other):
        return self.F < other.F
    
    def find_H (self):
        goal = [123456789]
        count = 0
        for i in range(len(self.values)): 
            if not (self.values[i] == goal[i]): count +=1
        return count

class Solver:
    def __init__(self) :
        self.keyboard = Controller()
        parser = OptionParser(description="Sliding puzzle")
        parser.add_option('-i', '--image', type=str, default='img.png',
                        help="path to image")
        args, _ = parser.parse_args()
        self.puzzle = Puzzle(args.image, 3)
        self.puzzle.master.title('Sliding puzzle')
        self.solve()
        # self.slide_pieces()
        self.puzzle.mainloop()
    
    
    
    def ret_values(self):
        arr = []
        ret = []
        for i in self.puzzle.board: arr.append((i['value'],(i['pos_final'][1],i['pos_final'][0])))
        arr.sort(key = lambda x: x[1])
        for i in arr:ret.append(i[0])
        return(ret) 
       
    def find_neighbors(self):
        keysym = [('Up','Down'),('Down','Up'),('Left','Right'),('Right','Left')]
        neighbors = []
        
        
        for move in keysym:
            if(self.puzzle.slide2(move[0])):
              neighbors.append(self.ret_values())
              self.puzzle.slide2(move[1])
            else : continue
        return neighbors
    
    def solve(self):
            open, close = [] , []
            keysym = [('Up','Down'),('Down','Up'),('Left','Right'),('Right','Left')]
            node_start, node_goal = Node(0,sys.maxsize,sys.maxsize,self.ret_values()), Node(sys.maxsize,0,sys.maxsize,[123456789])
            node_start.G, node_start.H , node_start.F = 0, node_start.find_H() , node_start.find_H()
            open.append(node_start)
            print(f"original : {self.ret_values()} {node_start.H}")
            node_start.neighbors = self.find_neighbors()
            print(node_start.neighbors)
            # while changed to if for debugging
            # while(open):
            #     g = 1
            #     open.sort()
            #     node_curr = Node()
            #     node_curr = open.pop(0)
            #     print(node_curr.values)
            #     if node_curr.values == node_goal.values : 
            #         print("Found")
                    # break
                # for move in keysym:
                #     node_neighbor = Node()
                #     node_neighbor.prev = node_curr
                #     self.puzzle.slide2(move[0])
                #     print(self.puzzle.retValues())
                #     node_neighbor.values = self.puzzle.retValues()
                #     node_neighbor.G = g
                #     node_neighbor.H = self.find_H()
                #     node_neighbor.F = node_neighbor.G + node_neighbor.H
                #     node_curr.neighbors.append(self.puzzle.retValues())
                #     if not (node_neighbor in open): open.append(node_neighbor)
                #     self.puzzle.slide2(move[1])
                # g+=1

                # self.puzzle.slide2(keysym[0][0])
                # self.puzzle.retValues()
            return 0

        
    
class main:
    if __name__ == '__main__':
        Solver()