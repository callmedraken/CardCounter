### John Hsiao 7/30/2019
### Card counter program for playing blackjack

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
    trueCount = 0
    

def main():
    print("Welcome to the Card Counter Program")
    deckCount = input("Input the number of decks being used: ")
    cardCounting(deckCount)

if __name__ == '__main__':
    main()