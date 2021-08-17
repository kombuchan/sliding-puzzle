import random
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
from collections import deque
import time

MAX_BOARD_SIZE = 500


class Puzzle(tk.Frame):

    def __init__(self, image, board_grid=4):
        tk.Frame.__init__(self)
        self.grid()
        self.board_grid = board_grid if board_grid > 2 else 3
        self.set_image(image)
        self.steps = 0
        self.widgets()
        self.events()
        self.create_board()
        self.shuffle()
        unsolvable = self.check_unsolvable()
        while(unsolvable):
            self.shuffle()
            unsolvable = self.check_unsolvable()
        self.show()
        
        

    def set_image(self, image):
        image = Image.open(image)
        board_size = min(image.size)
        if image.size[0] != image.size[1]:
            image = image.crop((0, 0, board_size, board_size))
        if board_size > MAX_BOARD_SIZE:
            board_size = MAX_BOARD_SIZE
            image = image.resize((board_size, board_size), Image.ANTIALIAS)
        self.image = image
        self.board_size = board_size
        self.piece_size = self.board_size / self.board_grid

    def widgets(self):
        args = dict(width=self.board_size, height=self.board_size)
        self.canvas = tk.Canvas(self, **args)
        self.canvas.grid()

    def events(self):
        self.canvas.bind_all('<KeyPress-Up>', self.slide)
        self.canvas.bind_all('<KeyPress-Down>', self.slide)
        self.canvas.bind_all('<KeyPress-Left>', self.slide)
        self.canvas.bind_all('<KeyPress-Right>', self.slide)

    def slide(self, event):
        pieces = self.move_pieces()
        if event.keysym == ('Up') and pieces['bottom']:
            self._slide(pieces['bottom'], pieces['center'], 
                        (0, -self.piece_size))
            
        if event.keysym == ('Down') and pieces['top']:
            self._slide(pieces['top'], pieces['center'],
                        (0, self.piece_size))
            
        if event.keysym == ('Left') and pieces['right']:
            self._slide(pieces['right'], pieces['center'],
                        (-self.piece_size, 0))
            
        if event.keysym == ('Right') and pieces['left']:
            self._slide(pieces['left'], pieces['center'],
                        (self.piece_size, 0))
            
        self.check_status()
        
        
    def slide2(self,condition):
        self.canvas.update()
        time.sleep(0.5)
        pieces = self.move_pieces()
        if condition == 'Up' and pieces['bottom']:
            self._slide(pieces['bottom'], pieces['center'], 
                        (0, -self.piece_size))
            return 1
        if condition ==('Down') and pieces['top']:
            self._slide(pieces['top'], pieces['center'],
                        (0, self.piece_size))
            return 1
        if condition == ('Left') and pieces['right']:
            self._slide(pieces['right'], pieces['center'],
                        (-self.piece_size, 0))
            return 1
        if condition == ('Right') and pieces['left']:
            self._slide(pieces['left'], pieces['center'],
                        (self.piece_size, 0))
            return 1
        self.check_status()
        return 0  
    
    def takeSecond(self,element):
        return element[1]

    def retValues(self):
        arr = []
        ret = []
        for piece in self.board:
            arr.append((piece['value'],piece['pos_final']))
        arr.sort(key=self.takeSecond)
        for piece in arr:
            ret.append(piece[0])
        print(ret)
        return ret

    def _slide(self, from_, to, coord):
        self.canvas.move(from_['id'], *coord)
        to['pos_final'], from_['pos_final'] = from_['pos_final'], to['pos_final']
        self.steps += 1

    def move_pieces(self):
        curr = {'center': None,
                  'right' : None,
                  'left'  : None,
                  'top'   : None,
                  'bottom': None}
        for piece in self.board:
            if  piece['value'] == 9:
                curr['center'] = piece
                break
        x0, y0 = curr['center']['pos_final']
        for piece in self.board:
            x1, y1 = piece['pos_final']
            if y0 == y1 and x1 == x0 + 1:
                curr['right'] = piece
            if y0 == y1 and x1 == x0 - 1:
                curr['left'] = piece
            if x0 == x1 and y1 == y0 - 1:
                curr['top'] = piece
            if x0 == x1 and y1 == y0 + 1:
                curr['bottom'] = piece
        return curr

    def create_board(self):
        self.board = []
        val = 1
        for y in range(self.board_grid):
            for x in range(self.board_grid):
                x0 = x * self.piece_size
                y0 = y * self.piece_size
                x1 = x0 + self.piece_size
                y1 = y0 + self.piece_size
                image = ImageTk.PhotoImage(
                        self.image.crop((x0, y0, x1, y1)))
                piece = {'id'     : None,
                         'image'  : image,
                         'pos_initial'  : (x, y),
                         'pos_final'  : None,
                         'visible': True,
                         'value' : val,
                         'visited' : False}
                self.board.append(piece)
                val+=1
        self.board[-1]['visible'] = False

    def check_status(self):
        for piece in self.board:
            if piece['pos_final'] != piece['pos_initial']:
                return
        title = 'You won!'
        message = 'You solved the puzzle in %d moves!' % self.steps
        messagebox.showinfo(title, message)

    def shuffle(self):
        index = 0
        random.shuffle(self.board)
        self.shuffled_board = []
        for y in range(self.board_grid):
            for x in range(self.board_grid):
                self.shuffled_board.append(self.board[index]['value'])
                index+=1

    def check_unsolvable(self):
        inv_count = 0
        index = 0
        arr = self.shuffled_board
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if (arr[i] < 9 and arr[j] < 9) and (arr[i] > arr[j]): inv_count += 1
        if inv_count % 2 == 1: return True
        else: return False

    def show(self):
        index = 0
        for y in range(self.board_grid):
            for x in range(self.board_grid):
                self.board[index]['pos_final'] = (x, y)
                if self.board[index]['visible']:
                    x1 = x * self.piece_size
                    y1 = y * self.piece_size
                    image = self.board[index]['image']
                    id = self.canvas.create_image(
                            x1, y1, image=image, anchor=tk.NW)
                    self.board[index]['id'] = id
                index += 1