from django.contrib import admin

from votes.models import Team


class TeamAdmin(admin.ModelAdmin):
    readonly_fields = ('votes',)

admin.site.register(Team, TeamAdmin)
