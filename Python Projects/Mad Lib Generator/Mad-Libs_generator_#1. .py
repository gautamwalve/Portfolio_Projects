
word_1  = input("What you wish to your lover before going to bed: ")
word_2 = input("life wanes at what age : ")
word_3 = input("After dark comes the : ")
word_4 = input("After Light comes the: ")
word_5 = input("Your wife is always ___: ")
word_6 = input("Where there is thunder, there is__ ")

#Displays the story based on the user input

text =( """\n\n\n\n Guess the Poem :)

Do not go gentle into that {word_1},{word_2} should burn and rave at close of day;
Rage, rage against the dying of the {word_3}.
\nThough wise men at their end know {word_4} is {word_5},
\nBecause their words had forked no {word_6} they
\nDo not go gentle into that {word_1} """).format(word_1=word_1,word_2=word_2,word_3=word_3,word_4=word_4,word_5=word_5,word_6=word_6)

print(text)
