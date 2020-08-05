from sportsreference.mlb.roster import Roster, Player
from sportsreference.mlb.teams import Teams
# from sportsreference.ncaaf.teams import Teams

summary_list = []

for x in range(1990, 1995):
    season = str(x)
    braves = Roster('ATL', season)
    pitchers = [player for player in braves.players if player.position == 'P']
    for pitcher in pitchers:
        summary_list.append((pitcher.name, season, pitcher.position, pitcher(season).games, pitcher(season).era, pitcher(season).wins, pitcher(season).whip))
    
print(summary_list)

# for x in range(2002, 2005):
#   teams = Teams(x)

#   for team in teams:
#     if team.abbreviation == 'NORTH-CAROLINA-STATE':
#       print(str(x) + ' - ' + team.abbreviation + " - " + str(team.wins) + " Rush yards: " + str(team.rush_yards))

for x in range(1992, 2005):
  teams = Teams(x)

  for team in teams:
    if team.abbreviation == 'ATL':
      print(str(x) + ' - ' + team.abbreviation + " - " + str(team.wins) + " ERA: " + str(team.earned_runs_against) + " Pythag - " + team.pythagorean_win_loss)
