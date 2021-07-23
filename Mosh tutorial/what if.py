useful = 30
average = 20
waste = 15


if useful > average:
    print("Too little useful! The world is doomed!")

if useful < average:
    print("A lot of useful! The world is saved!")

if useful > waste:
    print("The world is really fucked! Like for real!!")

if useful < waste:
    print("We all good.")


waste += 5

if average >= waste:
    print("Average is greater than or equal to waste.")

if average <= waste:
    print("Average are less than equal to waste.")


if average == waste:
    print("Average is waste.")