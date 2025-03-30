import random
'''
Mushroom Hunter Game
Practice for Codecademy "Learn Object Oriented Programming with Python" class
Goal: You are on a mission to find new edible mushrooms for your tribe. Find mushrooms,
    test them, try not to die.
-Player starts with 10 HP
-If a player is poisoned they lose 1 HP per round
-When player searches for mushroom:
    Present 3 randomly generated mushrooms
    Player can examine or eat each of three mushrooms

    A mushroom name is made of 2 parts from 2 lists
Classes: Player, Mushroom

Player:
    attributes:
        HP
            if HP == 0: gameOver
        isPoisoned
            if True -1 HP per round
        hadVision
            set True if psychedlic method called
    methods:
        searchForMushroom
            returns 3 mushrooms to pick from, uses 1 round
        examineMushroom
            check for tell-tale signs of a poisonous mushroom, uses 1/2(?) rounds
        chooseMushroom
            pick 1 of the three mushroom to eat, then eat it

Mushroom:
    attributes:
        name: comprised of random selection from 2 dictionaries (key "name": value "description)
        appearance: description of mushroom based on key values for name
        healthEffects:
            healthy - restore 1 health
            poisonous - sets isPoisoned condition
            psychedelic - restore 1 health, cure poison, lose 1 day (cosmetic)
    methods:
        heal
        inflictPoison
        psychedelic

'''
# Create our Player Class
class Player:
    def __init__(self, hp=10, isPoisoned = False, hadVision = False):
        self.hp = hp
        self.isPoisoned = isPoisoned
        self.hadVision = hadVision
        self.mushrooms = []

    def __str__(self):
        object = f"Your HP is {self.hp}.\n"
        if self.isPoisoned == True:
            object += f"You are poisoned.\n"
        if self.hadVision == True:
            object += f"You had a vision.\n"
        if self.hp <= 0:
            object += f"You are dead.\n"
        elif self.hp > 0 and self.hp <= 5:
            object += "You're knocking on death's door.\n"
        elif self.hp > 5 and self.hp <= 8:
            object += "You're in good shape.\n"
        elif self.hp > 8 and self.hp <= 10:
            object += "You're in great shape.\n"
        else:
            object += "You're in perfect shape.\n"
        return object
    # generate 3 mushrooms for our player to pick from
    def searchForMushroom(self):
        self.mushrooms = [Mushroom() for _ in range(3)]
        print("You found 3 mushrooms!")
        for i, mushroom in enumerate(self.mushrooms):
            print(f"Mushroom {i+1}:")
            print(mushroom)
    
    def pickMushroom(self):
        self.choice = input("Which mushroom would you like to try A, B, C? ")
        if self.choice == "A":
            self.eatMushroom(self.mushrooms[0])
        elif self.choice == "B":
            self.eatMushroom(self.mushrooms[1])
        elif self.choice == "C":
            self.eatMushroom(self.mushrooms[2])
        else:
            print("Invalid choice. Please pick A, B, or C.")

    def eatMushroom(self, mushroom):
        if mushroom.isHealthy == True:
            print(f"You ate the {mushroom.name} and it was healthy!")
            self.isHealthy = True
            self.hp += 1
        elif mushroom.isPoisoin == True:
            print(f"You ate the {mushroom.name} and it was poisonous!")
            self.isPoisoned = True
            self.hp -= 1
        elif mushroom.isPsychedelic == True:
            print(f"You ate the {mushroom.name} and it was psychedelic!")
            self.hadVision = True
            self.isPoisoned = False
            self.hp += 1
            print(f"You feel a rush of energy and your poison is cured!")
        else:
            print("You ate a regular mushroom. Nothing happened.")
        print(f"Current HP: {self.hp} / 10")

# Create Mushroom class
class Mushroom:
    colors = ["blue", "green", "cyan", "spotted grey"]
    shapes = ["bell", "hexagonal", "translucent", "bulbous", "square"]
    names1 = ["destroying", "memsmerizing", "sickening", "delectable"]
    names2 = ["angel", "puppy", "catgirl", "oyster", "magic", "shiitake"]
    def __init__(self):
        self.name = random.choice(self.names1) + " " + random.choice(self.names2)
        self.isHealthy = random.choice([True, False])
        self.isPoisoin = random.choice([True, False])
        self.isPsychedelic = random.choice([True, False])
        self.color = random.choice(self.colors)
        self.shape = random.choice(self.shapes)
        self.appearance = f"a {self.color} colored, {self.shape} shaped mushroom"
    def __str__(self):
        object = f"this mushroom is called {self.name}.\n"
        object += f"it looks like a {self.appearance} mushroom.\n"
        if self.isHealthy == True:
            object += f"It is healthy.\n"
        if self.isPoisoin == True:
            object += f"It is poisonous.\n"
        if self.isPsychedelic == True:
            object += f"It is psychedelic :)\n"
        return object
    def isPoisonous(self):
        if self.isPoisoin == True:
            player.isPoisoned = True

player = Player()
while player.hp > 0:
    player.searchForMushroom()
    player.pickMushroom()
    print(player.hp)