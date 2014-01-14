from django.contrib.auth.models import User


class Poll(models.Model):
    
    title = models.CharField()
    question = models.CharField()
    


class Vote(models.Model):
    
    poll = models.ForeignKey(Poll)
    choice = models.ForeignKey(Choice)
    user = models.ForeignKey(User)

Poll.objects.create(title='Jay likes polls', question='What?')



my_poll = Poll.objects.get(title='Jay likes polls')
votes = Vote.objects.filter(poll=my_poll)

my_user = User.objects.get(name='Jay')
votes = Vote.objects.filter(user=my_user)

choice = Choice.objects.get(text='foo', poll=my_poll)
Vote.objects.filter(poll=choice.poll, choice=choice)
