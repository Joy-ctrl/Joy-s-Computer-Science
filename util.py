# Module to create a pokemon class
# plus other utility methods

import random

# Create the pokemon, randomly
# generate a value for each attribute
class pokemon:
    def __init__(self, name):
        self.name=name
        self.health=genrandom(50,100)
        self.attack=genrandom(11,20)
        self.defence=genrandom(5,10)
    
    def change_health(self, num):
        self.health = self.heatlh + int(num)

    def change_attack(self, num):
        self.attack = self.attack + int(num)

    def change_defence(self, num):
        self.defence = self.defence + int(num)

# Takes number min, max and generates a random
# number in that range
def genrandom(min, max):   
   rndint = random.randint(min,max)
   return rndint

# Ensures opposing pokemon
# are different
def choose_opp(name):
   if name == "Charmander":
       opp_name = "Squirtle"
   elif name == "Squirtle":
       opp_name = "Bulbasaur"
   elif name == "Bulbasaur":
       opp_name = "Charmander"
   else:
       opp_name = "Unknown"
   return opp_name

