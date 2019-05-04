import Battles
import Inventory
import time
import Shops
import random


class Player:
    def __init__(self, x, y, game):
        self.bodyX = x
        self.bodyY = y
        self.health = 100
        self.attack = 3
        self.attackBonus = 0
        self.defense = 3
        self.defenseBonus = 0
        self.difficultyScale = 1
        self.game = game
        self.inventory = Inventory.Items(self)

        self.intimidation = 0
        self.gold = 0

    def eventt(self):
        num = random.randint(0, 100) + self.intimidation
        if num <= 75:
            battle = Battles.Battle(self)
            battle.start()
        else:
            shop = Shops.Shop(self)
            shop.displayItems()

    def wallCheck(self, x, y):
        if str(self.game.map[x][y]) == '#000000' and str(self.game.map[x][y + 1]) == '#000000' and str(
                self.game.map[x][y - 1]) == '#000000':
            return False
        return True

    def movementCheck(self, direction):
        if direction.char == "a" or direction.char == 'A' or direction.keycode == 37:  # left
            if self.wallCheck(self.bodyX - 1, self.bodyY):
                self.bodyX -= 1
                self.eventt()
                self.game.drawPlayer(self.bodyX, self.bodyY, self)
            return
        if direction.char == 'd' or direction.char == 'D' or direction.keycode == 39:  # right
            if self.wallCheck(self.bodyX + 1, self.bodyY):
                self.bodyX += 1
                self.eventt()
                self.game.drawPlayer(self.bodyX, self.bodyY, self)
            return
        if direction.char == 'w' or direction.char == 'W' or direction.keycode == 38:  # up
            if self.wallCheck(self.bodyX, self.bodyY - 1):
                self.bodyY -= 1
                self.eventt()
                self.game.drawPlayer(self.bodyX, self.bodyY, self)
            return
        if direction.char == 's' or direction.char == 'S' or direction.keycode == 40:  # down
            if self.wallCheck(self.bodyX, self.bodyY + 1):
                self.bodyY += 1
                self.eventt()
                self.game.drawPlayer(self.bodyX, self.bodyY, self)
            return
        if direction.char == 'r' or direction.char == 'R':  # down
            print("restarting...")
            self.game.main()
        if direction.char == 'p' or direction.char == 'P':  # down
            print("exiting...")
            exit()
        print('invalid movement')

    def end(self):
        print("press r to restart or p to exit")
        self.game.window.bind("<KeyPress>", self.endLoop)

    def endLoop(self, direction):
        if direction.char == 'r' or direction.char == 'R':  # down
            print("restarting...")
            self.game.main()
        if direction.char == 'p' or direction.char == 'P':  # down
            print("exiting...")
            exit()
