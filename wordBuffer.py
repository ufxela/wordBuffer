from random import randint

# read file

def readFile(filename):
    mythesaurus = {}
    datasource = open(filename, "r")
    if datasource.mode == 'r':
        contents = datasource.readlines()
        i = 1;
        while i < len(contents):
            line = contents[i]
            splitted = line.split("|")
            key = splitted[0]
            value = []
            for j in range(0, int(splitted[1])):
                synonyms = contents[i + 1 + j]
                splitSynonyms = synonyms.split("|", 1)
                listValues = splitSynonyms[1].split("|")
                value += listValues
            mythesaurus[key] = value
            i = i + int(splitted[1]) + 1
    return mythesaurus

# read in text
thesaurus = readFile("MyThesaurus.txt")

# ask user for words to replace & replace them
originalText = input("What text do you want to buff, buddy? ")

sentinel = 0
while sentinel == 0:
    try:
        wordToReplace = input("what's a word that you wanna buff up, home slice? ")
        synonyms = thesaurus[wordToReplace]
        randInteger = randint(0, len(wordToReplace) - 1)
        replacement = thesaurus[wordToReplace][randInteger]
        originalText = originalText.replace(wordToReplace, replacement, 1)
        originalText = originalText.replace("\n", "")
        print(originalText)
    except KeyError:
        print("the key was now found. try a different word, or a root word")
    except IndexError:
        print("try again")

    sentinel = int(input("do you still want to continue? 0 for yes, 1 for no "))

# way to extend this is to ask the user what part of speech their word is, and store that somehow.
# another thing is to add in functionality for plural words/nouns
# another thing is to add in functionality for different forms of words
# ask the user if they like the additions and if not they can reverse them
#fix caps/lowercase