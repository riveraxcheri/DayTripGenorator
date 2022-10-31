# Day Trip Generator- Harry Potter

import random

destinations = ["Hogwarts", "The Ministry of Magic", "Hogsmeade", "Diagon Alley"]
restaurants = ["The Three Broomsticks", "Honeydukes", "The Leaky Cauldron", "Hogwarts Dinning Hall"]
entertainment = ["A Quidditch Match", "The Triwizard Tournament", "Wizard's Chess", "Charms Class"]
transportation = ["The Hogwarts Express", "The Knight Bus", "Broomstick", "Flying Car", "Portkey"]

def select_destination():
    selected_destination = random.choice(destinations)
    return selected_destination

print (select_destination())

def select_restaurant():
    selected_restaurant = random.choice(restaurants)
    return selected_restaurant

print (select_restaurant())

def select_entertainment():
    selected_entertainment = random.choice(entertainment)
    return selected_entertainment

print (select_entertainment())

def select_transportation():
    selected_transport = random.choice(transportation)
    return selected_transport

print (select_transportation())