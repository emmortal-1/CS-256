# Start of the code for Lab 3
# The Goofy Silly Ah Adventure
# By: Logan Huffman and Cameron Harris
print("You wake up in the middle of a forest. You have no memory of how or why you came to be here.")
print("There is a sign in front of you and a sign behind you, the words 'North' and 'South' inscribed upon each sign respectively.")

# Ask the user which direction they would like to go
direction = input("Will you go North, or will you go South?")

# If the user chooses to go North
# This section of code was written by Logan Huffman
if direction == 'North':
    
    # The user encounters a cave
    print("You come across a large Cave Entrance. You enter the cave.")
    print("Inside the cave, you see a Giant Troll with a Cannon on its Shoulders.")
    
    # Ask the user if they would like to fight the troll or run away
    choice1 = input("Do you fight the Troll or run away? ")
    
    # If the user chooses to fight the troll
    if choice1 == 'Fight':
        print("You pick up a rock from the floor of the cave.")
        print("You throw the rock at a stalagtite on the roof of the Cave.")
        print("The stalagtite falls and crushes the Troll's neck.")
        print("You crawl into the cannon and launch yourself out of it, and fly into a nearby town, landing safely upon a conveniently placed wheelbarrow of goose down.")
        print("Good End")
    # If the user chooses to run away
    elif choice1 == 'Run away':
        print("You attempt to run away from the troll.")
        print("You trip over a rock, hitting your head on the ground, and die.")
    # If the user chooses something else
    else:
        print("You cant do that.")

# If the user chooses to go South
# This section of code was written by Cameron Harris
if direction == 'South':
        
        # The user encounters a stream
        print("You walk through the flora and fauna, and finally come across a flowing stream.")
        
        # Ask the user if they would like to drink the water or not
        choice2 = input("You are severely dehydrated. Do you drink the water from the stream, or do you not?")
        
        # If the user chooses to drink the water
        if choice2 == 'Drink':
             print("You drink the water from the stream.")
             print("At first, you feel somewhat strange; your head spins. But then, wings sprout from your back.")
             print("Elated, you fly above the roof of this forsaken prison of a forest, and continue flying until you come to civilization.")
             print("You are free. Good End.")
        
        # If the user chooses not to drink the water
        if choice2 == 'Do not drink':
            print("You ignore the urge to drink the water and travel alongside it.")
            print("You come across a house and knock upon the door, now severely desparate for food and water.")
            print("Out of the house comes an angry wizard, who takes out his Glock-19 and shoots you several times in the face and chest.")
            print("You are now very dead. Bad End.")