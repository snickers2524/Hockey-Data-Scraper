import requests
from MySQLCode import DataBaseConnection
from DataGeneratorClasses import Teams_Generator_Class

url = requests.get("https://statsapi.web.nhl.com/api/v1/teams")
url_data = url.json()
url_data = url_data["teams"]
connection = DataBaseConnection.mysqlopen()


for a in url_data:
    a = Teams_Generator_Class.Teams(a['id'], a['name'], a['link'], a['venue']['name'], a['venue']['link'], a['venue']['city'], a['venue']['timeZone']['tz'], a['abbreviation'],
                                    a['teamName'], a['locationName'], a['firstYearOfPlay'], a['division']['id'], a['conference']['id'], a['franchise']['teamName'],
                                    a['franchise']['link'], a['shortName'], a['officialSiteUrl'], a['franchiseId'], a['active'])
    a.query_insert(connection)
    del a

DataBaseConnection.mysqlclose(connection)
