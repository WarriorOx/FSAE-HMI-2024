import sqlite3

connection = sqlite3.connect("fsae.db")

cursor = connection.cursor()
cursor.execute("CREATE TABLE fsae_database (Date TEXT, Time TEXT, Parameter TEXT, Value INTEGER )")

cursor.execute("INSERT INTO fsae_database VALUES ('02/10/2024','8:37', 'Speed', 200)")
cursor.execute("INSERT INTO fsae_database VALUES ('02/10/2024','8:37', 'Motor Temp', 20)")
cursor.execute("INSERT INTO fsae_database VALUES ('02/10/2024','8:37', 'Bat Temp', 20)")
cursor.execute("INSERT INTO fsae_database VALUES ('02/10/2024','8:37', 'Battery %', 1)")
cursor.execute("INSERT INTO fsae_database VALUES ('02/10/2024','8:37', 'Power', 120)")
cursor.execute("INSERT INTO fsae_database VALUES ('02/10/2024','8:37', 'Lap Time', 10)")
cursor.execute("INSERT INTO fsae_database VALUES ('02/10/2024','8:37', 'Lap Power', 150)") #Hi



