from django.db.models import F
from django.shortcuts import render

from votes.models import Team

def results(request):
    teams = Team.objects.all()
    return render(request, 'results.html', {'teams': teams})

def vote(request):
    if request.method == 'POST':
        team = Team.objects.get(pk=request.POST['team'])
        team.votes = F('votes') + 1
        team.save()
        return render(request, 'done_voting.html', {'team': team})
    else:
        teams = Team.objects.all()
        return render(request, 'voting.html', {'teams': teams})
