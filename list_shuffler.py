import random

ex = [1,2,3,4,5,6,7,8,9,0]

def shuffler_oflist(mylist):
    ex = random.shuffle(mylist)
    return mylist


print(shuffler_oflist(ex))
