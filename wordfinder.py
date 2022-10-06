import random

"""Word Finder: finds random words from a dictionary."""
class WordFinder:
    ...

    def __init__(self, wordsfile):
        "Initializes start and inc variables"
        self.words = self.readwords(wordsfile)

    def readwords(self, wordsfile):
        file = open(wordsfile)
        words = [line for line in file]
        file.close()
        return words

    def random(self):
        return self.words[random.randrange(0, len(self.words) - 1)].rstrip()


wf = WordFinder('.\words.txt')

print(wf.random())
        



class SpecialWordFinder(WordFinder):

    def __init__(self, wordsfile):

        self.words = self.readwords(wordsfile)

    def readwords(self, wordsfile):
        file = open(wordsfile)
        words = [line.strip() for line in file if len(line.strip()) > 0 and not line[0] == '#']
        file.close()
        return words


swf = SpecialWordFinder('.\\test.txt')

print(swf.random())

    