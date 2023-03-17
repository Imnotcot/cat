import random


class Pet:
    def __init__(self, name):
        self.name = name
        self.water = 50
        self.hungry = 50
        self.xp = 1
        self.notlose = True

    def isnotlose(self):
        if self.hungry < 0:
            print(f'{self.name} is hungry')
            self.notlose = False
        elif self.water < 0:
            print(f'{self.name} is want to drink')
            self.notlose = False
        elif self.xp < 0:
            print(f'{self.name} is lose')
            self.notlose = False
        elif self.xp > 8:
            print(f'{self.name} is win!!!')
            self.notlose = False

    def end_of_day(self):
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
            self.to_hunt()
        else:
            self.shopping()
        print('Stats today:')
        self.end_of_day()
        self.isnotlose()

    def to_hunt(self):
        print('    Let`s to hunt!')
        if random.randint(1, 3) == 1:
            self.hungry += 2
            self.xp += 0.12
            print('    Hunt is complete!')
        else:
            self.hungry -= 2
            print('    Hunt is lose:(')
        self.water -= 2

    def shopping(self):
        print('    Time to shop!')
        if random.randint(1, 2) == 1:
            print('    Let`s shopping food!')
            self.buy_food()
        else:
            print('    Let`s shopping water!')
            self.buy_water()

    def buy_food(self):
        self.xp -= 0.02
        self.hungry += 3

    def buy_water(self):
        self.xp -= 0.02
        self.water += 5


cat = Pet(name='cat')

for day in range(1, 366):
    if cat.notlose:
        cat.live(day=day)
    else:
        end = f'It`s end for {cat.name}'
        print(f"{'':=^50}")
        print(f'{end:^^50}')
        print(f"{'':=^50}")
        break
