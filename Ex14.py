from sys import argv

[ex14, Jude] = argv
prompt = "> "

print("Hi %s, I'm the %s script." % (Jude, ex14))
print("I'd like to ask you a few questions.")
print("Do like me %s?" % Jude)
likes = input("yes: ")

print("Where do you live %s?" % Jude)
lives = input("MSA: ")

print("What kind of computer do you have?")
computer = input("HP: ")

print("""
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer))
