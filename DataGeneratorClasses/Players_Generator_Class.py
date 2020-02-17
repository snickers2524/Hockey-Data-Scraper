class Player:
    def __init__(self, player_id='NULL', first_name='NULL', last_name='NULL', number='NULL', birth_date='NULL', birth_city='NULL', birth_state='NULL', birth_country='NULL',
                 height='NULL', weight='NULL', alternate_captain='NULL', captain='NULL', rookie='NULL', shoots_catches='NULL', roster_status='NULL', current_team='NULL',
                 position='NULL',link = 'NULL'):
        self.player_id = player_id
        self.link = link
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.birth_date = birth_date
        self.birth_city = birth_city
        self.birth_state = birth_state
        self.birth_country = birth_country
        self.height = height
        self.weight = weight
        self.alternate_captain = alternate_captain
        self.captain = captain
        self.rookie = rookie
        self.shoots_catches = shoots_catches
        self.roster_status = roster_status
        self.current_team = current_team
        self.position = position

    def query(self, connection):
        self.first_name = f"\"{self.first_name}\"" if self.first_name != 'NULL' else 'NULL'
        self.last_name = f"\"{self.last_name}\"" if self.last_name != 'NULL' else 'NULL'
        self.birth_date = f"\"{self.birth_date}\"" if self.birth_date != 'NULL' else 'NULL'
        self.birth_city = f"\"{self.birth_city}\"" if self.birth_city != 'NULL' else 'NULL'
        self.birth_state = f"\"{self.birth_state}\"" if self.birth_state != 'NULL' else 'NULL'
        self.birth_country = f"\"{self.birth_country}\"" if self.birth_country != 'NULL' else 'NULL'
        self.shoots_catches = f"\"{self.shoots_catches}\"" if self.shoots_catches != 'NULL' else 'NULL'
        self.current_team = f"\"{self.current_team}\"" if self.current_team != 'NULL' else 'NULL'
        self.position = f"\"{self.position}\"" if self.position != 'NULL' else 'NULL'
        self.link = f"\"{self.link}\"" if self.link != 'NULL' else 'NULL'
        self.roster_status = f"\"{self.roster_status}\"" if self.roster_status != 'NULL' else 'NULL'

        query = f"insert into players values ({self.player_id},{self.link},{self.first_name},{self.last_name},{self.number},{self.birth_date},{self.birth_city}," \
                f"{self.birth_state},{self.birth_country},{self.height},{self.weight},{self.alternate_captain},{self.captain},{self.rookie},{self.shoots_catches}," \
                f"{self.roster_status},{self.current_team},{self.position});"
        print(query)
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()
