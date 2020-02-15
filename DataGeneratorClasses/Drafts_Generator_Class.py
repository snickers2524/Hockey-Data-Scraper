class Drafts:
    def __init__(self, year, round, pick_overall, pick_in_round, prospect_fullname, prospect_link, team_id, prospect_id=0):
        self.year = year
        self.round = round
        self.pick_overall = pick_overall
        self.pick_in_round = pick_in_round
        self.team_id = team_id
        self.prospect_id = prospect_id
        self.prospect_fullname = prospect_fullname
        self.prospect_link = prospect_link

    def query_insert(self,connection):
        query = f"insert into drafts values ({self.year},{self.round},{self.pick_overall},{self.pick_in_round},{self.team_id},{self.prospect_id},\"{self.prospect_fullname}\"," \
                f"'{self.prospect_link}')"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
