print("Welcome to the quiz")
player = input("DO you want to play? ")
if player != "yes":
    quit()
print(" Okay! Let's play")

Qustion1 = input("What is the full meaning of GUI?")
if Qustion1 == "Graphical User Interface":
    print("Correct!")
else:
    print("Wrong")

Qustion2 = input("What is the meaning of the word RAM?")
if Qustion2 == "Random Access Memory":
    print("Correct!")
else:
    print("Wrong")

Qustion3 = input("What was the year that Apple released the first-ever iPhone?")
if Qustion3 == "2007":
    print("Correct!")
else:
    print("Wrong")

if Qustion1 == "Graphical User Interface" and Qustion2 == "Random Access Memory" and Qustion3 == "2007":
    print("YOU WIN!")
else:
    print("YOU LOOSE")