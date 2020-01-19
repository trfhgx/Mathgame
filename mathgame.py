# Game  Project BETA 6.0
import os, random, time, sys, math
from importslx import loadingbar, gamepartystart


def game():
    level = input("Welcome Please choose between easy/medium/hard/impossible : ").lower()
    game_games = float(input("How Many partys do you want : "))
    g = game_games
    choices_forgame = ["-", "+", "*", "/"]
    points = 0
    while 0 < game_games:

        if level.startswith("ea"):
            gl = 1
            number_1 = random.randint(0, 10)
            number_2 = random.randint(1, 10)
        elif level.startswith("me"):
            gl = 3
            number_1 = random.randint(0, 50)
            number_2 = random.randint(1, 50)
            number_3 = random.randint(1, 1000)
            number_4 = random.randint(0, 10)
            number_3 *= number_3
            choices_forgame = ["-", "+", "*", "/", "**", "√"]
        elif level.startswith("ha"):
            gl = 5
            number_1 = random.randint(0, 1100)
            number_2 = random.randint(1, 2500)
            number_3 = random.randint(1, 1000)
            number_4 = random.randint(0, 100)
            number_3 *= number_3
            choices_forgame = ["-", "+", "*", "/", "**", "√"]
        elif level.startswith("im"):
            gl = 10
            number_1 = random.uniform(0, 113000)
            number_2 = random.uniform(1, 215000)
            number_3 = random.randint(1, 1000)
            number_4 = random.randint(0, 1000)
            number_3 *= number_3
            choices_forgame = ["-", "+", "*", "/", "**", "√"]
        else:
            print("?????????")
            game()


        mut = random.choices(choices_forgame)
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
        elif mut == "**":
            x = number_3 ** number_4
        elif mut == "√":
            finalinput = float(input(f"{number_4}{mut}{number_3} = "))
            x = number_4 * math.sqrt(number_3)


        if finalinput == x:
            print("True +")

            points += 1
        else:
            print(f"False - /  {x}")
        game_games -= 1

    iQ = points / g
    FinalIQ = (iQ * 100 * gl * points / g) + 30 + (0.3 * g * gl)
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
        grade = f"S  IQ = {FinalIQ}   Exellent!"

    print(f"You got a {points}/{g} *" + grade)
    Final = input("Type information to see your IQ/level/etc or anything else to finish : ").lower()
    if Final.startswith("inf"):
        print(f"""
        Grade = {grade[1:]} {grade[-10:]}
        Partys = {g}
        Level = {level}
        Points = {points}/{g}
        IQ = {FinalIQ}
        """)
    else:
        Try_again_ = input("Type f to try again or anything else to end or g to save your stats ! ")



gamepartystart()

# Beta 8.0  Levels futures