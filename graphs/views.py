from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Player, PlayerGame

# Create your views here.
def playerNames(): # Returns a list of all players in the database
    player_names = []
    for x in Player.objects.all():
        player_names.append(x.player_name_f + " " +  x.player_name_l)
    return player_names

def playerStats(p, s): # Returns a list of all the games for a single stat
    stats = []
    test = False # Used to reduce the time for now.
    for x in PlayerGame.objects.all():
        if p in str(x):
            test = True
            stats.append(getattr(x, s))
        elif p not in str(x) and test == True:
            break
    return stats

def graphs(request):
    if request.method == 'POST':
        try:
            player2 = request.POST.get('player2')
            player1 = request.POST.get('player1')
        except:
            player1 = request.POST.get('player1')

        stat = request.POST.get('stat')
        players_data = playerNames()

        try:
            stat2_data = playerStats(player2, stat.lower())
            stat1_data = playerStats(player1, stat.lower())
        except:
            stat1_data = playerStats(player1, stat.lower())

        # used to get the average over the last few games for that player
        i = 0
        stat_average = 0
        while i < len(stat1_data):
            stat_average = stat_average + stat1_data[i]
            i += 1

        stat_average = round(stat_average / i)
        try:
            page_data = {"player1" : player1, "player2" : player2, "players_data" : players_data,
                         "stat" : stat, "stat1_data" : stat1_data, "stat2_data" : stat2_data,
                         "stat_average" : stat_average}
        except:   
            page_data = {"player1" : player1, "players_data" : players_data,
                         "stat" : stat, "stat1_data" : stat1_data,
                         "stat_average" : stat_average}
        return render(request, 'graphs/graphs.html', page_data)
    else:
        players_data = playerNames()
        page_data = {"players_data" : players_data}
        return render(request, 'graphs/graphs.html', page_data)
