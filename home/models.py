from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    team_name = models.CharField(max_length=64)
    team_abbr = models.CharField(max_length=5)
    city = models.CharField(max_length=64)

    def __str__(self):
        return self.city + ' ' + self.team_name

class Player(models.Model):
    player_name_f = models.CharField(max_length=64)
    player_name_l = models.CharField(max_length=64)
    age = models.IntegerField()
    team = models.ForeignKey(Team, on_delete=models.SET_NULL, null = True)

    def __str__(self):
        return self.player_name_f + ' ' + self.player_name_l

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_players = models.ManyToManyField(Player, blank = True)
    favorite_teams = models.ManyToManyField(Team, blank = True)

    def __str__(self):
        return self.user.username 

class Game(models.Model):
    date = models.DateField()
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = 'team1')
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name = 'team2')
    team1_is_winner = models.BooleanField()
    score = models.CharField(max_length=8)

    def __str__(self):
        return str(self.team1) + ' vs ' + str(self.team2) + ' (Game ID #' + str(self.id) + ')'

class PlayerGame(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    pts = models.IntegerField()
    fanp = models.FloatField()
    mp = models.DurationField()
    fg = models.IntegerField()
    fga = models.IntegerField()
    fgp = models.FloatField(null=True)
    tp = models.IntegerField()
    tpa = models.IntegerField()
    tpp = models.FloatField(null=True)
    ft = models.IntegerField()
    fta = models.IntegerField()
    ftp = models.FloatField(null=True)
    orb = models.IntegerField()
    drb = models.IntegerField()
    trb = models.IntegerField()
    ast = models.IntegerField()
    stl = models.IntegerField()
    blk = models.IntegerField()
    tov = models.IntegerField()
    pf = models.IntegerField()
    
    def __str__(self):
        return str(self.player.player_name_f) +' ' + str(self.player.player_name_l) + ' in game id #' + str(self.game.id)