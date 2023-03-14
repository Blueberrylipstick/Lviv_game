'''студентів, кавалерів, лотрів, збуїв, батярів та лайдаків'''

class Person:
    def __init__(self, name) -> None:
        self.name = name
        self.description = ''

    def set_description(self, description):
        self.description = description

    def describe(self):
        return f'А тут на воротях в червоних чоботях {self.name} – {self.description}'

class Friend(Person):
    def __init__(self, name) -> None:
        self.inventory = []
        super().__init__(name)

    def set_inventory(self, inventory):
        self.inventory.append(inventory)

    def buy(self):
        things = '\n'.join([elem.name for elem in self.inventory])
        item = input(f'\nЦей добродій може продати от таке:\n{things}\nТо що, купуєм?\n>>>')
        good = [elem for elem in self.inventory if item in elem.name][0]
        return (good.get_cost(), good.get_healing())

    def describe(self):
        return super().describe() + f'Придивись, може зможеш чого прикупити чи обміняти'


class Enemy(Person):
    def __init__(self, name: str, cost: int) -> None:
        self.lives = 1
        self.cost = cost
        self.weapon: Weapon | None = None
        super().__init__(name)

    def fight(self, fight_with):
        if fight_with[1] >= self.lives:
            return (0, self.weapon) #  lives
        return (-1, None)

    def bribe(self):
        return self.cost

    def set_weapon(self, weapon):
        self.weapon = weapon

    def set_lives(self, lives):
        self.lives = lives

    def describe(self):
        return super().describe() + f'\nА от з такими гультіпаками хіба кудаками помахати\nХоча такому і коаійчина не лмшея буде'

class Special_enemy(Enemy):
    def __init__(self, name, cost) -> None:
        self.talk = ''
        super().__init__(name, cost)

    def set_talk(self, phrase):
        self.talk = phrase

    def fight(self, fight_with, gender):
        if gender:
            input(self.talk + "А візьміть но, панюнцю ружечку на пам'ять\n>>>")
            flower = Weapon('ружа-гожа', 2)
            flower.set_damage(3)
            flower.set_description('гарна квітка з гострими колючками')
            return (0, [flower, self.weapon])
        if fight_with[0] >= self.lives:
            return (0, self.weapon) # +-win, lives, trophy
        return (-1, None)


class Street:
    def __init__(self, name: str) -> None:
        self.name = name
        self.description = ''
        self.link = []
        self.character: Person | None = None
        self.item: Belonging | None = None

    def get_details(self):
        links = '\n'.join([f'The {elem[0].name} is {elem[1]}' for elem in self.link])
        print(f'{self.name}\n--------------------\n{self.description}\n{links}')

    def link_room(self, street, link):
        self.link.append([street, link])

    def move(self, command):
        for street, direction in self.link:
            if direction == command:
                return street

    def set_inhabitant(self, character):
        self.character = character

    def get_inhabitant(self):
        return self.character

    def set_description(self, description):
        self.description = description

class Belonging:
    def __init__(self, name, cost) -> None:
        self.name = name
        self.cost = cost
        self.description = ''

    def set_description(self, description):
        self.description = description

    def get_name(self):
        return self.name

    def get_cost(self):
        return self.cost

class Support(Belonging):
    def __init__(self, name, cost) -> None:
        self.healing = 0
        super().__init__(name, cost)

    def set_healing(self, value):
        self.healing = value

    def get_healing(self):
        return self.healing

class Weapon(Belonging):
    def __init__(self, name,cost) -> None:
        self.damage = 0
        super().__init__(name, cost)

    def set_damage(self, value):
        self.damage = value

    def get_damage(self):
        return self.damage

def beginning():
    characters = [('Йосиф', 0), ('Юзя', 1)]#gender (1 - female, 0 - male)
    while 1:
        choice = input(f'Ну, вітання туристам. То як кажеш тебе кличуть?\n1. {characters[0][0]}\n2. {characters[1][0]}\n>>>')
        if int(choice) == 1:
            return characters[0]
        elif int(choice) == 2:
            return characters[1]
        else:
            print('Ану введи щось путнє')

# you can get weapons only from enemies, from friends you can buy support
