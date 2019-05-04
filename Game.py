import sys
from tkinter import Tk, Canvas, PhotoImage, mainloop, LAST, Button, Text, END, Toplevel, Menu, Scrollbar, BOTH, BOTTOM, \
    Message
import random

import Functions
from Players import Player
import os
#from tkinter import *
import time


class TextOut(Text):

    def write(self, s):
        self.insert(END, s)
        self.see(END)

    def flush(self):
        pass


class Game:
    def __init__(self):
        self.WIDTH, self.HEIGHT = 640, 480
        self.map = 0
        self.window = Tk()

        menubar = Menu(self.window)
        menubar.add_command(label="New Game", command=self.main)
        menubar.add_command(label="Help", command=self.help)
        menubar.add_command(label="Exit", command=self.window.quit)

        self.window.config(menu=menubar)

        self.text = TextOut(self.window, height = 10)
        sys.stdout = self.text
        self.vsb = Scrollbar(self.text, orient="vertical", command=self.text.yview)
        self.text.config(yscrollcommand=self.vsb.set, height=50)
        self.text.bind("<Key>", lambda e: "break")
        self.text.pack(expand=True, fill=BOTH, side=BOTTOM)
        self.vsb.pack(side="right", fill="y")

        self.text.see('end')
        self.canvas = Canvas(self.window, width=self.WIDTH, height=self.HEIGHT, bg="#000000")
        self.img = 0
        self.goal = (None, None)

    def main(self):
        self.canvas.delete("all")
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
        # player = Player(x, y, self)
        self.window.bind("<KeyPress>", player.movementCheck)
        self.window.focus_set()
        self.window.wm_attributes("-topmost", 1)
        self.window.focus_force()
        self.window.mainloop()

    def drawPlayer(self, x, y,player):
        # print("in drawPlayer")
        self.img.put('#ffffff', (x, y))
        # line = self.canvas.create_line(x + 15, y + 15, x, y, fill='yellow', width=2,arrow=LAST)
        oval = self.canvas.create_oval(x + 30, y + 30, x - 30, y - 30, outline='yellow')
        self.canvas.after(2000, self.canvas.delete, oval)
        if x == self.goal[0] and y == self.goal[1]:
            print("You have made it across these dangerous lands to reach your destiny...")
            player.gameOver()

    def help(self):
        hText = "Using WASD or the arrow keys, you must navigate your character across the randomly generated " \
                "map to the arrow randomly placed on the map. If you emerge victorious in your battles " \
                "across the land, you will receive a small stat boost and some loot that will degrade " \
                "after each turn. Apart from items that increase difficulty, your movement will determine the " \
                "increase as well based on the color of the pixel you have moved to. During your journey," \
                " you will also encounter merchants that sell items that can be purchased multiple times " \
                "if you have the gold. NOTE: Restarting makes the windows unresponsive until it has fully loaded."
        h = Toplevel(self.window)
        h.wm_title("Help")
        msg = Message(h, text=hText)
        msg.pack()
        #l = Label(h, text=hText)
        #l.pack(side='top', fill="both", expand=True, padx=100, pady=100)


game = Game()
game.main()
