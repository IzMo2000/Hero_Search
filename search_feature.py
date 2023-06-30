from marvel import Marvel
from keys import MARVEL_PUBLIC, MARVEL_PRIVATE
import pandas as pd
import sqlite3
import sys

BASE_URL = "https://gateway.marvel.com:443/v1/public/"
URL = 'https://gateway.marvel.com:443/v1/public/characters?nameStartsWith=ju&apikey=65b63a958c2733164ab372a2d69e038b'

# initialize marvel API
marvel_data = Marvel(MARVEL_PUBLIC, MARVEL_PRIVATE)

character_data = marvel_data.characters

# Title: get_result_value
# Description: Retrieves Marvel character data using the character name
# Input: character_name (str) - name of the Marvel character to search for
# Output / Display: None
# Output / Returned: result (list) - list of Marvel character data or None if no results found
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
def print_hero_data(hero_data, print_check = False):

    # check for valid hero data
    if hero_data:
      
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

        # indicate print success
        return True
    
    # invalid hero data, print error and indicate unsuccessful print
    else:
        print("\nERROR collecting hero data, check for Marvel API status")

        return False



# Title: Hero Statistics
# Description: This function takes the hero data and stores it in a dictionary
# Input: hero_data (dictionary) - Hero data retrieved from the API
# Output / Display: None
# Output / Returned: hero_stats (dictionary) - Calculated statistics for the hero
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
            sys.exit(0)
        elif prompt == 'yes':
            search()
        else:
            print('Invalid option')
            re_prompt()



# Title: Default re_prompt
# Description: Prompts the user to continue or quit based on their input
# Input: None
# Output / Display: None
# Output / Returned: None
# Function: Re-prompts the user and goes to the options menu.
def default_re_prompt():
        prompt = input("Do you want to continue [Yes/No]? ").lower()
        if prompt == 'no':
            sys.exit(0)
        elif prompt == 'yes':
            options()
        else:
            print('Invalid option')
            default_re_prompt()

"""
  This function prompts the user to continue or quit the history options.

  Input:
    None

  Output / Display:
    A prompt asking the user to continue or quit.

  Output / Returned:
    None
"""

def history_re_prompt():
        prompt = input("Do you want to continue [Yes/No]? ").lower()
        if prompt == 'no':
            sys.exit(0)
        elif prompt == 'yes':
            history_options()
        else:
            print('Invalid option')
            history_re_prompt()



"""
Title: Search for hero data
Description: This function searches for hero data based on the user's input.
Input:
    * value: The user's input string.
    * char_name: The name of the hero to search for.
Output / Display:
    * If the hero data is found, the function prints the hero's stats in a table format.
    * If the hero data is not found, the function prompts the user to re-enter their input.
Output / Returned:
    * None.
"""
def search():
        try:
            user = input("Please enter the name of the Marvel character you want to search for: ")
        except Exception:
            print("Only numeric values allowed")
        else:
            value, char_name = check_input_string(user)
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
                    # Prompts user to re-enter if no hero data is found
                    re_prompt()
            else:
                # Prompts user to re-enter if input is invalid or empty
                re_prompt()

# Title: check_input_string
# Description: Validates user input for Marvel character name
# Input: None
# Output / Display: Prints error message if input is invalid
# Output / Returned: List [bool, str] indicating validity and the character name

def check_input_string(user):
  
        if isinstance(user, str) and user != '':
            return [True, user]
        else:
            print('No character name entered.')
            return [False, user]


# Title: options
# Description: Prompts the user to select an option and performs the corresponding action.
# Input: None
# Output / Display: Prints the available options and error messages if input is invalid.
# Output / Returned: None
def options():
        # Display the menu to the user
        print('What would you search up?')
        print('We got a set of options just for you! ')
        print('Options: ')
        print('1) Search up a hero')
        print('2) Check Previous search history')
        print('3) Quit ')

        try:
            # Prompt the user to enter an option and convert it to an integer
            option = int(input("Select an option [1/2/3] => "))

            # Check the selected option and perform the corresponding action
            if option == 1:
                search()
            elif option == 2:
                history_options()
            elif option == 3:
                sys.exit(0)
            else:
                # Display an error message for an invalid option and recursively call itself
                print("Invalid option")
                options()
        except ValueError:
            # Catch the ValueError if the user enters a non-integer value
            # Display an error message and recursively call itself
            print("Invalid option. Please enter a number.")
            options()


# Title: History Options
# Description: This function provides options for managing search history.
# Input: None
# Output / Display: Menu options for history management
# Output / Returned: None

def history_options():
        print(default_display())
        print()
        print('What would you like to do with your history:')
        print('1) Display entire data')
        print('2) Display specific hero data')
        print('3) Clear history')
        print('4) Go to main menu')

        try:
            num = int(input('Please select: '))

            if num == 1:
                print(display_data())
                options()
            elif num == 2:
                hero_name = input('Enter hero name: ').capitalize()  # Capitalize the first letter of each word of user input
                display = display_hero_data(hero_name)
                print(display)
                options()
            elif num == 3:
                print(clear_data())
                history_options()
            elif num == 4:
                options()
            else:
                print('Invalid Value')
        except ValueError:
            print('Invalid input. Please enter a number.')
            history_options()


# Title: Implement Table
# Description: Creates a table in the database if it does not exist and inserts the provided hero statistics into the table.
# Input: Dictionary of hero statistics (stats)
# Output / Display: None
# Output / Returned: None

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
        # return empty value
        return True

"""
    Title: Display Hero Data
    Description: This function displays the hero data for the specified hero name.
    Input:
        hero_name (str): The name of the hero to display data for.
    Output / Display:
        The hero data in a Pandas DataFrame.
    Output / Returned:
        None.
"""
def display_hero_data(hero_name):
        conn = sqlite3.connect("hero_data.db")

        # Query the database for the hero data
        query = f"SELECT * FROM Hero WHERE name = '{hero_name}'"
        df = pd.read_sql_query(query, conn)

        # Close the database connection
        conn.close()

        # Check if the DataFrame is empty
        if df.empty:
            return f"No data found for {hero_name}."
        else:
        # Display the hero data
            return df


# Title: Clear data from Hero database
# Description: This function deletes all data from the Hero table in the hero_data.db database.
# Input: None
# Output / Display: Prints a message indicating that the history was deleted successfully.
# Output / Returned: None

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

            return "History deleted successfully.  You are safe :) "
        except sqlite3.Error as e:
            return "Error occurred while deleting data:", e

"""
    Title: Display Hero Data
    Description: This function displays the hero data for the specified hero name.
    Input: hero_name (str): The name of the hero to display data for.
    Output / Display: The hero data in a Pandas DataFrame.
    Output / Returned: None.
"""
def display_data():
            conn = sqlite3.connect("hero_data.db")
            # Retrieve the inserted data and display it using pandas
            sql = pd.read_sql_query("SELECT * FROM Hero ORDER BY id DESC", conn)
            df = pd.DataFrame(sql, columns=["name", "comics", "series", "stories", "events"])
            conn.close()
            if df.empty:
                return "No data available."
            else:
                return df


"""
    Title: Default Display Function
    Description: This function connects to the hero_data.db database and retrieves the data from the Hero table. The data is then displayed using pandas.
    Input: None
    Output / Display: The data from the Hero table is displayed in a pandas DataFrame.
    Output / Returned: None
"""
def default_display():
        conn = sqlite3.connect("hero_data.db")

        # Retrieve the data from the database and display it using pandas
        sql = pd.read_sql_query("SELECT * FROM Hero ORDER BY id DESC", conn)
        df = pd.DataFrame(sql, columns=["name"])
        conn.close()
        if df.empty:
            return "No data available."
        else:
            return df


# comment each function    -------Done-----
# sorting based recent input        -------Done-----
# try and expect on the main options function   -------Done-----
# check values for re prompt if answer aside from no is entered    -------Done-----
# check when enter_a particular hero is not in table what to display   -------Done-----
# capitalize first letter of user input when checking for a specific data of a hero    -------Done-----
# call the re prompt inside the search_history functions    -------Done-----