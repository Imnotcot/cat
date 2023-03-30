import random


class Human:
    def __init__(self, name='Human',
                 job=None,
                 home=None,
                 car=None):
        self.name = name
        self.job = job
        self.home = home
        self.car = car

        self.gladness = 50
        self.saity = 50
        self.money = 100

    def get_home(self):
        pass

    def get_car(self):
        pass

    def get_job(self):
        pass

    def eat(self):
        pass

    def work(self):
        pass

    def get_shopping(self, manage):
        pass

    def chill(self):
        pass

    def clean_home(self):
        pass

    def to_repair(self):
        pass

    def dat_indexes(self, day):
        pass

    def is_alife(self):
        pass

    def life(self, day):
        pass


class Auto:
    def __init__(self, brand_dict):
        self.brand = random.choice(list(brand_dict))
        self.fuel = brand_dict[self.brand]['fuel']
        self.strength = brand_dict[self.brand]['strength']
        self.consumption = brand_dict[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.consumption -= self.consumption
            self.strength -= 1
            return True
        else:
            print('car cannot drive')
            return False


class House:
    def __init__(self):
        self.food = 0
        self.mess = 0


brands_of_car = {
    'BMW': {
        'fuel': 100,
        'strength': 60,
        'consumption': 15
    },
    'Audi': {
            'fuel': 90,
            'strength': 75,
            'consumption': 11
        },
    'Deo': {
            'fuel': 100,
            'strength': 50,
            'consumption': 7
        },
    'Moskvich': {
            'fuel': 100,
            'strength': 10,
            'consumption': 20
        }
}
