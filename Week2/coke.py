coins_left = 50
while coins_left > 0:
    print("Amount Due:", coins_left)
    coin = int(input("Insert Coin:"))
    if coin in [5, 10, 25,]:
        coins_left -= coin
change_owed = abs(coins_left)
print("Change Owed:", change_owed)

