import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="delpiero92",
  database="video_game"
)

print('cest good:',mydb)


def addGames():
    mycursor = mydb.cursor()
    mycursor.execute("DROP TABLE IF EXISTS games", multi=True)
    mycursor.execute("CREATE TABLE IF NOT EXISTS games(games_id int PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255), note int NOT NULL)")
    mySql_insert_query = """INSERT INTO games(name, note) VALUES('assassins screed', 6.8)"""
    cursor = mydb.cursor()
    mycursor.execute(mySql_insert_query)
    mydb.commit()
    print(cursor.rowcount,"Record inserted successfully into games table")
    cursor.close()

addGames()