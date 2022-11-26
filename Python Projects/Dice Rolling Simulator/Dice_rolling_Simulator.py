import random
x = "y"
while x == "y":
    x = random.randint(1,6)
    if x == 1:
        print("[0 _ _ _ _ _ ]")
    elif x == 2:
        print("[0 _ _ _ _ 0 ]")
    elif x == 3:
        print("[0 _ 0 _ _ 0 ]")
    elif x == 4:
        print("[0 0 _ _ 0 0 ]")
    elif x == 5:
        print("[0 0 0 _ 0 0 ]")
    elif x == 6:
        print("[0 0 0 0 0 0 ]")
    x = input("press y to roll again and n to exit:")
