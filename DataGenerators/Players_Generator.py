import requests
from MySQLCode import DataBaseConnection
from DataGeneratorClasses import Players_Generator_Class as ply


def weight_parser(weight):
    return int(weight[0])*30.48 + int(weight[2:4])*2.54


connection = DataBaseConnection.mysqlopen()

cursor = connection.cursor()
cursor.execute('(select distinct player_id from boxscore_player) union (select distinct player_id from boxscore_goalie);')
players = cursor.fetchall()
for player in players:
    url = requests.get(f"https://statsapi.web.nhl.com/api/v1/people/{player[0]}")
    url_data = url.json()
    url_data = url_data["people"][0]
    person = ply.Player(player_id=url_data['id'],link=url_data['link'])
    if "firstName" in url_data.keys():
        setattr(person,"first_name",url_data["firstName"])
    if "lastName" in url_data.keys():
        setattr(person,"last_name",url_data["lastName"])
    if "primaryNumber" in url_data.keys():
        setattr(person,"number",url_data["primaryNumber"])
    if "birthDate" in url_data.keys():
        setattr(person,"birth_date",url_data["birthDate"])
    if "birthCity" in url_data.keys():
        setattr(person,"birth_city",url_data["birthCity"])
    if "birthStateProvince" in url_data.keys():
        setattr(person, "birth_state",url_data["birthStateProvince"])
    if "birthCountry" in url_data.keys():
        setattr(person,"birth_country",url_data["birthCountry"])
    if "height" in url_data.keys():
        setattr(person,"height",weight_parser(url_data["height"]))
    if "weight" in url_data.keys():
        print("*************************")
        print(url_data["height"])
        setattr(person,"weight",url_data["weight"])
    if "alternateCaptain" in url_data.keys():
        setattr(person,"alternate_captain",url_data["alternateCaptain"])
    if "captain" in url_data.keys():
        setattr(person,"captain",url_data["captain"])
    if "rookie" in url_data.keys():
        setattr(person,"rookie",url_data["rookie"])
    if "shootsCatches" in url_data.keys():
        setattr(person,"shoots_catches",url_data["shootsCatches"])
    if "rosterStatus" in url_data.keys():
        setattr(person,"roster_status",url_data["shootsCatches"])
    if "currentTeam" in url_data.keys():
        if "id" in url_data["currentTeam"].keys():
            setattr(person, "current_team",url_data["currentTeam"]["id"])
    if "primaryPosition" in url_data.keys():
        if "code" in url_data["primaryPosition"].keys():
            setattr(person,"position",url_data["primaryPosition"]["code"])
    person.query(connection)
    del person


DataBaseConnection.mysqlclose(connection)
