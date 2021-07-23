from sys import argv # from system import file

script, input_file = argv

def print_all(f): # print all of file
    print(f.read()) # open file in read mode

def rewind(f): # have file ready but do not print it all
    f.seek(0) # look for certain line

def print_a_line(line_count, f): # define function to print specific line
    print(line_count, f.readline())

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file) # call print all function

print("Now let's rewind, kind of like a tape")

rewind(current_file) # use rewind function

print("Let's print three lines:")

# run print a line function
current_line = 1 # print line 1
print_a_line(current_line, current_file)

current_line = current_line + 1 # print line 1 + 1 (2)
print_a_line(current_line, current_file)

current_line = current_line + 1 # print line 2 + 1 (3)
print_a_line(current_line, current_file)

current_line = current_line + 1 # print line 3 + 1 (4)
print_a_line(current_line, current_file)