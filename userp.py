from random import randint

game_running = True


def cal_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


while game_running == True:
    new_round = True
    player = {'name': 'abc', 'attack': 12, 'health': 100, 'heal': 16}
    monster = {'name': 'attacker', 'attack_min': 15, 'attack_max': 35, 'health': 100}
    print('----' * 9)
    print('enter your partner')
    player['name'] = input()

    print('----' * 9)

    print(player['name'] + ' has ' + str(player['health']) + '  health')
    print(monster['name'] + ' has ' + str(monster['health']) + '  health')
    while new_round == True:
        player_won = False
        monster_won = False

        print('----' * 9)

        print('please select your option')
        print('1:attack')
        print('2:heal')
        print('3:exit game')

        player_choice = input()
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

            print(monster['health'])
            print(player['health'])

        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            monster_attack = randint(monster['attack_min'], monster['attack_max'])

            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

            if player['health'] <= 0:
                monster_won = True

                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True




        elif player_choice == '3 ':
            new_round = False
            game_running = False

        else:
            print('invalid option')

        if player_won == False and monster_won == False:
            print(player['name'] + 'has' + str(player['health']) + ' left')
            print(monster['name'] + 'has' + str(monster['health']) + ' left')
        elif player_won:
            print(player['name'] + ' won')
            new_round = False
        elif monster_won:
            print(' you lost')
            new_round = False

from random import randint

game_running = True


def cal_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


while game_running == True:
    new_round = True
    player = {'name': 'abc', 'attack': 12, 'health': 100, 'heal': 16}
    monster = {'name': 'attacker', 'attack_min': 15, 'attack_max': 35, 'health': 100}
    print('----' * 9)
    print('enter your partner')
    player['name'] = input()

    print('----' * 9)

    print(player['name'] + ' has ' + str(player['health']) + '  health')
    print(monster['name'] + ' has ' + str(monster['health']) + '  health')
    while new_round == True:
        player_won = False
        monster_won = False

        print('----' * 9)

        print('please select your option')
        print('1:attack')
        print('2:heal')
        print('3:exit game')

        player_choice = input()
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

            print(monster['health'])
            print(player['health'])

        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            monster_attack = randint(monster['attack_min'], monster['attack_max'])

            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

            if player['health'] <= 0:
                monster_won = True

                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True




        elif player_choice == '3 ':
            new_round = False
            game_running = False

        else:
            print('invalid option')

        if player_won == False and monster_won == False:
            print(player['name'] + 'has' + str(player['health']) + ' left')
            print(monster['name'] + 'has' + str(monster['health']) + ' left')
        elif player_won:
            print(player['name'] + ' won')
            new_round = False
        elif monster_won:
            print(' you lost')
            new_round = False

from random import randint

game_running = True


def cal_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


while game_running == True:
    new_round = True
    player = {'name': 'abc', 'attack': 12, 'health': 100, 'heal': 16}
    monster = {'name': 'attacker', 'attack_min': 15, 'attack_max': 35, 'health': 100}
    print('----' * 9)
    print('enter your partner')
    player['name'] = input()

    print('----' * 9)

    print(player['name'] + ' has ' + str(player['health']) + '  health')
    print(monster['name'] + ' has ' + str(monster['health']) + '  health')
    while new_round == True:
        player_won = False
        monster_won = False

        print('----' * 9)

        print('please select your option')
        print('1:attack')
        print('2:heal')
        print('3:exit game')

        player_choice = input()
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

            print(monster['health'])
            print(player['health'])

        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            monster_attack = randint(monster['attack_min'], monster['attack_max'])

            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

            if player['health'] <= 0:
                monster_won = True

                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True




        elif player_choice == '3 ':
            new_round = False
            game_running = False

        else:
            print('invalid option')

        if player_won == False and monster_won == False:
            print(player['name'] + 'has' + str(player['health']) + ' left')
            print(monster['name'] + 'has' + str(monster['health']) + ' left')
        elif player_won:
            print(player['name'] + ' won')
            new_round = False
        elif monster_won:
            print(' you lost')
            new_round = False

from random import randint

game_running = True


def cal_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


while game_running == True:
    new_round = True
    player = {'name': 'abc', 'attack': 12, 'health': 100, 'heal': 16}
    monster = {'name': 'attacker', 'attack_min': 15, 'attack_max': 35, 'health': 100}
    print('----' * 9)
    print('enter your partner')
    player['name'] = input()

    print('----' * 9)

    print(player['name'] + ' has ' + str(player['health']) + '  health')
    print(monster['name'] + ' has ' + str(monster['health']) + '  health')
    while new_round == True:
        player_won = False
        monster_won = False

        print('----' * 9)

        print('please select your option')
        print('1:attack')
        print('2:heal')
        print('3:exit game')

        player_choice = input()
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

            print(monster['health'])
            print(player['health'])

        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            monster_attack = randint(monster['attack_min'], monster['attack_max'])

            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

            if player['health'] <= 0:
                monster_won = True

                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True




        elif player_choice == '3 ':
            new_round = False
            game_running = False

        else:
            print('invalid option')

        if player_won == False and monster_won == False:
            print(player['name'] + 'has' + str(player['health']) + ' left')
            print(monster['name'] + 'has' + str(monster['health']) + ' left')
        elif player_won:
            print(player['name'] + ' won')
            new_round = False
        elif monster_won:
            print(' you lost')
            new_round = False

from random import randint

game_running = True


def cal_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


while game_running == True:
    new_round = True
    player = {'name': 'abc', 'attack': 12, 'health': 100, 'heal': 16}
    monster = {'name': 'attacker', 'attack_min': 15, 'attack_max': 35, 'health': 100}
    print('----' * 9)
    print('enter your partner')
    player['name'] = input()

    print('----' * 9)

    print(player['name'] + ' has ' + str(player['health']) + '  health')
    print(monster['name'] + ' has ' + str(monster['health']) + '  health')
    while new_round == True:
        player_won = False
        monster_won = False

        print('----' * 9)

        print('please select your option')
        print('1:attack')
        print('2:heal')
        print('3:exit game')

        player_choice = input()
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

            print(monster['health'])
            print(player['health'])

        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            monster_attack = randint(monster['attack_min'], monster['attack_max'])

            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

            if player['health'] <= 0:
                monster_won = True

                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True




        elif player_choice == '3 ':
            new_round = False
            game_running = False

        else:
            print('invalid option')

        if player_won == False and monster_won == False:
            print(player['name'] + 'has' + str(player['health']) + ' left')
            print(monster['name'] + 'has' + str(monster['health']) + ' left')
        elif player_won:
            print(player['name'] + ' won')
            new_round = False
        elif monster_won:
            print(' you lost')
            new_round = False

from random import randint

game_running = True


def cal_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


while game_running == True:
    new_round = True
    player = {'name': 'abc', 'attack': 12, 'health': 100, 'heal': 16}
    monster = {'name': 'attacker', 'attack_min': 15, 'attack_max': 35, 'health': 100}
    print('----' * 9)
    print('enter your partner')
    player['name'] = input()

    print('----' * 9)

    print(player['name'] + ' has ' + str(player['health']) + '  health')
    print(monster['name'] + ' has ' + str(monster['health']) + '  health')
    while new_round == True:
        player_won = False
        monster_won = False

        print('----' * 9)

        print('please select your option')
        print('1:attack')
        print('2:heal')
        print('3:exit game')

        player_choice = input()
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

            print(monster['health'])
            print(player['health'])

        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            monster_attack = randint(monster['attack_min'], monster['attack_max'])

            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

            if player['health'] <= 0:
                monster_won = True

                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True




        elif player_choice == '3 ':
            new_round = False
            game_running = False

        else:
            print('invalid option')

        if player_won == False and monster_won == False:
            print(player['name'] + 'has' + str(player['health']) + ' left')
            print(monster['name'] + 'has' + str(monster['health']) + ' left')
        elif player_won:
            print(player['name'] + ' won')
            new_round = False
        elif monster_won:
            print(' you lost')
            new_round = False

from random import randint

game_running = True


def cal_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


while game_running == True:
    new_round = True
    player = {'name': 'abc', 'attack': 12, 'health': 100, 'heal': 16}
    monster = {'name': 'attacker', 'attack_min': 15, 'attack_max': 35, 'health': 100}
    print('----' * 9)
    print('enter your partner')
    player['name'] = input()

    print('----' * 9)

    print(player['name'] + ' has ' + str(player['health']) + '  health')
    print(monster['name'] + ' has ' + str(monster['health']) + '  health')
    while new_round == True:
        player_won = False
        monster_won = False

        print('----' * 9)

        print('please select your option')
        print('1:attack')
        print('2:heal')
        print('3:exit game')

        player_choice = input()
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

            print(monster['health'])
            print(player['health'])

        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            monster_attack = randint(monster['attack_min'], monster['attack_max'])

            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

            if player['health'] <= 0:
                monster_won = True

                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True




        elif player_choice == '3 ':
            new_round = False
            game_running = False

        else:
            print('invalid option')

        if player_won == False and monster_won == False:
            print(player['name'] + 'has' + str(player['health']) + ' left')
            print(monster['name'] + 'has' + str(monster['health']) + ' left')
        elif player_won:
            print(player['name'] + ' won')
            new_round = False
        elif monster_won:
            print(' you lost')
            new_round = False

from random import randint

game_running = True


def cal_monster_attack():
    return randint(monster['attack_min'], monster['attack_max'])


while game_running == True:
    new_round = True
    player = {'name': 'abc', 'attack': 12, 'health': 100, 'heal': 16}
    monster = {'name': 'attacker', 'attack_min': 15, 'attack_max': 35, 'health': 100}
    print('----' * 9)
    print('enter your partner')
    player['name'] = input()

    print('----' * 9)

    print(player['name'] + ' has ' + str(player['health']) + '  health')
    print(monster['name'] + ' has ' + str(monster['health']) + '  health')
    while new_round == True:
        player_won = False
        monster_won = False

        print('----' * 9)

        print('please select your option')
        print('1:attack')
        print('2:heal')
        print('3:exit game')

        player_choice = input()
        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            else:
                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True

            print(monster['health'])
            print(player['health'])

        elif player_choice == '2':
            player['health'] = player['health'] + player['health']
            monster_attack = randint(monster['attack_min'], monster['attack_max'])

            player['health'] = player['health'] - monster_attack
            if player['health'] <= 0:
                monster_won = True

            if player['health'] <= 0:
                monster_won = True

                player['health'] = player['health'] - cal_monster_attack()
                if player['health'] <= 0:
                    monster_won = True




        elif player_choice == '3 ':
            new_round = False
            game_running = False

        else:
            print('invalid option')

        if player_won == False and monster_won == False:
            print(player['name'] + 'has' + str(player['health']) + ' left')
            print(monster['name'] + 'has' + str(monster['health']) + ' left')
        elif player_won:
            print(player['name'] + ' won')
            new_round = False
        elif monster_won:
            print(' you lost')
            new_round = False

