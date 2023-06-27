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


def get_character_json(character_name):
    data = character_data.all(name=character_name)
    return data['data']['results']

def get_result_value(character_name):
    data = character_data.all(name=character_name)
    if data['data']['results']:
        #print(data)
        return True
    else:
        print("No results found for the character.")
        return False

def re_prompt():
    prompt = input("Do you want to continue [Yes/No] ?").lower()
    if prompt == 'no':
        quit(0)
    else:
        search()

def search():
    print("Welcome to Hero Search!")

    value, char_name = check_input_string()
    #print(value)
    if value:
        if get_result_value(char_name):
            #prints expected value
            print(get_character_json(char_name))  # remodel to fit expected function
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


def main():
    search()


if __name__ == "__main__":
    main()

