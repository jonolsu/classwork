import random

import time

from actors import Wizard, Creature, SmallAnimal, Dragon


def main():
    print_header()
    game_loop()


def print_header():
    print('-------------------------------------')
    print('       Wizard Game App')
    print('-------------------------------------')
    print()


def game_loop():
    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 20, scaliness=20, breaths_fire=True),
        Wizard('Evil Wizard', 100)
    ]

    hero = Wizard('Gandolf', 75)

    done = False
    while not done:
        active_creature = random.choice(creatures)
        print('A {} of level {} appears from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()
        cmd = input('Do you [a]ttack, [r]un away, or [l]ook around? ')
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print("The wizard {} runs and hides, taking time to recover...".format(hero.name))
                time.sleep(5)
                print("The wizard {} returns revitalized!".format(hero.name))
        elif cmd == 'r':
            print('The wizard {} becomes unsure of his power and flees.'.format(hero.name))
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:',format(hero.name))
            for c in creatures:
                print(' * A {} of level {}'.format(c.name, c.level))
        else:
            print("ok, exiting game ... bye!")
            done = True

        if not(creatures):
            print("You defeated all the creatures.")
            done = True


if __name__ == '__main__':
    main()
