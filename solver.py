#A* Algorithm
import sys
from tkinter import Event
from puzzle import *
from optparse import OptionParser
from pynput.keyboard import Key, Controller
import time
from queue import PriorityQueue

class Node:
    def __init__(self,values,parent,g,h,f,move):
        self.g = g
        self.h = h
        self.f = f
        self.values = values
        self.parent = parent
        self.move = move
       

    def __lt__(self,other):
        return self.f < other.f
    
    def __eq__(self,other):
        return self.values == other.values

class Solver:
    def __init__(self) :
        self.keyboard = Controller()
        parser = OptionParser(description="Sliding puzzle")
        parser.add_option('-i', '--image', type=str, default='img.png',
                        help="path to image")
        args, _ = parser.parse_args()
        self.puzzle = Puzzle(args.image, 3)
        self.puzzle.master.title('Sliding puzzle')
        self.move = ""
        

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
        h=100
        for move in keysym:
            if(self.puzzle.possible_moves(move[0])):
              neighbors.append((self.ret_values(),move[0]))
              self.puzzle.possible_moves(move[1])
            else : continue
        return neighbors
    
    def find_H(self,arr):
        initial = arr
        goal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        return sum(abs(b%3 - g%3) + abs(b//3 - g//3)
            for b, g in ((initial.index(i), goal.index(i)) for i in range(1, 9)))
    

    def solve(self):
            g = 0
            h = self.find_H(self.ret_values())
            f = g + h

            start = Node(self.ret_values(),None,g,h,f,'')
            goal = Node([1,2,3,4,5,6,7,8,9],None,0,0,0,'')
            
            open = []
            closed = []
            neighbors = []
            open.append(start)

            while open:
                current = open[0]
                # print(f"current: {current.values} {current.move} ")
                # print(current.move)
                self.puzzle.slide2(current.move)
                if current.values == goal.values : 
                    print("Found")
                    break
                
                neighbors = self.find_neighbors()
                
        
                for n in neighbors:
                    node = Node(n[0],None,current.g+1,self.find_H(n[0]),g+1+self.find_H(n[0]),n[1])
                    # print(f" neighbor {self.find_H(n[0])} {n[1] } ")
                    
                    if node in closed : continue
                    if node in open and current.g < node.g : continue
                    open.append(node)
                closed.append(current)
                del open[0]
                open.sort()
        

        
    
class main:
    if __name__ == '__main__':
        Solver()