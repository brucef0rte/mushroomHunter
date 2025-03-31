import random
import os

# Create our Player Class
class Player:
    def __init__(self, hp=10, isPoisoned = False, hadVision = False):
        self.hp = hp
        self.isPoisoned = isPoisoned
        self.hadVision = hadVision
        self.mushrooms = []
        self.satchel = []
    # this will be returned when we print our player
    def __str__(self):
        object = f"Your HP is {self.hp}. "
        if self.isPoisoned == True:
            object += f"You are poisoned.\n"
        if self.hadVision == True:
            object += f"You had a vision.\n"
        elif self.hp > 0 and self.hp <= 5:
            object += "You're knocking on death's door.\n"
        elif self.hp > 5 and self.hp <= 8:
            object += "You're in good shape.\n"
        elif self.hp > 8 and self.hp <= 10:
            object += "You're in great shape.\n"
        else:
            object += "You're in perfect shape.\n"
        object += f"Your satchel has {len(self.satchel)} mushrooms in it. Just {5 - len(self.satchel)} to go."
        return object
    # check if we're dead or not
    def checkDead(self):
        if self.hp <= 1:
            print('you ded')
            exit
    # generate 3 mushrooms for our player to pick from
    def searchForMushroom(self):
        if self.hp > 10:
            self.hp = 10
        print(self)
        if self.isPoisoned:
            self.hp -= 1
            print(f"Oof. The poison rends your tummy for -1 hp.\n Current HP: {self.hp} / 10")
        self.checkDead()
        self.mushrooms = [Mushroom() for _ in range(3)]
        print("You found 3 mushrooms!")
        print(f"Mushroom A: {self.mushrooms[0]}")
        print(f"Mushroom B: {self.mushrooms[1]}")
        print(f"Mushroom C: {self.mushrooms[2]}")
    
    # use a,b,c or A,B,C to pick a mushroom
    def pickMushroom(self):
        self.choice = input("Which mushroom would you like to try A, B, C? ").upper()
        if self.choice == "A":
            self.eatMushroom(self.mushrooms[0])
        elif self.choice == "B":
            self.eatMushroom(self.mushrooms[1])
        elif self.choice == "C":
            self.eatMushroom(self.mushrooms[2])
        else:
            print("Invalid choice. Please pick A, B, or C.")
    # eat the mushroom and see what happens. Healthy mushrooms can be taken home, and restore 1 health. Poison mushrooms take 1 hp at the beigning of each round.
    # psychedlic mushrooms remove poison, and set a hadVision flag to true
    def eatMushroom(self, mushroom):
        if mushroom.isNeutral == True:
            print(f"You ate the {mushroom.name}. It's delicious and nutritious. You add it to your satchel.\n\n")
            self.satchel.append(mushroom)
            self.hp = self.hp + 1
        elif mushroom.isPoisoin == True:
            print(f"You ate the {mushroom.name} and it was poisonous!\n\n")
            self.isPoisoned = True
        elif mushroom.isPsychedelic == True:
            print(f"You ate the {mushroom.name} and it was psychedelic!\n\n")
            self.hadVision = True
            if self.isPoisoned == True:
                print("You feel the poison leaving your body.\n")
            self.isPoisoned = False
        else:
            print("This mushroom only hurt your tastebuds. Yuck!\n\n")
        self.checkDead()

# Create Mushroom class
class Mushroom:
    # lists of properties for random generation. Need to greatly expanded.
    colors = ["blue", "green", "cyan", "spotted grey"]
    shapes = ["bell", "hexagonal", "translucent", "bulbous", "square"]
    names1 = ["destroying", "memsmerizing", "sickening", "delectable"]
    names2 = ["angel", "puppy", "catgirl", "oyster", "magic", "shiitake"]

    # constructor to randomly set variables for mushroom type. Need to fix all the Poisoin typos, and make sure only 1 of the variables is set per mushroom.
    def __init__(self):
        self.name = random.choice(self.names1) + " " + random.choice(self.names2)
        self.isNeutral = random.choice([True, False])
        if self.isNeutral == False:
            self.isPoisoin = random.choice([True, False])
            if self.isPoisoin == False:
                self.isPsychedelic = random.choice([True, False])
        self.color = random.choice(self.colors)
        self.shape = random.choice(self.shapes)
        self.appearance = f"a {self.color} colored, {self.shape} shaped mushroom"
    def __str__(self):
        object = f"this mushroom is called {self.name}.\n"
        object += f"it looks like a {self.appearance} mushroom.\n"
        # if self.isHealthy == True:
        #     object += f"It is healthy.\n"
        # if self.isPoisoin == True:
        #     object += f"It is poisonous.\n"
        # if self.isPsychedelic == True:
        #     object += f"It is psychedelic :)\n"
        return object

player = Player()
while True:
    player.checkDead()
    if len(player.satchel) >= 5:
        print("You've gathered enough supplies from the tribe. Return home. You've earned your rest.")
        if player.hadVision == True:
            print("You bring back with you an apocalyptic vision of a world sized mushroom hurtling through space.")
        break
    player.searchForMushroom()
    player.pickMushroom()