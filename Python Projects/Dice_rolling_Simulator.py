import random

x= "y"

while x =="y":    
#"""#Generate a random number  #between  1 and 6 (including both 1 and 6)"""
    no = random.randint(1,6)
    
    if  no == 1:
        print("[           ]")
        print("[     0    ]")
        print("[           ]")
    elif no == 2:
        print("[ 0         ]")
        print("[            ]")
        print("[         0 ]")
    elif no == 3:
        print("[ 0         ]")
        print("[     0     ]")
        print("[         0 ]")
    elif no == 4:
        print("[ 0      0 ]")
        print("[            ]")
        print("[ 0      0 ]")
    elif no == 5:
        print("[ 0      0 ]")
        print("[     0     ]")
        print("[ 0      0 ]")
    elif no == 6:
        print("[ 0      0 ]")
        print("[ 0      0 ]")
        print("[ 0      0 ]")
    
    x = input("press y to roll again and n to exit: ")
    print("\n")
