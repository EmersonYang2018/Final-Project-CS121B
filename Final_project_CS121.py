#Emerson Yang
#BlackJack Game

#problem 1


import random
class Ace: #
    def __init__(self, shape):
        self.shape = shape
        self.value = 11

    def __str__(self):
        return "Ace of " + str(self.shape)

    def changeValue(self):
        self.value = 1

    def getValue(self):
        return int(self.value)

    def sayCard(self):
        return "Ace of " + str(self.shape)

DAce = Ace("Diamonds")
SAce = Ace("Spades")
HAce = Ace("Hearts")
CAce = Ace("Clubs")


defaultDeck = {"2 of Spades":2, "3 of Spades": 3, "4 of Spades":4, "5 of Spades":5, "6 of Spades":6, "7 of Spades":7, "8 of Spades":8, "9 of Spades":9,\
               "10 of Spades":10, "Jack of Spades":10, "Queen of Spades":10, "King of Spades":10, SAce:11, "2 of Clubs":2, "3 of Clubs": 3, "4 of Clubs":4,\
               "5 of Clubs":5, "6 of Clubs":6, "7 of Clubs":7, "8 of Clubs":8, "9 of Clubs":9, "10 of Clubs":10, "Jack of Clubs":10, "Queen of Clubs":10,\
               "King of Clubs":10, CAce:11, "2 of Hearts":2, "3 of Hearts": 3, "4 of Hearts":4, "5 of Hearts":5, "6 of Hearts":6, "7 of Hearts":7,\
               "8 of Hearts":8, "9 of Hearts":9, "10 of Hearts":10, "Jack of Hearts":10, "Queen of Hearts":10, "King of Hearts":10, HAce:11, "2 of Diamonds":2,\
               "3 of Diamonds": 3, "4 of Diamonds":4, "5 of Diamonds":5, "6 of Diamonds":6, "7 of Diamonds":7, "8 of Diamonds":8, "9 of Diamonds":9,\
               "10 of Diamonds":10, "Jack of Diamonds":10, "Queen of Diamonds":10, "King of Diamonds":10, DAce:11}


deck=[]
for i in defaultDeck.keys():
    deck.append(i)


def PCplay(): #Dealer
    PCsum = 0
    PCcards = []
    while PCsum < 17:
        ca = random.randrange(0, len(deck))
        card = deck[ca]
        PCsum = PCsum + int(defaultDeck[card])
        PCcards.append(card)
        deck.remove(card)
        for a in PCcards:
            if PCsum > 21 and isinstance(a, Ace) and a.getValue()==11:
                PCsum = PCsum - 10
                a.changeValue()
    for s in PCcards:
        if isinstance(s, Ace):
            PCcards[PCcards.index(s)] = s.sayCard()
    print(PCsum)
    print(PCcards[1:])
    print(PCcards)

PCplay()



class Player: #The person who plays the game
    def __init__(self):
        self.playersum = 0
        self.playerCards =[]
        self.playerStats = [self.playersum, self.playerCards]

    def hit(self,deck,defaultDeck,playerCards,playersum):
        ca = random.randrange(0, len(deck))
        card = deck[ca]
        self.playersum = int(self.playersum) + int(defaultDeck[card])
        self.playerCards.append(card)
        deck.remove(card)
        for a in playerCards:
            if self.playersum > 21 and isinstance(a, Ace) and a.getValue()==11:
                self.playersum = int(self.playersum) - 10
                a.changeValue()
        for s in self.playerCards:
            if isinstance(s, Ace):
                self.playerCards[self.playerCards.index(s)] = s.sayCard()
        self.playerStats = [self.playersum, self.playerCards, card]
        return self.playerStats

    def stopPlaying(self,):
        if PCsum < self.playersum:
            print(str(self) + " wins!")
        elif PCsum > self.playersum:
            print("All players lost")
        elif PCsum == self.playersum:
            print("You get your money back")

        PCsum = 0
        self.playersum = 0
        self.playerCards = []
        PCcards = []

        return
    
    #Test edit
