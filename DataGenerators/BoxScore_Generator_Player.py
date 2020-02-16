import requests
from MySQLCode import DataBaseConnection
from DataGeneratorClasses import BoxScore_Generator_Classes as bsg


def single_game_box_score(team, connection, url_data):
    for player in url_data[team]["players"]:
        person = url_data[team]["players"][player]["person"]

        if bool(not url_data[team]["players"][player]["stats"]):
            ply = bsg.BoxScore_Player(game_id=game, player_id=person["id"], team_id=url_data[team]["team"]["id"])
        else:
            # Dealing with Goalies here, passing data into a separate table
            if person["primaryPosition"]["code"] == "G":
                stats = url_data[team]["players"][player]["stats"]["goalieStats"]
                print(stats)
                if "shortHandedSavePercentage" in stats.keys():
                    ply = bsg.BoxScore_Goalie(game_id=game, player_id=person["id"], team_id=url_data[team]["team"]["id"], TOI=stats["timeOnIce"], assists=stats["assists"],
                                              goals=stats["goals"], shots=stats["shots"], ppSaves=stats['powerPlaySaves'], shSaves=stats["shortHandedSaves"],
                                              evenSaves=stats["evenSaves"],
                                              savePercentage=stats["savePercentage"], ppSavePercentage=stats["powerPlaySavePercentage"],
                                              esSavePercentage=stats["evenStrengthSavePercentage"], shSavePercentage=stats["shortHandedSavePercentage"])
                else:
                    ply = bsg.BoxScore_Goalie(game_id=game, player_id=person["id"], team_id=url_data[team]["team"]["id"], TOI=stats["timeOnIce"], assists=stats["assists"],
                                              goals=stats["goals"], shots=stats["shots"], ppSaves=stats['powerPlaySaves'], shSaves=stats["shortHandedSaves"],
                                              evenSaves=stats["evenSaves"],
                                              savePercentage=stats["savePercentage"], ppSavePercentage=stats["powerPlaySavePercentage"],
                                              esSavePercentage=stats["evenStrengthSavePercentage"])
            else:
                stats = url_data[team]["players"][player]["stats"]["skaterStats"]
                ply = bsg.BoxScore_Player(game_id=game[0], player_id=person["id"], team_id=url_data[team]["team"]["id"], TOI=stats["timeOnIce"], assists=stats["assists"],
                                          hits=stats["hits"], goals=stats["goals"], shots=stats["shots"], PPG=stats["powerPlayGoals"], PPA=stats["powerPlayAssists"],
                                          faceOffWins=stats["faceOffWins"], faceOffTaken=stats["faceoffTaken"], takeaways=stats["takeaways"], giveaways=stats["giveaways"],
                                          SHG=stats["shortHandedGoals"], SHA=stats["shortHandedAssists"], blocked=stats["blocked"], pluMinus=stats["plusMinus"],
                                          evenTOI=stats["evenTimeOnIce"], ppTOI=stats["powerPlayTimeOnIce"], shTOI=stats["shortHandedTimeOnIce"])
                ply.query(connection)
                del ply


connection = DataBaseConnection.mysqlopen()

cursor = connection.cursor()
cursor.execute('select game_id from schedule where game_date<"2020-02-15" and season_id>=20152016;')
all_games = cursor.fetchall()

for game in all_games:
    url = requests.get(f"https://statsapi.web.nhl.com/api/v1/game/{game[0]}/boxscore")
    print(f"https://statsapi.web.nhl.com/api/v1/game/{game[0]}/boxscore")
    url_data = url.json()
    url_data = url_data["teams"]
    # Away team ********************
    single_game_box_score("away", connection, url_data)
    # Home Team *****************
    single_game_box_score("home", connection, url_data)

DataBaseConnection.mysqlclose(connection)
