### John Hsiao 7/30/2019
### Card counter program for playing blackjack

import sys
import math

def cardCounting(deckCount):
    switcher = {
        "1": -1,
        "A": -1,
        "a": -1,
        "2": 1,
        "3": 1,
        "4": 1,
        "5": 1,
        "6": 1,
        "7": 0,
        "8": 0,
        "9": 0,
        "10": -1,
        "11": -1,
        "J": -1,
        "j": -1,
        "12": -1,
        "Q": -1,
        "q": -1,
        "13": -1,
        "K": -1,
        "k": -1
    }
    runningCount = 0
    totalCardsLeft = deckCount * 52
    decksLeft = deckCount
    round = 0
    while True:
        print("Round #: ", round)
        ### Initial deal of everyone else's cards
        otherCards = str(input("Other cards: "))
        if otherCards == "quit":
            sys.exit(0)
        tempCount, tempCards, otherCards = parseCards(otherCards, switcher)
        runningCount += tempCount
        totalCardsLeft -= tempCards


        ### What is the dealers hand?
        dealerUp = str(input("Dealer Upcard: "))
        if dealerUp == "quit":
            sys.exit(0)
        tempCount, tempCards, dealerUp = parseCards(dealerUp, switcher)
        runningCount += tempCount
        totalCardsLeft -= tempCards


        ### What is your hand?
        yourHand = str(input("Your initial hand: "))
        if yourHand == "quit":
            sys.exit(0)
        tempCount, tempCards, yourHand = parseCards(yourHand, switcher)
        runningCount += tempCount
        totalCardsLeft -= tempCards

        decksLeft = math.floor(totalCardsLeft/52)
        trueCount = runningCount / decksLeft
        print("True Count :", trueCount, "Running count:", runningCount)
        if deckCount > 2:
            illustrious18(dealerUp, yourHand)

        round+=1


def illustrious18(dealerUp, yourHand):
    cardTally = 0
    print(yourHand)
    return


def parseCards(cards, dict):
    cardList = [x.strip() for x in cards.split(',')]
    print(cardList)
    count = 0
    cardCount = 0
    for card in cardList:
        val = dict.get(card)
        count += val
        cardCount += 1
    return count, cardCount, cardList


def main():
    print("Welcome to the Card Counter Program")
    print("Separate cards by a comma")
    print("Input \"quit\" at any time to exit the program")
    deckCount = input("Input the number of decks being used: ")
    if deckCount == "quit":
        sys.exit(0)
    cardCounting(int(deckCount))
    print("Thanks for playing!")

if __name__ == '__main__':
    main()