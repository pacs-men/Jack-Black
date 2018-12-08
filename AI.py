from fonctions import *
import random
   

#AI with random choice
def rand(cards, dealer,  deck, param):
    return random.choice([True,  False])

#AI that draws cards until a caertain number param is reaced
def stop_nb(cards, dealer, deck,  param):
    if score(cards)>= param:
        return False
    else:
        return True


#AI that know all the remaining cards and calculates probabilities to make the best decision
def prob_bust(cards, dealer, deck,  param):
    # creates a dictionnary linking the values of the cards with the
    # number of cards having this value
    instances = dict([(i, 0) for i in range(1, 11)])
    for c in cards:
        instances[valueCard(c)] += 1
        

    # transfrom the instances dict to probabilities
    probas = dict(instances)
    for p in probas:
        probas[p] = probas[p]/len(cards)

    sc = score(cards)
    reach = 21-sc

    p_bust = 0
    for i in range(reach, 11):
        try:
            
    
        
    

# calculates the expectency of different AI functions using n decks of cards
# over iterations
def prob_win(AI, n, iterations, param = 0):
    deck = initdraw(n)

    wins = 0
    loss = 0
    draws = 0

    for i in range(iterations):

        cards = draw_card(deck, n, 2)
        dealer = draw_card(deck, n)

        while score(cards) < 21 and AI(cards, dealer, deck, param):
            cards.append(draw_card(deck, n)[0])
           
        while score(dealer) < 17:
            dealer.append(draw_card(deck, n)[0])

        result = win(score(cards), score(dealer))

        if result == 2:
            wins += 1
            
        elif result == 1:
            draws += 1
            
        else:
            loss +=1

    return (wins+ 0.5*draws)/iterations

for i in range(1, 22):
    print("For i = ", i, "The expectency is:",prob_win(stop_nb, 1, 10000, i)) 
    
    
    

    
