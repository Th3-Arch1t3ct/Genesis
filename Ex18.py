# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print("args1: %r, arg2: %r" % (arg1, arg2))

# ok, that *arg is actually pointless, we can just do this
def print_two_again(arg1, arg2):
    print("arg1 : %r, arg2: %r" % (arg1, arg2))

# this just takes one argument
def print_one(arg1):
    print("arg1: %r" % arg1)

# this one takes no argument
def print_none():
    print("I got nothin.")

print_two("Ozy","Mandias")
print_two_again("Ozy","Mandias")
print_one("First!")
print_none()
