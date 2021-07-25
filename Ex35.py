from sys import exit


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = input("> ")
    if "0" in next or "1" in next:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
    if how_much > 50:
        print("you greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bitch?")
    bear_moved = True

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("The bear sees you and bitch slaps you.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear fucks off, thinking dem man wicked. pass through.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            print("there bear says dem man wicked, but me wickeder dan dem")
            bear_moved = False
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil cthulhu.")
    print("It stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good Job!")
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left")
    print("Which one do you take?")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()


start()
