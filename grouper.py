def grouper(iterable, n):
    args = [iter(iterable)] * n
    text = zip(*args)
    textBlocks = [''.join(i) for i in text]
    return textBlocks

