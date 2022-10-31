# Day Trip Generator- Harry Potter

import random

destinations = ["Hogwarts", "The Ministry of Magic", "Hogsmeade", "Diagon Alley"]
restaurants = ["The Three Broomsticks", "Honeydukes", "The Leaky Cauldron", "Hogwarts Dinning Hall"]
entertainment = ["A Quidditch Match", "The Triwizard Tournament", "Wizard's Chess", "Charms Class"]
transportation = ["The Hogwarts Express", "The Knight Bus", "Broomstick", "Flying Car", "Portkey"]

def select_destination():
    selected_destination = random.choice(destinations)
    return selected_destination

def select_restaurant():
    selected_restaurant = random.choice(restaurants)
    return selected_restaurant

def select_entertainment():
    selected_entertainment = random.choice(entertainment)
    return selected_entertainment

def select_transportation():
    selected_transport = random.choice(transportation)
    return selected_transport

def print_full_trip():
    print ("Here is your trip:")
    print (f"Destination: {select_destination()}")
    print (f"Restaurant: {select_restaurant()}")
    print (f"Entertainment: {select_entertainment()}")
    print (f"Transportation: {select_transportation()}")

def determine_satisfaction():
    user_input = input("Are you satisfied with your trip? (Y/N) ")
    if user_input is "Y":
        print (f"Great! Here is your final trip: {print_full_trip()}")
    else:
        print (generate_new())

def generate_new():
    user_input = input("What part of your trip would you like to change? ")
    if user_input is "Destination":
        new_destination = random.choice(destinations.remove(select_destination())) 
        print (new_destination)         

print_full_trip()

determine_satisfaction()

  
