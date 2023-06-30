import pandas as pd
import sqlite3

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
        return f"No data found for {hero_name}."
    else:
        # Display the hero data
        return df


# Title: Clear data from Hero database
# Description: This function deletes all data from the Hero table
#              in the hero_data.db database.
# Input: None
# Output / Display: Prints a message indicating that the history was
#                   deleted successfully.
# Output / Returned: None

def clear_data():
    try:

        # Connect to the SQLite database
        conn = sqlite3.connect("hero_data.db")
        # Create a cursor object to execute SQL statements
        cur = conn.cursor()

        # Delete all data from the Hero table
        cur.execute("DELETE FROM Hero")

        # Commit the changes
        conn.commit()

        # Close the database connection
        conn.close()


        # Return a success message
        return "History deleted successfully.  You are safe :) "
    except sqlite3.Error as e:
        # Return an error message if an exception occurs
        return "Error occurred while deleting data:", e


# Title: Display Hero Data
# Description: This function displays the hero data for the specified
#                  hero name.
# Input: hero_name (str): The name of the hero to display data for.
# Output / Display: The hero data in a Pandas DataFrame.
# Output / Returned: None.
def display_data():
    conn = sqlite3.connect("hero_data.db")
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


def default_display():
    # Connect to the database
    conn = sqlite3.connect("hero_data.db")

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
