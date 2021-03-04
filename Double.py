def double(cipher):
    doubleCipher = ''
    while int(cipher) > 0:
        doubleCipher = str(cipher % 2) + doubleCipher
        cipher = cipher // 2
    return doubleCipher