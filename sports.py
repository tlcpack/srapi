from sportsipy.mlb.roster import Roster, Player
# from sportsipy.mlb.teams import Teams
from sportsreference.ncaaf.teams import Teams
from sportsipy.ncaab.schedule import Schedule

# purdue_schedule = Schedule('purdue')
# for game in purdue_schedule:
#     print(game.date)

summary_list = []

# for x in range(1990, 1995):
# season = str(1991)
# braves = Roster('ATL', season)
# pitchers = [player for player in braves.players if player.position == 'P']
# for pitcher in pitchers:
#     summary_list.append((pitcher.name, season, pitcher.position, pitcher(season).games, pitcher(season).era, pitcher(season).wins, pitcher(season).whip))

# print(summary_list)

# for x in range(2002, 2005):
teams = Teams(2003)

for team in teams:
    if team.abbreviation == 'NORTH-CAROLINA-STATE':
        print(team.abbreviation + " - " + str(team.wins) + " Rush yards: " + str(team.rush_yards))

# for x in range(1992, 2005):
#   teams = Teams(x)

#   for team in teams:
#     if team.abbreviation == 'ATL':
#       print(str(x) + ' - ' + team.abbreviation + " - " + str(team.wins) + " ERA: " + str(team.earned_runs_against) + " Pythag - " + team.pythagorean_win_loss)
