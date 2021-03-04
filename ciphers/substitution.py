import random
import saveKey
import grouper

lengthBlock = 16

def makeKey(alphabet):
   alphabet = list(alphabet)
   random.shuffle(alphabet)
   return ''.join(alphabet)

def encodeSubstitution(plaintext, alphabet, iter, round):
    key = makeKey(alphabet)
    saveKey.saveKey(key, "Sub", round, iter)
    keyMap = dict(zip(alphabet, key))
    textBlocks = grouper.grouper(plaintext, lengthBlock)

    encodeText = ""
    for i in textBlocks:
        encodeText += ''.join(keyMap.get(c, c) for c in i)
    return encodeText

def decodeSubstitution(cipher, key, alphabet):
    keyMap = dict(zip(key, alphabet))
    return ''.join(keyMap.get(c, c) for c in cipher)

