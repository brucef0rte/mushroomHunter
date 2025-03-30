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

    def searchForMushroom(self):
        self.mushrooms = [Mushroom() for _ in range(3)]
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
    def __repr__(self):
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

    def isHealthy(self):
        if self.isHealthy == True:
            player.hp += 1

    def isPsychedelic(self):
        if self.isPsychedelic == True:
            player.hp += 1
            player.hadVision = True
player = Player()
player.searchForMushroom()
print(player.mushrooms[0])