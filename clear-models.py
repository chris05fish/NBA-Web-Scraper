import os, django, shelve, logging
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nbaStats.settings")
django.setup()
from home.models import Player, Game, PlayerGame
logging.basicConfig(filename='./logs/csv-conversion.log', level=logging.DEBUG, format='[%(asctime)s] %(levelname)s: %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')


confirm = input("Warning: this will delete all models from the Games, Player-Games, and Player models on django and make prevoiusly process csv files unprocess. Type 'yes' to confirm: ")
if confirm == 'yes':
    Player.objects.all().delete()
    Game.objects.all().delete()
    PlayerGame.objects.all().delete()
    shelve_db = shelve.open('shelveData')
    shelve_db['files'] = []
    shelve_db.close()
    logging.info('CLEAR-MODELS.PY ran')
else:
    exit()