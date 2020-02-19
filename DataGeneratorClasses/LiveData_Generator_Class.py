class Live_Data:
    def __init__(self, game_event_id, game_id, date_time, event_id, goals_away, goals_home, period_, period_time, period_time_remaining, period_type, x_coord='NULL',
                 y_coord='NULL', player1_id='NULL', player1_type='NULL', player2_id='NULL', player2_type='NULL', event_description='NULL', event_type='NULL'):
        self.game_event_id = game_event_id
        self.game_id = game_id
        self.date_time = date_time
        self.event_id = event_id
        self.goals_away = goals_away
        self.goals_home = goals_home
        self.period_ = period_
        self.period_time = period_time
        self.period_time_remaining = period_time_remaining
        self.period_type = period_type
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.player1_id = player1_id
        self.player1_type = player1_type
        self.player2_id = player2_id
        self.player2_type = player2_type
        self.event_description = event_description
        self.event_type = event_type

    def query(self, connection):
        self.player1_type = f"\"{self.player1_type}\"" if self.player1_type != 'NULL' else self.player1_type
        self.player2_type = f"\"{self.player2_type}\"" if self.player2_type != 'NULL' else self.player2_type
        self.event_description = f"\"{self.event_description}\"" if self.event_description != "NULL" else self.event_description
        self.event_type = f"\"{self.event_type}\"" if self.event_type != 'NULL' else self.event_type

        query = f"insert into live_data values ({self.game_event_id}, {self.game_id}, \"{self.date_time}\", {self.event_id}, {self.goals_away}, {self.goals_home}, {self.period_}," \
                f"\"{self.period_time}\", \"{self.period_time_remaining}\", \"{self.period_type}\", {self.x_coord}, {self.y_coord}, {self.player1_id}, {self.player1_type}," \
                f"{self.player2_id}, {self.player2_type}, {self.event_description}, {self.event_type})"

        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
