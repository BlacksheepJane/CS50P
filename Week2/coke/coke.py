cents = 50
while cents > 0:
    print("Amount Due:", cents)
    s = int(input("Insert Coin: "))
    if s in [5, 10, 25]:
        cents -= s
print("Change Owed:", -cents)
