# Hockey-Data-Scraper
This scraper was written to scrape the play-by-play data from the NHLs Api.  To explain the code, an explanation of each directory has been written below.

## MySQLCode
For the entirety of this project, the SQL code is all written in MySQL.  If the user wishes to write the data into a different database, the user will need to adjust the code in this section.
In this section, several tables have been created that will written into in other sections, as well as the DataBaseConnection functions are included in this section as well.

## Helper Functions
This section includes functions that are called periodically elsewhere.

## Data Generator Classes
This section contains the objects that are used in the DataGenerator Files to write the data into the database.

## DataGenerators

### Teams Generator
This file writes information about each nhl team into the teams table.  See the table to see what data is generated.

### Seasons Generator
This file writes information about each season from the 2000-2001 season onwards into the seasons table.  NOTE: this file must be run before the schedule file.

### Schedule Generator
By querying data from the seasons table this file generates the complete schedule for each season from 2000-2001 onwards.  To adjust the seasons see line 8 of the file.
NOTE: This file MUST be run before the BoxScore file or the LiveFeed file.

### LiveFeed Generator
This file generates the live play by play data for each game.  To adjust which games the data is generated for see line 12 of the file.  
NOTE: Before running this file, you must first run the Seasons and Schedule Generator files.  The order for which is Seasons -> Schedule -> LiveFeed.

### BoxScore Generator
This file generates the boxscore data for each game.  To adjust which games the data is generated for see line 92 of the file.  
NOTE: Before running this file, you must first run the Seasons and Schedule Generator files.  The order for which is Seasons -> Schedule -> BoxScore.

### Drafts Generator
This file generates the draft selections for each year.  To adjust which years see line 5 of the file.

### Players Generator
This file generates data for each player.  To adjust the parameters of which players see line 13 of the file.
NOTE: Before running this file, you must first run the Seasons, Schedule, and BoxScore Generator files.  The order for which is Seasons -> Schedule -> BoxScore -> Players.