import sys
arguments = sys.argv
line = "+================================="
print(line + "+")
if len(arguments) < 2: #Argument present?
    print("What do you want?")
    command = input("[1] for People\n[2] for Drinks\n")
if len(arguments) > 2: #Multiple arguments?
    print('I can not multitask, one thing at a time please')
    exit()
if  command == "1": #(arguments[1]) == 'get-people' or
    print("|            PEOPLE")
    print(line + "|")
    people = ['Tom', 'Dick', 'Harry']
    for person in people:
        print("| " + person)
if command == "2": #arguments[1] == "get-drinks" or 
    print("|             DRINKS")
    print(line + "|")
    drinks = ['Coke', 'Pepsi', 'Rum']
    for drink in drinks:
        print("| "  + drink)
#if arguments[1] != 'get-people' and arguments[1] != 'get-drinks':
#    print("I don't know how to do that")
print(line + "+") 