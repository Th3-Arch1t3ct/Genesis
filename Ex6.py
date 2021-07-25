# Store the sentence "There are 10 types of people." in the variable x
x = "There are %d types of people." % 10
# Assign the string "binary" to the variable "binary
binary = "binary"
# Assign the string "don't" to the variable "do_not"
do_not = "don't"
# Store the sentence "those who know %s and those who %s." in the variable y
y = "those who know %s and those who %s." % (binary, do_not)

# print the content of the variable y
print(x)
# print the content of the variable x
print(y)

# print "I said 'there are 10 types of people.'."
print("i said %r." % x)
# print i also said: 'those who know binary and those who don't.'."
print("i also said: '%s'." % y)

# store the boolean value False in the variable "hilarious"
hilarious = False
# store the boolean value "Isn't that joke so funny?!" in the variable 'joke_evaluation'
joke_evaluation = "Isn't that joke so funny?! %r"

# print out "isn't that joke so funny?! False" by assigning the %r character to hilarious of which the value is false
print(joke_evaluation % hilarious)

# store the sentence "This is the left side of..." in the variable w
w = "This is the left side of..."
# store the sentence "a string with a right side." in the variable e
e = "a string with a right side."

# combine the strings from variables "w" and "e". After that, print them.
print(w + e)

