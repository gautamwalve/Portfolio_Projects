
def scene1():
    import time
    print(
    """
    WELCOME TO THE ADVENTURE GAME !
    Let's start the game !\n
    
    Lily wakes up in her bedroom in the middle of the night .\n She Heard
    a loud "BANG" outside the house. Now she has two choices\n
    1. She can either stay in the room [STAY]
    2. She can check what the sound might be[CHECK]\n\n

    [STAY] or [CHECK] 
    """)
    c1= input( )
    time.sleep(2)
    ans = 'incorrect'
    while (ans=='incorrect'):
        if(c1.upper()=='STAY'):
            print("\n Lily decides to stay in the room and ends up staying inside forever as none seems to come to help her")
            ans = 'correct'
        elif(c1.upper()=='CHECK'):
            print("Lily exits the room silently and reaches the main hall.")
            ans = 'correct'
            scene2()
        else:
            print("Enter the correct choice! Stay or Check")
            c1 = input()
            
def scene2() :
    import time
    
    print("""
            In the main hall, she find a strange but cute teddy bear on the floor\n
            She wanted to pick the teddy up.
            But should she?, It doesn't belong to her.(^_^)
            Type your choice: [PICK] or [IGNORE]
            """)
    time.sleep(2)
    c1=input()
    ans = 'incorrect'
    while(ans=='incorrect'):
        if (c1.upper()=="PICK"):
            print("""description
            """
            "\nThe moment Lily picked up the teddy bear. The Teddy bear starts TALKING!. The Bear tells Lily that she is in grave danger, as there is a monster in the house. And the monster has captured her Parents as well! But he hugged her and told her not to get scared as he knows how to beat the monster. """)
            time.sleep(2)
            print("""
                \n The Bear handed Lily a magical potion which can weaken the monster and make him run away! He handed her the potion and then DISAPPEARED ! Lily moved forward.
                """)
            ans = 'correct'
            pick = 'True'
        elif(c1.upper() == 'IGNORE'):
            print("""\nLily decided not to pick up the bear and walked forward """)
            ans = 'correct'
            pick = "False"
        else:
            print("Wrong input! Enter Pick or ignore")
            c1=input()
            time.sleep(2)
            scene3(pick)
            
def scene3(pick_value):
        import time
        print(""" 
            \n\nAfter walking for a while, Lily saw the MONSTER in front of her !
            It had red eyes and evil looks. She got very scared               """)
        time.sleep(2)
        if (pick_value == "True"):
            time.sleep(2)
            print("""
            \nBut then she remembered !. She had the magic portion and she threw it on the monster,\n Well, She had nothing to lose!
            """)
            time.sleep(2)
            print("\n The Monster SCREAMED in pain but he managed to make a portal and pushed Lily to a new world!")
        elif(pick_value =="False"):
            print("The Monster attached Lily and hurt her!, She was then thrown to the new world by the monster! ")
scene1()
print("\n\n")
print("===============END OF CHAPTER 1================================================================")