class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = Song(["All i want for my birthday",
                   "Is a big booty hoe, and blow",
                   "And plenty cash to sow"])

bulls_on_parade = Song(["Big booty hoes flock",
                        "Bout to kill two hens with one cock"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()