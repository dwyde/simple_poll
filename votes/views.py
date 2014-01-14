from django.db.models import F
from django.shortcuts import render

from votes.models import Team

def results(request):
    teams = Team.objects.all()
    return render(request, 'results.html', {'teams': teams})

def vote(request):
    if request.method == 'POST':
        team_id = request.POST.get('team')
        if team_id is not None:
            Team.objects.filter(pk=team_id).update(votes=F('votes') + 1)
        return render(request, 'done_voting.html', {'team': team_id})
    else:
        teams = Team.objects.all()
        return render(request, 'voting.html', {'teams': teams})
