# Game  Project BETA 2.0
import os, random, time, sys

def loadingbar():
    for i in range(21):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
        sys.stdout.flush()
        time.sleep(0.15)


def gamepartystart():
    print("Hi Player Please wait to connect you to the game !")
    loadingbar()
    print(" \n Done")
    game()

def game():
    level = input("Welcome Please choose between easy/meduim/hard : ")
    game_games = int(input("How Many partys do you want : "))
    g = game_games
    choices_forgame = ["-", "+", "*", "/"]
    points = 0
    while 0 < game_games:
        number_1 = random.randint(0,10)
        mut = random.choices(choices_forgame)
        number_2 = random.randint(1,10)
        mut = ' '.join([str(elem) for elem in mut])

        finalinput = float(input(f"{number_1} {mut} {number_2} = "))
        if mut == "-":
            x = number_1 - number_2
        elif mut == "+":
             x = number_1 + number_2
        elif mut == "*":
             x = number_1 * number_2
        elif mut == "/":
             x = number_1 / number_2
        if finalinput == x:

            print("True +")

            points += 1
        else:
            print("False -")
        game_games -= 1

    iQ = points / g
    FinalIQ = (iQ * 100 * points / g) + 30 + (0.3 * g)
    if iQ < 0.3:
        grade = f"F  IQ = {FinalIQ}   Awful"
    elif iQ < 0.5 and iQ >= 0.3:
        grade = f"E  IQ = {FinalIQ}    Bad"
    elif iQ < 0.6 and iQ >= 0.5:
        grade = f"D  IQ = {FinalIQ}   Not bad"
    elif iQ < 0.7 and iQ >= 0.6:
        grade = f"C  IQ = {FinalIQ}   Pretty good"
    elif iQ < 0.9 and iQ >= 0.7:
        grade = f"B  IQ = {FinalIQ}   Good"
    elif iQ >= 0.9 and iQ < 1:
        grade = f"A  IQ = {FinalIQ}   Great!"
    else:
        grade = f"S  IQ = {(iQ * 100 * points / g) + 30 + (0.3 * g)}   Exellent!"

    print(f"You got a {points}/{g} *" + grade)
    Final = input("Type information to see your IQ/level/etc or anything else to finish : ")
    if Final.startswith("inf".lower()):
        print(f"""
        Grade = {grade[1:]} {grade[-10:]}
        Partys = {g}
        Level = {level}
        Points = {points}/{g}
        IQ = "---"
        
        """)
    else:
        Try_again_ = input(" ----------------------------------- ")
    print(FinalIQ)





gamepartystart()

# Beta 3.0 Better performance / Less code / Better Choosing / Levels futures  soon on beta 6.0 ! 
