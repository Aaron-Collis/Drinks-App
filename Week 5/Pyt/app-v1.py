import sys
import time
import pymysql
#import csv

people = ['Aaron', 'Kate', 'Santa']
drinks_prefrence = {
    'Aaron' : 4,
    'Kate' : 2,
    'Santa' : 5
}
drinks_list = {
    1: 'Nothing',
    2: 'Water',
    3: 'Tea',
    4: 'Coffe',
    5: 'Hot Chocolate',
    6: 'G&T'
}

MAIN_MENU = ['Get People', 'Add People', 'Get Prefrences', 'Ammend Prefrences', 'Get Drinks', 'Add Drinks']

def print_table(Header, Content):
    print("\n     " + Header.upper() + "\n")
    i = 1
    for item in Content:
        print(f"     [{i}] " + item)
        i += 1

def print_menu():
    time.sleep(1)
    print('\n     Welcome to the main menu\n')
    i = 1
    for item in MAIN_MENU:
        print(f'     [{i}]     {item}')
        i += 1
    print(f'     [{i}]     Exit')
    user_choice = int(input('\n     Please choose an option: '))     #TODO doesn't handle bad input yet

    if user_choice == 1: #Get People
        print_table('People',people)
        print_menu()

    if user_choice == 2: #Add People
        name = input("Please type the name of the person you wish to add: ")
        people.append(name)
        drinks_prefrence[name] = 1
        print_menu()

    if user_choice == 3: #Get Prefrences #TODO Try/Catch after adding new person
        current_prefrences = []
        for person,prefrence in drinks_prefrence.items():
            current_prefrences.append(f'{person} prefers to drink {drinks_list[prefrence]}')
        print_table('Prefrences', current_prefrences)
        print_menu()

    if user_choice == 4: #Ammend Prefrences
        print("\n")
        print_table('People',people)
        name = input("\n Please type the name of the person you would you like to ammend prefrences for: ")
        if name in people:
            print_table('Drinks', drinks_list.values())
            pref = int(input(f"\nWhich drink number would {name} like to change their prefrence to: "))
            if pref in drinks_list.keys():
                drinks_prefrence[name] = pref
                print("Prefrences Ammened :)")
            else:
                print("\n Sorry that drink ID does not exisit in the database")
                print_menu()
        else:
            print("\n Sorry that name does not exisit in the database")
            print_menu()
        print_menu()

    if user_choice == 5: #Get Drinks
        print_table('Drinks', drinks_list.values())
        print_menu()

    if user_choice == 6: #Add Drinks
        
        drinks_list[len(drinks_list.keys()) + 1] = input("\n Please enter name of drink to be added: ")
        print_menu()

    #if user_choice == 7: #Make a round
    #    print(MAIN_MENU[user_choice - 1] + ' STUFF HAPPENS')     #TODO Make stuff happen   
    #    print_menu()     

### EXIT FUNCTION TO REMAIN LAST IF STATEMENT ####
    if user_choice == i:
        print('Okayyyyyyyyyyyyyyy byyyyyyyyyeeee')
        exit()

print_menu()