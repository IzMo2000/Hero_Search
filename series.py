import sqlite3
import pandas as pd

def create_series_table(table_name,data):
    conn = sqlite3.connect("hero_data.db")
    cur = conn.cursor()

    # Check if Hulk_series table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(table_name))
    table_exists = cur.fetchone()

    if not table_exists:
        # Create the Hulk_series table
        cur.execute("""
            CREATE TABLE {}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                series VARCHAR(255) NOT NULL,
                link VARCHAR(255) NOT NULL
            )
        """.format(table_name))

        available_series = len(data["series"]["items"])
        for i in range(available_series):
            name = data["series"]["items"][i]["name"]
            link = data["series"]["items"][i]["resourceURI"]
            cur.execute("""
                INSERT INTO {} (series, link)
                VALUES ('{}', '{}')
            """.format(table_name, name, link))

        conn.commit()
        #print("Table created and data inserted.")
    else:
        #print("Table already exists. Skipping creation and insertion.")
        pass
    conn.close()

def display_series_table(table_name):
    conn = sqlite3.connect("hero_data.db")
    # Retrieve the inserted data and display it using pandas
    sql = pd.read_sql_query("SELECT * FROM {} ORDER BY id DESC".format(table_name), conn)
    df = pd.DataFrame(sql, columns=["series", "link"])
    conn.close()
    if df.empty:
        return "No data available."
    else:
        return df