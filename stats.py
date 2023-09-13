# This page has things that are fun

player_name = ''
player_class = 'None'
player_level = 1
player_xp = 0
player_skills = []
player_max_stamina = 50
player_stamina = 0

player_classes = ['Hunkydory Punchy Dudo', 'Majik Big Brain', 'Scharpe Stik Boi', 'Cowardly Pew-Pew Wooosh']

# Contains a list of base skills for each class
# Skills denoted [name, base damage, stamina usage, debuff]

# Boxer
boxer_skills = [['Punch', 10, 0, 'None'], ['Kick', 15, 10, 'Bruised']]

# Mage
mage_skills = [['Light ball', 10, 0, 'None'], ['Water ball', 8, 10, 'Wet']]

# Swordsman
swordsman_skills = [['Slash', 10, 0, 'None'], ['Thrust', 15, 15, 'Bleed']]

# Archer
archer_skills = [['Standard pewpew', 7, 0, 'None'], ['Power pewpew', 20, 20, 'none']]


# Set skills
def set_skills(selected_class):
    global player_skills
    if selected_class == player_classes[0]:
        player_skills = boxer_skills
    elif selected_class == player_classes[1]:
        player_skills = mage_skills
    elif selected_class == player_classes[2]:
        player_skills = swordsman_skills
    elif selected_class == player_classes[3]:
        player_skills = archer_skills
    else:
        print('You picked an invalid class! You are screwed!')
    print('Your skills are:', end=' ')
    for i in range(len(player_skills)):
        print(player_skills[i][0], end=', ')
    print('\b\b')
    return
