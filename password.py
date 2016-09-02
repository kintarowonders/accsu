import os
import random

randomBytes = os.urandom(16777216)
integer = int.from_bytes(randomBytes, byteorder='big')
random.seed(integer)

def generatePassword():
    # passwords from github repo https://github.com/dwyl/english-words.git
    # use the file words2.txt as the other passwords contain symbols.
    f = open("wordlist.txt",'r')

    x=0
    wordlist = []
    for line in f:
        word = line
        x = x + 1
        wordlist.append(word.rstrip('\n'))
    words = x

    password = ""
    for x in range(0,4):
        word = wordlist[random.randrange(0,words)]
        password = password + word + " "
    return password.rstrip(' ')

# With passwords like this, why argue:
# Pindarist unwebbing Trappist stipendial
# coelenteron mnemonic inscriptioned ungypsylike
# ... See?
