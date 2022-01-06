import constants
import copy

DATA_BASE = [player for player in constants.PLAYERS.copy()]
bandits = []
panthers  = []
warriors  = []


def clean_data():
    for player in DATA_BASE:
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split('and')
        player['guardians'] = ', '.join(player['guardians'])
        if player['experience'] == 'YES':
            player['experience'] = True
        else:
            player['experience'] = False
                
                
def balance(team, data):
    experienced = []
    inexperienced = []
    for player in data.copy():
        if len(team) < 6:
            #print(player['experience'] and len(experienced) < 3)
            if player['experience'] and len(experienced) < 3:
                experienced.append(player)
                data.remove(player)
            elif not player['experience'] and len(inexperienced) < 3:
                inexperienced.append(player)
                data.remove(player)
    team.extend(experienced)
    team.extend(inexperienced)


def roster_info_for(team_name, team_data):
    print(f'\nTeam: {team_name}')
    print('_'*14)
    experience = [value['experience'] for key, value in enumerate(team_data)]
    height_average = sum([value['height'] for key, value in enumerate(team_data)]) / len(team_data)
    print(f'Total experienced: {experience.count(True)}')
    print(f'Total inexperienced: {experience.count(False)}')
    print(f'Average height: {height_average}')
    players_names = [player['name'] for player in team_data]
    players_names = ', '.join(players_names)
    print(f'Players on Team: \n {players_names}')


clean_data()
balance(panthers, DATA_BASE)
balance(bandits, DATA_BASE)
balance(warriors, DATA_BASE)



while True:
    print("""
    BASKETBALL TEAM STATS TOOL \n
        _____Menu_____ \n
    Here are your menu options:
    (A). Display Team Stats
    (B). Quit
    """)
    
    choose_option = input('Select one of the two menu options above: ')
    if choose_option.upper() == 'A':
        print('(A). Panthers\n(B). Bandits\n(C). Warriors\n')
        choose_team = input('Select one of the 3 teams available above: ')
        if choose_team.upper() == 'A':
            roster_info_for('Panthers', panthers)
        elif choose_team.upper() == 'B':
            roster_info_for('Bandits', bandits)
        elif choose_team.upper() == 'C':
            roster_info_for('Warriors', warriors)
    elif choose_option.upper() == 'B':
        print("Have a good day!")
        break
    continue_using_stats_tool = input('\nPress ENTER to continue...' )
    if continue_using_stats_tool == '':
        continue