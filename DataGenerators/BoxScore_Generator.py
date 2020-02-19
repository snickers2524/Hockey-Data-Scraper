import requests
from MySQLCode import DataBaseConnection
from DataGeneratorClasses import BoxScore_Generator_Classes as bsg
from HelperFunctions import TImeChange as tc

def single_game_box_score(connection, url_data, game):
    for player in url_data["players"]:
        ply = url_data["players"][player]["person"]
        stats = url_data["players"][player]["stats"]
        if (ply["primaryPosition"]["code"] == "G") & (stats != {}):
            stats = stats["goalieStats"]
            ply_object = bsg.BoxScore_Goalie(game_id=game, player_id=ply["id"], team_id=url_data["team"]["id"])
            if "timeOnIce" in stats.keys():
                setattr(ply_object, "TOI", tc.time_change(stats["timeOnIce"]))
            if "assists" in stats.keys():
                setattr(ply_object, "assists", stats["assists"])
            if "goals" in stats.keys():
                setattr(ply_object, "goals", stats["goals"])
            if "shots" in stats.keys():
                setattr(ply_object, "shots", stats["shots"])
            if "saves" in stats.keys():
                setattr(ply_object, "saves", stats["saves"])
            if "powerPlaySaves" in stats.keys():
                setattr(ply_object, "ppSaves", stats["powerPlaySaves"])
            if "shortHandedSaves" in stats.keys():
                setattr(ply_object, "shSaves", stats["shortHandedSaves"])
            if "evenSaves" in stats.keys():
                setattr(ply_object, "evenSaves", stats["evenSaves"])
            if "powerPlaySavePercentage" in stats.keys():
                setattr(ply_object, "ppSavePercentage", stats["powerPlaySavePercentage"])
            if "shortHandedSavePercentage" in stats.keys():
                setattr(ply_object, "shSavePercentage", stats["shortHandedSavePercentage"])
            if "evenStrengthSavePercentage" in stats.keys():
                setattr(ply_object, "esSavePercentage", stats["evenStrengthSavePercentage"])
            if "shortHandedShotsAgainst" in stats.keys():
                setattr(ply_object, "shShotsAgainst", stats["shortHandedShotsAgainst"])
            if "evenShotsAgainst" in stats.keys():
                setattr(ply_object, "esShotsAgainst", stats["evenShotsAgainst"])
            if "powerPlayShotsAgainst" in stats.keys():
                setattr(ply_object, "ppShotsAgainst", stats["powerPlayShotsAgainst"])
            ply_object.query(connection)
            del ply_object

        elif (ply["primaryPosition"]["code"] != "G") & (stats != {}):
            stats = stats["skaterStats"]
            ply_object = bsg.BoxScore_Player(game_id=game, player_id=ply["id"], team_id=url_data["team"]["id"])
            if "timeOnIce" in stats.keys():
                setattr(ply_object, "TOI", stats["timeOnIce"])
            if "assists" in stats.keys():
                setattr(ply_object, "assists", stats["assists"])
            if "hits" in stats.keys():
                setattr(ply_object, "hits", stats["hits"])
            if "goals" in stats.keys():
                setattr(ply_object, "goals", stats["goals"])
            if "shots" in stats.keys():
                setattr(ply_object, "shots", stats["shots"])
            if "powerPlayGoals" in stats.keys():
                setattr(ply_object, "PPG", stats["powerPlayGoals"])
            if "powerPlayAssists" in stats.keys():
                setattr(ply_object, "PPA", stats["powerPlayAssists"])
            if "faceOffWins" in stats.keys():
                setattr(ply_object, "faceOffWins", stats["faceOffWins"])
            if "faceoffTaken" in stats.keys():
                setattr(ply_object, "faceOffTaken", stats["faceoffTaken"])
            if "takeaways" in stats.keys():
                setattr(ply_object, "takeaways", stats["takeaways"])
            if "giveaways" in stats.keys():
                setattr(ply_object, "giveaways", stats["giveaways"])
            if "shortHandedGoals" in stats.keys():
                setattr(ply_object, "SHG", stats["shortHandedGoals"])
            if "shortHandedAssists" in stats.keys():
                setattr(ply_object, "SHA", stats["shortHandedAssists"])
            if "blocked" in stats.keys():
                setattr(ply_object, "blocked", stats["blocked"])
            if "plusMinus" in stats.keys():
                setattr(ply_object, "plusMinus", stats["plusMinus"])
            if "evenTimeOnIce" in stats.keys():
                setattr(ply_object, "evenTOI", stats["evenTimeOnIce"])
            if "powerPlayTimeOnIce" in stats.keys():
                setattr(ply_object, "ppTOI", stats["powerPlayTimeOnIce"])
            if "shortHandedTimeOnIce" in stats.keys():
                setattr(ply_object, "shTOI", stats["shortHandedTimeOnIce"])
            ply_object.query(connection)
            del ply_object


connection = DataBaseConnection.mysqlopen()

cursor = connection.cursor()
cursor.execute('select game_id from schedule where game_date<"2020-02-15" and season_id>=20152016;')
all_games = cursor.fetchall()

for game in all_games:
    url = requests.get(f"https://statsapi.web.nhl.com/api/v1/game/{game[0]}/boxscore")
    url_data = url.json()
    url_data = url_data["teams"]
    # Away team ********************
    single_game_box_score(connection, url_data["away"], game[0])
    # Home Team *****************
    single_game_box_score(connection, url_data["home"], game[0])

DataBaseConnection.mysqlclose(connection)
