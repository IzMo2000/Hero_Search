import os
import textwrap
from marvel import Marvel
from keys import MARVEL_PUBLIC, MARVEL_PRIVATE
import requests
import pandas as pd 
import sqlalchemy as db

def json_to_sql(hero_dict):

    # upload hero dictionary into a dataframe
    hero_df = pd.DataFrame.from_dict(hero_dict)

    # create database engine based on villager database
    engine = db.create_engine('sqlite:///hero_info.db')

    # convert dataframe to sql database using engine
    hero_df.to_sql('hero_table', con=engine, if_exists='replace',
                       index=False)

    # return database conversion engine
    return engine


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