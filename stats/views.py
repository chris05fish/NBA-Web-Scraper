from django.shortcuts import render, redirect
from django.http import HttpResponse
from home.models import Player, PlayerGame
from django.db.models import Avg

def playerNames(): # Returns a list of all players in the database
    player_names = []
    for x in Player.objects.all():
        player_names.append(x.player_name_f + " " +  x.player_name_l)
    return player_names

def stats(request):
    player_stats = []
    if request.method == "POST":
        if "searchPlayer" in request.POST:
            if request.POST.get("playerName") != "":
                player_name = request.POST.get("playerName").split(' ')
                searched_player = Player.objects.get(player_name_f = player_name[0], player_name_l = player_name[1])
                searched_player_games = PlayerGame.objects.filter(player = searched_player)
                searched_player_stats = searched_player_games.aggregate(Avg('pts'), Avg('fanp'), Avg('mp'), Avg('fg'), Avg('fga'), Avg('fgp'), 
                    Avg('tp'), Avg('tpa'), Avg('tpp'), Avg('ft'), Avg('fta'), Avg('ftp'), Avg('orb'), Avg('drb'), Avg('trb'), 
                    Avg('ast'), Avg('stl'), Avg('blk'), Avg('tov'), Avg('pf'))
                searched_player_stats["name"] = player_name[0] + ' ' + player_name[1]
                player_stats.append(searched_player_stats)
                print(searched_player_stats)

    for player in Player.objects.all():
        cur_player_games = PlayerGame.objects.filter(player = player)
        cur_player_stats = cur_player_games.aggregate(Avg('pts'), Avg('fanp'), Avg('mp'), Avg('fg'), Avg('fga'), Avg('fgp'), 
            Avg('tp'), Avg('tpa'), Avg('tpp'), Avg('ft'), Avg('fta'), Avg('ftp'), Avg('orb'), Avg('drb'), Avg('trb'), 
            Avg('ast'), Avg('stl'), Avg('blk'), Avg('tov'), Avg('pf'))

        cur_player_stats["name"] = player.player_name_f + ' ' + player.player_name_l
        player_stats.append(cur_player_stats)

    if request.method == "POST":
        if request.POST.get("sortStat") != "Choose Stat...":
            remove_rows = []
            for i in range(len(player_stats)):
                if player_stats[i][request.POST.get("sortStat") + '__avg'] == None:
                    remove_rows.insert(0, i)

            for row in remove_rows:
                del player_stats[row]

            player_stats = sorted(player_stats, key=lambda d: d[request.POST.get("sortStat") + '__avg'], reverse = True)

    page_data = {
        "player_stats": player_stats,
        "players": playerNames(),
    }
    return render(request, 'stats/stats.html', page_data)
