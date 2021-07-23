def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split()
    return words

def sort_words(words):
    """Sort the words."""
    return sorted(words)

def print_first_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print(word)

def sort_sentence(sentence):
    words = break_words(sentence)
    return  sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sentence_sorted(sentence):
    """Sorta the words then prints the first and last one."""
    word = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)

print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.")

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love 
nor comprehend passion from intuition
and requires and explanation
\n\t\twhere there is none.
"""


print("------------")
print("poem")
print("------------")

five = 10 - 2 + 3 - 5
print("This should be five: %s" % five)

def secret_formula(started):
    jelly_beans = started * 500
    # bug: jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates

start_point = 10000
# bug: beans, jars, crates == secret_formula(start_point)
beans, jars, crates = secret_formula(start_point)

# bug: print "With a starting point of: %d" % start_point
print("With a starting point of: %d" % start_point)
print("We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates))

start_point = start_point / 10

print("We can also do that this way:")
print("We'd have %d beans.=, %d jars, and %d crab-apples." % secret_formula(start_point))


# 0ug: sentence = "All good\t things come those who wait."
sentence = "All good\t things come those who wait."

# bug: words = ex25.break_words(sentence)
words = ex25.break_words(sentence)
# bug: sort_words = ex25.sort_words(words)
sort_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
# bug: print_first_word(sorted_words)
print_first_word(sort_words)
# bug: sort_words = ex25.sort_sentence(sentence)
sort_words = ex25.sort_sentence(sentence)
print_sorted_words
# bug: print_first_and_last(sentence)
print_first_and_last(sentence)

# bug: print_first_and_last_sentence_sorted(sentence)
print_first_and_last_sentence_sorted(sentence)