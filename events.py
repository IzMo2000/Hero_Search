import sqlite3
import pandas as pd


def create_event_table(table_name,data):
    conn = sqlite3.connect("hero_data.db")
    cur = conn.cursor()

    # Check if the Hulk_events table already exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(table_name))
    table_exists = cur.fetchone()

    if table_exists:
        #print("Table 'Hulk_events' already exists. Skipping table creation and data insertion.")
        pass
    else:
        # Create the Hulk_events table
        cur.execute("""
            CREATE TABLE {}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                events VARCHAR(255) NOT NULL,
                link VARCHAR(255) NOT NULL
            )
        """.format(table_name))

        available_event = len(data["events"]["items"])
        for i in range(available_event):
            name = data["events"]["items"][i]["name"]
            link = data["events"]["items"][i]["resourceURI"]
            cur.execute("""
                INSERT INTO {} (events, link)
                VALUES ('{}', '{}')
            """.format(table_name,name, link))

        #print(f"Table '{table_name}' created and data inserted.")

    conn.commit()
    conn.close()

def display_event_table(table_name):
    conn = sqlite3.connect("hero_data.db")
    # Retrieve the inserted data and display it using pandas
    sql = pd.read_sql_query("SELECT * FROM {} ORDER BY id DESC".format(table_name), conn)
    df = pd.DataFrame(sql, columns=["events", "link"])
    conn.close()
    if df.empty:
        return "No data available."
    else:
        return df