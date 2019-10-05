# Module to create a pokemon class
# plus other utility methods

import random

# Create the pokemon, randomly
# generate a value for each attribute
class pokemon:
    def __init__(self, name):
        self.name=name
        self.health=genrandom(1,10)
        self.attack=genrandom(1,10)
        self.defence=genrandom(1,10)

# Takes number min, max and generates a random
# number in that range
def genrandom(min, max):   
   rndint = random.randint(min,max)
   return rndint

# Ensures opposing pokemon
# is different
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


