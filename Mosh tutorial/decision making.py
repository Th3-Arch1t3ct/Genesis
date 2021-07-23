print("You enter a dark room with two doors. Do you go through door #1 or door #2?")

choice = input("> ")


if choice == "1":
    print("There's a giant bear here eating a cheese cake. What do you do?")

    choice = input("> ")


    if "Take The Cake" in choice:
        print("2. Scream at the bear.")

    choice = input("> ")

    if "bear" in choice == "1":
        print("The bear eats your face off. Good job!")
    elif "bear" in choice == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print("Well, doing %s is probably better. Bear runs away.") % bear

elif choice == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    choice = input("> ")

    if "1" == choice or "2" == choice:
        print("your body survives powered by a mind of jello. Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck. Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")