import sqlite3
with sqlite3.connect('security1.db') as conn:
    c = conn.cursor()
    c.execute("""CREATE TABLE log 
                (date1 text PRIMARY KEY , policy text, port int, source_address text, source_zone text, destination_address,
                 destination_zone)""")
    conn.commit()

