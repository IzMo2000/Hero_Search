import sqlite3
import pandas as pd


def create_comic_table(table_name,data):
    conn = sqlite3.connect("hero_data.db")
    cur = conn.cursor()

    # Check if the Hulk table exists
    cur.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='{}'".format(table_name))
    table_exists = cur.fetchone()

    if not table_exists:
        # Create the Hulk table if it doesn't exist
        cur.execute("""
            CREATE TABLE {}(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                comic VARCHAR(255) NOT NULL,
                link VARCHAR(255) NOT NULL
            )
        """.format(table_name))

        available = len(data["comics"]["items"])
        for i in range(available):
            name = data["comics"]["items"][i]["name"]
            link = data["comics"]["items"][i]["resourceURI"]
            cur.execute("""
                INSERT INTO {} (comic, link)
                VALUES (?, ?)
            """.format(table_name), (name, link))

        conn.commit()
        #print("Table created and data inserted.")
    else:
        # print("Table already exists. No data inserted.")
        pass
    conn.close()

def display_comic_table(table_name):
    conn = sqlite3.connect("hero_data.db")
    # Retrieve the inserted data and display it using pandas
    sql = pd.read_sql_query("SELECT * FROM {} ORDER BY id DESC".format(table_name), conn)
    df = pd.DataFrame(sql, columns=["comic", "link"])
    conn.close()
    if df.empty:
        return "No data available."
    else:
        return df