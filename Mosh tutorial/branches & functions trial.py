def gold_room():
    print("This room is full of gold, jewels and money. How much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much > 50:
        print("Nice, you're not greedy"),
        print("You get a pretty wife"),
        print("but you're broke so she leaves you!")
    if how_much < 50:
        print("You greedy bastard!")

    if choice == "< 50":
        escape()

    elif choice == "bounce":
        escape()


def escape():
    print("The opps try to regain their loot that you discovered. They are coming squad deep and strapped")

    choice = input("> ")
    if "attack" in choice:
        print("Chop heads with Katana swords and leave swiss holes with the blicky.")
    if "valhalla" in choice:
        print("Fuck it. Jump down with C4 and grenades.")

        if choice == "attack":
            survived()
        elif choice == "valhalla":
            start()


def survived():
    print("You managed to survive the opps.")
    print("Now enjoy your newly acquired wealth")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door")
    print("How are you going to move the bear?")
    bear_moved = True

    while True:
        choice = input("> ")

        if next == "take honey":
            print("The bear looks at you then slaps your face off.")
        elif next == "taunt bear" and not bear_moved:
            print("The bear has moved from the door. You can go through it now")
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            print("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()


def cthulhu_room():
    print("here you see that great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        escape()
    elif "head" in choice:
        print("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("Greedy Grafter")


def start():
    print("Your target is in the room.")
    print("There is a door to your right and left, and a window above you.")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    elif choice == "up":
        gold_room()
    else:
        print("You stumble around the room until you starve.")


start()
