#A* Algorithm
import sys
from tkinter import Event
from puzzle import *
from optparse import OptionParser
from pynput.keyboard import Key, Controller
import time

class Node:
    def __init__(self):
        self.values = []
        self.H = 0
        self.G = sys.maxsize
        self.F = sys.maxsize
        prev = 0

    def __lt__(self,other):
        return self.F < other.F

class Solver:

    def __init__(self) :
        self.keyboard = Controller()
        parser = OptionParser(description="Sliding puzzle")
        parser.add_option('-i', '--image', type=str, default='img.png',
                        help="path to image")
        args, _ = parser.parse_args()
        self.puzzle = Puzzle(args.image, 3)
        self.puzzle.master.title('Sliding puzzle')
        self.find_H()
        self.solve()
        # self.slide_pieces()
        self.puzzle.mainloop()
    
    def find_H (self):
        # Hamming distance
        count = 0
        for piece in self.puzzle.board:
            if piece['value'] != 9 and (piece['pos_final'] != piece['pos_initial']): count+=1
        return count
    

    def solve(self):
        open = []
        close = []
        neighbors = []
        keysym = [('Up','Down'),('Down','Up'),('Left','Right'),('Right','Left')]
        node_start, node_goal = Node(), Node()
        for i in self.puzzle.board: node_start.values.append(i['value'])
        node_goal.values = [123456789]
        

        node_start.G, node_start.H , node_start.F = 0, self.find_H() , self.find_H()
        open.append(node_start)
        print(f"original : {self.puzzle.retValues()}")
        # while changed to if for debugging
        while(open):
            g = 1
            open.sort()
            node_curr = open.pop(0)
            if node_curr.values == node_goal.values : 
                print("Found")
                # break
            for move in keysym:
                node_neighbor = Node()
                node_neighbor.prev = node_curr
                self.puzzle.slide2(move[0])
                print(self.puzzle.retValues())
                node_neighbor.values = self.puzzle.retValues()
                node_neighbor.G = g
                node_neighbor.H = self.find_H()
                node_neighbor.F = node_neighbor.G + node_neighbor.H
                neighbors.append(self.puzzle.retValues())
                if not (node_neighbor in open): open.append(node_neighbor)
                self.puzzle.slide2(move[1])
            g+=1

            # self.puzzle.slide2(keysym[0][0])
            # self.puzzle.retValues()
        return 0

        
    
class main:
    if __name__ == '__main__':
        Solver()