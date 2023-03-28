import random


class Pet:
    def __init__(self, name,
                 minusxp=0.2, buywater=5, buyfood=3,
                 persentofwinhunt=3, hunthungry=2, huntwater=2):

        self.name = name #Ім'я тваринки
        self.water = 50 #Вода
        self.hungry = 50 #Їжа
        self.xp = 1 #Прогрес

        self.minusxp = minusxp #Скільки буде знімати прогресу за покупку
        self.persentofwinhunt = persentofwinhunt #Який вірогідність вдачної охоти
        self.buywater = buywater #Скільки прибовляється води за покупку
        self.buyfood = buyfood #Скільки прибовляється їжі за покупку
        self.hunthungry = hunthungry #Скільки прибовляється або віднімається їжі при вдачному або навпаки полюванні
        self.huntwater = huntwater #Скільки приболяється або віднімається води при вдачному або навпаки полюванні

        self.notendofgame = True #Чи настав кінець гри

    def __isnotlose(self):
        if self.hungry < 0:
            print(f'{self.name} is hungry')
            self.notendofgame = False
        elif self.water < 0:
            print(f'{self.name} is want to drink')
            self.notendofgame = False
        elif self.xp < 0:
            print(f'{self.name} is lose')
            self.notendofgame = False
        elif self.xp > 8:
            print(f'{self.name} is win!!!')
            self.notendofgame = False

    def __end_of_day(self):
        if self.hungry > 100:
            self.hungry = 100
        elif self.water > 100:
            self.water = 100
        print(f'    Hungry - {self.hungry}')
        print(f'    Water - {self.water}')
        print(f'    Xp - {round(self.xp, 2)}')

    def live(self, day):
        day = f'Day #{day} of {self.name} life!'
        print(f'{day:=^50}')
        print('Do today:')
        cube = random.randint(1, 2)
        if cube == 1:
            self.__to_hunt()
        else:
            self.__shopping()
        print('Stats today:')
        self.__end_of_day()
        self.__isnotlose()

    def __to_hunt(self):
        print('    Let`s to hunt!')
        if random.randint(1, self.persentofwinhunt) == 1:
            self.hungry += self.hunthungry
            self.xp += 0.12
            print('    Hunt is complete!')
        else:
            self.hungry -= self.hunthungry
            print('    Hunt is lose:(')
        self.water -= self.huntwater

    def __shopping(self):
        print('    Time to shop!')
        if random.randint(1, 2) == 1:
            print('    Let`s shopping food!')
            self.__buy_food()
        else:
            print('    Let`s shopping water!')
            self.__buy_water()

    def __buy_food(self):
        self.xp -= self.minusxp
        self.hungry += self.buyfood

    def __buy_water(self):
        self.xp -= self.minusxp
        self.water += self.buywater


cat = Pet(name='cat')

for day in range(1, 366):
    if cat.notendofgame:
        cat.live(day=day)
    else:
        end = f'It`s end for {cat.name}'
        print(f"{'':=^50}")
        print(f'{end:^^50}')
        print(f"{'':=^50}")
        break
