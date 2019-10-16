import time
import random


def Squirtle():
    print("You chose Squirtle\nGreat ok!")
    time.sleep(1)
    print("Now let's have a look at your attributes")
    time.sleep(1)
    Shealth = random.randint(49,58)
    print("The health of your pokemon is " + str(Shealth))
    time.sleep(1)
    Sdefence = random.randint(47,59)
    print("The defence of your pokemon is " + str(Sdefence))
    time.sleep(1)
    Sattack = random.randint(54,62)
    print("The attack of your pokemon is " +str(Sattack))
    time.sleep(1)
    Sspeed = random.randint(31,52)
    print("The speed of your pokemon is " + str(Sspeed))
    
    time.sleep(4)
    print("Now you know your attributes, let's look at your opponent")
    time.sleep(1)
    print("You are fighting Bulbasaur")
    time.sleep(1)
    print("Let's look at the Bulbasaur's attributes")
    time.sleep(1)
    Bhealth = random.randint(51,60)
    print("The health of your pokemon is " + str(Bhealth))
    time.sleep(1)
    Bdefence = random.randint(46,58)
    print("The defence of your pokemon is " + str(Bdefence))
    time.sleep(1)
    Battack = random.randint(57,61)
    print("The attack of your pokemon is " +str(Battack))
    time.sleep(1)
    Bspeed = random.randint(34,56)
    print("The speed of your pokemon is " + str(Bspeed))
    time.sleep(1)
    print("You're walking through a forest... when a wild Bulbasaur appears!")
    time.sleep(1)
    battle_turn = 1
    if battle_turn == 1:
        print("You have a higher speed, so you attack first!")
    attack1 = input("Pick an attack:\n1 - Tackle\n2 - Water Gun\n3 - Bubble Beam\n ")
    if int(attack1) == 1: 
        print("You tackled the wild Bulbasaur")
        time.sleep(1)
    elif int(attack1) == 2:
        print("You performed Water Gun on the wild Bulbasaur")
        time.sleep(1)
    elif int(attack1) == 3:
        print("You blinded the wild Bulbasaur with Bubble Beam")
        Bhealth = Bhealth - Sattack + Bdefence
        time.sleep(1)
    else:
        print("Sorry that didn't work please try again")
    exit()
    if Bspeed > Sspeed:
        print("Bulbasaur has a higher speed, so they attack first!")
        print("Bulbasaur uses Vine Whip")
    Shealth = Shealth - Battack + Sdefence
    if Shealth > 0 and Bhealth <= 0:
        print("The winner is Squirtle!")
    if Bhealth > 0 and Shealth <= 0:
        print("The winner is Bulbasaur")




def Charmander():
    print("You chose Charmander\nGreat ok!")
    time.sleep(1)
    print("Now let's have a look at your attributes")
    Chealth = random.randint(54,61)
    print("The health of your pokemon is " + str(Chealth))
    time.sleep(1)
    Cdefence = random.randint(49,57)
    print("The defence of your pokemon is " + str(Cdefence))
    time.sleep(1)
    Cattack = random.randint(55,61)
    print("The attack of your pokemon is " +str(Cattack))
    time.sleep(1)
    Cspeed = random.randint(32,51)
    print("The speed of your pokemon is " + str(Cspeed))
    time.sleep(4)
    print("Now you know your attributes, let's look at your opponent")
    time.sleep(1)
    print("You are fighting Squirtle")
    time.sleep(1)
    print("Let's have a look at Squirtle's attributes")
    time.sleep(1)
    Shealth = random.randint(49,60)
    print("The health of Squirtle is " + str(Shealth))
    time.sleep(1)
    Sdefence =random.randint(51,57)
    print("The defence of Squirtle is " + str(Sdefence))
    time.sleep(1)
    Sattack = random.randint(55,60)
    print("The attack of Squirtle is " +str(Sattack))
    time.sleep(1)
    Sspeed = random.randint(33,52)
    print("The speed of Squirtle is " + str(Sspeed))
    time.sleep(1)
    print("You're on a boat at sea... when a wild Squirtle appears!")
    if Cspeed > Sspeed:
        print("You have a higher speed, so you attack first!")
        attack = input("Pick an attack:\n1 -Scratch\n2 -Fire Spin\n3 - Smokescreen\n")
        if int(attack) == 1:
            print("You whipped the wild Squirtle")
        elif int(attack) == 2:
            print("You performed Fire Spin on the wild Squirtle")
        elif int(attack) == 3:
            print("You blinded the wild Squirtle with Smokescreen")
        else:
            print("Sorry that didn't work please try again")
            exit()
    else:
        print("Sorry that didn't work, please try again")
        exit()
    if Sspeed > Cspeed:
        print("Charmander has a higher speed, so they attack first!")
        print("Charmander uses Fire Spin")
    else:
        print("Sorry that didn't work, please try again")
        exit()




def Bulbasaur():
    print("You chose Bulbasaur\nGreat ok!")
    time.sleep(1)
    print("Now let's have a look at your attributes")
    time.sleep(1)
    Bhealth = random.randint(57,59)
    print("The health of your pokemon is " + str(Bhealth))
    time.sleep(1)
    Bdefence = random.randint(52,53)
    print("The defence of your pokemon is " + str(Bdefence))
    time.sleep(1)
    Battack = random.randint(57,59)
    print("The attack of your pokemon is " +str(Battack))
    time.sleep(1)
    Bspeed = random.randint(56,62)
    print("The speed of your pokemon is " + str(Bspeed))
    time.sleep(4)
    print("Now you know your attributes, let's look at your opponent")
    time.sleep(1)
    print("You are fighting Charmander")
    time.sleep(1)
    print("Let's look at the Charmander's attributes")
    time.sleep(1)
    Chealth = random.randint(57,59)
    print("The health of your pokemon is " + str(Chealth))
    time.sleep(1)
    Cspeed = random.randint(54,67)
    print("The speed of your pokemon is " + str(Cspeed))
    time.sleep(1)
    Cdefence = random.randint(51,55)
    print("The defence of your pokemon is " + str(Cdefence))
    time.sleep(1)
    Cattack = random.randint(53,61)
    print("The attack of your pokemon is " +str(Cattack))
    time.sleep(1)
    print("You're climbing a volcano... when a wild Charmander appears!")
    time.sleep(1)
    if Bspeed > Cspeed:
        print("You have a higher speed, so you attack first!")
        attack = input("Pick an attack:\n1 - Vine Whip\n2 - Razor Leaf\n3 - Poison Powder\n")
        if int(attack) == 1:
            print("You whipped the wild Charmander")
        elif int(attack) == 2:
            print("You performed Razor Leaf on the wild Charmander")
        elif int(attack) == 3:
                print("You blinded the wild Charmander with Smokescreen")
        else:
            print("Sorry that didn't work please try again")
            exit()
# will cause exit before Cspeed > Bspeed
#    else:
#        print("Sorry that didn't work, please try again")
#        exit()
    if Cspeed > Bspeed:
        print("Charmander has a higher speed, so they attack first!")
        print("Charmander uses Fire Spin")
    # Theres only one other scenario here Cspeed = Bspeed
    # you could  use  "else"  as its the  onlty other logical  condition
    # or in  my opinion  its better to have another if to make it clearer
    # the intention of the program
    
    #else:
    if Cspeed == Bspeed:
        print("Both  Pokemon  have identical  speed!")
        exit()
    # Add something here to decide  what to do in this scenario

print("Hi there, welcome to Pokemon!")
time.sleep(1)
name = raw_input("What is your name? ") #This is a variable that is going to hold user input.
print("Hi Master " + name) #This is a print statement that includes a variable in it
choice  = input("Pick a starter Pokemon:\n1 - Bulbasaur\n2 - Squirtle\n3 - Charmander\n")
if int(choice) == 1: 
    Bulbasaur()  #The line of code is indented due to it being dependent on the line above being true. This line of ode will only happen if 1 is entered.

elif int(choice) == 2:
    Squirtle()

elif int(choice) == 3:
    Charmander()
else:  #This is the final part of the conditional set. It is almost always necessary to use ELSE.
       #Otherwise your program might crash
   print("Thats not a valid option, please try again.")
   time.sleep(1.5)
   exit()

"""
*** Notes for Suli ***

Anything within a block of triple " is a comment by the way.

I could be wrong but I dont necessarily agree with the comment above about else
if you have your last "elif" statement then you can just drop out of that, you 
don't always need an "else". You only need an else if you want to say "if nothing 
else then do this"

I put some comments above, basically where your speed comparisons were, when the
CPU pokemon's speed was greater you'd just drop out at the else statement, as I
said  above, the final "else" statement is not always necessary.  You'll need to 
edit your other functions in the same way.
"""

