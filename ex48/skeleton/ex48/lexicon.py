directions = ("north", "south", "east", "west", "down", "up", "left", "right", "back")
verbs = ("go", "stop", "kill", "eat")
stops = ("the", "in", "of", "from", "at", "it")
nouns = ("door", "bear", "princess", "cabinet")

def select(raw_word):
    word = raw_word.lower()
    if word in directions:
        return ("direction", raw_word)
    elif word in verbs:
        return ("verb", raw_word)
    elif word in stops:
        return ("stop", raw_word)
    elif word in nouns:
        return ("noun", raw_word)
    else:
        try:
            return ("number", int(raw_word))
        except ValueError:
            return ("error", raw_word)

def scan(words):
    word_list = str(words).split()
    return map(select, word_list)

if __name__ == '__main__':
    print scan('North go the door 1 WSAD')
