def saveKey(key, cipherName, round, iter):
    f = open('keysDecode.txt', 'a', encoding="utf-8")
    print(cipherName, round, iter, key)
    f.write(str(round) + " " + str(iter) + " " + cipherName + " " + str(key) + '\n')
