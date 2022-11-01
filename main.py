# Day Trip Generator- Harry Potter

import random

destinations = ["Hogwarts", "The Ministry of Magic", "Hogsmeade", "Diagon Alley"]
restaurants = ["The Three Broomsticks", "Honeydukes", "The Leaky Cauldron", "Hogwarts Dinning Hall"]
entertainment = ["A Quidditch Match", "The Triwizard Tournament", "Wizard's Chess", "Charms Class"]
transportation = ["The Hogwarts Express", "The Knight Bus", "Broomstick", "Flying Car", "Portkey"]

def select_destination(destination_list):
    selected_destination = random.choice(destination_list)
    return selected_destination

user_destination = select_destination(destinations)

def reselect_destination(destination_list):
    new_destination = random.choice(destination_list.remove(user_destination))
    return new_destination

def select_restaurant(restaurant_list):
    selected_restaurant = random.choice(restaurant_list)
    return selected_restaurant

user_restaurant = select_restaurant(restaurants)

def select_entertainment(entertainment_list):
    selected_entertainment = random.choice(entertainment_list)
    return selected_entertainment

user_entertainment = select_entertainment(entertainment)

def select_transportation(transportation_list):
    selected_transport = random.choice(transportation_list)
    return selected_transport

user_transportation = select_transportation(transportation)

def greeting():
    print ("Welcome to the Hogwarts Day Trip Generator! Here are your trip details:")

def display_full_trip():
    print (f"Destination: {user_destination}")
    print (f"Restaurant: {user_restaurant}")
    print (f"Entertainment: {user_entertainment}")
    print (f"Transportation: {user_transportation}")

def determine_satisfaction(): 
    confirm_bool = True
    while confirm_bool:
        user_input = input("Are you satisfied with your trip? (y/n) ")
        if user_input == "n":
            reselect_item()
        else:
            confirm_bool = False
    return final_msg()

def final_msg():
    print ("Great! Here are your final trip details:")
    print (display_full_trip())
    print ("Enjoy your day!")

def reselect_item():
    user_input = input("What part of your trip would you like to change? ")
    if user_input == "Destination":
        reselect_destination()
    else:
        print ("Please type in a valid trip detail.")    

greeting()
display_full_trip()
determine_satisfaction()

  
