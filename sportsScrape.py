import re
import time
from bs4 import BeautifulSoup
import requests

#determines if a string is numeric
def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

team_dict = {'Athletic Club': 'athletic-club', 'Atletico de Madrid': 'atletico-de-madrid',
            'CA Osasuna': 'c-a-osasuna', 'Cadiz CF': 'cadiz-cf','Deportivo Alaves': 'd-alaves',
            'Elche CF': 'elche-c-f', 'FC Barcelona': 'fc-barcelona', 'Getafe CF': 'getafe-cf',
            'Granada CF': 'granada-cf', 'Levante UD': 'levante-ud','Rayo Vallecano': 'rayo-vallecano',
            'RC Celta': 'rc-celta', 'RCD Espanyol': 'rcd-espanyol', 'RCD Mallorca': 'rcd-mallorca',
            'Real Betis': 'real-betis', 'Real Madrid': 'real-madrid', 'Real Sociedad': 'real-sociedad',
            'Sevilla FC': 'sevilla-fc', 'Valencia CF': 'valencia-cf', 'Villarreal CF': 'villarreal-cf'}
while True:
    print('\nA list of LaLiga teams.\n')
    #Output all the teams.
    t=0
    while t < len(team_dict):
        print([key for key in team_dict.keys()][t])
        t+=1

    #Have user type in a team
    notATeam = True
    while notATeam:
        team = input('\nPlease enter a team name from above: ')
        if team_dict.get(team):
            notATeam = False
        else:
            print('\nPlease enter a valid team.')
        
        

    #Iterate through all teams.
    #for team in team_dict.keys():

    #Retrieve url to parse
    source = requests.get('https://www.laliga.com/en-ES/clubs/' + team_dict[team] + '/stats').text
    soup = BeautifulSoup(source, 'lxml')

    #Scrape team's statistics
    stats = soup.find('div', class_="styled__LeagueFastStatsContainer-sc-81pxi-0 kIOpQe").text

    string = str(stats)
    print('\n' + string + '\n')

    assists = ''
    goals = ''
    wins =''
    draws =''
    matches =''

    done = True

    #Tell user to ask a question.
    answer = input('\nWhat statistic would you like to know about ' + team + '?\n')

    while done:
        i = 0

        if 'match' in answer:
            #Determine number of matches played.
            while i < len(string):
                if(string[i] == 'p'):
                    i+=1
                    if(string[i] == 'l'):
                        i+=1
                        if(string[i] == 'a'):
                            i+=1
                            if(string[i] == 'y'):
                                i+=1
                                if(string[i] == 'e'):
                                    i+=1
                                    if(string[i] == 'd'):
                                        i+=1
                                        while string[i] != 'T':
                                            matches += string[i]
                                            i+=1
                                        break
                i+=1

            print('\n' + team + ' has played ' + matches + ' matches.')
            time.sleep(1)
            answer = input('\nAnything else you would like to know about ' + team + '?\nIf not, and you would like to choose another team, type NEW.\nIf not, type DONE.\n-')

        if 'wins' in answer:
            #Loop determining number of wins
            while i < len(string):
                if(string[i] == 'W'):
                    i+=1
                    if(string[i] == 'i'):
                        i+=1
                        if(string[i] == 'n'):
                            i+=1
                            if(string[i] == 's'):
                                i+=1
                                while string[i] != 'D':
                                #print(string[k])
                                    wins += string[i]
                                    i+=1
                                break
                i+=1
            print('\n' + team + ' has ' + wins + ' wins.')
            time.sleep(1)
            answer = input('\nAnything else you would like to know about ' + team + '?\nIf not, and you would like to choose another team, type NEW.\nIf not, type DONE.\n-')

        if 'draw' in answer:
            #Enter loop to determine number of draws.
            while i < len(string):
                if(string[i] == 'D'):
                    i+=1
                    if(string[i] == 'r'):
                        i+=1
                        if(string[i] == 'a'):
                            i+=1
                            if(string[i] == 'w'):
                                i+=1
                                if(string[i] == 'n'):
                                    i+=1
                                    while string[i] != ' ':
                                        draws += string[i]
                                        i+=1
                                    break
                i+=1
            print('\n' + team + ' has drawn ' + draws + ' draws.')
            time.sleep(1)
            answer = input('\nAnything else you would like to know about ' + team + '?\nIf not, and you would like to choose another team, type NEW.\nIf not, type DONE.\n-')

        if 'goal' in answer:
            #Enter loop to determine number of Goals.
            while i < len(string):
                if(is_integer(string[i])):
                    if(string[i + 1] == " "):
                        i+=1
                        while string[i] != 'G':
                            goals += string[i]
                            i+=1
                        break
                i+=1

            print('\n' + team + ' has scored' + goals + ' goals.')
            time.sleep(1)
            answer = input('\nAnything else you would like to know about ' + team + '?\nIf not, and you would like to choose another team, type NEW.\nIf not, type DONE.\n-')

        if 'assist' in answer:
            #Enter loop to determine number of Assists.
            while i < len(string):
                #print(string[i])
                if(string[i] == 'G'):
                    #print(string[i])
                    i+=1
                    if(string[i] == 'o'):
                        #print(string[i])
                        i+=1
                        if(string[i] == 'a'):
                            #print(string[i])
                            i+=1
                            if(string[i] == 'l'):
                                #print(string[i])
                                i+=1
                                if(string[i] == 's'):
                                    #print(string[i])
                                    i+=1
                                while string[i] != 'A':
                                    assists += string[i]
                                    i+=1
                                break
                i+=1

            print('\n' + team + ' has a total of ' + assists + ' assists.')
            time.sleep(1)
            answer = input('\nAnything else you would like to know about ' + team + '?\nIf not, and you would like to choose another team, type NEW.\nIf not, type DONE.\n-')

        if 'DONE' in answer:
            print ('goodbye')
            exit()

        if 'NEW' in answer:
            done = False
            
        else:
            print('Sorry try asking again.\n')
            answer = input('-')