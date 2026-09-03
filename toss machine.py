import random

print("TOSS MACHINE")
ht = ["heads", "tails"]
win = 0
loss = 0

while True:
    inp = input("HEADS OR TAILES: ").lower()
    if inp in ["heads", "tails"]:
        out = random.choice(ht)

    else:
        while inp not in ["heads", "tails"]:
            print("what do u mean?? try again ")
            inp = input("HEADS OR TAILES: ").lower()
        out = random.choice(ht)

    print(f"you chose: {inp}")
    print(f"coin landed on: {out}")

    if inp == out:
        print("you win the toss ")
        win = win + 1
    else:
        print("you lose ")
        loss = loss + 1

    print(f"counter win= {win} loss = {loss}") 
