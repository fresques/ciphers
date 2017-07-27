# vigenere cipher
# hannah fresques
# July 18, 2017

import numpy as np

import sys
inFile    = sys.argv[1]
outFile   = sys.argv[2]
key       = sys.argv[3]
direction = sys.argv[4]

# read file
with open(inFile,'r') as i:
    textIn = i.read()



# code from internet to convert letters to numbers. I don't understand it.
# import string
# di=dict(zip(string.letters,[ord(c)%32 for c in string.letters]))


# my function to convert letters to numbers and viceversa
# def toNum(charStr):
# 	charStr = charStr.lower()
# 	numStr = []
# 	for character in charStr:
# 	    number = ord(character) - 96
# 	    numStr.append(number)
# 	return np.array(numStr)

# def toChar(numStr):
# 	charStr = ""
# 	for number in numStr:
# 	    character = chr(number + 96)
# 	    charStr = charStr + character
# 	return charStr

# repeatedKey = (key*int(np.ceil(len(textIn)/len(key))))[0:len(textIn)]
# repeatedKey2 = toNum(repeatedKey)


textOut = ""
i=len(key)
for eachIn in textIn:
	if eachIn.isalpha():
		i=i % len(key)
		key2 = ord(key[i].lower()) - 96
		eachIn2 = ord(eachIn.lower()) - 96
		if direction=='encrypt':
			eachOut = (eachIn2 + key2) % 26
		elif direction=='decrypt':
			eachOut = (eachIn2 - key2 + 1) % 26
		eachOut = chr(eachOut + 96)
		if eachIn.isupper():
			eachOut = eachOut.upper()
	else:
		eachOut = eachIn
	textOut = textOut + eachOut

			


with open(outFile,'w') as o:
    for line in textOut:
        o.write(line)


