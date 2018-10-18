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

def draw_card()

if __name__ == "__main__":
    print(initdraw(1))
    

