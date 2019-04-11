# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random

WORDLIST_FILENAME = "C:/Users/salah el-ashaal/Desktop/dev stuff/hangman/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    z = []
    x = []
    if len(lettersGuessed) == 0:
        return False
    else: 
        for i in secretWord:
                z.append(i)
        z.sort()
        for i in lettersGuessed:
            if i in secretWord:
                x.append(i)   
        x.sort()     
        if z == x:
            return True
        else:
            return False



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    x = []
    y = []
    z = []
    for i in secretWord:
        z.append(i)
    if len(lettersGuessed) == 0:
        for i in secretWord:
            x.append("_")
        return ' '.join(x)
    for i in z:
        if i in lettersGuessed:
            y.append(i)
        else:
            y.append("_")
    return ' '.join(y)


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    x = 'abcdefghijklmnopqrstuvwxyz'
    y = []
    for i in x:
        y.append(i)
    z = y
    for i in range(len(lettersGuessed)):
        if lettersGuessed[i] in y:
            del z[y.index(lettersGuessed[i])]
    return ''.join(z)
    

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    a = secretWord
    wordlength = len(a)
    lettersGuessed = []
    numberofGuesses = 0
    print("Welcome to the game Hangman!")
    print("I'm thinking of a word", wordlength, "letters long")
    while numberofGuesses < 8:
        print("------------")
        print("You have", (8 - numberofGuesses), "guesses Left")
        print("Available Letters:", getAvailableLetters(lettersGuessed))
        guess = input("Please enter a letter: ").lower()
        if isWordGuessed(secretWord, lettersGuessed) == True:
            break
        else: 
            if guess in getAvailableLetters(lettersGuessed):
                lettersGuessed.append(guess)
                if guess in secretWord:
                    print("Good Guess:", getGuessedWord(secretWord, lettersGuessed))
                else:
                    numberofGuesses += 1
                    print("Oops! that letter is not in my word:", getGuessedWord(secretWord, lettersGuessed) )
            else:
                print("Oops! You've already guessed that letter:", getGuessedWord(secretWord, lettersGuessed))
    if numberofGuesses < 8:
        print("-------")
        print("Congratulations, you Won!")
    else:
        print("-------")
        print("you lost, the word was", a)






# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
