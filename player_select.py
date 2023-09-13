# This file handles player starting
import stats


def player_select():
    print('Let\'s begin with some easy stuff.')
    playername = input('What be thy name? ')
    stats.player_name = playername
    print('Your name is', stats.player_name)
    for i in range(len(stats.player_classes)):
        if i <= len(stats.player_classes):
            print(stats.player_classes[i], end=', ')
        else:
            print(stats.player_classes[-1])
    print('\b\b')
    playerclass = input('What would you like your class to be? Choose from those above. ')
    for i in range(len(stats.player_classes)):
        if playerclass == stats.player_classes[i - 1]:
            stats.player_class = stats.player_classes[i - 1]
    print('You are now a(n)', stats.player_class)
    stats.set_skills(playerclass)
    return

