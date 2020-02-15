class Season:
    def __init__(self, id, regular_season_start_date, regular_season_end_date, season_end_date, number_of_games, ties_in_use, olympic_participation, conferences_in_use,
                 divisions_in_use, wild_card_in_use):
        self.id = id
        self.regular_season_start_date = regular_season_start_date
        self.regular_season_end_date = regular_season_end_date
        self.season_end_date = season_end_date
        self.number_of_games = number_of_games
        self.ties_in_use = ties_in_use
        self.olympic_participation = olympic_participation
        self.conferences_in_use = conferences_in_use
        self.divisions_in_use = divisions_in_use
        self.wild_card_in_use = wild_card_in_use

    def query(self,connection):
        query = f"insert into seasons values ({self.id},\"{self.regular_season_start_date}\",\"{self.regular_season_end_date}\",\"{self.season_end_date}\",{self.number_of_games}," \
                f"{self.ties_in_use},{self.olympic_participation},{self.conferences_in_use},{self.divisions_in_use},{self.wild_card_in_use})"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

