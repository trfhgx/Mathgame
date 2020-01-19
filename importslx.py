import os, random, time, sys, math


def loadingbar():
    for i in range(21):
        sys.stdout.write('\r')
        # the exact output you're looking for:
        sys.stdout.write("[%-20s] %d%%" % ('=' * i, 5 * i))
        sys.stdout.flush()
        time.sleep(0.15)


def gamepartystart():
    from mathgame import game
    print("Hi Player Please wait to connect you to the game !")
    loadingbar()
    print(" \n Done")
    game()
