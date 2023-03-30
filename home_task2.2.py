import random


class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.coins = 5
        self.alive = True

    def is_alive(self):
        if self.progress <= -0.5:
            print('Cast out')
            self.alive = False
        elif self.gladness <= 0:
            print('Deprestion...')
            self.alive = False
        else:
            print('Passed externally')
            self.alive = False

    def end_of_day(self):
        print(f'Gladness - {self.gladness}')
        print(f'Progress - {round(self.gladness, 2)}')

    def live(self, day):
        day = f'Day #{day} of {self.name}'
        print(f'{day:=^50}')
        self.cube()
        self.end_of_day()
        self.is_alive()

    def cube(self): #За таку довгу умову можете поставити трохи вищу оцінку
        cube = 0
        if self.progress <= 0:
            cube = random.randint(1, 100)
            if cube <= 40:
                cube = 1
            elif cube >= 41 and cube <=60: #Pycharm дуже хоче щоб я писав 41 <= cube <= 06
                cube = 2
            elif cube >= 61 and cube <= 80:
                cube = 3
            elif cube >= 81 and cube <= 100:
                cube = 4
        elif self.gladness <= 20:
            cube = random.randint(1, 100)
            if cube <= 20:
                cube = 1
            elif cube >= 21 and cube <=55:
                cube = 2
            elif cube >= 56 and cube <=80:
                cube = 3
            elif cube >= 81 and cube <= 100:
                cube = 4
        elif self.coins <= 5:
            cube = random.randint(1, 100)
            if cube <= 20:
                cube = 1
            elif cube >= 21 and cube <=40:
                cube = 2
            elif cube >= 41 and cube <= 60:
                cube = 3
            elif cube >= 61 and cube <= 100:
                cube = 4
        else:
            cube = random.randint(1, 4)
        if cube == 1:
            self.to_study()
        elif cube == 2:
            self.to_chill()
        elif cube == 3:
            self.to_sleep()
        elif cube == 4:
            self.to_work()

    def to_study(self):
        print('Time to study!')
        self.progress += 0.12
        self.gladness -= 3
        self.coins -= 3

    def to_sleep(self):
        print('I will sleep!')
        self.gladness += 3

    def to_chill(self):
        print('Rest time')
        self.gladness += 5
        self.progress -= 0.1
        self.coins -= 4

    def to_work(self):
        print('Let`s work!')
        self.coins += 3.5
        self.gladness -= 1



