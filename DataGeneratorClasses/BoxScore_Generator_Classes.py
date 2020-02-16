class BoxScore_Player:
    def __init__(self, game_id, player_id, team_id, TOI="00:00:00", assists=0, hits=0, goals=0, shots=0, PPG=0, PPA=0, faceOffWins=0, faceOffTaken=0, takeaways=0, giveaways=0,
                 SHG=0, SHA=0, blocked=0, pluMinus=0, evenTOI="00:00:00", ppTOI="00:00:00", shTOI="00:00:00"):
        self.game_id = game_id
        self.player_id = player_id
        self.team_id = team_id
        self.TOI = TOI
        self.assists = assists
        self.hits = hits
        self.goals = goals
        self.shots = shots
        self.PPG = PPG
        self.PPA = PPA
        self.faceOffWins = faceOffWins
        self.faceOffTaken = faceOffTaken
        self.takeaways = takeaways
        self.giveaways = giveaways
        self.SHG = SHG
        self.SHA = SHA
        self.blocked = blocked
        self.plusMinus = pluMinus
        self.evenTOI = evenTOI
        self.ppTOI = ppTOI
        self.shTOI = shTOI

    def query(self, connection):
        query = f"insert into boxscore_player values ({self.game_id},{self.player_id},{self.team_id},\"{self.TOI}\",{self.assists},{self.hits},{self.goals},{self.shots}," \
                f"{self.PPG},{self.PPA},{self.faceOffWins},{self.faceOffTaken},{self.takeaways},{self.giveaways},{self.SHG},{self.SHA},{self.blocked},{self.plusMinus}," \
                f"\"{self.evenTOI}\",\"{self.ppTOI}\",\"{self.shTOI}\")"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()


class BoxScore_Goalie:
    def __init__(self,game_id, player_id, team_id, TOI="00:00:00", assists=0, hits=0, goals=0, shots=0,saves=0,ppSaves=0,shSaves=0,evenSaves=0,
                 savePercentage=0,ppSavePercentage=0,shSavePercentage=0,esSavePercentage=0):
        self.game_id = game_id
        self.player_id = player_id
        self.team_id = team_id
        self.TOI = TOI
        self.assists = assists
        self.hits = hits
        self.goals = goals
        self.shots = shots
        self.saves = saves
        self.ppSaves = ppSaves
        self.shSaves = shSaves
        self.evenSaves = evenSaves
        self.savePercentage = savePercentage
        self.ppSavePercentage = ppSavePercentage
        self.shSavePercentage = shSavePercentage
        self.esSavePercentage = esSavePercentage

    def query(self,connection):
        query = f"insert into boxscore_player values ({self.game_id},{self.player_id},{self.team_id},\"{self.TOI}\",{self.assists},{self.goals},{self.shots}," \
                f"{self.saves},{self.ppSaves},{self.ppSaves},{self.shSaves},{self.evenSaves},{self.savePercentage},{self.ppSavePercentage},{self.shSavePercentage}," \
                f"{self.esSavePercentage}"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

