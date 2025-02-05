from django.contrib import admin
from home.models import Player, Team, UserProfile, Game, PlayerGame

admin.site.register(Player)
admin.site.register(Team)
admin.site.register(UserProfile)
admin.site.register(Game)
admin.site.register(PlayerGame)