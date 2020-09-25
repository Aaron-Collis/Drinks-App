import sys
import csv
import halp
import texttable as tt
welcome = tt.Texttable()
tab = tt.Texttable()
menu = tt.Texttable()
arguments = sys.argv
string_len = 0
i = 0
line = ""
people = []
drinks_order = []
number_of_people = "x"
welcome.add_row("WELCOME TO VSCafe")
headings_menu = ['index','Drinks', 'Cost']                          #TODO LOAD THIS FROM FILE
menu_idx = ['1', '2', '3', '4', '5']                                #TODO LOAD THIS FROM FILE
drinks_list = ['Water', 'Tea', 'Coffe', 'Hot Chocolate', 'G&T']     #TODO LOAD THIS FROM FILE
cost = ['£0.00', '£2.50', '£2.50', '£3.00', '£4.50']                #TODO LOAD THIS FROM FILE
####################################################################
print(halp.halp("life"))
####################################################################
def save_round():
    with open('round.csv', 'w') as csvfile:    
        writer = csv.writer(csvfile)
        writer.writerow(headings_menu)
        i = 0
        while i < 5:
            writer.writerow([menu_idx[i], drinks_list[i], cost[i]])
            i += 1
#####################################################################
class drink_round:
    def __init__(self, name, drink_num):
        self.name = name
        self.drink = drink_num
def line_len(x):
    global line
    line = "+" + ("-"*x) + "+"
menu.header(headings_menu)
# something = int(input("""
# [1] Edit menu
# [2] Take order
# [3] Exit
#  : """))
# if something == 1:
    # command = int(input("""
    # [1] Add Drink
    # [2] Ajust Price
    # [3] Delete Drink
    #  : """))
for row in zip(menu_idx,drinks_list,cost):
    menu.add_row(row)
print(welcome.draw())
number_of_people = input("""
    [1]    One
    [2]    Two
    [3]    Three
    [4]    Four
    [0]    None, I'll leave now

How many drinks will you be ordering today: """)
if number_of_people.isnumeric() == True:
    number_of_people = int(number_of_people)
else:
    print("Numbers in numeric format only")
if number_of_people >= 5:
    print("I'm sorry maximum per group is four people at the moment")
    exit()
elif number_of_people < 0:
    print("get lost you ding bat, you can't have negitive drinks")
    exit()
#else:
#    print("please use numbers only")
if number_of_people == 0:
    print("DAMN STRAIT YOU'LL LEAVE!\n" + line)
    exit()
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
    name = input(line + "\n What is the " + order + " person's name: ")
    drink = int(input(menu.draw() + "\n\nWhat number item on the menu "+ name + " like to drink: "))
    people.append(name)                             #TODO use classes here
    drinks_order.append(drinks_list[drink - 1])     #TODO use classes here
    i += 1
headings_order = ["Names", "Drinks"]
tab.header(headings_order)
for row in zip(people,drinks_order):
    tab.add_row(row)
print("\nHere is your order:\n" + tab.draw())