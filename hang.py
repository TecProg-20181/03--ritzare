import random
import string

WORDLIST_FILENAME = "palavras.txt"


def loadWordssmall():
    list = []
    guesses = 8
    """
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    for item in wordlist:
     if difletters(item) < guesses:
           list.append(item)
    print "  " ,  len(list), "words loaded."
    return random.choice(list )  

def isWordGuessed(secretWord, lettersGuessed):
    secretLetters = []


    for letter in secretWord:
        if letter in lettersGuessed:
            pass
        else:
             return False

    return True
    
def getAvailableLetters():
    import string
    # 'abcdefghijklmnopqrstuvwxyz'
    available = string.ascii_lowercase


    return available

def difletters(secretWord):
        num = 0
        for letter in getAvailableLetters():
            if letter in secretWord:
                num += 1
        return num




def findGessed(secretWord, lettersGuessed):
    guessed = ''
    for letter in secretWord: 
        if letter in lettersGuessed:
            guessed += letter
        else:
            guessed += '_ '


                
    return guessed

def hangman(secretWord):
    resposta = 0
    differentsletters = 0
    guessed = ''
    guesses = 8
    lettersGuessed = []
    print 'Welcome to the game, Hangam!'
    print 'I am thinking of a word that is', len(secretWord), ' letters long.'
    print '-------------'   
    resposta = input('Do you want to know how many differents letters? 1 : yes | 0 : no: ')
    
    if resposta == 1:
           differentsletters = difletters(secretWord)  
           print 'Number of differents letters:',differentsletters

    while  isWordGuessed(secretWord, lettersGuessed) == False and guesses >0:
            print 'You have ', guesses, 'guesses left.'

            available = getAvailableLetters()
            for letter in available:
                if letter in lettersGuessed:
                    available = available.replace(letter, '')

            print 'Available letters', available
            letter = raw_input('Please guess a letter: ')
            if letter in lettersGuessed:        
                guessed = findGessed(secretWord, lettersGuessed)  
                print 'Oops! You have already guessed that letter: ', guessed
            elif letter in secretWord:
                lettersGuessed.append(letter)    
                guessed = findGessed(secretWord, lettersGuessed)       
                print 'Good Guess: ', guessed
            else:
                guesses -=1
                lettersGuessed.append(letter)   
                guessed = findGessed(secretWord, lettersGuessed)        
                print 'Oops! That letter is not in my word: ', guessed
            print '------------'

    else:
            if isWordGuessed(secretWord, lettersGuessed) == True:
                print 'Congratulations, you won!'
            else:
                print 'Sorry, you ran out of guesses. The word was ', secretWord, '.'    
            
   
        
        
          





secretWord = loadWordssmall().lower()
hangman(secretWord)
