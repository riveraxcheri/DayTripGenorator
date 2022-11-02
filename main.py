#Day Trip Generator- Harry Potter


import random

#Greeting

def greeting():
    print ("""
    Welcome to the Hogwarts Day Trip Generator!

    Here are your trip details:""")

# Lists

destinations = ["Hogwarts", "The Ministry of Magic", "Hogsmeade", "Diagon Alley"]
restaurants = ["The Three Broomsticks", "Honeydukes", "The Leaky Cauldron", "Hogwarts Dinning Hall"]
entertainment = ["A Quidditch Match", "The Triwizard Tournament", "Wizard's Chess", "Charms Class"]
transportation = ["The Hogwarts Express", "The Knight Bus", "Broomstick", "Flying Car", "Portkey"]

## Destinations
def select_destination(destination_list):
    selected_destination = random.choice(destination_list)
    return selected_destination

user_destination = select_destination(destinations)

## Restaurants
def select_restaurant(restaurant_list):
    selected_restaurant = random.choice(restaurant_list)
    return selected_restaurant

user_restaurant = select_restaurant(restaurants)

## Entertainment
def select_entertainment(entertainment_list):
    selected_entertainment = random.choice(entertainment_list)
    return selected_entertainment

user_entertainment = select_entertainment(entertainment)

## Transportation
def select_transportation(transportation_list):
    selected_transport = random.choice(transportation_list)
    return selected_transport

user_transportation = select_transportation(transportation)

def reselect_destination(destination_list):
    return (random.choice(destination_list))

# Regenerate specific items on trip details 
# def reselect_item():
#     user_input = input("What part of your trip would you like to change? ")
#     if user_input == "Destination":
#         destinations.remove(user_destination)
#         user_destination = reselect_destination(destinations)
#         print (gen_full_trip())
#         determine_satisfaction()   
#     else:
#         print ("Please type in a valid trip detail.")   

#Trip Details

def gen_full_trip():
    return (f"""
    Destination: {select_destination(destinations)}
    Restaurant: {select_restaurant(restaurants)}
    Entertainment: {select_entertainment(entertainment)}
    Transportation: {select_transportation(transportation)}
    """)

def determine_satisfaction(): 
    confirm_bool = True
    while confirm_bool:
        user_input = input("Are you satisfied with your trip? (y/n) ")
        if user_input == "n":
            print (gen_full_trip()) and determine_satisfaction()
        else:
            confirm_bool = False
    return final_msg()

# def display_new_trip():
#     (f"""
#     Destination:{reselect_destination(destinations)}
#     Restaurant:
#     Entertainment:
#     Transportation:
#     """)

# Ending

def final_msg():
    print (f"""
    Thank you for traveling with us!
    Enjoy your day!""")

# Calling the functions

greeting()
print (gen_full_trip())
determine_satisfaction()


