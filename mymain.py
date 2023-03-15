import mygame


rynok = mygame.Street('Площа Ринок')
rynok.set_description('Тут, біля музею скла, все почнеться. З цього серця Львова можна дістатись до будь-якої вулиці')
kopalnya = mygame.Street('Копальня кави')
kopalnya.set_description('Місцк, проппахле кавою, де Юрія Кульчицького постає перед очима')
virmenska = mygame.Street('Вірменська вулиця')
virmenska.set_description('Центральна вулиця Вірменського району')
svobody = mygame.Street('Проспект свободи')
svobody.set_description('Центральна вулиця Львова, одна з найкрасивіших і найпрестижніших у місті, епіцентр ділового й культурного життя.')
krakivska = mygame.Street('Вултця Краківська')
krakivska.set_description('Малекький куточок Польщі у Львові')
drykarska = mygame.Street('Вулиця Друкарська')
drykarska.set_description('Цікаво, що ж ховає ця вулиця')
halytska = mygame.Street('Вулиця Галицька')
halytska.set_description('Вулиця, що виникла на давньому торговельному шляху, що провадив до Галича й був продовженням дороги, що вела з Волині')
rynok.link_room(kopalnya, '1')
rynok.link_room(virmenska, '2')
rynok.link_room(svobody, '3')
rynok.link_room(krakivska, '4')
rynok.link_room(drykarska, '5')
rynok.link_room(halytska, '6')
kopalnya.link_room(rynok, '1')
virmenska.link_room(rynok, '1')
svobody.link_room(rynok, '1')
krakivska.link_room(rynok, '1')
drykarska.link_room(rynok, '1')
halytska.link_room(rynok, '1')
krakivska.link_room(virmenska, '2')
virmenska.link_room(krakivska, '2')
kopalnya.link_room(svobody, '2')
svobody.link_room(kopalnya, '2')
streets = [rynok, virmenska, krakivska, drykarska, halytska]

student = mygame.Friend('спудей Захарій')
student.set_description('Хлопець хоч гроша за душею не має, але вгостить любого\n')
bread = mygame.Support('Хліб зі смальцем', 2)
bread.set_description('Смачне, ще й корисне')
bread.set_healing(1)
student.set_inventory(bread)
svobody.set_inhabitant(student)

fists = mygame.Weapon('кулаки', 0)
fists.set_damage(2)
fists.set_description('Зброя, дана від народження')

laydak = mygame.Friend('лайдака')
laydak.set_description('Хоч гроша за душею не має, але вгостить любого\n')
armor = mygame.Support('Шкіряні рукавичкиб', 3)
armor.set_healing(3)
armor.set_description('Ну потерті трохи, і що')
laydak.set_inventory(armor)
kopalnya.set_inhabitant(laydak)


kavaler = mygame.Special_enemy('Кавалєр', 5)
kavaler.set_description('Чоловік, який розважає жінку в товаристві, супроводить її під час прогулянки тощо\n')
kavaler.set_lives(1)
stick = mygame.Weapon('Дрючок', 2)
stick.set_damage(3)
stick.set_description('палиця з дерева, все просо і красиво')
kavaler.set_weapon(stick)
kavaler.set_talk('Завжди до послуг файниз панянок')
krakivska.set_inhabitant(kavaler)

batyar = mygame.Special_enemy('Батяр', 7)
batyar.set_description('Популярний у жінок брутальний чоловік кінця 19-початку 20 століття\n')
batyar.set_lives(3)
charisma = mygame.Weapon('харизма', 3)
charisma.set_description('Ну і як від такого встояти')
charisma.set_damage(6)
batyar.set_weapon(charisma)
batyar.set_talk('Ой а хто тут такий забрів\n>>>')
virmenska.set_inhabitant(batyar)


lotr = mygame.Enemy('Лотр', 3)
lotr.set_description('Той ще фацет\n')
lotr.set_lives(2)
glass = mygame.Weapon('склянка', 2)
glass.set_damage(4)
glass.set_description('просто склянка, зате як летить')
lotr.set_weapon(glass)
halytska.set_inhabitant(lotr)


zbuj = mygame.Enemy('Збуй', 1)
zbuj.set_description('Розбійник, грабіжник\n')
zbuj.set_lives(5)
kolt = mygame.Weapon('револьвер', 8)
kolt.set_description('нц кольт це ж класика...')
kolt.set_damage(9)
zbuj.set_weapon(kolt)
drykarska.set_inhabitant(zbuj)


name, gender = mygame.beginning()
backpack = [(fists.name, fists.damage)]
money = 5
health = (3 if gender else 4)
current_location = rynok

while health:
    print('\n')
    current_location.get_details()

    inhabitant = current_location.get_inhabitant()
    if inhabitant is not None:
        print(inhabitant.describe())

    command = input('>>>')
    if command == 'битися':
        print('\n'.join([elem[0] for elem in backpack]))
        if inhabitant is not None:
            if isinstance(inhabitant, mygame.Enemy) and not isinstance(inhabitant, mygame.Special_enemy):
                fight_with = input('Ну і чим битись будем?\n>>>')
                if fight_with in [elem[0] for elem in backpack]:
                    damage = [val[1] for val in backpack if val[0] == fight_with][0]
                    res = inhabitant.fight((fight_with, damage))
                    health += res[0]
                    weapon = res[1]
                    if weapon:
                        backpack.append((weapon.get_name(), weapon.get_damage()))
                        current_location.set_inhabitant(None)
                        print('А ти диви, перемогли!')
                    else:
                        print(f"Та то перед тим, як кулаками махати маєш покумекати!\nТепер у тебе {health} балів здоров'я\nА може задобрити?")
                        if health == 0:
                            health += mygame.death()
                            if health != 0:
                                continue
                            print('Не кожен ж день свято. Але ви приїздіть, приїздіть, раптом пощастить наступного разу')
                        answer = input('>>>')
                        cost = inhabitant.bribe()
                        if money < cost and answer == 'так':
                            print(f'Ти думажш я, лтвівський {inhabitant.name} ся продам за таку копійчину?! Біжи поки цілий і на очі не попадайся, бо Біг ми Боже...')
                        elif money >= cost and answer == 'так':
                            money -= cost
                            current_location.set_inhabitant(None)
                            print('А ти диви, перемогли!')
                        else:
                            continue
                else:
                    print('А нема ' + fight_with)

            elif isinstance(inhabitant, mygame.Special_enemy):
                fight_with = input('Ну і чим битись будем?\n>>>')
                if fight_with in [elem[0] for elem in backpack]:
                    damage = [val[1] for val in backpack if val[0] == fight_with]
                    res = inhabitant.fight((fight_with, damage), gender)
                    health += res[0]
                    weapon = res[1]
                    if weapon:
                        for elem in weapon:
                            if elem:
                                backpack.append((elem.name, elem.damage))
                        current_location.set_inhabitant(None)
                        print('А ти диви, перемогли!')
                    else:
                        print(f"Та то перед тим, як кулаками махати маєш покумекати!\nТепер у тебе {health} балів здоров'я\nА може задобрити?")
                        if health == 0:
                            health += mygame.death()
                            if health != 0:
                                continue
                            print('Не кожен ж день свято. Але ви приїздіть, приїздіть, раптом пощастить наступного разу')
                        answer = input('>>>')
                        cost = inhabitant.bribe()
                        if health == 0:
                            print('Ну, не коден ж день святом має бути. Але ти приїзди іншим разом, може вийде')
                        if money < cost and answer == 'так':
                            print(f'Ти думажш я, лтвівський {inhabitant.name} ся продам за таку копійчину?! Біжи поки цілий і на очі не попадайся, бо Біг ми Боже...')
                        elif money >= cost and answer == 'так':
                            money -= cost
                            current_location.set_inhabitant(None)
                            print('А ти диви, перемогли!')
                        else:
                            continue
                else:
                    print('А нема' + fight_with)
        else:
            print('Радість моя, досить зі слупом балакати! Ніц тута нікого нема')
    elif command == ('гешефт'):
        choice = input('Куплятимеш чи продаш?\n>>>')
        if choice == 'купити':
            item = inhabitant.buy()
            health += item[1]
            # backpack.append(item.get_name())
            money -= item[0]
            print(f"Вітаю, тепер твоє здоров'я = {health}\nУ тебе залишилось{money} монет")
        elif choice == 'продати':
            print('\n'.join([elem[0] for elem in backpack]))
            value = input('То що з цього продаси?\n>>>')
            item = [elem for elem in backpack if elem[0] == value]
            backpack = [elem for elem in backpack if elem[0] != value]
            money += 3
            print(f'А тепер у тебе {money} монет')
        else:
            print(f'Йой, а що то таке {choice}? Як то робити')
    elif int(command) in [*range(7)]:
        current_location = current_location.move(command)
    else:
        print(f'Йой, а що то таке {command}? Як то робити')

    if not any(street.get_inhabitant() for street in streets):
        print('Мої вітання, всіх перемогли.\nТепер гайда на Високий Замок то святкувати')
        break

