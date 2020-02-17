class BoxScore_Player:
    def __init__(self, game_id, player_id, team_id, TOI="NULL", assists="NULL", hits="NULL", goals="NULL", shots="NULL", PPG="NULL", PPA="NULL", faceOffWins="NULL",
                 faceOffTaken="NULL", takeaways="NULL", giveaways="NULL", SHG="NULL", SHA="NULL", blocked="NULL", pluMinus="NULL", evenTOI="NULL", ppTOI="NULL", shTOI="NULL"):
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
        self.evenTOI = f"\"{self.evenTOI}\"" if self.evenTOI != 'NULL' else self.evenTOI
        self.ppTOI = f"\"{self.ppTOI}\"" if self.ppTOI != 'NULL' else self.ppTOI
        self.shTOI = f"\"{self.shTOI}\"" if self.shTOI != 'NULL' else self.shTOI
        query = f"insert into boxscore_player values ({self.game_id},{self.player_id},{self.team_id},\"{self.TOI}\",{self.assists},{self.hits},{self.goals},{self.shots}," \
                f"{self.PPG},{self.PPA},{self.faceOffWins},{self.faceOffTaken},{self.takeaways},{self.giveaways},{self.SHG},{self.SHA},{self.blocked},{self.plusMinus}," \
                f"{self.evenTOI},{self.ppTOI},{self.shTOI})"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()


class BoxScore_Goalie:
    def __init__(self, game_id, player_id, team_id, TOI="NULL", assists="NULL", goals="NULL", shots="NULL", saves="NULL", ppSaves="NULL", shSaves="NULL", evenSaves="NULL",
                 savePercentage="NULL", ppSavePercentage="NULL", shSavePercentage="NULL", esSavePercentage="NULL", shShotsAgainst = "NULL", esShotsAgainst = "NULL",
                 ppShotsAgainst = "NULL"):
        self.game_id = game_id
        self.player_id = player_id
        self.team_id = team_id
        self.TOI = TOI
        self.assists = assists
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
        self.shShotsAgainst = shShotsAgainst
        self.esShotsAgainst = esShotsAgainst
        self.ppShotsAgainst = ppShotsAgainst

    def query(self, connection):
        self.TOI = f"\"{self.TOI}\"" if self.TOI != 'NULL' else self.TOI
        query = f"insert into boxscore_goalie values ({self.game_id},{self.player_id},{self.team_id},{self.TOI},{self.assists},{self.goals},{self.shots}," \
                f"{self.saves},{self.ppSaves},{self.shSaves},{self.evenSaves},{self.savePercentage},{self.ppSavePercentage},{self.shSavePercentage}," \
                f"{self.esSavePercentage}, {self.shShotsAgainst}, {self.esShotsAgainst}, {self.ppShotsAgainst})"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
