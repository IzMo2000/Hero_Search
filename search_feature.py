import os
from marvel import Marvel
from keys import MARVEL_PUBLIC, MARVEL_PRIVATE
import requests
import pandas as pd
import sqlalchemy as db

BASE_URL = "https://gateway.marvel.com:443/v1/public/"
URL = 'https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=ju&apikey=65b63a958c2733164ab372a2d69e038b'

# initialize marvel API
marvel_data = Marvel(MARVEL_PUBLIC, MARVEL_PRIVATE)

character_data = marvel_data.characters


def get_result_value(character_name):
    data = character_data.all(name=character_name)
    result = data['data']['results']
    if result:
        #print(data)
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

def re_prompt():
    prompt = input("Do you want to continue [Yes/No] ?").lower()
    if prompt == 'no':
        quit(0)
    else:
        search()

def search():
    
    value, char_name = check_input_string()
    #print(value)
    if value:
        hero_data = get_result_value(char_name)
        if hero_data is not None:
            #prints expected value
            return hero_data
        else:
            re_prompt()
    else:
        re_prompt()

def check_input_string():
    try:
        user = input("Please enter the name of the Marvel character you want to search for: ")

        if isinstance(user, str) and user != '':
            return [True, user]
        else:
            print('No character name entered.')
            return [False, user]
    except Exception as e:
        print("Only numeric values allowed")




