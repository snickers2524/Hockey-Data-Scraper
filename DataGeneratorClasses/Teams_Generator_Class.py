class Teams:
    def __init__(self, id, name, link, venue_name, venue_link, venue_city, venue_timezone, abbreviation,
                 teamName, locationName,
                 firstYearOfPlay, division_id, conference_id, franchise_teamName, franchise_link,
                 shortName, officialSiteUrl, franchiseId,active):
        self.id = id
        self.name = name
        self.link = link
        self.venue_name = venue_name
        self.venue_link = venue_link
        self.venue_city = venue_city
        self.venue_timezone = venue_timezone
        self.abbreviation = abbreviation
        self.team_name = teamName
        self.locationName = locationName
        self.firstYearOfPlay = firstYearOfPlay
        self.division_id = division_id
        self.conference_id = conference_id
        self.franchise_teamName = franchise_teamName
        self.franchise_link = franchise_link
        self.shortName = shortName
        self.officialSiteUrl = officialSiteUrl
        self.franchiseId = franchiseId
        self.active = active

    def query_insert(self,connection):
        query = f"insert into teams (id,name,link,venue_name,venue_link,venue_city,venue_timezone,abbreviation,team_name,locationName,firstYearOfPlay,division_id," \
                f"conference_id,franchise_teamName,franchise_link,shortName,officialSiteUrl,franchiseId,active) values ({self.id},'{self.name}','{self.link}','{self.venue_name}'," \
                f"'{self.venue_link}','{self.venue_city}','{self.venue_timezone}','{self.abbreviation}','{self.team_name}','{self.locationName}','{self.firstYearOfPlay}'," \
                f"{self.division_id}," \
                f"{self.conference_id},'{self.franchise_teamName}','{self.franchise_link}','{self.shortName}','{self.officialSiteUrl}',{self.franchiseId}," \
                f"{self.active});"
        cursor = connection.cursor()
        cursor.execute(query)
        connection.commit()

