import saveKey
import random
from random import choice
from string import ascii_letters


def generateKey(keyLength, iter, round, alphabet):
    key = ''.join(choice(ascii_letters) for i in range(keyLength))
    # Запись ключа в файл
    saveKey.saveKey(key, "Gamma", round, iter)
    return key
