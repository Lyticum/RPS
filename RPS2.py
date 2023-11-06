import random
from enum import Enum
import sys

game_count= 0
win_count=0
lose_count=0
draw_count=0

class RPS(Enum):
    Taş = 2
    Kağıt = 3
    Makas = 1

def RPS1():
    print(" ")
    player = int(input("Makas için 1 \nTaş için 2\nKağıt için 3'e basın\n\n"))

    if player not in [1, 2, 3]:
        print("Lütfen anlamlı bir sayı giriniz!")
        return RPS1()

    computer = int(random.choice("123"))
    print(computer)

    print(f"{str(RPS(player)).replace("RPS.", "").title()} seçtiniz!")
    print(f"{str(RPS(computer)).replace("RPS.", "").title()} seçti!")
    def winner (player, computer):
        if player == 1 and computer == 2:
            print("Kaybettiniz!")
            global lose_count
            lose_count += 1
        elif player == 2 and computer == 1:
            print("Kazandınız!")
            global win_count
            win_count += 1
        elif player == 1 and computer == 3:
            print("Kazandınız!")
            win_count
            win_count += 1
        elif player == 3 and computer == 1:
            print("Kaybettiniz!")
            lose_count
            lose_count += 1
        elif player == 2 and computer == 3:
            print("Kaybettiniz!")
            lose_count
            lose_count += 1
        elif player == 3 and computer == 2:
            print("Kazandınız!")
            win_count
            win_count += 1
        elif player == computer:
            print("Berabere")
            global draw_count
            draw_count += 1
    result = winner(player, computer)
    title="scoreboard"
    print(title.upper().center(20, "="))
    global game_count
    game_count += 1
    print(f"Oyun Sayisi; {str (game_count)}")
    print(f"Kazanılan Oyun Sayisi; {str (win_count)}")
    print(f"Kaybedilen Oyun Sayisi; {str (lose_count)}")
    print(f"Berabere Oyun Sayisi; {str (draw_count)}")
    return RPS1()

if __name__ == "__main__":
    TKM =RPS1()
    TKM()
