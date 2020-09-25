import sys
import texttable as tt
tab = tt.Texttable()
menu = tt.Texttable()
arguments = sys.argv
string_len = 0
line = ""
def line_len(x):
    global line
    line = "+" + ("-"*x) + "+"
#prefrences = [] # Create empty dictionary
number_of_people = "x"
i = 0
headings_menu = ['index','Drinks', 'Cost']
menu_idx = ['1', '2', '3', '4', '5']
drinks_list = ['Water', 'Tea', 'Coffe', 'Hot Chocolate', 'G&T']
cost = ['£0.00', '£2.50', '£2.50', '£3.00', '£4.50']
menu.header(headings_menu)
for row in zip(menu_idx,drinks_list,cost):
    menu.add_row(row)
people = []
drinks_order = []
#leader = input("Hi, I am skynet. Whats your name?\n" + line + "\n    :")
#while number_of_people.isnumeric:
#string_len = 
line_len(len('    How many drinks will you be ordering today?'))
number_of_people = (input(line + """\n  Hi, welcome to VSCafe,

    How many drinks will you be ordering today?
        [1]    One
        [2]    Two
        [3]    Three
        [4]    Four
        [0]    None, I'll leave now
        : """))
if number_of_people.isnumeric() == True:
    number_of_people = int(number_of_people)
if number_of_people == 0:
    print("DAMN STRAIT YOU'LL LEAVE!\n" + line)
    exit
covid = "    Due to covid-19 I'm going to have to ask for the names of each person while I get your drinks order"
line_len(len(covid))
print(line + "\n" + covid)   
while i < number_of_people:
    if i == 0:
        order = 'first'
    if i == 1:
        order = 'second'    
    if i == 2:
        order = 'third'
    if i == 3:
        order = 'fourth'    
    name = input(line + "\n What is person " + order + "'s name: ")
    drink = int(input(menu.draw() + "\n\nWhat number item on the menu "+ name + " like to drink: "))
    people.append(name)
    drinks_order.append(drinks_list[drink - 1])
    # """
    # [1]    Water
    # [2]    Tea
    # [3]    Coffe
    # [4]    Hot Choc
    # [5]    G&T
    # :""")
    # global prefrences
    # prefrences[name] = menu[int(drink)]
    i += 1
headings_order = ["Names", "Drinks"]
tab.header(headings_order)
for row in zip(people,drinks_order):
    tab.add_row(row)
print("\nHere is your order:\n" + tab.draw())









# prefrences[leader] = int(drink)
# drink = input(line + "\nRight so thats one " + menu[drink] + "for " + leader + """,
# is there anything else I can help you with?
#     [1]    Water
#     [2]    Tea
#     [3]    Coffe
#     [4]    Hot Choc
#     :""")






#     print("|            PEOPLE")
#     print(line + "|")
#     people = ['Tom', 'Dick', 'Harry']
#     for person in people:
#         print("| " + person)
# if command == "2": #arguments[1] == "get-drinks" or 
#     print("|             DRINKS")
#     print(line + "|")
#     drinks = {1: 'water', 2: 'tea', 3: 'coffe', 4: 'hot choc',}
#     for drink in drinks:
#         print("| "  + drink[drink_choice])
# #if arguments[1] != 'get-people' and arguments[1] != 'get-drinks':
# #    print("I don't know how to do that")
# print(line + "+") 