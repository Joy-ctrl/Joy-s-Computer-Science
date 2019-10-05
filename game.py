# Main game

from util import pokemon
import util

# Choose the pokemon. This is where
# we create the player and cpu pokemon
# making sure we dont choose the same types
def choose_pokemon(name):
     global user_pokemon
     global opp_pokemon 
     user_pokemon = pokemon(name)
     opp_name = util.choose_opp(name)
     opp_pokemon = pokemon(opp_name)

# function to print out message and return input
def prompt(message):
    reply = raw_input(message + ": ")
    return reply

# Main function, calls all the user input and
# other game logic
def main():
    print("Hi there, welcome to Pokemon!")
    name = prompt("What is your name? ")
    print("Hi Master " + str(name))
    choice  = prompt("Pick a starter Pokemon:\n1 - Bulbasaur\n2 - Squirtle\n3 - Charmander\n")
    if int(choice) == 1:
        print("You chose Bulbasaur!\n")
        chosen = "Bulbasaur"
    elif int(choice) == 2:
        print("You chose Squirtle!\n")
        chosen = "Squirtle"
    elif int(choice) == 3:
        print("You chose Charmander!\n")
        chosen = "Charmander"
    else:
        print("No valid choice made, please try again.")
        exit()
    
    # Create the user and opposing pokemon
    choose_pokemon(chosen)
    
    # Just for debugging
    debug()
    
# fucntion to just print out pokemon attributes
def debug():
    print "Your pokemon: " + str(user_pokemon.name)
    attrs = vars(user_pokemon)
    for att in  attrs.items():
        print att

    print "CPU pokemon: " + str(opp_pokemon.name)
    attrs = vars(opp_pokemon)
    for att in  attrs.items():
        print att

if __name__ == "__main__":
    main()
