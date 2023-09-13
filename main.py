# This is game, have fun
import rungame

# Introductory script
print('Welcome to a game that nobody honestly cares about.')
print('This is a game where you just kill stuff, level up, kill stuff, and maybe buy new stuff.\n')

# This asks the player if they actually want to play game
if input('Type \'Start\' to continue ') == 'Start':
    start_condition = True
else:
    print('Understandable, have a nice day.')
    start_condition = False

# Handles fun stuff but is 100% not necessary and could have been done in the last statement, but I didn't feel like it
if start_condition:
    print('Let\'s start game\n')
    rungame.run_game()
else:
    input('Press enter to quit')
