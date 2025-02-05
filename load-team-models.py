# creates Team models
import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nbaStats.settings")
django.setup()
from home.models import Team

Team.objects.all().delete()

team_list = [
    ['ATL', 'Atlanta', 'Hawks'],
    ['BKN', 'Brooklyn', 'Nets'],
    ['BOS', 'Boston', 'Celtics'],
    ['CHA', 'Charlotte', 'Hornets'],
    ['CHI', 'Chicago', 'Bulls'],
    ['CLE', 'Cleveland', 'Cavaliers'],
    ['DAL', 'Dallas', 'Mavericks'],
    ['DEN', 'Denver', 'Nuggets'],
    ['DET', 'Detroit', 'Pistons'],
    ['GSW', 'Golden State', 'Warriors'],
    ['HOU', 'Houston', 'Rockets'],
    ['IND', 'Indiana', 'Pacers'],
    ['LAC', 'Los Angeles', 'Clippers'],
    ['LAL', 'Los Angeles', 'Lakers'],
    ['MEM', 'Memphis', 'Grizzlies'],
    ['MIA', 'Miami', 'Heat'],
    ['MIL', 'Milwaukee', 'Bucks'],
    ['MIN', 'Minnesota', 'Timberwolves'],
    ['NOP', 'New Orleans', 'Pelicans'],
    ['NYK', 'New York', 'Knicks'],
    ['OKC', 'Oklahoma City', 'Thunder'],
    ['ORL', 'Orlando', 'Magic'],
    ['PHI', 'Philadelphia', '76ers'],
    ['PHX', 'Phoenix', 'Suns'],
    ['POR', 'Portland Trail', 'Blazers'],
    ['SAC', 'Sacramento', 'Kings'],
    ['SAS', 'San Antonio', 'Spurs'],
    ['TOR', 'Toronto', 'Raptors'],
    ['UTA', 'Utah', 'Jazz'],
    ['WAS', 'Washington', 'Wizards']
]

for item in team_list:
    abbr = item[0]
    city = item[1]
    name = item[2]

    new_team = Team(team_name = name, team_abbr = abbr, city = city)
    new_team.save()