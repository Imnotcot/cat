import random
from random import randint

class Functions:
    def not_secret(self, num1, num2):
        self.__num1 = num1
        self.__num2 = num2
        self.__secret_shto_to(self.__num1, self.__num2)

    def __secret_shto_to(self, number1, number2):
        n = randint(1, 4)
        if n == 1:
            print(number1 + number2)
        elif n == 2:
            print(number1 - number2)
        elif n == 3:
            print(number1 * number2)
        else:
            print(number1 / number2)

object1 = Functions()
object1.not_secret(int(input('Ведіть число одие')), int(input('Ведіть число два')))