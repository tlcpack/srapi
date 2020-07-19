from sportsreference.mlb.roster import Roster, Player

summary_list = []

for x in range(1990, 1995):
    season = str(x)
    braves = Roster('ATL', season)
    pitchers = [player for player in braves.players if player.position == 'P']
    for pitcher in pitchers:
        summary_list.append((pitcher.name, season, pitcher.position, pitcher(season).games, pitcher(season).era, pitcher(season).wins, pitcher(season).whip))
    
print(summary_list)