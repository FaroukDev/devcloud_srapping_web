import importlib
import mysql.connector
from  app import getXBox, getPs5, getPc

my_dict = getXBox()
my_dict1 = getPs5()
my_dict2 = getPc()


mydb = mysql.connector.connect(
  host="ms1",
  user="root",
  password="delpiero92",
  database="video_game"
)

def addGames(games, mycursor,games_dict):
    my_cursor = mycursor.cursor()
    my_cursor.execute("DROP TABLE IF EXISTS games", multi=True)
    my_cursor.execute("DROP TABLE IF EXISTS ps5", multi=True)
    my_cursor.execute("DROP TABLE IF EXISTS pc", multi=True)
    my_cursor.execute("CREATE TABLE IF NOT EXISTS games(games_id int PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255))")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS ps5(games_id int PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255))")
    my_cursor.execute("CREATE TABLE IF NOT EXISTS pc(games_id int PRIMARY KEY NOT NULL AUTO_INCREMENT, name VARCHAR(255))")
    
addGames("games",mydb,my_dict)
addGames("ps5",mydb,my_dict1)
addGames("pc",mydb,my_dict2)

def insertGames(games,mycursor,games_dict):
    my_cursor = mycursor.cursor()
    for i in range (1,6):
                mySql_insert_query = f"""INSERT INTO {games} (name) VALUES ('{games_dict[i]}')"""
                my_cursor.execute(mySql_insert_query)  
                mycursor.commit()

insertGames("games",mydb,my_dict)
insertGames("ps5",mydb,my_dict1)
insertGames("pc",mydb,my_dict2)


def selectGames(games,mycursor):
    my_cursor = mycursor.cursor()
    my_cursor.execute("SELECT * FROM games")
    myresult = my_cursor.fetchall()
    for i in range(0,5):
        print(myresult[i])

selectGames("games",mydb)