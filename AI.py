from fonctions import *
import random
   
import matplotlib.pyplot as plt


#AI with random choice
def rand(cards, dealer,  deck, param):
    return random.choice([True,  False])


# RANDOM AI that a param probablity of stopping at each turn
def rand_param(cards, dealer,  deck, param):
    r = random.random()
    if r>param:
        return True
    else:
        return False

#AI that draws cards until a caertain number param is reached
def stop_nb(cards, dealer, deck,  param):
    if score(cards)>= param:
        return False
    else:
        return True

#semi random AI whose probability of drawing is determined with its distance to 21
def rand_dist_21(cards, dealer, deck,  param):
    dist = 21 - score(cards)
    r = random.random()*21
    if r>dist:
        return False
    else:
        return True

    
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


def compare_AI(iterations):
    ls_AI = [(rand, 0), (rand_param, 1), (stop_nb, 17), (rand_dist_21, 0)]

    probs = []
    for AI in ls_AI:
        probs.append(prob_win(AI[0], 1, iterations, AI[1]))

    I = list(range(4))
    plt.bar(I, height = probs)
    plt.xticks(I, ["rand", "rand_param", "stop_nb", "rand_dist_21"])

    plt.ylabel("probability of winning")
    plt.xlabel("AI")
    plt.show()


def compare_val_stop_nb(iterations):

    I = []
    prob = []
    for i in range(1, 22):
        I.append(i)
        prob.append(prob_win(stop_nb, 1, 10000, i))
        print("For i = ", i, "The expectency is:",prob[-1])


    plt.bar(I, height = prob)
    plt.xticks(I, I)

    plt.ylabel("probability of winning")
    plt.xlabel("number at which the AI stops")
    plt.show()



def compare_val_rand_param(iterations):
    
    I = []
    prob = []
    for i in range(0, 11):
        I.append(i)
        prob.append(prob_win(rand_param, 1, 10000, i/10))
        print("For i = ", i/10, "The expectency is:",prob[-1])


    plt.bar(I, height = prob)
    plt.xticks(I, I)

    plt.ylabel("probability of winning")
    plt.xlabel("probability of stopping at each turn")
    plt.show()

    

    
