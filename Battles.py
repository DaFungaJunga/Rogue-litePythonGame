import random
import Enemys
import Functions
import time


class Battle:
    def __init__(self, player):
        self.player = player
        self.enemy = Enemys.Enemy(player.difficultyScale, player.health, player.attack, player.defense)
        self.map = player.game.map

    def start(self):
        print('You encounter ' + self.enemy.name + '\n')
        self.attack()

    def attack(self):
        # playerAttack = self.player.attack * random.randint(1, 4) - self.player.difficultyScale - self.enemy.defense
        playerAttack = (self.player.attackBonus + self.player.attack) * random.uniform(1, 4) - self.enemy.defense
        if playerAttack > 0:
            self.enemy.health -= playerAttack
        print("You attack " + self.enemy.name + " for " + str(round(playerAttack)) + " damage. Enemy Health: " + str(
            round(self.enemy.health)))
        # time.sleep(0.5)
        # self.player.game.text.after(500)

        if self.enemy.health > 0:
            # enemyAttack = self.enemy.attack * random.randint(1, 4) - self.player.difficultyScale - self.player.defense
            enemyAttack = self.enemy.attack * random.uniform(0.5, 4) - (self.player.defenseBonus + self.player.defense)
            if enemyAttack > 0:
                self.player.health -= enemyAttack
            print(self.enemy.name + " attacks you for " + str(round(enemyAttack)) + " damage. Your Health: " + str(
                round(self.player.health)))
            # time.sleep(0.5)
            # self.player.game.text.after(500)
            if self.player.health > 0:
                self.player.inventory.degrade()
                self.attack()
                return
            else:
                self.gameOver()
        else:
            c1 = int(Functions.getV(str(self.map[self.player.bodyX][self.player.bodyY]), 1))
            c2 = int(Functions.getV(str(self.map[self.player.bodyX][self.player.bodyY]), 2))
            c3 = int(Functions.getV(str(self.map[self.player.bodyX][self.player.bodyY]), 3))
            c4 = int(Functions.getV(str(self.map[self.player.bodyX][self.player.bodyY]), 4))
            c5 = int(Functions.getV(str(self.map[self.player.bodyX][self.player.bodyY]), 5))
            c6 = int(Functions.getV(str(self.map[self.player.bodyX][self.player.bodyY]), 6))
            if (c1 + c2 + c3 + c4 + c5 + c6) != 0:
                self.player.difficultyScale += random.uniform(1 / (c1 + c2 + c3 + c4 + c5 + c6), 0.5)
            else:
                self.player.difficultyScale += random.uniform(0, 0.1)
            self.player.health += random.uniform(0, abs((100 - self.player.health))) * self.player.difficultyScale
            self.player.inventory.rollItem(5)
            self.player.gold += round(random.randint(10, 100) + 2 * self.player.difficultyScale)
            if self.player.health <= 0:
                self.gameOver()
            print("Current Difficulty: " + str(round(self.player.difficultyScale)))
            print("Current Attack Power: " + str(round(self.player.attack)))
            print("Current Attack Bonus: " + str(round(self.player.attackBonus)))
            print("Current Defense: " + str(round(self.player.defense)))
            print("Current Defense Bonus: " + str(round(self.player.defenseBonus)))
            print("Current Health: " + str(round(self.player.health)))
            print("Current Gold: " + str(self.player.gold))

    def gameOver(self):
        print('Game Over')
        print("---------------------")
        print("Enemy Health: " + str(round(self.enemy.health)))
        print("Enemy Attack: " + str(round(self.enemy.attack)))
        print("Enemy Defense: " + str(round(self.enemy.defense)))
        print("---------------------")
        print("Current Difficulty: " + str(round(self.player.difficultyScale)))
        print("---------------------")
        print("Current Attack Power: " + str(round(self.player.attack + self.player.attackBonus)))
        print("Current Defense: " + str(round(self.player.defense + self.player.defenseBonus)))
        print("Current Gold: " + str(self.player.gold))
        self.player.end()
