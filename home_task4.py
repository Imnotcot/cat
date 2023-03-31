import random

dict_with_enemy = {}
list_with_enemy = []
dict_with_structure = {}
list_with_structure = []


class Object:
    def __init__(self):
        super().__init__()
        self.y = random.randint(-10, 10)
        self.x = random.randint(-10, 10)

#================================================================================

class Walking:
    def __init__(self):
        self.fast = 1

    def move(self, move_by_x=0, move_by_y=0):
            self._move_by_x(move_by_x)
            self._move_by_y(move_by_y)

    def _move_by_x(self, direct):
        self.x += direct*self.fast

    def _move_by_y(self, direct):
        self.y += direct*self.fast

#================================================================================

class Player(Object, Walking):
    def __init__(self):
        super().__init__()
        self.fsquat = False
        for i in range(10):
            list_with_enemy.append(None)
            list_with_enemy[i] = Enemys()

        for i in range(10):
            list_with_structure.append(None)
            list_with_structure[i] = Structures()


    def asking(self):
        asking = input(f'Wasd for walk, and q for squat: ')
        self.__msquat1(press_q=asking == 'q')
        self.__keys_to_move(press_key=asking)
        self.__printing()

    def __msquat1(self, press_q):
        if press_q:
            self.fsquat = not self.fsquat

        if self.fsquat:
            self.fast = 0.5
        else:
            self.fast = 1

    def __keys_to_move(self, press_key):
        if press_key == 'w':
            self.move(move_by_y=1)
        elif press_key == 's':
            self.move(move_by_y=-1)
        elif press_key == 'a':
            self.move(move_by_x=-1)
        elif press_key == 'd':
            self.move(move_by_x=1)

    def __printing(self):
        print(f'My x in {self.x}, and my y in {self.y}')
        print(f'{"":=^100}')
        for i in range(10):
            print(f'Hi! I`m friendly enemy and my name is {list(dict_with_enemy)[i]},'
                  f' My x is {dict_with_enemy["enemy" + str(i+1)][0]},'
                  f'my y is {dict_with_enemy["enemy" + str(i+1)][1]}')
        print(f'{"":=^100}')
        for i1 in range(10):
            print(f'Hi! I`m structure and my name is {list(dict_with_structure)[i1]},'
                  f' My x is {dict_with_structure["structure" + str(i1+1)][0]},'
                  f'my y is {dict_with_structure["structure" + str(i1+1)][1]}')


#================================================================================


class Enemys(Object, Walking):
    def __init__(self):
        super().__init__()
        self.fast = 1

        if list(dict_with_enemy) == []: #Я пробував if list(dict_with_enemy): але це не спрацювало
            self.NAME = 'enemy1'
        else:
            self.NAME = 'enemy' + str(int(list(dict_with_enemy)[-1][-1]) + 1)

        dict_with_enemy.update([(self.NAME, [self.x, self.y])])

    def moving(self):
        self.move(random.randint(-1, 1), random.randint(-1, 1))
        dict_with_enemy.update([(self.NAME, [self.x, self.y])])


#================================================================================


class Structures(Object): #Структури відрізняються від Enemy тим що вони не можуть ходити як Enemy й тому вони належить тілько до Object
    def __init__(self):
        super().__init__()
        if list(dict_with_structure) == []:
            self.name = 'structure1'
        else:
            self.name = 'structure' + str(int(list(dict_with_structure)[-1][-1]) + 1)

        dict_with_structure.update([(self.name, [self.x, self.y])])
        self.name = None


player = Player()
print('Керування за допомогою букв wasd й q щоб присісти або навпаки')
while 1:
    for i in range(10):
        list_with_enemy[i].moving()
    player.asking()
