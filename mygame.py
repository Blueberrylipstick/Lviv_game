'''Module with classes for the game'''

class Person:
    '''
    class to describe person in general
    '''
    def __init__(self, name) -> None:
        """Initialization

        Args:
            name (str): name
        """
        self.name = name
        self.description = ''

    def set_description(self, description):
        """Function to set one's description

        Args:
            description (str): description
        """
        self.description = description

    def describe(self):
        """Function to describe a person

        Returns:
            str: description
        """
        return f'А тут на воротях в червоних чоботях {self.name} – {self.description}'

class Friend(Person):
    '''class to describe subclass of Person'''
    def __init__(self, name) -> None:
        """Initialization

        Args:
            name (str): name
        """
        self.inventory = []
        super().__init__(name)

    def set_inventory(self, inventory):
        """Function to add an item to the inventory

        Args:
            inventory (Support | Weapon): item to add to the inventory
        """
        self.inventory.append(inventory)

    def buy(self) -> tuple:
        """Function to buy smth from a friend

        Returns:
            tuple: cost and healing of an item
        """
        things = '\n'.join([elem.name for elem in self.inventory])
        item = input(f'\nЦей добродій може продати от таке:\n{things}\nТо що, купуєм?\n>>>')
        good = [elem for elem in self.inventory if item in elem.name][0]
        return (good.get_cost(), good.get_healing())

    def describe(self):
        """Function to describe a person

        Returns:
            str: description
        """
        return super().describe() + f'Придивись, може зможеш чого прикупити чи обміняти'


class Enemy(Person):
    '''class to describe subclass of Person'''
    def __init__(self, name: str, cost: int) -> None:
        """Initialization

        Args:
            name (str): name
            cost (int): cost of a weapon
        """
        self.lives = 1
        self.cost = cost
        self.weapon: Weapon | None = None
        super().__init__(name)

    def fight(self, fight_with):
        """Function to run a fight

        Args:
            fight_with (tuple): name and power of a weapon

        Returns:
            tuple: num of life to subtract from player and a trophy weapon
        """
        if fight_with[1] >= self.lives:
            return (0, self.weapon) #  lives
        return (-1, None)

    def bribe(self):
        """Function to bribe an enemy

        Returns:
            int: how much money you spend to bribe him
        """
        return self.cost

    def set_weapon(self, weapon):
        """Function to set a weapon for an enemy

        Args:
            weapon (Weapon): weapon
        """
        self.weapon = weapon

    def set_lives(self, lives):
        """Function to set lives of an NPC

        Args:
            lives (int): lives of an NPC
        """
        self.lives = lives

    def describe(self):
        """Function to describe a person

        Returns:
            str: description
        """
        return super().describe() + f'\nА от з такими гультіпаками хіба кудаками помахати\nХоча такому і коаійчина не лмшея буде'

class Special_enemy(Enemy):
    '''subclass of an enemy'''
    def __init__(self, name, cost) -> None:
        """Initialization

        Args:
            name (_type_): _description_
            cost (_type_): _description_
        """
        self.talk = ''
        super().__init__(name, cost)

    def set_talk(self, phrase):
        """Function to set character's speech

        Args:
            phrase (str): character's speech
        """
        self.talk = phrase

    def fight(self, fight_with, gender):
        """Function to run a fight

        Args:
            fight_with (tuple): name and strength of the weapon
            gender (int): gender of the player

        Returns:
            tuple: num of life to subtract from player and a trophy weapon
        """
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
    '''class to decribe a street'''
    def __init__(self, name: str) -> None:
        """Initialization

        Args:
            name (str): street's name
        """
        self.name = name
        self.description = ''
        self.link = []
        self.character: Person | None = None
        self.item: Belonging | None = None

    def get_details(self) -> str:
        """Function to get description

        Returns:
            str: description
        """
        links = '\n'.join([f'The {elem[0].name} is {elem[1]}' for elem in self.link])
        print(f'{self.name}\n--------------------\n{self.description}\n{links}')

    def link_room(self, street, link):
        """Function to link a street to others

        Args:
            street (name): linked street's name
            link (int): direction
        """
        self.link.append([street, link])

    def move(self, command):
        """Function to relocate character to another room

        Args:
            command (str): direction to the next room

        Returns:
            str: name of the next room
        """
        for street, direction in self.link:
            if direction == command:
                return street

    def set_inhabitant(self, character):
        """Function to set an inhabitant of the a street

        Args:
            character (_type_): _description_
        """
        self.character = character

    def get_inhabitant(self):
        """Function to get inhabitant of the street

        Returns:
            Enemy | Friend: inhabitant
        """
        return self.character

    def set_description(self, description):
        """Function to set street's description

        Args:
            description (str): _description_
        """
        self.description = description

class Belonging:
    '''class to describe belonging'''    
    def __init__(self, name, cost) -> None:
        """Initialization

        Args:
            name (str: name
            cost (int): cost of an item
        """
        self.name = name
        self.cost = cost
        self.description = ''

    def set_description(self, description):
        """Function to get description

        Args:
            description (str): _description_
        """
        self.description = description

    def get_name(self):
        """Function to get item's name

        Returns:
            str: name
        """
        return self.name

    def get_cost(self):
        """Function to get item's cost

        Returns:
            int: cost
        """
        return self.cost

class Support(Belonging):
    '''subclass of item'''    
    def __init__(self, name, cost) -> None:
        """Initialization

        Args:
            name (str): name
            cost (int): cost
        """
        self.healing = 0
        super().__init__(name, cost)

    def set_healing(self, value):
        """Function to srt support item's healing

        Args:
            value (int): healing points
        """
        self.healing = value

    def get_healing(self):
        """Function to get healing points of an item

        Returns:
            int: healing points
        """
        return self.healing

class Weapon(Belonging):
    '''subclass of belonging'''
    def __init__(self, name,cost) -> None:
        """Initialization

        Args:
            name (str): name
            cost (int): cost
        """
        self.damage = 0
        super().__init__(name, cost)

    def set_damage(self, value):
        """Function to set damage

        Args:
            value (int): damage points of the weapon
        """
        self.damage = value

    def get_damage(self):
        """Function to get item's damage points

        Returns:
            int: damage points
        """
        return self.damage

def beginning():
    """Function to begin a game

    Returns:
        int: 1 for girl, 0 for boy
    """
    characters = [('Йосиф', 0), ('Юзя', 1)]#gender (1 - female, 0 - male)
    while 1:
        choice = input(f'Ну, вітання туристам. То як кажеш тебе кличуть?\n1. {characters[0][0]}\n2. {characters[1][0]}\n>>>')
        if int(choice) == 1:
            return characters[0]
        elif int(choice) == 2:
            return characters[1]
        else:
            print('Ану введи щось путнє')
