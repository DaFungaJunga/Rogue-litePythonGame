import random


class Items:
    # maybe add teleportation and random names for items
    def __init__(self, player):
        self.items = []
        self.player = player

    def createShield(self):
        shield = Shield(self.player)
        self.items.append(shield)
        self.player.defenseBonus += shield.defenseBuff
        print("You found salvaged a " + shield.name + ". +" + str(round(shield.defenseBuff)) + " to defense for " + str(
            shield.durability) + " turns")

    def createSword(self):
        sword = Sword(self.player)
        self.items.append(sword)
        self.player.attackBonus += sword.attackBuff
        print("You found salvaged a " + sword.name + ". + " + str(round(sword.attackBuff)) + " to attack for " + str(
            sword.durability) + " turns")

    def createPotion(self):
        num = random.randint(0, 1)
        if num == 0:
            potion = HealthPotion(self.player)
        else:
            potion = Poison(self.player)
        self.player.health += potion.healthBuff
        print("You found and drank a " + potion.name + ". Health: " + str(round(self.player.health)))

    def createFragment(self):
        gem = CrisisGem()
        self.player.difficultyScale += gem.difficultyBuff
        print("You have absorbed a " + gem.name + ". You sense that your surrounding have become more threatening...")

    def rollItem(self, lastItem):
        num = random.randint(0, 3)
        if num == 0:
            self.createSword()
        if num == 1:
            self.createShield()
        if num == 2:
            self.createPotion()
        if num == 3:
            self.createFragment()

    def shopItem(self):
        num = random.randint(0, 3)
        if num == 0:
            return Sword(self.player)
        if num == 1:
            return Shield(self.player)
        if num == 2:
            return HealthPotion(self.player)
        if num == 3:
            return AmuletA(self.player)
        if num == 4:
            return AmuletI(self.player)

    def degrade(self):
        for i in range(len(self.items)):
            print(self.items[i].name + " durability: " + str(self.items[i].durability))
            self.items[i].durability -= 1
            if self.items[i].durability <= 0:
                if isinstance(self.items[i], Shield):
                    print(self.items[i].name + " has broken---------------------------------")
                    self.player.defenseBonus -= self.items[i].defenseBuff
                if isinstance(self.items[i], Sword):
                    self.player.attackBonus -= self.items[i].attackBuff
                    print(self.items[i].name + " has broken---------------------------------------")
                self.items.remove(self.items[i])
                return


class Shield:
    def __init__(self, player):
        self.name = "Armor Piece"
        self.defenseBuff = random.uniform(0.5, 5) * player.difficultyScale
        self.durability = random.randint(1, 25)
        self.cost = 250 + 5 * player.difficultyScale


class Sword:
    def __init__(self, player):
        self.name = "Whetstone"
        self.attackBuff = random.uniform(0.5, 5) * player.difficultyScale
        self.durability = random.randint(1, 25)
        self.cost = 250 + 5 * player.difficultyScale


class HealthPotion:
    def __init__(self, player):
        self.name = "Health Potion"
        self.healthBuff = random.uniform(0, 50) * player.difficultyScale
        self.cost = 150 + 5 * player.difficultyScale


class Poison:
    def __init__(self, player):
        self.name = "Poisonous Potion"
        self.healthBuff = random.uniform(-25, 0) * player.difficultyScale


class AmuletI:
    def __init__(self, player):
        self.name = "Amulet of Intimidation"
        self.intimidation = random.uniform(0, 20) * player.difficultyScale
        self.cost = 150 + 5 * player.difficultyScale


class AmuletA:
    def __init__(self, player):
        self.name = "Amulet of Attraction"
        self.intimidation = random.uniform(-20, 0) * player.difficultyScale
        self.cost = 150 + 5 * player.difficultyScale


class CrisisGem:
    def __init__(self):
        self.name = "Crisis Gem Fragment"
        self.difficultyBuff = random.uniform(-0.5, 0.5)
        self.durability = random.randint(1, 10)
