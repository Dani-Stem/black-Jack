# import time 
# import random

# your_cards = []
# dealers_cards = []
# down_card = 0
# move = ''
# your_turn = 1
# next_card = 0

# print("welcom to BlackJack")
# time.sleep(.5)
# input("press enter to start")
# time.sleep(.5)
# print("lets play!")
# time.sleep(.5)
# print("Shuffling Deck...")
# time.sleep(1)
# print("The Dealer is ready")
# time.sleep(.5)
# print("Dealing Cards...")
# time.sleep(1)

# next_card = random.randint(2, 11)
# your_cards.insert(1, next_card)
# next_card = random.randint(2, 11)
# your_cards.insert(1, next_card)
# next_card = random.randint(2, 11)
# dealers_cards.insert(1, next_card)
# next_card = random.randint(2, 11)
# dealers_cards.insert(1, next_card)

# print("your cards: " + str(your_cards))
# time.sleep(.5)
# print("Dealers cards: " + str(dealers_cards[-1]) + ", *")

# time.sleep(.5)
# down_card = random.randint(2,11)
# print("The Dealer place down a card: " + str(down_card))
# time.sleep(.5)

# for i in your_cards:

#     if your_turn == 1:

#         move = input("Enter H to hit or S to Stand: ").lower()
#         if move == "h":
#             next_card = random.randint(2, 11)
#             your_cards.insert(1, next_card)
#             print(your_cards)
#             cards_total = sum(your_cards)
#             time.sleep(.5)
#             if cards_total > 21:
#                 print(cards_total)
#                 print("you lose..")
#                 time.sleep(.5)
#                 break
#             else: 
#                 move = "N"
#             move = "N"
#             your_turn = 0
            
#         elif move == "s":
#             your_turn = 0
#             move = "N"
#         else:
#             print("Invalid Input, please try again.")
#             time.sleep(.5)

#     else: 
#         time.sleep(.5)
#         print("Dealers move...")
#         time.sleep(.5)
#         next_card = random.randint(2, 11)
#         dealers_cards.insert(1, next_card)
#         print("Dealers cards: " + str(dealers_cards[:-1]) + ", *")
#         cards_total = sum(dealers_cards)
#         if cards_total > 21:
#             time.sleep(.5)
#             print("Dealer exceeded 21..")
#             time.sleep(.5)
#             print("You win!")
#             time.sleep(.5)
#             break
#         else:
#             your_turn = 1
#             move = 'N'

import pygame
import random

# Initialize Pygame and fonts
pygame.init()
pygame.font.init()
font = pygame.font.SysFont(None, 30)


# Screen Configuration
WIDTH, HEIGHT = 900, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Black Jack")

# Colors
GREEN = (34, 139, 34)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
CARD_BACK_COLOR = (50, 100, 200)

# Card Dimensions
CARD_WIDTH = 100
CARD_HEIGHT = 145

# Varaibles 
your_turn = 1

class Card:
    def __init__(self, suit, value):
        self.suit = suit          # 'Hearts', 'Diamonds', 'Clubs', 'Spades'
        self.value = value        # '2' through '10', 'J', 'Q', 'K', 'A'
        self.is_face_up = True   # Toggle visibility state
        
        # Assign colors based on suit
        self.color = RED if suit in ['Hearts', 'Diamonds'] else BLACK
        
        # Set up fonts for rendering text labels
        self.font = pygame.font.SysFont('Arial', 24, bold=True)
        self.suit_symbols = {'Hearts': '♥', 'Diamonds': '♦', 'Clubs': '♣', 'Spades': '♠'}

    def draw(self, surface, x, y):
        # 1. Base Card Outline & Background
        card_rect = pygame.Rect(x, y, CARD_WIDTH, CARD_HEIGHT)
        pygame.draw.rect(surface, WHITE, card_rect, border_radius=8)
        pygame.draw.rect(surface, BLACK, card_rect, width=2, border_radius=8)
        
        if self.is_face_up:
            # 2. Draw Text Details (Value and Suit symbol)
            symbol = self.suit_symbols[self.suit]
            text_surface = self.font.render(f"{self.value}{symbol}", True, self.color)
            
            # Position text in top-left and bottom-right corners
            surface.blit(text_surface, (x + 8, y + 8))
            
            # Flipped version or lower corner text
            lower_text = self.font.render(f"{self.value}", True, self.color)
            surface.blit(lower_text, (x + CARD_WIDTH - 25, y + CARD_HEIGHT - 35))
        else:
            # Draw Card Back Design
            inner_rect = card_rect.inflate(-12, -12)
            pygame.draw.rect(surface, CARD_BACK_COLOR, inner_rect, border_radius=5)

class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        # Create full 52 card deck via nested loop
        self.cards = [Card(suit, val) for suit in suits for val in values]

    def shuffle(self):
        random.shuffle(self.cards)

    def draw_deck_pile(self, surface, x, y):
        # Draw overlapping cards to look like a thick deck pile
        for i in range(min(len(self.cards), 5)):
            offset_x = x + (i * 2)
            offset_y = y - (i * 2)
            
            # Simple card back placeholder for the main deck pile
            rect = pygame.Rect(offset_x, offset_y, CARD_WIDTH, CARD_HEIGHT)
            pygame.draw.rect(surface, WHITE, rect, border_radius=8)
            pygame.draw.rect(surface, CARD_BACK_COLOR, rect.inflate(-10, -10), border_radius=5)
            pygame.draw.rect(surface, BLACK, rect, width=2, border_radius=8)

# Core Setup
deck = Deck()
deck.shuffle()

# Deal a test your_hand of cards to display side by side
down_card = [deck.cards.pop() for _ in range(1)]

# Deal a test your_hand of cards to display side by side
your_hand = [deck.cards.pop() for _ in range(2)]

# Deal a test dealer_hand of cards to display side by side
dealer_hand = [deck.cards.pop() for _ in range(1)]

# Deal a test dealer_hand of cards to display side by side
dealer_hidden_card = [deck.cards.pop() for _ in range(1)]

# Main Game Loop
running = True
clock = pygame.time.Clock()

# Define the exact deck box for click detection
DECK_RECT = pygame.Rect(100, 250, CARD_WIDTH, CARD_HEIGHT)

def draw_text(surface, text, font, color, x, y):
    text_surface = font.render(text, True, color)
    surface.blit(text_surface, (x, y))


while running:
    # 1. Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Click the deck to add a new card 
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            # Check if user clicked the static deck position and deck has cards left
            if DECK_RECT.collidepoint(mx, my) and len(deck.cards) > 0:
                # pop() returns a single Card object directly instead of a list
                new_card = deck.cards.pop() 
                your_hand.append(new_card)
    
    # 2. Drawing pipeline (Moved OUTSIDE the event loop)
    screen.fill(GREEN)  # Draw poker table background
    
    # Draw remaining main deck pile on left
    deck.draw_deck_pile(screen, 35, 230)

    # Draw dealt down_card spread horizontally on right
    for i, card in enumerate(down_card):
        start_x = 155 + (i * (CARD_WIDTH + 15))  # 15px gap spacing
        start_y = 220
        card.draw(screen, start_x, start_y)
    
    # Draw dealt your_hand spread horizontally on right
    for i, card in enumerate(your_hand):
        start_x = 200 + (i * (CARD_WIDTH + 15))  # 15px gap spacing
        start_y = 425
        card.draw(screen, start_x, start_y)

    # Draw dealt dealer_hand spread horizontally on right
    for i, card in enumerate(dealer_hand):
        start_x = 315 + (i * (CARD_WIDTH + 15))  # 15px gap spacing
        start_y = 30
        card.draw(screen, start_x, start_y)

    # Draw dealt dealer_hidden_card spread horizontally on right
    for i, card in enumerate(dealer_hidden_card):
        start_x = 200 + (i * (CARD_WIDTH + 15))  # 15px gap spacing
        start_y = 30
        card.is_face_up = False
        card.draw(screen, start_x, start_y)

    draw_text(screen, "Dealers Hand", font, (255, 255, 255), 30, 50)    
    draw_text(screen, "Your Hand", font, (255, 255, 255), 50, 440)
    if your_turn == 1:
        draw_text(screen, "Its your move. Press H to hit or S to stand", font, (255, 255, 255), 290, 280)

        
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
