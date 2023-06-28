import os
from marvel import Marvel
from keys import MARVEL_PUBLIC, MARVEL_PRIVATE
import requests
import pandas as pd
import sqlalchemy as db

# initialize marvel API
marvel_data = Marvel(MARVEL_PUBLIC, MARVEL_PRIVATE)

character_data = marvel_data.characters


# Title: get_result_value
# Description: Retrieves Marvel character data using the character name
# Input: character_name (str) - name of the Marvel character to search for
# Output / Display: None
# Output / Returned: result (list) - list of Marvel character data or None if
#                    no results found
def get_result_value(character_name):
    data = character_data.all(name=character_name)
    result = data['data']['results']
    if result:
        # print(data)
        return result
    else:
        print("No results found for the character.")
        return None


# Title: print_hero_data
# Description: converts json dictionary to SQL database, returns created engine
# Input: villager json data (dict)
# Output / Display: None
# Output / Returned: engine used to create database
def print_hero_data(hero_data):
    # print hero's name
    print(f"\nHero: {hero_data['name']}")

    # print hero description (if it exists)
    if hero_data['description']:
        print(f"\nDescription: {hero_data['description']}")

    # show hero appearance stats
    print(f"\n{hero_data['name']} has been in:")
    print(f"    {hero_data['comics']['available']} comics")
    print(f"    {hero_data['series']['available']} series")
    print(f"    {hero_data['stories']['available']} stories")
    print(f"    {hero_data['events']['available']} events")


# Title: re_prompt
# Description: Prompts the user to continue or quit based on their input
# Input: None
# Output / Display: None
# Output / Returned: None
# Function: Re-prompts the user for input to continue or quit the program.
def re_prompt():
    prompt = input("Do you want to continue [Yes/No]? ").lower()
    if prompt == 'no':
        quit(0)
    else:
        search()


# Title: Default re_prompt
# Description: Prompts the user to continue or quit based on their input
# Input: None
# Output / Display: None
# Output / Returned: None
# Function: Re-prompts the user and goes to the options menu.
def default_re_prompt():
    prompt = input("Do you want to continue [Yes/No]? ").lower()
    if prompt == 'no':
        quit(0)
    else:
        options()


# Title: search
# Description: Searches for a Marvel character based on user input
#              and retrieves hero data.
# Input: None
# Output / Display: None
# Output / Returned: Hero data (dict) if found, None otherwise
def search():
    value, char_name = check_input_string()
    # print(value)
    if value:
        hero_data = get_result_value(char_name)
        if hero_data is not None:
            # prints expected value
            print_hero_data(hero_data[0])
            default_re_prompt()
        else:
            re_prompt()  # Prompts user to re-enter if no hero data is found
    else:
        re_prompt()  # Prompts user to re-enter if input is invalid or empty


# Title: check_input_string
# Description: Validates user input for Marvel character name
# Input: None
# Output / Display: Prints error message if input is invalid
# Output / Returned: List [bool, str] indicating validity and
#                    the character name
def check_input_string():
    try:
        user = input("Please enter the name of the Marvel character you " +
                     "want to search for: ")

        if isinstance(user, str) and user != '':
            return [True, user]
        else:
            print('No character name entered.')
            return [False, user]
    except Exception as e:
        print("Only numeric values allowed")


def options():
    print('What would you search up?')
    print('We got a set of options just for you! ')
    print('Options: ')
    print('1) Search up a hero')
    print('2) Check names with few characters')
    print('3) Check Previous search history')
    print('4) Quit ')

    option = int(input("Select an option [1/2/3/4] => "))
    if option == 1:
        start()
    elif option == 2:
        start2()
    elif option == 3:
        history_lookup()
    elif option == 4:
        quit(0)
    else:
        print("Invalid option")
        options()


def start():
    while True:
        search()


def start2():
    pass


def history_lookup():
    pass
