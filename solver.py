#A* Algorithm
from tkinter import Event
from puzzle import *
from optparse import OptionParser
from pynput.keyboard import Key, Controller

class Node:
    def __init__(self):
        self.values = []
        self.H = 0
        self.G = 0
        self.F = 0

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
        self.puzzle.mainloop()
        
    def find_G (self):
        return 0
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
        node_start, node_goal = Node(), Node()
        for i in self.puzzle.board: node_start.values.append(i['value'])
        node_goal.values = [123456789]
        

        node_start.H , node_start.F = self.find_H() , self.find_H()
        open.append(node_start)
        print(node_start.values)
        # while changed to if for debugging
        if(open):
            open.sort()
            node_curr = open[0]
            if node_curr.values == node_goal.values : 
                print("Found")
                # break
            self.puzzle.canvas.event_generate('<KeyPress-Up>')
                
        return 0

        

    
class main:
    if __name__ == '__main__':
        Solver()