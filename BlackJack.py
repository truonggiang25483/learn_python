###BackJack###
from random import *
#User Name#
uname = input("Enter your name:\n")
play = 1
while play == 1:
    #Card Faces#
    cardFace = {
        1:"Ace",
        2:"2",
        3:"3",
        4:"4",
        5:"5",
        6:"6",
        7:"7",
        8:"8",
        9:"9",
        10:"10",
        11:"Jack",
        12:"Queen",
        13:"King"
        }
    #Deal Method#
    def deal():
        return randint(1,13)


    def hand_val(cards):
        val = 0
        for card in cards:
            if 1 < card <= 10:
                val += card
            elif card > 10:
                val += 10

        if 1 in cards  and val + 21:
            return val + 11
        elif 1 in cards:
            return val + 1
        else:
            return val

    def show(name, cards):
        faces = [cardFace[card] for card in cards]
        val = hand_val(cards)
        if val == 21:
            winMsg = "BackJack!!!"
        else:
            winMsg = ""
        print("%s's Hand: %s, %s \nTotal:%s\t %s" %(name, faces[0], faces[1], val, winMsg))

    for name in ("Dealer",uname):
        cards = (deal(),deal())
        show(name, cards)

        if input("Continue?\n") == "yes":
            play = 1
        else:
            play = 0
