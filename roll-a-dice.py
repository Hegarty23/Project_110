import random
response = "y" 
while response == "y":
    no = random.randint(1, 6)
    if no == 1:
        print("You got a one(1), loser")
    if no == 2:
        print("You rolled a two(2). Meh")
    if no == 3:
        print("You got a three(3) oof, not good or bad")
    if no == 4:
        print("You got a four(4). Decent roll")
    if no == 5:
        print("You rolled a five(5). Soooo close to six(6).")
    if no == 6:
        print("You rolled a six(6). Yeesss, you get good luck for a week.")
    response = input("press y to roll again and n to exit ")
    print("\n")