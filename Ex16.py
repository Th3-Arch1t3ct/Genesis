from sys import argv

script, Ex16.py = argv

print("We're going to erase %r." % Ex16.py)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening file...")
target = open("Ex16.py", 'w')

print("Truncating the file. Goodbye.")
target.truncate()

print("Now im going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1)
target.write("\n")