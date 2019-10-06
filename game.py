# Main game

from util import pokemon
import util

# Choose the pokemon. This is where
# we create the player and cpu pokemon
# making sure we dont choose the same types
def choose_pokemon(name):
     global user_pokemon
     global cpu_pokemon 
     user_pokemon = pokemon(name)
     cpu_name = util.choose_opp(name)
     cpu_pokemon = pokemon(cpu_name)

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
    
    # Create the user and cpuosing pokemon
    choose_pokemon(chosen)
    
    # Just for debugging
    debug()

    # Start the battle
    battle()

# This is where the battle happens    
def battle():
    # Start the battle
    print(user_pokemon.name + " will battle " + cpu_pokemon.name + "!")
    # Prints the battle status
    status()

    battle_turn = 1
    while user_pokemon.health > 0 and cpu_pokemon.health > 0:
        if battle_turn == 1:
            prompt("Your turn to attack, hit enter...")
            cpu_pokemon.health = cpu_pokemon.health - user_pokemon.attack + cpu_pokemon.defence
            battle_turn = 2
        else:
            prompt("CPUs turn to attach, hit enter...")
            user_pokemon.health = user_pokemon.health - cpu_pokemon.attack + user_pokemon.defence
            battle_turn = 1
        status()
    
    # Declare winner
    if user_pokemon.health > 0 and cpu_pokemon.health <= 0:
        print ">>> The winner is: " + user_pokemon.name + "!!! <<<"
    elif cpu_pokemon.health > 0 and user_pokemon.health <= 0:
        print ">>> The winner is: " + cpu_pokemon.name + "!!! <<<"
    else:
        print ">>> Its a draw!!! <<<"

# Prints game status
def status():
    print "*** " + user_pokemon.name + " health: " + str(user_pokemon.health)
    print "*** " + cpu_pokemon.name + " health: " + str(cpu_pokemon.health)




# fucntion to just print out pokemon attributes
def debug():
    print "Your pokemon: " + str(user_pokemon.name)
    attrs = vars(user_pokemon)
    for att in  attrs.items():
        print att

    print "CPU pokemon: " + str(cpu_pokemon.name)
    attrs = vars(cpu_pokemon)
    for att in  attrs.items():
        print att

if __name__ == "__main__":
    main()
