import requests
from MySQLCode import DataBaseConnection
from DataGeneratorClasses import Drafts_Generator_Class as dft

years = list(range(2000, 2020))

url_string = "https://statsapi.web.nhl.com/api/v1/draft/"

connection = DataBaseConnection.mysqlopen()

for yr in years:
    print(f"THE YEAR IS: {yr}")
    url = requests.get(f"{url_string}{yr}")
    url_data = url.json()
    url_data = url_data['drafts'][0]['rounds']
    for rounds in url_data:
        for pick in rounds['picks']:
            if pick['prospect']['fullName'] == "":  # Player Does Not Exists ************************
                continue
            elif (pick['prospect']['fullName'] != "") & ("id" not in pick['prospect']):  # Player exists but does not have a prospect ID *********************************
                d = dft.Drafts(year=pick['year'], round=pick['round'], pick_overall=pick['pickOverall'], pick_in_round=pick['pickInRound'], team_id=pick['team']['id'],
                           prospect_fullname=pick['prospect']['fullName'], prospect_link=pick['prospect']['link'])
            else:
                d = dft.Drafts(year=pick['year'], round=pick['round'], pick_overall=pick['pickOverall'], pick_in_round=pick['pickInRound'], team_id=pick['team']['id'],
                               prospect_id=pick['prospect']['id'], prospect_fullname=pick['prospect']['fullName'],prospect_link=pick['prospect']['link'])
            d.query_insert(connection)
            del d

DataBaseConnection.mysqlclose(connection)
