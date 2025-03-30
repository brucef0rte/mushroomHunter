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
    def __init__(self, hp, isPoisoned = False, hadVision = False):
        self.hp = hp
        self.isPoisoned = isPoisoned
        self.hadVision = hadVision

    def searchForMushroom():
        pass

# Create Mushroom class
class Mushroom:
    color_options = ["blue", "green", "cyan", "spotted grey"]
    appearance_options = ["bell shaped", "hexagonal", "translucent"]
    def __init__(self, name, appearance, isHealthy = False, isPoison = False, isPsychedelic = False):
        self.name = name
        self.appearance = appearance
        self.isHealthy = isHealthy
        self.isPoisoin = isPoison
        self.isPsychedelic = isPsychedelic