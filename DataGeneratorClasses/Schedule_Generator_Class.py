class Schedule:
    def __init__(self, game_id, season_id, date, home_team_id, away_team_id, live_link, content_link, game_type):
        self.game_id = game_id
        self.season_id = season_id
        self.date = date
        self.home_team_id = home_team_id
        self.away_team_id = away_team_id
        self.live_link = live_link
        self.content_link = content_link
        self.game_type = game_type

    def query(self,connection):
        query = f"insert into schedule values ({self.game_id},{self.season_id},\"{self.date}\",{self.home_team_id},{self.away_team_id},\"{self.live_link}\"," \
                f"\"{self.content_link}\",\"{self.game_type}\")"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
