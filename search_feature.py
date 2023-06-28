import os
from marvel import Marvel
from keys import MARVEL_PUBLIC, MARVEL_PRIVATE
import requests
import pandas as pd
import sqlalchemy as db
import sqlite3

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
        return result[0]
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


def hero_stat(hero_data):
    name = hero_data['name']
    comics = hero_data['comics']['available']
    series = hero_data['series']['available']
    stories = hero_data['stories']['available']
    events = hero_data['events']['available']

    hero_stats = {
        'name': name,
        'comics': comics,
        'series': series,
        'stories': stories,
        'events': events
    }

    return hero_stats


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

def history_re_prompt():
    prompt = input("Do you want to continue [Yes/No]? ").lower()
    if prompt == 'no':
        quit(0)
    else:
        history_options()


def search():
    value, char_name = check_input_string()
    # print(value)
    if value:
        hero_data = get_result_value(char_name)
        if hero_data is not None:
            # prints expected value
            stats = hero_stat(hero_data)
            implement_table(stats)
            print_hero_data(hero_data)
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

    try:
        option = int(input("Select an option [1/2/3/4] => "))
        if option == 1:
            start()
        elif option == 2:
            print('Still a work in progress :(')
            start2()
        elif option == 3:
            history_lookup()
        elif option == 4:
            quit(0)
        else:
            print("Invalid option")
            options()
    except ValueError:
        print("Invalid option. Please enter a number.")
        options()

def start():
    while True:
        search()


def history_lookup():
    history_options()

def history_options():
    default_display()
    print()
    print('What would you like to do with your history:')
    print('1) Display entire data')
    print('2) Search more on a particular hero data')
    print('3) Clear history')
    print('3) Go to main menu')

    try:
        num = int(input('Please select: '))

        if num == 1:
            display_data()
            default_re_prompt()
        elif num == 2:
            hero_name = input('Enter hero name: ')
            display_hero_data(hero_name)
            default_re_prompt()
        elif num == 3:
            clear_data()
            default_re_prompt()
        elif num == 4:
            default_re_prompt()
        else:
            print('Invalid Value')
    except ValueError:
        print('Invalid input. Please enter a number.')
        history_re_prompt()

def start2():
    pass


def implement_table(stats):
    conn = sqlite3.connect("hero_data.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS Hero(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(255) NOT NULL,
        comics INTEGER NOT NULL,
        series INTEGER NOT NULL,
        stories INTEGER NOT NULL,
        events INTEGER NOT NULL
    )
    """)

    hero_stats = stats

    def insert_into():
        # Insert the extracted hero data into the database
        cur.execute("""
        INSERT INTO Hero (name, comics, series, stories, events)
        VALUES ('{}', '{}', '{}', '{}', '{}')
        """.format(hero_stats['name'], hero_stats['comics'], hero_stats['series'], hero_stats['stories'],
                   hero_stats['events']))
        conn.commit()

    insert_into()


def display_hero_data(hero_name):
    conn = sqlite3.connect("hero_data.db")

    # Query the database for the hero data
    query = f"SELECT * FROM Hero WHERE name = '{hero_name}'"
    df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    # Display the hero data
    print(df)

def clear_data():
    try:
        conn = sqlite3.connect("hero_data.db")
        cur = conn.cursor()

        # Delete all data from the Hero table
        cur.execute("DELETE FROM Hero")

        # Commit the changes
        conn.commit()

        # Close the database connection
        conn.close()

        print("History deleted successfully.  You are safe :) lol")
    except sqlite3.Error as e:
        print("Error occurred while deleting data:", e)


def display_data():
        conn = sqlite3.connect("hero_data.db")
        cur = conn.cursor()
        # Retrieve the inserted data and display it using pandas
        sql = pd.read_sql_query("SELECT * FROM Hero", conn)
        df = pd.DataFrame(sql, columns=["name", "comics", "series", "stories", "events"])
        if df.empty:
            print("No data available.")
        else:
            print(df)
        conn.close()


def default_display():
    conn = sqlite3.connect("hero_data.db")
    cur = conn.cursor()

    # Retrieve the data from the database and display it using pandas
    sql = pd.read_sql_query("SELECT * FROM Hero", conn)
    df = pd.DataFrame(sql, columns=["name"])

    if df.empty:
        print("No data available.")
    else:
        print(df)

    conn.close()


# trying putting limit
# sorting based recent input
# throw and expect on the main options function
# check values for re prompt if answer aside from no is entered
