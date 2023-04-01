import random


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


    def n_asking(self):
        self.f_asking = input('Введіть клавіши для контролю: ')
        self.__msquat1(press_q=self.f_asking == 'q')
        self.__keys_to_move(press_key=self.f_asking)
        self.__another_keys(press_key=self.f_asking)

    def __msquat1(self, press_q):
        if press_q:
            self.fsquat = not self.fsquat

        if self.fsquat:
            self.fast = 0.5
        else:
            self.fast = 1

    def __keys_to_move(self, press_key):
        if self.fast == 0.5:
            print('Ви у присіді')
        if press_key == 'w':
            self.move(move_by_y=1)
        elif press_key == 's':
            self.move(move_by_y=-1)
        elif press_key == 'a':
            self.move(move_by_x=-1)
        elif press_key == 'd':
            self.move(move_by_x=1)

    def __another_keys(self, press_key):
        if press_key == 'k':
            print(f'Ваші кординати: x - {self.x}, y - {self.y}')
        elif press_key == '1':
            veleus = ''
            for i in range(10):
                veleus += f'{list(system.dict_with_enemy.values())[i][0]}, {list(system.dict_with_enemy.values())[i][1]}'
                if i != 9:
                    veleus += '; '
                else:
                    veleus += '.'
            print(f'Список кординат enemys`: {veleus}')
        elif press_key == '3':
            veleus = ''
            for i in range(10):
                veleus += f'{list(system.dict_with_structure.values())[i][0]}, {list(system.dict_with_structure.values())[i][1]}'
                if i != 9:
                    veleus += '; '
                else:
                    veleus += '.'
            print(f'Список кординат структур: {veleus}')



#================================================================================


class Enemys(Object, Walking):
    def __init__(self):
        super().__init__()
        global system
        self.fast = 1
        if list(system.dict_with_enemy) == []: #Я пробував if list(dict_with_enemy): але це не спрацювало
            self.NAME = 'enemy1'
        else:
            self.NAME = 'enemy' + str(int(list(system.dict_with_enemy)[-1][-1]) + 1)

        system.dict_with_enemy.update([(self.NAME, [self.x, self.y])])

    def moving(self):
        self.move(random.randint(-1, 1), random.randint(-1, 1))
        system.dict_with_enemy.update([(self.NAME, [self.x, self.y])])


#================================================================================


class Structures(Object): #Структури відрізняються від Enemy тим що вони не можуть ходити як Enemy й тому вони належить тілько до Object
    def __init__(self):
        super().__init__()
        if list(system.dict_with_structure) == []:
            self.name = 'structure1'
        else:
            self.name = 'structure' + str(int(list(system.dict_with_structure)[-1][-1]) + 1)

        system.dict_with_structure.update([(self.name, [self.x, self.y])])
        self.name = None


#================================================================================

class System:
    def __init__(self):
        self.dict_with_enemy = {}
        self.list_with_enemy = []
        self.dict_with_structure = {}
        self.list_with_structure = []
        self.list_with_text = []
        for i in range(25):
            self.list_with_text.append({'x': None, 'y': None, 'objects': [' ']})


    def create(self):
        self.player = Player()
        for i in range(10):
            self.list_with_enemy.append(None)
            self.list_with_enemy[i] = Enemys()

        for i in range(10):
            self.list_with_structure.append(None)
            self.list_with_structure[i] = Structures()


    def game_loop(self):
        print('Керування за допомогою букв wasd й q щоб присісти або навпаки.')
        print('Щоб побачити свої кординати натисніть k.')
        print('Щоб побачити кординати об`єктів з ім`ям enemy натисніть 1.')
        print('Щоб побачити список кординат з структурами натисніть 3.')
        input('Натисніть Enter щоб продовжити.')
        while 1:
            for element in self.list_with_enemy:
                element.moving()
            self.player.n_asking()
            if self.player.f_asking == 'e':
                print('Game stop!')
                break
            self.create_field()
            self.__printing()

    def create_field(self):
        x = -2
        y = 2
        for i in range(25):
            self.list_with_text[i]['x'] = self.player.x + x
            self.list_with_text[i]['y'] = self.player.y + y
            if x == 2:
                x = -2
                y -= 1
            else:
                x += 1

    def __printing(self):
        for i in range(25):
            if self.list_with_text[i]['x'] == self.player.x and self.list_with_text[i]['y'] == self.player.y:
                if self.list_with_text[i]['objects'] == [' ']:
                    self.list_with_text[i]['objects'] = []
                self.list_with_text[i]['objects'].append('P')
            for i1 in range(10):
                if self.list_with_text[i]['x'] == list(self.dict_with_enemy.values())[i1][0] and self.list_with_text[i]['y'] == list(self.dict_with_enemy.values())[i1][1]:
                    if self.list_with_text[i]['objects'] == [' ']:
                        self.list_with_text[i]['objects'] = []
                    self.list_with_text[i]['objects'].append('E')
                    break
            for i1 in range(10):
                if self.list_with_text[i]['x'] == list(self.dict_with_structure.values())[i1][0] and self.list_with_text[i]['y'] == list(self.dict_with_structure.values())[i1][1]:
                    if self.list_with_text[i]['objects'] == [' ']:
                        self.list_with_text[i]['objects'] = []
                    self.list_with_text[i]['objects'].append('S')
                    break

        zminna = 0
        zminna2 = ''
        for i in range(5):
            veluses = 0
            for i1 in range(5):
                if len(self.list_with_text[i + i1 * 5]['objects']) > veluses:
                    veluses = len(self.list_with_text[i +i1 * 5]['objects'])
            for i1 in range(5):
                while veluses > len(self.list_with_text[i + i1 * 5]['objects']):
                    self.list_with_text[i + i1 * 5]['objects'].append(' ')


        for i in range(25):
            zminna2 += str(self.list_with_text[i]['objects'])
            zminna += 1
            if zminna == 5:
                zminna = 0
                print(zminna2)
                zminna2 = ''

        self.list_with_text.clear()
        for i in range(25):
            self.list_with_text.append({'x': None, 'y': None, 'objects': [' ']})


system = System()
system.create()
system.game_loop()

