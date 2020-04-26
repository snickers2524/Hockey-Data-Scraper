import requests
from MySQLCode import DataBaseConnection
from DataGeneratorClasses import LiveData_Generator_Class as ldg
from HelperFunctions import DateTimeParser as dtp
from HelperFunctions import TImeChange as tc

years = list(range(2000, 2020))

connection = DataBaseConnection.mysqlopen()

cursor = connection.cursor()
cursor.execute("select live_link, game_id from schedule where game_date < '2020-03-12' and game_id!=2018021252 and game_id>2018021252 ;")
links = cursor.fetchall()

for link in links:
    url = requests.get(f"https://statsapi.web.nhl.com{link[0]}")
    data = url.json()
    data = data['liveData']['plays']['allPlays']
    for event in data:
        game_event_id = int(str(link[1]) + str(event['about']['eventId']))
        ld = ldg.Live_Data(game_event_id=game_event_id, game_id=link[1], date_time=dtp.date_time_parser(event['about']['dateTime']), event_id=event['about']['eventId'],
                           goals_away=event['about']['goals']['away'], goals_home=event['about']['goals']['home'], period_=event['about']['period'],
                           period_time=tc.time_change(event['about']['periodTime']), period_time_remaining=tc.time_change(event['about']['periodTimeRemaining']),
                           period_type=tc.time_change(event['about']['periodType']))
        if "coordinates" in event.keys():
            if 'x' in event['coordinates'].keys() and 'y' in event['coordinates'].keys():
                setattr(ld, "x_coord", event['coordinates']['x'])
                setattr(ld, "y_coord", event['coordinates']['y'])
        if "players" in event.keys():
            setattr(ld, "player1_id", event['players'][0]['player']['id'])
            setattr(ld, "player1_type", event['players'][0]['playerType'])
            if len(event['players']) > 1:
                setattr(ld, "player2_id", event['players'][1]['player']['id'])
                setattr(ld, "player2_type", event['players'][1]['playerType'])
        if "result" in event.keys():
            setattr(ld, "event_description", event["result"]["description"])
            setattr(ld, "event_type", event['result']['event'])
        ld.query(connection)
        del ld

DataBaseConnection.mysqlclose(connection)
