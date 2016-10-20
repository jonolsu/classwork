import os
import random
import time
import colorama
import sys


class Game:
    def __init__(self):
        self.history = []
        self.plays = [
            (colorama.Fore.RED + colorama.Back.WHITE + 'Red', 'r'),
            (colorama.Fore.YELLOW + colorama.Back.WHITE + 'Yellow', 'y'),
            (colorama.Fore.GREEN + colorama.Back.WHITE + 'Green', 'g'),
            (colorama.Fore.BLUE + colorama.Back.WHITE + 'Blue', 'b')
        ]
        colorama.init()
        print(colorama.Back.WHITE)

    def show_level(self):
        self.clear()
        for h in self.history:
            print(h[0], end='  ')
            sys.stdout.flush()
            time.sleep(1)

        self.clear()

    def add_move(self):
        self.history.append(random.choice(self.plays))

    def test_player(self):
        print(colorama.Fore.MAGENTA + "{} moves:".format(len(self.history)))
        for t,v in self.history:
            guess = input("Next [r,g,b,y]: ")
            if guess != v:
                print(colorama.Fore.WHITE + colorama.Back.BLACK)
                self.clear()
                return False
        return True


    def clear(self):
        if (sys.platform == 'win32'):
            os.system('cls')
        else:
            os.system('clear')
            # better way is to check OS to call appropriate command
