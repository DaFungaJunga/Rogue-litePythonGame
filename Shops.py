import Inventory


class Shop:
    def __init__(self, player):
        self.player = player
        self.optionOne = player.inventory.shopItem()
        self.optionTwo = player.inventory.shopItem()
        self.optionThree = player.inventory.shopItem()
        self.optionFour = player.inventory.shopItem()

    def displayInfo(self, option):
        if isinstance(option, Inventory.Shield):
            print("+" + str(round(option.defenseBuff)) + " to defense for " + str(option.durability) + " turns. " + str(
                option.cost) + " Gold")
        if isinstance(option, Inventory.Sword):
            print("+" + str(round(option.attackBuff)) + " to attack for " + str(option.durability) + " turns. " + str(
                option.cost) + " Gold")
        if isinstance(option, Inventory.HealthPotion):
            print("+" + str(round(option.healthBuff)) + " Health. " + str(option.cost) + " Gold")
        if isinstance(option, Inventory.AmuletA):
            print(str(round(option.intimidation)) + " Intimidation. " + str(option.cost) + " Gold")
        if isinstance(option, Inventory.AmuletI):
            print("+" + str(round(option.intimidation)) + " Intimidation. " + str(option.cost) + " Gold")

    def addItem(self, option):
        if self.player.gold >= option.cost:
            if isinstance(option, Inventory.Shield):
                self.player.inventory.items.append(option)
                self.player.defenseBonus += option.defenseBuff
                self.player.gold -= option.cost
            if isinstance(option, Inventory.Sword):
                self.player.inventory.items.append(option)
                self.player.attackBonus += option.attackBuff
                self.player.gold -= option.cost
            if isinstance(option, Inventory.HealthPotion):
                if self.player.health >= 200:
                    print("You seem healthy enough, and do not have the carry capacity for additional potions")
                    return
                else:
                    self.player.health += option.healthBuff
                    self.player.gold -= option.cost
            if isinstance(option, Inventory.AmuletA):
                self.player.intimidation += option.intimidation
                self.player.gold -= option.cost
            if isinstance(option, Inventory.AmuletI):
                self.player.intimidation += option.intimidation
                self.player.gold -= option.cost
        print("Insufficient Funds")

    def displayItems(self):
        print("You have met a Merchant")
        print("Press W or Up for " + self.optionOne.name)
        self.displayInfo(self.optionOne)

        print("Press A or Left for " + self.optionTwo.name)
        self.displayInfo(self.optionTwo)

        print("Press S or Down for " + self.optionThree.name)
        self.displayInfo(self.optionThree)

        print("Press D or Right for " + self.optionFour.name)
        self.displayInfo(self.optionFour)

        print("To exit the shop, press G")
        self.player.game.window.bind("<KeyPress>", self.buyItem)

    def buyItem(self, direction):
        if direction.char == "a" or direction.char == 'A' or direction.keycode == 37:  # left
            self.addItem(self.optionTwo)
            return
        if direction.char == 'd' or direction.char == 'D' or direction.keycode == 39:  # right
            self.addItem(self.optionFour)
            return
        if direction.char == 'w' or direction.char == 'W' or direction.keycode == 38:  # up
            self.addItem(self.optionOne)
            return
        if direction.char == 's' or direction.char == 'S' or direction.keycode == 40:  # down
            self.addItem(self.optionThree)
            return
        if direction.char == 'r' or direction.char == 'R':  # down
            print("restarting...")
            self.player.game.main()
        if direction.char == 'p' or direction.char == 'P':  # down
            print("exiting...")
            exit()
        if direction.char == 'g' or direction.char == "G":
            print("Leaving Merchant")
            self.player.game.window.bind("<KeyPress>", self.player.movementCheck)
        print('invalid choice')
