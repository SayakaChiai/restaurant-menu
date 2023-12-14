# DONE in menu choose what you want to eat
# check if all ingredients are present to make the basic version
# if not, remove from menu
# ask if you want to upgrade the food
# if yes, check if there are enough ingredients for the upgrade
# if not, remove from menu
# DONE no menu items left = quit


import sys

class CheckIfEnough:
    def __init__(self, ingredients, amount):
        self.ingr = ingredients
        self.nr = amount

# to help build the menu in the restaurant
class Menu:
    def __init__(self, menuitem, status):
        self.item = menuitem
        self.yesno = status

# available ingredients
fridge = [
CheckIfEnough ('beef', 1),
CheckIfEnough ('cheese', 1),
CheckIfEnough ('dough', 2),
CheckIfEnough ('lettuce', 3),
CheckIfEnough ('tomato', 1)
]

# 1 = item is available
# how to add other items to the list as well
menu = [
    Menu ('pizza', 1),
    Menu ('hamburger', 1),
    Menu ('sandwich', 1)
]

# 1 = item is available
upgrades = [
    ('pizza with lettuce', 1),
    ('hamburger with cheese', 1),
    ('sandwich with lettuce', 1)
]

# numbers are how many of the ingredient is needed
pizzarecipe = [
    ('dough', 1),
    ('beef', 1),
    ('cheese', 1)
]

pizzaupgrade = [
    ('cheese', 1)
]

hamburgerrecipe = [
    ('dough', 1),
    ('beef', 1),
    ('lettuce', 1),
    ('tomato', 1)
]

hamburgerupgrade = [
    ('cheese', 1)
]

sandwichrecipe = [
    ('dough', 1),
    ('cheese', 1)
]

sandwichupgrade = [
    ('lettuce', 1)
]

# functions

# check if enough ingredients are available
# has to support a changing recipe
# don't subtract ingredients if not possible
def checkifchoiceispossible (item):
    if item == 'pizza':
        print ('checking fridge for pizza ingredients')
        # check what ingredients are needed, and how many
        # check if enough of each ingredient
        # subtract               

# user chooses what to eat
def makechoice (input):
    while True:
        choice = input ('\n')
        if choice.startswith('san'):   
            choice = 'sandwich'
            print ('Let me check if we have everything to make a sandwich!')
            checkifchoiceispossible ('sandwich')
            break
        if choice.startswith('ham'):
             choice = 'hamburger'
             print ('Let\'s check up on the cows!')
             checkifchoiceispossible ('hamburger')
             break
        if choice.startswith('piz'):
            choice = 'pizza'
            print ('Let\'s see if I have everything for pizza!')
            checkifchoiceispossible ('pizza')
            break
        else:
            choice = input ('What did you say? Can you type more clearly?\n\n')
            continue

def showmenu (items):
    print ('Welcome to the restaurant. What do you want to eat?\n')
    availableitems = 0
    for x in items:
# yesno checks if the items is available
        if x.yesno==1:
            availableitems += 1
            print(x.item)
# quit if nothing is on the menu
    if availableitems == 0:
       input ('We can\'t make any food right now. Press ENTER to leave the restaurant.')
       sys.exit(0)

    #make choice
    makechoice (input)

# show menu
showmenu (menu)