from sportsreference.ncaaf.teams import Teams
from sportsreference.ncaaf.boxscore import Boxscore
from sportsreference.ncaaf.schedule import Schedule
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

purdue_schedule = Schedule('PURDUE')
for game in purdue_schedule:
    # print(game.date)  # Prints the date the game was played
    # print(game.result)  # Prints whether the team won or lost
    # Creates an instance of the Boxscore class for the game.
    if game.opponent_abbr == 'iowa':
      frame = pd.DataFrame(game.dataframe)
      print(frame)