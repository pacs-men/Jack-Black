import random



#This file includes all of the consants and basic fonction of the game




colors = ["Clubs", "Diamonds", "Hearts", "Spades"]
values  = {"2":2, "3":3, "4":4,"5":5, "6":6 , "7":7,
          "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10, "Ace":0}


def deck():
    dek = []
    for color in colors:
          for value in values:
              dek.append(value+ " of "+color)

    return dek


def valueCard(card):
    return values[card.split()[0]]


def initdraw(n):
    dek = []
    for i in range(n):
        dek.append(deck())
        random.shuffle(dek[i])
    return dek

def initJoueurs(n) :
    joueurs = []
    for i in range(n) :
        joueurs.append(str(input("Nom du joueur " + str(i) + " ? ")))
    return joueurs

def initScores(joueurs, v=0) :
    scores = {}
    for i in range(len(joueurs)) :
        scores[joueurs[i]] = v
    return scores

def draw_card(d, x = 1):
    cards = []
    for i in range(x):
        cards.append(d[0])
        del d[0]
    return cards

def score(cards):
    ace = 0
    sc = 0
    for c in cards:
        if valueCard(c) == 0:
            ace += 1
        else:
            sc += valueCard(c)
    for i in range(ace):
        if sc <= 21-11:
            sc += 11
        else:
            sc+= 1
    return sc

def premierTour(players):
    scores = initScores(players)
    deck = initdraw(len(players))
    for i in range(len(players)):
        c = draw_card(deck[i], 2)
        scores[players[i]] = score(c)
    return scores

def gagnant(scores) :
    scorespoubelle = dict(scores)
    gagnants = []
    for nom in scorespoubelle :
        if scorespoubelle[nom] == scores[max(scorespoubelle)] :
            if scorespoubelle[nom] <= 21 :
                gagnants.append(nom)
                gagnants.append(scorespoubelle[nom])
            else :
                del scorespoubelle[nom]
    return gagnants

if __name__ == "__main__":
    print(initdraw(1))
    
