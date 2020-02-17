import requests
from MySQLCode import DataBaseConnection
from DataGeneratorClasses import Drafts_Generator_Class as dft
import pprint as p

years = list(range(2000, 2020))



connection = DataBaseConnection.mysqlopen()

cursor = connection.cursor()
cursor.execute("select live_link, game_id from schedule where game_date < '2020-02-16' and game_id=2019020790;")
links = cursor.fetchall()

for link in links:
    url = requests.get(f"https://statsapi.web.nhl.com{link[0]}")
    data = url.json()
    data = data['liveData']['plays']['allPlays']
    p.pprint(data)
    print(type(data))







DataBaseConnection.mysqlclose(connection)
