import requests
from MySQLCode import DataBaseConnection
from DataGeneratorClasses import Schedule_Generator_Class as sch

connection = DataBaseConnection.mysqlopen()

cursor = connection.cursor()
cursor.execute('select season_id from seasons;')
seasons = cursor.fetchall()

for ss in seasons:
    print(ss[0])
    url = requests.get(f"https://statsapi.web.nhl.com/api/v1/schedule?season={ss[0]}")
    url_data = url.json()
    url_data = url_data["dates"]
    for date in url_data:
        current_date = date["date"]
        date = date["games"]
        for game in date:
            g = sch.Schedule(game["gamePk"], game["season"], current_date, game["teams"]["home"]["team"]["id"], game["teams"]["away"]["team"]["id"], game["link"],
                             game["content"]["link"], game["gameType"])
            g.query(connection)
            del g

DataBaseConnection.mysqlclose(connection)
