import random

print("ROCK PAPER ANDDDDDDDD SISSORS")
print("------------------------------------------------------------")
print("\n")

count = 0
repet = 'y'

while repet == 'y':

    inp = input("What do you choose: rock, paper or sissors? ").lower()

    while inp not in ['rock', 'paper', 'sissors']:
        print("Invalid input, try again")
        inp = input("What do you choose: rock, paper or sissors? ").lower()

    ranch = random.choice(['rock', 'paper', 'sissors'])

    if inp == 'rock':

        if ranch == 'rock':
            print(f"You chose {inp}")
            print(f"Opponent chose {ranch}")
            print("DRAW")

        elif ranch == 'paper':
            print(f"You chose {inp}")
            print(f"Opponent chose {ranch}")
            print("LOSS")
            count -= 1

        elif ranch == 'sissors':
            print(f"You chose {inp}")
            print(f"Opponent chose {ranch}")
            print("WIN")
            count += 1

    elif inp == 'paper':

        if ranch == 'paper':
            print(f"You chose {inp}")
            print(f"Opponent chose {ranch}")
            print("DRAW")

        elif ranch == 'sissors':
            print(f"You chose {inp}")
            print(f"Opponent chose {ranch}")
            print("LOSS")
            count -= 1

        elif ranch == 'rock':
            print(f"You chose {inp}")
            print(f"Opponent chose {ranch}")
            print("WIN")
            count += 1

    elif inp == 'sissors':

        if ranch == 'sissors':
            print(f"You chose {inp}")
            print(f"Opponent chose {ranch}")
            print("DRAW")

        elif ranch == 'rock':
            print(f"You chose {inp}")
            print(f"Opponent chose {ranch}")
            print("LOSS")
            count -= 1

        elif ranch == 'paper':
            print(f"You chose {inp}")
            print(f"Opponent chose {ranch}")
            print("WIN")
            count += 1

    print(f"Count: {count}")

    repet = input("Do you wanna play again? Y/N: ").lower()

print("Thanks for playing!")
