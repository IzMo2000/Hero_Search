from search_feature import search, print_hero_data, re_prompt, options
from marvel import Marvel
from keys import MARVEL_PUBLIC, MARVEL_PRIVATE
import requests
import pandas as pd
import sqlalchemy as db


# initialize marvel API
marvel_data = Marvel(MARVEL_PUBLIC, MARVEL_PRIVATE)
character_data = marvel_data.characters


def main():
    print("Welcome to Hero Search!")
    options()


if __name__ == "__main__":
    main()
