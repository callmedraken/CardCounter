### John Hsiao 7/30/2019
### Card counter program for playing blackjack

import sys

def cardCounting(deckCount):
    switcher = {
        1: -1,
        "A": -1,
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 0,
        8: 0,
        9: 0,
        10: -1,
        11: -1,
        "J": -1,
        12: -1,
        "Q": -1,
        13: -1,
        "K": -1
    }
    runningCount = 0
    remainingDecks = deckCount
    trueCount = runningCount/remainingDecks
    while True:
        inp = input("Dealt card: ")
        
        if inp == "quit":
            sys.exit(0)



def main():
    print("Welcome to the Card Counter Program")
    print("Input \"quit\" at any time to exit the program")
    deckCount = input("Input the number of decks being used: ")
    if deckCount == "quit":
        sys.exit(0)
    cardCounting(deckCount)
    print("Thanks for playing!")

if __name__ == '__main__':
    main()