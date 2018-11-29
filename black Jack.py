from fonctions import *

blackJack = """
$$$$$$$\  $$\                     $$\                $$$$$\                     $$\       
$$  __$$\ $$ |                    $$ |               \__$$ |                    $$ |      
$$ |  $$ |$$ | $$$$$$\   $$$$$$$\ $$ |  $$\             $$ | $$$$$$\   $$$$$$$\ $$ |  $$\ 
$$$$$$$\ |$$ | \____$$\ $$  _____|$$ | $$  |            $$ | \____$$\ $$  _____|$$ | $$  |
$$  __$$\ $$ | $$$$$$$ |$$ /      $$$$$$  /       $$\   $$ | $$$$$$$ |$$ /      $$$$$$  / 
$$ |  $$ |$$ |$$  __$$ |$$ |      $$  _$$<        $$ |  $$ |$$  __$$ |$$ |      $$  _$$<  
$$$$$$$  |$$ |\$$$$$$$ |\$$$$$$$\ $$ | \$$\       \$$$$$$  |\$$$$$$$ |\$$$$$$$\ $$ | \$$\ 
\_______/ \__| \_______| \_______|\__|  \__|       \______/  \_______| \_______|\__|  \__|

"""


"""
Rules Used:

Players: there is n players each against the dealer

Start:
Every players bets a sum of money
each player gets two cards the dealer gets one
all of the cards coming from the same deck made from c neck of 56 cards
(if the deck runs out of cards another new deck is created and used)

Round:
- every player has the choice to draw another card or to stop
(the player is autommatically stopped if his score is superior to 21)
- and then another round starts with the players who are still in the game

score compting:
the score of each player is automatically calculated with the most
advantagous value for him (aces)
End:
once every player finished playing:
-the dealer starts playing and draws cards until his score his superior or equal to 17
For each player:
-if his score is 21 he gets twice his bet
-if his score is superior to the dealer's score while inferior to 21
 he wins twice his bet
-if his score is equal to the dealer's he gets his bat back
-if his score is smallers than the dealer's or superior to 21 he loses his bet
 
"""



print(blackJack)
print()
print("Game of Black Jack")
nPlayers = int(input("How many players? :"))
players = initJoueurs(nPlayers)
n = int(input("How many decks of 56 cards do you want to play with? :"))


continue_playing = True

deck = initdraw(n)

while continue_playing:
    cards = premierTour(players, deck, n)

    dealer = draw_card(deck, n)
        
    complete_players(players, cards, dealer, deck, n)

    dealer_turn(deck, n, card)

    for p in players:
        print("")
        
    continue_playing = ("y"== input("do you want to continue playing (y, n)"))

print("good bye")


    



    




#colors = ["♣", "♦", "♥", "♠"]



