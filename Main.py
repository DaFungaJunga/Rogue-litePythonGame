
from tkinter import Tk, Canvas, PhotoImage, mainloop, LAST, Button , Text, END
import random

import Functions
from Players import Player

import os
from tkinter import *
from subprocess import Popen, PIPE


class IORedirector(object):
    '''A general class for redirecting I/O to this Text widget.'''

    def __init__(self, text_area):
        self.text_area = text_area


class StdoutRedirector(IORedirector):
    '''A class for redirecting stdout to this Text widget.'''
    def write(self, str):
        self.text_area.insert("end", str)

class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 640, 480
        self.map = 0
        self.window = Tk()
        #self.text = Text(self.window)
        #self.text.pack()
        #self.text.insert(END, output)
        self.canvas = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT, bg="#000000")
        self.img = 0
        self.goal=(None,None)
    def redirector(inputStr=""):
        import sys
        root = Toplevel()
        T = Text(root)
        sys.stdout = StdoutRedirector(T)
        T.pack()
        T.insert(END, inputStr)

    def main(self):

        self.canvas.pack()
        self.img = PhotoImage(width=self.WIDTH, height=self.HEIGHT)
        self.canvas.create_image((self.WIDTH / 2, self.HEIGHT / 2), image=self.img, state="normal")
        one = Functions.numberPicker()
        two = Functions.numberPicker()
        three = Functions.numberPicker()
        four = Functions.numberPicker()
        five = Functions.numberPicker()
        six = Functions.numberPicker()
        x = round(self.WIDTH / 2)
        y = round(self.HEIGHT / 2)

                # button1 = Button(window, text = "Restart", command = os.system('C:\Users\s7840363\PycharmProjects\untitled\venv\Scripts\python.exe C:/Users/s7840363/PycharmProjects/untitled/Players.py'))
        # button1.pack(side='left', padx=10)

        self.map = [['#000000' for i in range(self.HEIGHT)] for j in range(self.WIDTH)]
        for i in range(0, 100000):
            b = random.randint(0, 1)
            c = random.randint(0, 1)
            if b == 0:
                x = x + 1
            else:
                x = x - 1
            if c == 0:
                y = y + 1
            else:
                y = y - 1

            if x > self.WIDTH - 1:
                x = self.WIDTH - 1
            if x < 0:
                x = 1
            if y > self.HEIGHT - 1:
                y = self.HEIGHT - 1
            if y < 0:
                y = 1

            if i == 0:
                playerStart = (x, y)

            a = Functions.sixPick(one, two, three, four, five, six)
            self.img.put(a, (abs(x), abs(y)))
            self.map[x][y] = a

        self.goal = [x, y]
        self.canvas.create_line(self.goal[0] + 15, self.goal[1] + 15, self.goal[0], self.goal[1], fill='white', width=2,
                                arrow=LAST)
        player = Player(playerStart[0], playerStart[1], self)
        #player = Player(x, y, self)
        self.window.bind("<KeyPress>", player.movementCheck)
        self.window.focus_set()
        r = self.redirector()
        self.window.mainloop()


    def drawPlayer(self, x, y):
        #print("in drawPlayer")
        self.img.put('#ffffff', (x, y))
        # line = self.canvas.create_line(x + 15, y + 15, x, y, fill='yellow', width=2,arrow=LAST)
        oval = self.canvas.create_oval(x + 10, y + 10, x - 10, y - 10, outline='yellow')
        self.canvas.after(2000, self.canvas.delete, oval)
        if x == self.goal[0] and y==self.goal[1]:
            print("You have made it across these dangerous lands to reach your destiny...")


game = Game()
game.main()
