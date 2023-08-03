# Class ISMN-6650-001
# Capstone Project
# Will Ankenbrandt, Ethan Lyons, Irida Medina Petit, Josh Petramale, Boston Smith
# Project Name: StatsFinder

# Main Program

import requests
import json

# SearchPlayers function
def searchPlayers(name):
        url = "https://api-american-football.p.rapidapi.com/players"
        querystring = {"search":name}

        headers = {
	                "X-RapidAPI-Key": "cb2916656emshd38c99fd811d55ap13669ejsne4d62997b95f",
	                "X-RapidAPI-Host": "api-american-football.p.rapidapi.com"
                  }

        response = requests.request("GET", url, headers=headers, params=querystring)

        data = json.loads(response.text)
        resp = data.get('response')

        #Initialize variables
        players_array = []
        player = []

        if resp:
            count = 0
            for item in resp:
                player.append(item['id'])
                player.append(item['name'])
                team = getStats(item['id'], 'N')
                player.append(team)
                # player.append(item['age'])
                # player.append(item['height'])
                # player.append(item['weight'])
                # player.append(item['college'])
                player.append(item['group'])
                player.append(item['position'])
                player.append(item['number'])
                # player.append(item['salary'])
                # player.append(item['image'])
                
                players_array.append(player)
                player = []
                count+=1          
        return players_array #df

# getStats function:
# If print_flag is 'N', it gets the team info for a specific ID and returns it
# If print_flag is 'Y', it gets all the statistics data for a specific ID and prints them
def getStats(id, print_flag):
    url = "https://api-american-football.p.rapidapi.com/players/statistics"
    querystring = {"season": '2022',"id":id}

    headers = {
	            "X-RapidAPI-Key": "cb2916656emshd38c99fd811d55ap13669ejsne4d62997b95f",
	            "X-RapidAPI-Host": "api-american-football.p.rapidapi.com"
              }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = json.loads(response.text)
    resp = data.get('response')

    if resp:
        for line in resp:
            pname = (line['player'].get('name'))
            #Get the Teams name
            for team in line['teams']:
                dteam = team.get('team')
                fteam = dteam.get('name')
                #Get the Stats and print them
                if print_flag == 'Y':
                    print('--------------------------------------------------------------------------------------------------------------')
                    print('Name: ', pname)
                    print('Team: ', fteam)
                    for group in team['groups']:
                        print('Position: ', group.get('name'))
                        print('--------------------------------------------------------------------------------------------------------------')
                        for stat in group['statistics']:
                            print('%-50s%5s' %(stat['name'], stat['value']))
        return fteam

#Main Program
def main():
    print('--------------------------------------------------------------------------------------------------------------')
    print('-----------------------------------------  NCAA and NFL StatsFinder  -----------------------------------------')
    print('--------------------------------------------------------------------------------------------------------------')
    print('Welcome to StatsFinder!')

    #Initialize variables
    control_flag = 'Y'
    last_5_list = []

    #Loops through the program while the user wants to check another player
    while (control_flag == 'Y'):
        
        #Prints the last 5 searched players if they exist
        if last_5_list:
            print('--------------------------------------------------------------------------------------------------------------')
            print('-----------------------------------------  NCAA and NFL StatsFinder  -----------------------------------------')
            print('--------------------------------------------------------------------------------------------------------------')
            print('Last Searched:')
            print('%-5s%30s%30s%10s%15s%15s' %('ID', 'Name', 'Team', 'Group', 'Position', 'Number'))
            count = 0
            for player in last_5_list:
                print('%5s%30s%30s%10s%15s%15s' %(last_5_list[count][0],
                                                  last_5_list[count][1],
                                                  last_5_list[count][2],
                                                  last_5_list[count][3],
                                                  last_5_list[count][4],
                                                  last_5_list[count][5]))
                count +=1
            print('--------------------------------------------------------------------------------------------------------------')
        
        #Ask the user for a player name
        name = input('Enter a player\'s name: ')

        #Calls the searchPlayers function to look up players with that name
        p_list = searchPlayers(name)

        #If it finds players, it prints them
        if p_list:
            print('%-5s%30s%30s%10s%15s%15s' %('ID', 'Name', 'Team', 'Group', 'Position', 'Number'))
            print('--------------------------------------------------------------------------------------------------------------')
            count = 0
            for player in p_list:
                print('%5s%30s%30s%10s%15s%15s' %(player[0],player[1],player[2],player[3],player[4],player[5]))
                count +=1

            #Ask the user what player they want to check
            player_id = input('What Player ID do you want to check?: ')

            #Call the getStats function to get the statistics for that player
            getStats(player_id, 'Y')

            #We add the ID to our history list
            last_player = []
            for player in p_list:
                if str(player[0]) == str(player_id):
                    last_player.append( player[0])
                    last_player.append( player[1])
                    last_player.append( player[2])
                    last_player.append( player[3])
                    last_player.append( player[4])
                    last_player.append( player[5])
            
            last_5_list.append(last_player)
            print(last_5_list)

            #We make sure we always have the last 5
            if len(last_5_list)>5:
                last_5_list.pop(0)

            #We ask the user if they want to check another player
            control_flag = input('Do you want to check another player? (Y/N): ')
        
        #Condition if no players found
        else:
            print('No players found.')

    # Message for the user before closing
    print('Thank you for using our app!')

#Calling main program      
main()

