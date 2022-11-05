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


## Restaurants
def select_restaurant(restaurant_list):
    selected_restaurant = random.choice(restaurant_list)
    return selected_restaurant



## Entertainment
def select_entertainment(entertainment_list):
    selected_entertainment = random.choice(entertainment_list)
    return selected_entertainment



## Transportation
def select_transportation(transportation_list):
    selected_transport = random.choice(transportation_list)
    return selected_transport



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

def gen_full_trip(d,r,e,t):
    return (f"""
    Destination: {d}
    Restaurant: {r}
    Entertainment: {e}
    Transportation: {t}
    """)

def determine_satisfaction(d,r,e,t): 
    confirm_bool = True
    while confirm_bool:
        d=d
        r=r
        e=e
        t=t
        user_input = input("Are you satisfied with your trip? (y/n) ")
        if user_input == "n":
            user_reselect = input ("What to change? d, r, e, t ")
            if user_reselect == "d":
                d = select_destination(destinations)
            elif user_reselect == "r":
                r = select_destination(restaurants)
            elif user_reselect == "e":
                e = select_destination(entertainment)
            elif user_reselect == "t":
                t = select_destination(transportation)
            print (gen_full_trip(d,r,e,t)) 
            return determine_satisfaction(d,r,e,t)
        elif user_input == "y":
            confirm_bool = False
        else:
            print ("message")
            continue
    print (gen_full_trip(d,r,e,t)) 
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
    return (f"""
    Thank you for traveling with us!
    Enjoy your day!""")

# Calling the functions

def dtg():
    greeting()
    user_destination = select_destination(destinations)
    user_restaurant = select_restaurant(restaurants)
    user_entertainment = select_entertainment(entertainment)
    user_transportation = select_transportation(transportation)
    print (gen_full_trip(user_destination, user_restaurant, user_entertainment, user_transportation))
    return determine_satisfaction()

print (dtg())