RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9",
         "10", "J", "Q", "K"]
SUITS = ["c", "d", "h", "s"]
def __init__(self, rank, suit, face_up = True):
 self.rank = rank
 self.suit = suit
 self.is_face_up = face_up
import random as rd

print("Welcome to the world's simplest game!\n")

again = None
while again != "n":
    players = []
    num = int(input("How many players? (2 - 5): "))
    for i in range(num):
        name = input("Player name: ")
        score = rd.randrange(100) + 1
        player = (name, score)
        players.append(player)

    print("\nhere are the game results:")
    for player in players:
        print(player)

    again = input("\nDo you want to play again? (y/n): ")

input("\n\nPress the enter key to exit.") 
