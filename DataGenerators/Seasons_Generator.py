import requests
from MySQLCode import DataBaseConnection
from DataGeneratorClasses import Seasons_Generator_Class as ss


url = requests.get("https://statsapi.web.nhl.com/api/v1/seasons")
url_data = url.json()
url_data = url_data["seasons"]

connection = DataBaseConnection.mysqlopen()

for year in url_data:
    if int(year["seasonId"]) < 20002001:
        continue
    season = ss.Season(year["seasonId"],year["regularSeasonStartDate"],year["regularSeasonEndDate"],year["seasonEndDate"],year["numberOfGames"],year["tiesInUse"],
                       year["olympicsParticipation"],year["conferencesInUse"],year["divisionsInUse"],year["wildCardInUse"])
    season.query(connection)

DataBaseConnection.mysqlclose(connection)