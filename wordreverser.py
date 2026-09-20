def master_yoda(text):
    wlist = text.split()
    reversewl = wlist[::-1]
    return ' '.join(reversewl)
print(master_yoda('I am home'))
