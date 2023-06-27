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
    return character_data.all(nameStartsWith=character_name)

def user_input()
    character_name = input("Please enter the name of the Marvel character you want to search for: ").lower()
    return character_name

def check_input_string(user_input):

   try:
       str(character_name) 
       return True
    except ValueError:
        return False

    if isinstance(user_input, str):
        return True
    else:
        user_input()


def main():
        
        print(get_character_json("Hulk"))
  

if __name__=="__main__":
    main()

