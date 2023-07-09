import random
print("Trò Chơi Búa Kéo Bao ")
Player1 = ""
while True:
    Player = str(input("Mời bạn nhập vào tương ứng búa, kéo, bao:  "))
    Player = Player.upper()
    if Player != "BÚA" and Player != "BUA" and Player != "KÉO" and Player != "KEO" and Player != "BAO":
        print("Vui Lòng nhập đúng định dạng !!!")
    else:
        Player1 = Player
        break
Player2 = random.randint(1, 3)
#SỐ 1 TƯƠNG ỨNG VỚI BÚA.
#SỐ 2 TƯƠNG ỨNG VỚI KÉO.
#SỐ 3 TƯƠNG ỨNG VỚI BAO.
if Player1 == "BÚA" or Player1 == "BUA":
    if Player2 == 1:
        print("Đối Thủ cũng ra Búa. Hòa")
    elif Player2 == 2:
        print("Đối thủ ra Kéo. Bạn đã thắng")
    elif Player2 == 3:
        print("Đối thủ ra Bao. Bạn đã thua")
elif Player1 == "KÉO" or Player1 == "KEO":
    if Player2 == 1:
        print("Đối Thủ ra Búa. Bạn đã thua")
    elif Player2 == 2:
        print("Đối thủ cũng ra Kéo. Hòa")
    elif Player2 == 3:
        print("Đối thủ ra Bao. Bạn đã thắng")
elif Player1 == "BAO":
    if Player2 == 1:
        print("Đối Thủ cũng ra Búa. Bạn đã thắng")
    elif Player2 == 2:
        print("Đối thủ ra Kéo. Bạn đã Thua")
    elif Player2 == 3:
        print("Đối thủ cũng ra Bao. Hòa")