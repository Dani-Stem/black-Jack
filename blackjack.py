import time 
import random

your_cards = []
dealers_cards = []
down_card = 0
move = ''
your_turn = 1
next_card = 0

print("welcom to BlackJack")
time.sleep(.5)
input("press enter to start")
time.sleep(.5)
print("lets play!")
time.sleep(.5)
print("Shuffling Deck...")
time.sleep(1)
print("The Dealer is ready")
time.sleep(.5)
print("Dealing Cards...")
time.sleep(1)

next_card = random.randint(2, 11)
your_cards.insert(1, next_card)
next_card = random.randint(2, 11)
your_cards.insert(1, next_card)
next_card = random.randint(2, 11)
dealers_cards.insert(1, next_card)
next_card = random.randint(2, 11)
dealers_cards.insert(1, next_card)

print("your cards: " + str(your_cards))
time.sleep(.5)
print("Dealers cards: " + str(dealers_cards[-1]) + ", *")

time.sleep(.5)
down_card = random.randint(2,11)
print("The Dealer place down a card: " + str(down_card))
time.sleep(.5)

for i in your_cards:

    if your_turn == 1:

        move = input("Enter H to hit or S to Stand: ").lower()
        if move == "h":
            next_card = random.randint(2, 11)
            your_cards.insert(1, next_card)
            print(your_cards)
            cards_total = sum(your_cards)
            time.sleep(.5)
            if cards_total > 21:
                print(cards_total)
                print("you lose..")
                time.sleep(.5)
                break
            else: 
                move = "N"
            move = "N"
            your_turn = 0
            
        elif move == "s":
            your_turn = 0
            move = "N"
        else:
            print("Invalid Input, please try again.")
            time.sleep(.5)

    else: 
        time.sleep(.5)
        print("Dealers move...")
        time.sleep(.5)
        next_card = random.randint(2, 11)
        dealers_cards.insert(1, next_card)
        print("Dealers cards: " + str(dealers_cards[:-1]) + ", *")
        cards_total = sum(dealers_cards)
        if cards_total > 21:
            time.sleep(.5)
            print("Dealer exceeded 21..")
            time.sleep(.5)
            print("You win!")
            time.sleep(.5)
            break
        else:
            your_turn = 1
            move = 'N'






