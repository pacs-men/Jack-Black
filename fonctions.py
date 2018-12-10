import random



#This file includes all of the constant and basic fonction of the game




colors = ["Clubs", "Diamonds", "Hearts", "Spades"]
values  = {"2":2, "3":3, "4":4,"5":5, "6":6 , "7":7,
          "8":8, "9":9, "10":10, "Jack":10, "Queen":10, "King":10, "Ace":1}

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
        joueurs.append(str(input("Name of the player " + str(i) + " ? ")))
    return joueurs

#create a dictionnary of the different players's scores
def initScores(joueurs, v=0) :
    scores = {}
    for i in range(len(joueurs)) :
        scores[joueurs[i]] = v
    return scores

# draw x cards from the deck
def draw_card(d,n,x = 1):
    cards = []
    if len(d)>=x:
        for i in range(x):
            cards.append(d[0])
            del d[0]
    else:
        d = initdraw(n)
        cards = draw_card(d, n, x)
    return cards

# calculates the scores from a list of cards
def score(cards):
    ace = 0
    sc = 0
    for c in cards:
        # counts the number of acess
        if valueCard(c) == 1:
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

#deals the first two cards of each player and returns
#a dictionnary with the players cards
# and a list of the remaining cards in the deck
def premierTour(players, deck, n):

    cards = {}

    for i in range(len(players)):
        c = draw_card(deck,n,2)
        cards[players[i]] = c
    return cards

#calculates of much of his bet the player is getting back :
#0 if he loses 2 if he wins 1 if there is a draw
def win(score_p, score_d):
   
    if score_p >21:
        return 0
    elif score_p == score_d:
        return 1
    else:
        if score_d >21:
            return 2
        elif score_d > score_p:
            return 0
        else:
            return 2

# asks the player if he wants to draw another card retrun a boolean
def actionJoueur():
    valide = False
    while not valide:
        a = input("do you want to draw another card of stop?(d/s):")
        valide = (a == "d" or a == "s")
    return a == "d"


    
# displays all the nessesarry information to the player then asks him
# if he wants todraw another card
def tour_joueur(joueur, cartes, dealer, deck, n):
    print("------------------------------------------------")
    print("Turn of : ", joueur)
    print("Cards:")
    for c in cartes[joueur]:
        print(c)
    print("which makes a score of :", score(cartes[joueur]))
    print()
    print("the dealers' card is :", dealer[0])
    print("which gives it a score of :", score(dealer))
    print()
    action = actionJoueur()

    if action:
        c = draw_card(deck, n)
        print("you drew:", c[0])
        cartes[joueur].append(c[0])
        print("your score is now:", score(cartes[joueur]))

        if score(cartes[joueur]) >21:
            print("you busted, you lost")
            input("next players' turn (press any key)")
            return True
        input("next players' turn (press any key)")
        return False

    else:
        print("you ended this round with a score of ", score(cartes[joueur]))

        input("next players' turn (press any key)")
        return True

def complete_players(players,  cards, dealer, deck, n):
    remaining_players = list(players)
    while remaining_players != []:
        for pl in players:
            if pl in remaining_players:
                stops = tour_joueur(pl, cards, dealer, deck, n)
                if stops:
                    remaining_players.remove(pl)

def dealer_turn(deck, n, card):
    while score(card) < 17:
        card.append(draw_card(deck, n)[0])
        print("the dealer drew",  card[-1])
        print("his score is now", score(card))
        input("...")
    print("the dealer has finished playing")


def initMoney(players):
    v = int(input("How much money does every player start with?  :"))

    money = {}
    for p in players:
        money[p] = v

    print("Each player now has ", v, "$")
    return money


#returns a dictionary with the Bets of each player
def initBets(players, money):
    InitialBets = {}
    for name in players:
        print("Player " + name +": you have", money[name], "$")
        bet_ok = False
        while not bet_ok:
            bet = int(input("How much do you want to bet?"))

            if 0<bet<=money[name]:
               bet_ok = True
            else:
                print("you can't bet this value")
        InitialBets[name] = bet

        
    return InitialBets

#returns a dictionnary with what each player wins after a turn,
#using the function win(score_p, score_d)
def WinAntes(players) :
    InitialAntes = initAntes(players)
    valueWon = {}
    for name in players :
        won = win(score_p, score_d) * InitialAntes[name]
        valuewWon[name] = won
    return valueWon


if __name__ == "__main__":

    pass
