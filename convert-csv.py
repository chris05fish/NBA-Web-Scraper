import shelve, csv, logging
import os, django, datetime
from pathlib import Path

# setting up interface with django and logging configurations
logging.basicConfig(filename='./logs/csv-conversion.log', level=logging.DEBUG, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nbaStats.settings")
django.setup()
from home.models import Player, Team, Game, PlayerGame

# using object persistance to stored known files
shelve_db = shelve.open('shelveData')
try:
    known_files = shelve_db['files']
except KeyError:
    known_files = []

csv_directory = Path('./csvfiles')
csv_files = os.listdir(csv_directory)

for csv_f in csv_files:
    # looping through all unprocess csv files
    if csv_f not in known_files:
        logging.info("Processing csv file '" + csv_f + "'")
        cur_csv = list(csv.reader(open('./csvfiles/' + csv_f, encoding="utf8")))
        for row_num, row in enumerate(cur_csv[1:]):
            # parsing csv rows relating to Game model
            try:
                game_date = datetime.datetime.strptime(row[4], "%Y-%m-%d")
                team1 = Team.objects.get(team_abbr = row[2])
                team2 = Team.objects.get(team_abbr = row[3])
                game_score = row[5]
                team1_win = True if row[6] == '1' else False
            except Exception as inst:
                logging.warning('Parsing error on row: ' + str(row_num) + ' ' + str(inst))

            try: 
                cur_game = Game.objects.get(date = game_date, team1 = team1, team2 = team2)
                logging.debug('row #' + str(row_num) + ' game model already exist')
            except Game.DoesNotExist:
                try:
                    # checking if game exists but team references are reverse 
                    cur_game = Game.objects.get(date = game_date, team1 = team2, team2 = team1)
                    logging.debug('row #' + str(row_num) + ' game model already exist')
                except Game.DoesNotExist:
                    try:
                        cur_game = Game(date = game_date, team1 = team1, team2 = team2, team1_is_winner = team1_win, score = game_score)
                        cur_game.save()
                        logging.debug('row #' + str(row_num) + ' game model created')
                    except Exception as inst:
                        logging.error(str(inst) + ' when saving game model on row' + str(row_num))

            # parsing csv rows relating to Player model 
            try:
                full_name = row[0].split(' ')
                first_name = full_name[0]
                last_name = full_name[1]
                age = int(row[1])
            except Exception as inst:
                logging.warning('Parsing error on row: ' + str(row_num) + ' ' + str(inst))

            try:
                cur_player = Player.objects.get(player_name_f = first_name, player_name_l = last_name)
                logging.debug('row #' + str(row_num) + ' player model already exist')
            except:
                try:
                    cur_player = Player(player_name_f = first_name, player_name_l = last_name, age = age, team = team1)
                    cur_player.save()
                    logging.debug('row #' + str(row_num) + ' player model created')
                except Exception as inst:
                    logging.error(str(inst) + ' when saving player model on row', str(row_num))

            # parsing csv rows relating to PlayerGame model
            try:
                PlayerGame.objects.get(player = cur_player, game = cur_game)
                logging.debug('row #' + str(row_num) + ' player-game model already exist')
            except:
                try:
                    pts = int(row[7])
                    fanp = float(row[8])
                    mp_string = row[9]
                    mp_list = mp_string.split(':')
                    if(mp_string.count(':') == 1):
                        mp = datetime.timedelta(minutes=int(mp_list[0]), seconds=int(mp_list[1]))
                    else:
                        mp = datetime.timedelta(hours=int(mp_list[0]), minutes=int(mp_list[1]), seconds=int(mp_list[2]))
                    fg = int(row[10])
                    fga = int(row[11])
                    fgp = None if row[12] == 'NULL' or row[12] == '' else float(row[12])
                    tp = int(row[13])
                    tpa = int(row[14])
                    tpp = None if row[15] == 'NULL' or row[15] == '' else float(row[15])
                    ft = int(row[16])
                    fta = int(row[17])
                    ftp = None if row[18] == 'NULL' or row[18] == '' else float(row[18])
                    orb = int(row[19])
                    drb = int(row[20])
                    trb = int(row[21])
                    ast = int(row[22])
                    stl = int(row[23])
                    blk = int(row[24])
                    tov = int(row[25])
                    pf = int(row[26])
                except Exception as inst:
                    logging.warning('Parsing error on row: ' + str(row_num) + ' ' + str(inst))

                try:
                    new_playergame = PlayerGame(player=cur_player, game=cur_game, pts=pts, fanp=fanp, mp=mp, fg=fg,
                        fga=fga, fgp=fgp, tp=tp, tpa=tpa, tpp=tpp,ft=ft, fta=fta, ftp=ftp, orb=orb, drb=drb, trb=trb,
                        ast=ast, stl=stl, blk=blk, tov=tov, pf=pf)
                    new_playergame.save()
                    logging.debug('row #' + str(row_num) + ' player-game model created')
                except Exception as inst:
                    logging.error(str(inst) + ' when saving player-game model on row', str(row_num))

        known_files.append(csv_f)
    else:
        logging.info("skipping proccessing of '" + csv_f + "'; is a known file")

shelve_db['files'] = known_files
shelve_db.close()