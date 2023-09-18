# 1. Напишіть гру "rock-paper-scissors-lizard-Spock". Ввід даних гравцем - ченез input. Рекомендую подумати над такими класами як Player, GameFigure, Game. Памʼятайте про чистоту і простоту коду (DRY, KISS), коментарі та докстрінги.

import random


class Computer:
    def computer_random_number(self):
        return random.randint(1, 5)


class User:
    def cycle_user_input(self):
        max_attempts = 3
        attempts = 0
        while attempts <= max_attempts:
            try:
                user_input = input(
                    'Enter a number from 1 to 5.\nWhere:\n1 - scissors \n2 - paper \n3 - stone \n4 - lizard \n5 - Spock\n ')
                if user_input.isdigit():
                    user_input = int(user_input)
                    if 1 <= user_input <= 5:
                        return user_input
                    else:
                        print ('wrong! enter a number between 1 and 5.')
                        attempts += 1
                else:
                    print ('wrong! Enter a number!')
                attempts += 1
                remaining_attempts = max_attempts - attempts
                print (f"remaining attempts: {remaining_attempts}")
            except ValueError:
                print ("enter a valid number from 1 to 5")
        print ("exceeded maximum attempts")
        exit()


class Game:
    def __init__(self, computer_number, user_number):
        self.computer_number = computer_number
        self.user_number = user_number

    def Rules_of_the_Game(self):
        self.dict_characters = {
            1: ['Scissors'],
            2: ['Paper'],
            3: ['Rock'],
            4: ['Lizard'],
            5: ['Spock']
        }

        self.dict_Game = {
            1: ['2', '4'],
            2: ['3', '5'],
            3: ['4', '1'],
            4: ['5', '2'],
            5: ['1', '3']
        }

        while self.computer_number == self.user_number:
            print ("you and your opponent chose the same numbers. You need to make a choice again.")
            self.computer_number = Computer().computer_random_number()
            self.user_number = User().cycle_user_input()

        for value in self.dict_Game[self.user_number]:
            pass
        if value == str(self.computer_number):
            print (f'victory! your character {self.dict_characters[self.user_number]} defeated{self.dict_characters[self.computer_number]}.')
        else:
            print (f'defeat! your character {self.dict_characters[self.user_number]} was destroyed by an enemy character{self.dict_characters[self.computer_number]}')


computer_1 = Computer()
computer_number = computer_1.computer_random_number()

user_1 = User()
user_number = user_1.cycle_user_input()

game_1 = Game(computer_number=computer_number, user_number=user_number)
game_1.Rules_of_the_Game()
