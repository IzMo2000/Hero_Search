import pandas as pd
import sqlite3
from comics import create_comic_table, display_comic_table
from events import create_event_table, display_event_table
from stories import create_stories_table, display_stories_table
from series import create_series_table, display_series_table


# - `pandas`: This library provides data manipulation and analysis tools.
# - `sqlite3`: This module is used for working with SQLite databases.


# Title: Implement Table
# Description: Creates a table in the database if it does not exist
#              and inserts the provided hero statistics into the table.
# Input: Dictionary of hero statistics (stats)
# Output / Display: None
# Output / Returned: None

def implement_table(stats):
    conn = sqlite3.connect("hero_data.db")
    cur = conn.cursor()

    # Create the Hero table if it doesn't exist
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
        """.format(hero_stats['name'], hero_stats['comics'],
                   hero_stats['series'], hero_stats['stories'],
                   hero_stats['events']))
        conn.commit()

    # Call the insert_into function to insert the hero data
    insert_into()
    # Return True to indicate that the table has been implemented
    return True


# Title: Display Hero Data
# Description: This function displays the hero data for the
#                  specified hero name.
# Input: hero_name (str): The name of the hero to display data for.
# Output / Display: The hero data in a Pandas DataFrame.
# Output / Returned: None.
def display_hero_data(hero_name):
    conn = sqlite3.connect("hero_data.db")

    # Query the database for the hero data
    query = f"SELECT * FROM Hero WHERE name = '{hero_name}'"
    df = pd.read_sql_query(query, conn)

    # Close the database connection
    conn.close()

    # Check if the DataFrame is empty
    if df.empty:
        return [f"No data found for {hero_name}.", False]
    else:
        # Display the hero data
        return [df, True]

# Title: Display Hero Data
# Description: This function displays the hero data for the specified
#                  hero name.
# Input: hero_name (str): The name of the hero to display data for.
# Output / Display: The hero data in a Pandas DataFrame.
# Output / Returned: None.
def display_data(database_name):
    conn = sqlite3.connect(database_name)
    # Retrieve the inserted data and display it using pandas
    sql = pd.read_sql_query("SELECT * FROM Hero ORDER BY id DESC", conn)
    df = pd.DataFrame(sql, columns=["name", "comics", "series",
                                    "stories", "events"])
    conn.close()
    if df.empty:
        return "No data available."
    else:
        return df


# Title: Default Display Function
# Description: This function connects to the hero_data.db database
#             and retrieves the data from the Hero table. The data is
#             then displayed using pandas.
# Input: None
# Output / Display: The data from the Hero table is displayed in a pandas
#                 DataFrame.
# Output / Returned: None


def default_display(database_name):
    # Connect to the database
    conn = sqlite3.connect(database_name)
    # Retrieve the data from the database and display it using pandas
    sql = pd.read_sql_query("SELECT * FROM Hero ORDER BY id DESC", conn)

    # Create a DataFrame from the retrieved data with specified column names
    df = pd.DataFrame(sql, columns=["name"])
    # Close the database connection
    conn.close()

    # Check if the DataFrame is empty or not
    if df.empty:
        # Return a message indicating that no data is available
        return "No data available."
    else:
        # Return the DataFrame containing the retrieved data
        return df

def hero_to_table(hero_name):
    name = hero_name.replace(" ", "_")
    table_name = {"name_to_comic": name + "_comic", "name_to_story": name + "_story",
                  "name_to_series": name + "_series", "name_to_events": name + "_events"}
    return table_name

def create_hero_tables(table_name, data):
    create_stories_table(table_name["name_to_story"], data)
    create_event_table(table_name["name_to_events"], data)
    create_series_table(table_name["name_to_series"], data)
    create_comic_table(table_name["name_to_comic"], data)
    return True


def drop_all_tables(database_name):
    conn = sqlite3.connect(database_name)
    cur = conn.cursor()

    # Get the list of table names excluding 'sqlite_sequence'
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_sequence'")
    table_names = cur.fetchall()

    # Drop each table
    for table in table_names:
        table_name = table[0]
        cur.execute(f"DROP TABLE IF EXISTS {table_name}")

    conn.commit()
    conn.close()
    return True


def table_options(hero_name):
    table_name = hero_to_table(hero_name)
    # Display the menu to the user
    print('\nWould you like to check more on this hero')
    print('\nWe got a set of options! ')
    print('Options: ')
    print('1) Check the comics')
    print('2) Check the series')
    print('3) Check the stories ')
    print('4) Check the events ')
    print('5) Go to main menu ')

    try:
        # Prompt the user to enter an option and convert it to an integer
        option = int(input("Select an option [1/2/3/4/5] => "))

        # Check the selected option and perform the corresponding action
        if option == 1:
            print(display_comic_table(table_name["name_to_comic"]))
            table_options(hero_name)
        elif option == 2:
            print(display_series_table(table_name["name_to_series"]))
            table_options(hero_name)
        elif option == 3:
            print(display_stories_table(table_name["name_to_story"]))
            table_options(hero_name)
        elif option == 4:
            print(display_event_table(table_name["name_to_events"]))
            table_options(hero_name)
        elif option == 5:
            pass
        else:
            # Display an error message for an invalid option and recursively
            # call itself
            print("Invalid option")
            table_options(hero_name)
    except ValueError:
        # Catch the ValueError if the user enters a non-integer value
        # Display an error message and recursively call itself
        print("Invalid option. Please enter a number.")
        table_options(hero_name)

def name_and_data(hero_name, hero_data):  # handles table creation
    table_name = hero_to_table(hero_name)
    create_hero_tables(table_name, hero_data)
    return True

def is_database_empty(database_name):
    """Checks if the specified database is empty.

  Args:
    database_name: The name of the database.

  Returns:
    True if the database is empty, False otherwise.
  """

    conn = sqlite3.connect(database_name)
    cur = conn.cursor()

    # Get the list of table names
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name!='sqlite_sequence'")
    table_names = cur.fetchall()

    conn.commit()
    conn.close()

    # If there are no tables, then the database is empty
    return len(table_names) == 0