import random



#This file includes all of the consants and basic fonction of the game




colors = ["Clubs", "Diamonds", "Hearts", "Spades"]
values  = {"2":2, "3":3, "4":4,"5":5, "6":6 , "7":7,
          "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10, "Ace":0}

# creates an organized deck of 56 cards
def deck():
    dek = []
    for color in colors:
          for value in values:
              dek.append(value+ " of "+color)

    return dek

#return the value of a card (special value for ace dealt with later)
def valueCard(card):
    return values[card.split()[0]]


# returns a shuffled deck out of n deck of 56 cards
def initdraw(n):
    d = []
    for i in range(n):
        d += deck()
        
    random.shuffle(d)
    return d

#ask the name of the differents players and returns a list of their names
def initJoueurs(n) :
    joueurs = []
    for i in range(n) :
        joueurs.append(str(input("Nom du joueur " + str(i) + " ? ")))
    return joueurs

#create a dictionnary of the different players' scores
def initScores(joueurs, v=0) :
    scores = {}
    for i in range(len(joueurs)) :
        scores[joueurs[i]] = v
    return scores

# draw x cards from the deck
def draw_card(d, x = 1):
    cards = []
    for i in range(x):
        cards.append(d[0])
        del d[0]
    return cards

# calculates the scores from a list of cards
def score(cards):
    ace = 0
    sc = 0
    for c in cards:
        # counts the number of aces
        if valueCard(c) == 0:
            ace += 1
        else:
            sc += valueCard(c)
    #calculates the most advantagious scores for the players number of aces
    i = 1
    while i<=ace:
        if sc <= 21-11-(ace-i):
            sc += 11
        else:
            sc+= 1
        i+=1
    return sc

#deals the first two cards to each players and returns
#a dictionnaries with the players  cards
# and a list of the remaining cards in the deck
def premierTour(players, n):
    
    cards = {}
    deck = initdraw(n)
    for i in range(len(players)):
        c = draw_card(deck, 2)
        cards[players[i]] = c
    return cards, deck

#calculates of much of his bet the player is getting back 0 if he loses 2 if he wins 1 if draw
def gagnant(score_p, score_d):
    if score_p >21:
        return 0
    elif score_p == 21:
        return 2
    elif score_p == score_d:
        return 1
    else:
        if score_d >=21:
            return 2
        elif score_d > score_p:
            return 0
        else:
            return 2


def actionJoueur():
    valide = False
    while not valide:   
        a = input("voulez vous piocher ou vous arreter?(p/a):")
        valide = (a == "a" or a == "p")
    return a == "p"


def tour_joueur(joueur, cartes, dealer):
    print("------------------------------------------------")
    print("Tour du joueur: ", joueur)
    print("Cartes:")
    for c in cartes[joueur]:
        print(c)
    print("Ce qui donne un score de:", score(cartes[joueur]))
    print()
    print("la carte du dealeur est:", dealer[0])
    print("ce qui lui donne un score de:", score(dealer))
    print()
    action = actionJoueur()
    
    if action:
        print("cous piochez un carte")
    else:
        print("vous vous couchez")
        
    
    
if __name__ == "__main__":
    cartes , pioche = premierTour(["emeric"], 1)
    dealeur = ["2 of ermjf"]
    tour_joueur("emeric", cartes, dealeur)
    
