#A* Algorithm
from puzzle import *
from optparse import OptionParser


class Node:
    def __init__(self,values,path,parent,g,h,f,move):
        self.g = g
        self.h = h
        self.f = f
        self.values = values
        self.path = path
        self.parent = parent
        self.move = move
       

    def __lt__(self,other):
        return self.f < other.f
    
    def __eq__(self,other):
        return self.values == other.values

class Solver:
    def __init__(self) :
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
        keysym = {('Up','Down'),('Down','Up'),('Left','Right'),('Right','Left')}
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
            keysym = {'Up':'Down','Down':'Up','Left':'Right','Right':'Left','':''}
            
            g = 0
            h = self.find_H(self.ret_values())
            f = g + h

            start = Node(self.ret_values(),None,None,g,h,f,'')
            goal = Node([1,2,3,4,5,6,7,8,9],None,None,0,0,0,'')
            
            open = []
            closed = []
            neighbors = []
            open.append(start)
            path = []
            prev = start
            while open:
                current = open[0]
                print(f"current: {current.f} {current.move} ")
                # print(current.move)
                # if current != start and current.parent != prev:
                #     while(prev != current) : self.puzzle.slide2(keysym[path.pop()])
                self.puzzle.slide2(current.move)
                path.append(current.move)
                if current.values == goal.values : 
                    print("Found")
                    break
                closed.append(current)
                neighbors = self.find_neighbors()
                n_fval = []
        
                for n in neighbors:
                    node = Node(n[0],path,current,current.g+1,self.find_H(n[0]),g+1+self.find_H(n[0]),n[1])
                    print(f" neighbor: {node.f} {node.move}")
                    n_fval.append(node)
                    if node in closed : continue
                    if node not in open: open.append(node)
                    for n in open:
                        # open_node = open[open.index(node)]
                        # if node.g < open_node.g:
                        #     open_node.g = node.g
                        #     open_node.f = node.f
                        #     open_node.path = node.path
                        #     open_node.move = node.move
                        if node.f == n.f:
                             if n.g > node.g:
                                n.g = node.g
                                n.f = node.f
                                n.path = node.path
                                n.move = node.move
                                n.parent = node.parent

                # if current != start : 
                #     greater = 0
                #     for n in n_fval: 
                #         if len(open) >= 2 and n.f <= open[1].f: greater = 1
                #     if greater == 0 : self.puzzle.slide2(keysym[current.move])
                
                # if len(open) == 1 and current.values != goal.values:
                #     for n in current.path:
                #         self.puzzle.slide2(keysym[n])
                #     open.append(current)

                if current != start : prev = current
                del open[0]
                open.sort()
        

        
    
class main:
    if __name__ == '__main__':
        Solver()